## Pre-requisites

- Install Docker - [Docker >= 20.10.7](https://docs.docker.com/get-docker/)
- Install Python - [Python >= 3.10.6](https://www.python.org/downloads/)
  <br/>

## Start applications by running docker containers

- cd /path/to/application/parent_folder <cybertrust>/
- docker compose up

## Run Application Locally

- cd /path/to/application/parent_folder <cybertrust>/
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

- transactionapi/get_dataset/<id>/ (Transaction History)

## Understanding Code Structure

Folderstructure and what each file does.

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
