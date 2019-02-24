# order and cart services

## cart

Before running cart please add the following secret
kubectl create secret generic redis-pass --from-literal=password=password

## order

Before running order please add the following secret
kubectl create secret generic order-mongo-pass --from-literal=password=password
