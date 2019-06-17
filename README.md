# Demo of ACME Fitness App

## Getting Started

These instructions will allow you to run entire ACME Fitness App 

## Requirements

Based on the type of deployment the requirements will vary 

1. **docker-compose** - Needs docker-compose version 1.23.1+
2. **kubernetes**
2. **helm**

Other deployment modes coming soon

## Overview

![Acmeshop Architecture](https://github.com/vmwarecloudadvocacy/acme_fitness_demo/blob/master/acmeshop.png)


## Instructions

1. Clone this repository 

2. You will notice the following directory structure

``` 
.
├── README.md
├── traffic-generator
├── docker-compose
│   ├── README.md
│   └── docker-compose.yml
├── kubernetes-manifests
│   ├── README.md
│   ├── cart-redis-total.yaml
│   ├── cart-total.yaml
│   ├── catalog-db-initdb-configmap.yaml
│   ├── catalog-db-total.yaml
│   ├── catalog-total.yaml
│   ├── frontend-total.yaml
│   ├── order-db-total.yaml
│   ├── order-total.yaml
│   ├── payment-total.yaml
│   ├── users-db-initdb-configmap.yaml
│   ├── users-db-total.yaml
│   ├── users-total.yaml
└── helm
    ├── README.md
    └── acmefitness
        ├── Chart.yaml
        ├── values.yaml
        └── templates
```

3. Switch to the appropriate directory for deployment

a. [docker-compose](docker-compose)  
b. [kubernetes-manifest](kubernetes-manifests)  
b. [helm](helm)  


### Additional Info

The [traffic-generator](traffic-generator) is based on **locust** and can be used to create various traffic patterns, if you need it for other demos associated with **Monitoring and Observability.** 

