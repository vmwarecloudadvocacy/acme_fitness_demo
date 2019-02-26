# order and cart services

## cart

Before running cart please add the following secret
```
kubectl create secret generic redis-pass --from-literal=password=password
```

## order

Before running order please add the following secret
```
kubectl create secret generic order-mongo-pass --from-literal=password=password
```

## catalog

Before running order please add the following secret
```
kubectl create secret generic catalog-mongo-pass --from-literal=password=password
```

Next you need to run the following:
```
kubectl create -f catalog-db-initdb-configmap.yaml
```

This will initialize the DB with the catalog items.


