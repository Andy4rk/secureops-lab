# scripts/mitre_lookup.py
#!/usr/bin/env python3
"""
MITRE ATT&CK lookup: search techniques by ID (e.g., T1059.001) or by name/description.
- Accepts data as { "techniques": [...] } or a plain list of technique dicts.
- Supports exact ID, substring, or regex search.
- Outputs table or JSON.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any, Dict, Iterable, List, Optional, Tuple

ATTACK_ID_RE = re.compile(r"^T\d{4}(?:\.\d{3})?$", re.IGNORECASE)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="mitre_lookup",
        description="Search MITRE ATT&CK techniques by ID, name, or description.",
    )
    parser.add_argument(
        "-f", "--file", required=True, help="Path to ATT&CK data JSON file."
    )
    parser.add_argument(
        "query",
        nargs="+",
        help="Technique ID(s) (e.g., T1059.001) or search text/regex depending on flags.",
    )
    parser.add_argument(
        "--field",
        choices=["id", "name", "description", "all"],
        default="all",
        help="Field to search when not an exact ATT&CK ID.",
    )
    parser.add_argument(
        "--contains",
        action="store_true",
        help="Use case-insensitive substring search (default behavior).",
    )
    parser.add_argument(
        "--regex",
        action="store_true",
        help="Treat query as a regular expression (overrides --contains).",
    )
    parser.add_argument(
        "--json",
        dest="as_json",
        action="store_true",
        help="Output raw JSON array of matches.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum number of results to display (table mode).",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI colors in table output.",
    )
    return parser.parse_args(argv)


def load_attack_data(file_path: str) -> List[Dict[str, Any]]:
    """Load techniques list from JSON file. Accepts { 'techniques': [...] } or a plain list.

    Why: Many exports differ; this avoids brittle schema coupling.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        # Common shapes: {"techniques": [...]}, {"objects": [...] } (STIX)
        if "techniques" in data and isinstance(data["techniques"], list):
            return [x for x in data["techniques"] if isinstance(x, dict)]
        if "objects" in data and isinstance(data["objects"], list):
            # STIX bundles often contain multiple object types; filter techniques
            return [x for x in data["objects"] if isinstance(x, dict)]
        # Fallback to all dict values that are lists of dicts (best-effort)
        for v in data.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                return [x for x in v if isinstance(x, dict)]
        raise ValueError("Could not locate a list of technique-like objects in JSON.")
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    raise ValueError("Unsupported JSON structure for techniques.")


def normalize_attack_id(s: str) -> str:
    """Uppercase and strip spaces to compare ATT&CK IDs consistently."""
    return s.strip().upper().replace(" ", "")


def is_attack_id(s: str) -> bool:
    return bool(ATTACK_ID_RE.match(s.strip()))


def extract_id(item: Dict[str, Any]) -> Optional[str]:
    """Find an ATT&CK-like ID in the item.

    Why: Different datasets use 'id', 'external_id', 'external_references', etc.
    """
    # Direct keys
    for k in ("id", "external_id", "attack_id", "technique_id"):
        v = item.get(k)
        if isinstance(v, str) and is_attack_id(v):
            return normalize_attack_id(v)
    # STIX external_references
    ext = item.get("external_references") or item.get("externalReferences")
    if isinstance(ext, list):
        for ref in ext:
            if not isinstance(ref, dict):
                continue
            for vk in ("external_id", "externalId", "id"):
                v = ref.get(vk)
                if isinstance(v, str) and is_attack_id(v):
                    return normalize_attack_id(v)
    return None


