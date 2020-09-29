# Repository Overview

## Components

Scicat is made up of the following technologies:

* Web based frontend - [Catanie](https://github.com/SciCatProject/catanie): An Angular based application that uses ngrx to communicate with the SciCat API and provide a searchable interface for datasets, as well as the option to carry out actions \(i.e. archiving\).

* API Server - [Catamel: ](https://github.com/SciCatProject/catamel)A NodeJS application that uses the Loopback framework to generate RESTful APIs from JSON files that define models \(such as: Users, Datasets, Instruments etc\). Follows the Swagger API format and SDKs can be generated in almost any language.

* Database - [MongoDB](https://www.mongodb.com/) Free, open source, NoSQL, document-based database

* Data Ingestion - [Node-RED](https://nodered.org/): A NodeJS based visual programming tool to handle flows of data from one source to another.

## TODO work here...
## Catamel

Backend technology consisting of loopback in a Node.JS app, linking to a MongoDB database. In order for catamel to run locally \(without Kubernetes\) then the following software is required:

1. Node.JS \(and npm\)
2. MongoDB
3. RabbitMQ

For further setup instructions, please refer to the [Catamel README.](/./Devops/Catamel/README.md)

Catamel relies on two other repositories: config and secrets that handle the setup.

### Secrets

This repository holds site specific secrets \(primarily in the \`server\`  folder\). There are scripts in the Catamel repository to copy the contents in. Note that a symbolic link will **NOT** work as there are relative paths.

### Config

Config primarily holds configuration files for the Catamel, relating to the connection of datasources and middleware. 

## Catanie

The set up details for Catanie are in the [Catanie README.](/./Devops/Catanie/README.md) By default it connects to a localhost instance of Catamel, This can be changed by modifying the runtime environment.





