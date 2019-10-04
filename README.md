# Demo of ACME Fitness Shop

## Getting Started

These instructions will allow you to run entire ACME Fitness Shop

## Requirements

Based on the type of deployment the requirements will vary

1. **docker-compose** - Needs docker-compose version 1.23.1+
2. **kubernetes**
3. **AWS Fargate** 

Other deployment modes coming soon

## Overview

![Acmeshop Architecture](./acmeshop.png)

## Instructions

1. Clone this repository

2. You will notice the following directory structure

```text
├── README.md
├── acmeshop.png
├── aws-fargate
│   ├── README.md
│   ├── acme-fitness-shop.yaml
│   └── cf-template.png
├── docker-compose
│   ├── README.md
│   └── docker-compose.yml
├── kubernetes-manifests
│   ├── README.md
│   ├── cart-redis-total.yaml
│   ├── cart-total.yaml
│   ├── catalog-db-initdb-configmap.yaml
│   ├── catalog-db-total.yaml
│   ├── catalog-total.yaml
│   ├── catalog-v2-total.yaml
│   ├── frontend-total.yaml
│   ├── order-db-total.yaml
│   ├── order-total.yaml
│   ├── payment-total.yaml
│   ├── users-db-initdb-configmap.yaml
│   ├── users-db-total.yaml
│   └── users-total.yaml
└── traffic-generator
    ├── README.md
    ├── locustfile.py
    └── requirements.txt
```

3. Switch to the appropriate directory for deployment

* [docker-compose](./docker-compose)  
* [kubernetes-manifest](./kubernetes-manifests)
* [aws-fargate](./aws-fargate)

### Additional Info

The [traffic-generator](./traffic-generator) is based on **locust** and can be used to create various traffic patterns, if you need it for other demos associated with **Monitoring and Observability.**
