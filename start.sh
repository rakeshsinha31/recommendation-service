#!/bin/bash

# Change to the directory containing RECOMMENDER-SERVICE docker-compose.yml file
cd recommender/

# Docker swarm for RECOMMENDER-SERVICE
docker build -t recommender-service:latest .
docker swarm init
docker stack deploy -c docker-compose.yml recommender-service


# Change to the directory containing USER-PRODUCT-SERVICE docker-compose.yml file
cd ../userproduct/

# Docker swarm for RECOMMENDER-SERVICE
docker build -t user-product-service:latest .
docker stack deploy -c docker-compose.yml user-product-services

