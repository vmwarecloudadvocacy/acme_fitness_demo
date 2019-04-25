# ACMEFIT K8s

This repo contains a Polyglot demo application comprised of (presently) 6 microservices and 4 datastores.

The contents here are the necessary YAML files to deploy the ACMEFIT application in a kubernetes cluster.

This app is developed by team behind www.cloudjourney.io

## Datastore Dependent Services

This section covers the deployment of the datastore dependent microservices. It is recommended to deploy these services first.

### Cart Service

Before deploying the cart datastore (Redis) and cart service please add a secret for the service to use in authenticating with the cache.
*Note: Please replace 'value' in the command below with the desired password text. Changing the name of the secret object or the 'password' key may cause deployment issues*

```
kubectl create secret generic redis-pass --from-literal=password=<value>
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

Before deploying the orders datastore (mongo) and order service please add a secret for the service to use in authenticating with the cache.
*Note: Please replace 'value' in the command below with the desired password text. Changing the name of the secret object or the 'password' key may cause deployment issues*

Before running order please add the following secret:

```
kubectl create secret generic order-mongo-pass --from-literal=password=<value>
```

Once the secret object is created, deploy the mongo instance and order service:

```
kubectl apply -f order-db-total.yaml
kubectl apply -f order-total.yaml
```

### Users Service

Before deploying the users datastore (mongo) and users service please add a secret for the service to use in authenticating with the cache.
*Note: Please replace 'value' in the command below with the desired password text. Changing the name of the secret object or the 'password' key may cause deployment issues*

Before running order please add the following secret:

```
kubectl create secret generic users-mongo-pass --from-literal=password=<value>
```

Next you need to run the following to initialize the database with an initial set of users:

```
kubectl create -f users-db-initdb-configmap.yaml
```

Once the secret object is created, and the users database is seeded, deploy the users database and users service:

```
kubectl apply -f users-db-total.yaml
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
