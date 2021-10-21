#!/bin/bash
if [ $# -lt 1 ]; then
  echo "Usage: apply_smooth_shape_traffic.sh <namespace>"
  exit 1
fi

pods=`kubectl -n $1 get pods -o name --ignore-not-found=true -l app=acme-locust`
kubectl -n $1 delete configmap --ignore-not-found=true acme-locustfile-shaped
kubectl -n $1 create configmap acme-locustfile-shaped --from-file=locustfile.py=./locustfile.py --from-file=shape.py=./shape_smooth.py
kubectl -n $1 apply -f headless_shaped_loadgen.yaml
if [[ $pods ]]; then
    kubectl -n $1 delete --ignore-not-found=true ${pods}
fi