def extract_name(item: Dict[str, Any]) -> Optional[str]:
    for k in ("name", "technique", "title", "x_mitre_deprecated_name"):
        v = item.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def extract_description(item: Dict[str, Any]) -> Optional[str]:
    for k in ("description", "summary", "details"):
        v = item.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def extract_tactics(item: Dict[str, Any]) -> List[str]:
    """Heuristically collect tactic/phase names if present."""
    tactics: List[str] = []
    # kill_chain_phases: [{ kill_chain_name, phase_name }]
    kcp = item.get("kill_chain_phases") or item.get("killChainPhases")
    if isinstance(kcp, list):
        for e in kcp:
            if isinstance(e, dict):
                pn = e.get("phase_name") or e.get("phaseName")
                if isinstance(pn, str):
                    tactics.append(pn)
    # common alternatives
    for k in ("tactic", "tactics", "phases"):
        v = item.get(k)
        if isinstance(v, list):
            for s in v:
                if isinstance(s, str):
                    tactics.append(s)
        elif isinstance(v, str):
            tactics.append(v)
    # de-dup while preserving order
    seen = set()
    out = []
    for t in tactics:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def match_item(
    item: Dict[str, Any],
    query: str,
    mode: str,
    field: str,
    compiled_re: Optional[re.Pattern[str]] = None,
) -> bool:
    """Return True if item matches."""
    q_norm = query.lower()
    id_val = extract_id(item) or ""
    name_val = extract_name(item) or ""
    desc_val = extract_description(item) or ""

    def field_texts() -> Iterable[str]:
        if field == "id":
            yield id_val
        elif field == "name":
            yield name_val
        elif field == "description":
            yield desc_val
        else:
            yield id_val
            yield name_val
            yield desc_val

    if mode == "exact_id":
        return id_val == normalize_attack_id(query)
    if mode == "regex":
        assert compiled_re is not None
        return any(bool(compiled_re.search(text)) for text in field_texts())
    # contains (case-insensitive)
    return any(q_norm in (text or "").lower() for text in field_texts())


def truncate(s: str, width: int) -> str:
    if len(s) <= width:
        return s
    return s[: max(0, width - 1)] + "…"


def color(s: str, code: str, enabled: bool) -> str:
    if not enabled:
        return s
    return f"\033[{code}m{s}\033[0m"


def print_table(rows: List[Tuple[str, str, str]], use_color: bool, limit: int) -> None:
    """Render a simple table."""
    if not rows:
        print("No results.")
        return
    limited = rows[: max(1, limit)]
    id_w = max(len("ID"), *(len(r[0]) for r in limited))
    name_w = max(len("Name"), *(len(r[1]) for r in limited))
    tact_w = max(len("Tactics"), *(len(r[2]) for r in limited))
    header = f"{'ID'.ljust(id_w)}  {'Name'.ljust(name_w)}  {'Tactics'.ljust(tact_w)}"
    sep = "-" * len(header)
    print(color(header, "1", use_color))
    print(sep)
    for i, n, t in limited:
        print(f"{i.ljust(id_w)}  {truncate(n, name_w).ljust(name_w)}  {truncate(t, tact_w).ljust(tact_w)}")
    if len(rows) > len(limited):
        print(f"... {len(rows) - len(limited)} more omitted (use --limit to show more)")


def to_result_dict(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": extract_id(item),
        "name": extract_name(item),
        "description": extract_description(item),
        "tactics": extract_tactics(item),
        "raw": item,
    }


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    try:
        items = load_attack_data(args.file)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    use_color = sys.stdout.isatty() and not args.no_color

    results: List[Dict[str, Any]] = []
    for q in args.query:
        # Prefer exact ID when pattern matches to avoid noisy results.
        if is_attack_id(q):
            mode = "exact_id"
            compiled = None
        elif args.regex:
            mode = "regex"
            try:
                compiled = re.compile(q, re.IGNORECASE)
            except re.error as e:
                print(f"Invalid regex '{q}': {e}", file=sys.stderr)
                return 2
        else:
            mode = "contains"
            compiled = None

        for it in items:
            if match_item(it, q, mode, args.field, compiled):
                results.append(to_result_dict(it))

    # De-dup results by ID+Name to avoid listing same technique twice from multiple queries.
    dedup: Dict[Tuple[Optional[str], Optional[str]], Dict[str, Any]] = {}
    for r in results:
        key = (r["id"], r["name"])
        dedup[key] = r
    results = list(dedup.values())

    if args.as_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    # If a single exact-ID query with one match, show full detail.
    single_exact = len(args.query) == 1 and is_attack_id(args.query[0]) and len(results) == 1
    if single_exact:
        r = results[0]
        title = f"{r['id'] or 'UNKNOWN'}: {r['name'] or '(no name)'}"
        print(color(title, "1", use_color))
        tactics = ", ".join(r["tactics"]) if r["tactics"] else "(no tactics)"
        print(f"Tactics: {tactics}")
        print()
        print(r["description"] or "(no description)")
        return 0

    # Otherwise, show a compact table.
    table_rows: List[Tuple[str, str, str]] = []
    for r in results:
        table_rows.append(
            (r["id"] or "", r["name"] or "", ", ".join(r["tactics"]) if r["tactics"] else "")
        )
    print_table(table_rows, use_color=use_color, limit=args.limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
