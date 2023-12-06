## Description
Product recommendation application, based on customer's transaction history.
This repo contains two Microservices, running on separate PORTS (Yeah! I know each MS should have its own repo :-(, 
it will be done as an upcoming enhancement)

The projects are orchestrated ``` using Docker & Docker Swarm ``` for Scalability and reliability.
The Application doesn't support Auto Scaling. Kubernetes would have been a better option in that case, 
but due to time constraints I have chosen to use Docker Swarm

1. Recommender (port: 8000):
   This project has two applications - Auth and Recon. This exposes endpoints to:
    - Register a user
    - Login
    - Recommend products for a given customer

  
2. User-Product (port: 8001):
  This project has two applications - User and Product. This exposes endpoints to:
    - Create a Customer
    - Get all/single Customer profile
    - Update Customer Profile
    - Create a Product
    - Get all/single Products
    - Update a Product

Usage:
  See the Endpoints section


## Pre-requisites

- Install Docker - [Docker >= 20.10.7](https://docs.docker.com/get-docker/)
- Install Python - [Python >= 3.10.6](https://www.python.org/downloads/)
  <br/>

## Run Application Locally

- git clone https://github.com/rakeshsinha31/recommendation-service.git
- cd recommendation-service/
- ./start.sh

## Endpoints

RecommenderApp

POST:

- /authapi/register
- /authapi/login

GET

- /authapi/user
- /reconapi/recommendations/<customer ID: int> (Fetch Recommendations for given customer ID)

User_Product App
Customer APIs
POST:

- /customerapi/products/
- /customerapi/user-profiles/

PATCH:

- /customerapi/products/<id>/
- /customerapi/user-profiles/<id>/

GET:

- /customerapi/user-profiles/
- /customerapi/user-profiles/<id>/
- /customerapi/products/
- /customerapi/products/<id>/

Transaction APIs

POST:

- /transactionapi/create-transaction/1/

GET:

- transactionapi/get_dataset/<id: int>/ (Transaction History)

## Understanding Code Structure

Folder structure and file description.
```
📦CYBERTRUST
 ┣ 📂RECOMMENDER           => Django Project (Recommender Service)
 ┃ ┃ 📂authapp              => Auth App
 ┃ ┣ ┣ ┣ 📂migrations
 ┃ ┃ ┃  ┣📜0001_initial.py
 ┃ ┃ ┣ 📜admin.py           => admin file
 ┃ ┃ ┣ 📜apps.py            => app file
 ┃ ┃ ┗ 📜models.py          => Models for authapp
 ┃ ┃ ┗ 📜serializers.py     => auth serializer
 ┃ ┃ ┗ 📜urls.py            => auth urls
 ┃ ┃ ┗ 📜views.py           => auth view
 ┣ ┃ ┗📂reconapp            => Recommendation App
 ┃ ┣ ┣ ┣ 📂migrations
 ┃ ┃ ┃  ┣📜0001_initial.py
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┗ 📜models.py
 ┃ ┃ ┗ 📜serializers.py
 ┃ ┃ ┗ 📜urls.py
 ┃ ┃ ┗ 📜views.py
 ┣ 📂USERPRODUCT            => Django Project (UserProduct Service)
 ┃ ┃ 📂transactions         => Transactions  App
 ┃ ┣ ┣ ┣ 📂migrations
 ┃ ┃ ┃  ┣📜0001_initial.py
 ┃ ┃ ┣ 📜admin.py           => admin file
 ┃ ┃ ┣ 📜apps.py            => app file
 ┃ ┃ ┗ 📜models.py          => Models for authapp
 ┃ ┃ ┗ 📜serializers.py     => auth serializer
 ┃ ┃ ┗ 📜urls.py            => auth urls
 ┃ ┃ ┗ 📜views.py           => auth view
 ┣ ┃ ┗📂user                => Customer App
 ┃ ┣ ┣ ┣ 📂migrations
 ┃ ┃ ┃  ┣📜0001_initial.py
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┗ 📜models.py
 ┃ ┃ ┗ 📜serializers.py
 ┃ ┃ ┗ 📜urls.py
 ┃ ┃ ┗ 📜views.py
 ┣ 📜start.sh               => Entry point for both the projects
 ┣ 📜README.md              => Ream Me
```
