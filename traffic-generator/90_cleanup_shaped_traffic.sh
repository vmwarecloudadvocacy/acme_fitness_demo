#!/bin/bash
if [ $# -lt 1 ]; then
  echo "Usage: cleanup_shaped_traffic.sh <namespace>"
  exit 1
fi

kubectl -n $1 delete configmap --ignore-not-found=true acme-locustfile-shaped
kubectl -n $1 delete deploy --ignore-not-found=true acme-locust
