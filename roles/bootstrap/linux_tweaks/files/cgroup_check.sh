#!/bin/bash

set -euo pipefail

LIMIT=50000
CGROUPS="$(cat /proc/cgroups |tail -n +2 |awk '{print $3}')"
RESET_CACHE=0

while IFS= read -r c; do
  if [[ ${c} -gt ${LIMIT} ]]; then
    echo "Limit reached: ${c}"
    RESET_CACHE=1
  fi
done <<< "${CGROUPS}"

if [[ "${RESET_CACHE}" == "1" ]]; then
  echo "Reset filesystem cache"
  echo 3 > /proc/sys/vm/drop_caches
fi
