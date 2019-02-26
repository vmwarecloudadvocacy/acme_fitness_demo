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

Before running catalog please add the following secret
```
kubectl create secret generic catalog-mongo-pass --from-literal=password=password
```

Next you need to run the following:
```
kubectl create -f catalog-db-initdb-configmap.yaml
```

This will initialize the DB with the catalog items.

## users

Before running users please add the following secret
```
kubectl create secret generic users-mongo-pass --from-literal=password=password
```

Next you need to run the following:
```
kubectl create -f users-db-initdb-configmap.yaml
```

This will initialize the DB with the catalog items.


