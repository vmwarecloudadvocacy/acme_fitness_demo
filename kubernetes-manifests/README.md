# ACMEFIT K8s

This repo contains a Polyglot demo application comprised of (presently) 6 microservices and 4 datastores.

The contents here are the necessary YAML files to deploy the ACMEFIT application in a kubernetes cluster.

This app is developed by team behind www.cloudjourney.io

The current version of the application passes JSON Web Tokens (JWT) for authentication on certain API calls. The application will not work as expected if the `users` service is not present to issue / authenticate these tokens.

## Datastore Dependent Services

This section covers the deployment of the datastore dependent microservices. It is recommended to deploy these services first.

### Cart Service

Before deploying the cart datastore (Redis) and cart service please add a secret for the service to use in authenticating with the cache.
*Note: Please replace 'value' in the command below with the desired password text. Changing the name of the secret object or the 'password' key may cause deployment issues*

```
kubectl create secret generic cart-redis-pass --from-literal=password=<value>
```

Once the secret object is created, deploy the redis cache and cart service:

```
kubectl apply -f cart-redis-total.yaml
kubectl apply -f cart-total.yaml
```

### Catalog Service

Before deploying the catalog datastore (mongo) and catalog service please add a secret for the service to use in authenticating with the cache.
*Note: Please replace 'value' in the command below with the desired password text. Changing the name of the secret object or the 'password' key may cause deployment issues*

```
kubectl create secret generic catalog-mongo-pass --from-literal=password=<value>
```

Run the following command to initialize the catalog database with items:

```
kubectl create -f catalog-db-initdb-configmap.yaml
```

Finally, deploy the mongo instance and catalog service:

```
kubectl apply -f catalog-db-total.yaml
kubectl apply -f catalog-total.yaml
```
### Payment Service

The payment service does not have an associated datastore. It can be deployed with the following command:

```
kubectl apply -f payment-total.yaml
```
   NOTE: PAYMENT SERVICE MUST BE UP FIRST IN ORDER FOR ORDER SERVICE TO PROPERLY COMPLETE TRANSACTIONS
   
### Order Service

Before deploying the orders datastore (postgres) and order service please add a secret for the service to use in authenticating with the cache.
*Note: Please replace 'value' in the command below with the desired password text. Changing the name of the secret object or the 'password' key may cause deployment issues*

Before running order please add the following secret:

```
kubectl create secret generic order-postgres-pass --from-literal=password=<value>
```

Once the secret object is created, deploy the mongo instance and order service:

```
kubectl apply -f order-db-total.yaml
kubectl apply -f order-total.yaml
```

### Users Service

Before deploying the users datastore (mongo), users cache (redis) and users service please add secrets for the service to use in authenticating with the database and cache.
*Note: Please replace 'value' in the command below with the desired password text. Changing the name of the secret object or the 'password' key may cause deployment issues*

Before running order please add the following secret:

```
kubectl create secret generic users-mongo-pass --from-literal=password=<value>
kubectl create secret generic users-redis-pass --from-literal=password=<value>
```

Next you need to run the following to initialize the database with an initial set of users:

```
kubectl create -f users-db-initdb-configmap.yaml
```

Once the secret object is created, and the users database is seeded, deploy the users database and users service:

```
kubectl apply -f users-db-total.yaml
kubectl apply -f users-redis-total.yaml
kubectl apply -f users-total.yaml
```
**_NOTE: The base set of users is preconfigured. For now, please login as one of this set (eric, dwight, han, or phoebe). The password for these users is 'vmware1!'_**

## Datastore Independent Services

### Front End Service

The front end service also functions without an associated datastore. The manifests in this repository deploy the front end service as a NodePort type for testing purposes. If suitable for the deployment environment, the service type could be changed to 'LoadBalancer' in the `frontend-total.yaml` manifest in this repository.

To deploy the front end service, run the following command:

```
kubectl apply -f frontend-total.yaml
```

To find the external port on which to access the site in browser, run the following command:

```
kubectl get services -l service=frontend
```

The output of the above command should be similar to this:

```
$ kubectl get services -l service=frontend
NAME       TYPE       CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
frontend   NodePort   10.0.0.81    <none>        3000:30430/TCP   3d
```

The external value appears under 'PORT(S)'. It is after the '3000:' and before the '/TCP' portion of the string. Appending it to the public address of the Kubernetes cluster (or loadbalancer fronting the cluster) to access the site.

### Point-of-Sales

Just like the front end service, the Point-of-Sales app functions without any associated datastores. The only prerequisite is that the FrontEnd service is deployed. The manifests in this repository deploy the Point-of-Sales service as a NodePort type for testing purposes. If you're running the Point-of-Sales app on a different Kubernetes cluster, or as a standalone container, you'll have to update the value of `FRONTEND_HOST` (set to `frontend.default.svc.cluster.local` by default) to match the IP or FQDN of the front end service.

To deploy the service, run the following command:

```
kubectl apply -f point-of-sales-total.yaml
```

To find the external port on which to access the site in browser, run the following command:

```
kubectl get services -l service=pos
```

The output of the above command should be similar to this:

```
$ kubectl get services -l service=frontend
NAME       TYPE       CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
pos        NodePort   10.0.0.81    <none>        3000:30431/TCP   3d
```

The external value appears under 'PORT(S)'. It is after the '3000:' and before the '/TCP' portion of the string. Appending it to the public address of the Kubernetes cluster (or loadbalancer fronting the cluster) to access the Point-of-Sales app.

## Distributed Tracing

**Note: Distributed tracing is advanced functionality which requires additional configuration to use successfully. Please read this section carefully before attempting to test / demonstrate tracing**

The current version of the application has been augmented with distributed tracing funcionality. Each of the services has two relevant environment vairables `JAEGER_AGENT_HOST` and `JAEGER_AGENT_PORT`. Regardless of the span aggregator being used, the code expects that these two values to be populates with the hostname and port of whichever span collecter is being used *likely the jaeger agent*.

To avoid issues with unresolvable hostnames, `JAEGER_AGENT_HOST` is set to `localhost` in all of the manifests in this repo. To use tracing, this value will need to be replaced. If using the `jaeger-all-in-one.yml` manifest included in this repo, this value should be changed to `jaeger.<jaeger namespace>`.

It is strongly recommended that the `JAEGER_AGENT_PORT` values not be modified as the tracing library implementations for specific languages favor certain ports.
