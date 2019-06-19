# Wavefront - Kubernetes with Jaeger Configuration

**This is a modified version of the configuration and installation instructions provided by Wavefront including updated kubernetes manifests. For the original documentation please follow the links below.**

[Kubernetes Setup](https://try.wavefront.com/integration/kubernetes/setup)
[Jaeger Integration Setup](https://try.wavefront.com/integration/jaeger/setup)

**This has been tested with AKS**

## Wavefront Proxy Deployment

### Deploy a Wavefront Proxy in Kubernetes
Download jaeger-wavefront.yaml to your system. Edit the file and set the following environment variables, container port and service port specifications.

**Wavefront**

* WAVEFRONT_URL
..* value: <YOUR WAVEFRONT URL>
* WAVEFRONT_TOKEN
..* value: <YOUR WAVEFRONT TOKEN>

**Wavefront Jaeger Integrations**

* WAVEFRONT_PROXY_ARGS
..* value: --traceJaegerListenerPorts <YOUR JAEGER PORT>

**Container Port**

Update the container port with the same port specified in the WAVEFRONT_PROXY_ARGS environment variable. 

```
# Jaeger Tracing Port
- containerPort: <YOUR JAEGER PORT>
  protocol: TCP
```

**Service Port**

Update the Service Port with the same Jaeger Port specified in the WAVEFRONT_PROXY_ARGS environment variable.

```
  # Added for Jaeger Tracing
  - name: jaeger
    port: <YOUR JAEGER PORT>
    targetPort: <YOUR JAEGER PORT>
    protocol: TCP
```

Run `kubectl create -f jaeger-wavefront.yaml` to deploy the proxy.

The Wavefront proxy and a wavefront-proxy service should now be running in Kubernetes.

## Kube-State Metrics

### Deploy the kube-state-metrics Service
Download kube-state.yaml to your system and `run kubectl create -f kube-state.yaml`.

The kube-state-metrics service should now be running on your cluster.

## Deploy Wavefront Kubernetes Collector
Download the wavefront-collector-dir to your system:

0-collector-namespace.yaml
1-collector-cluster-role.yaml
2-collector-rbac.yaml
3-collector-service-account.yaml
4-collector-deployment.yaml

### Edit 4-collector-deployment.yaml as follows:

Replace <YOUR CLUSTER NAME> to uniquely identify your Kubernetes cluster.

```
 command:
 - /wavefront-collector
 - --source=kubernetes.summary_api:''
 - --sink=wavefront:?proxyAddress=wavefront-proxy.default.svc.cluster.local:2878&clusterName=<YOUR CLUSTER NAME>&includeLabels=true
 - --v=2
```

Run `kubectl create -f </path/to/wavefront-collector-dir>/` to deploy the collector on your cluster.

To verify the collector is deployed, `run kubectl get pods -n wavefront-collector`.

If you do not see metrics in the Kubernetes dashboard, check the logs from the collector and proxy pods.