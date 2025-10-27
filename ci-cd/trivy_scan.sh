# ci-cd/trivy_scan.sh

#!/bin/bash

IMAGE=$1
OUTPUT="trivy_report_$(date +%F).txt"

if [ -z "$IMAGE" ]; then
  echo "Usage: ./trivy_scan.sh <docker-image>"
  exit 1
fi

echo "Scanning $IMAGE..."
trivy image $IMAGE > $OUTPUT
echo "Report saved to $OUTPUT"
