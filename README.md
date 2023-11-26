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
 ┣ 📂recommender                         => Destination folder for all the auto created .js files
 ┃ ┃ 📂authapp                        => Source directory
 ┃ ┣ ┣ ┣ 📂migrations
 ┃ ┃ ┃  ┣📜0001_initial.py           => Client to conect to mongodb database
 ┃ ┃ ┣ 📜admin.py                => Contains all the cities as object
 ┃ ┃ ┣ 📜apps.py      => Comume messages published by publish service
 ┃ ┃ ┗ 📜models.py                  => Entrypoint for the application
 ┃ ┃ ┗ 📜serializers.py     => Publish message to the message broker
 ┃ ┃ ┗ 📜urls.py
 ┃ ┃ ┗ 📜views.py     => Integrates extenal API
 ┣ ┃ ┗📂reconapp                        => Source directory
 ┃ ┣ ┣ ┣ 📂migrations
 ┃ ┃ ┃  ┣📜0001_initial.py           => Client to conect to mongodb database
 ┃ ┃ ┣ 📜admin.py                => Contains all the cities as object
 ┃ ┃ ┣ 📜apps.py      => Comume messages published by publish service
 ┃ ┃ ┗ 📜models.py                  => Entrypoint for the application
 ┃ ┃ ┗ 📜serializers.py     => Publish message to the message broker
 ┃ ┃ ┗ 📜urls.py
 ┃ ┃ ┗ 📜views.py                        => Configuration files
 ┣ 📜start.sh           => bash file to start apps
 ┣ 📜README.md                  => READ FILE
```
