# SciCat Data Catalogue Developer Guide

This guide aims to help developers understand the overall structure of the software and therefore enables people to contribute back to develop and improve this tool.
Please refer to [Overview in the Operator Manual](../Operator/) for a bird-eye view of the components that are part of SciCat.

If you want to contribute to this software, please read the [Contributing](./contributing.md) section, which among others links to the git workflow to be used.

## Introduction to SciCat architecture
SciCat architecture has been designed embracing the micro-services philosophy.
The software has two main components:
* Frontend
* Backend

with the addition of a mongodb instance which is not included in the distribution. It is left to each facility how to deploy the database in their IT infrastructure
The two main components are build with different technologies, listed  in teh following two sections.
It is highly recommended to familiarize with all the tools and technologies listed below before starting to develop for SciCat project.

### Backend
The backend provides the REST API with all the functionalities related to data management.
You can read a brief introduction in the [overview](./backend_overview.html) and more indepth information in the [related pages](./backend/backend.html)
Technologies:
* [Node > 16.x](https://nodejs.org/en/)
* [NestJs > 9.x](https://nestjs.com)
* [MongoDB > 3.x](https://www.mongodb.com)


### Frontend
The frontend provides a single page UI application running in the browser intended to provide a easy to use interface to the backend functionalities
Technologies:
* [Angular 9+](https://angular.io/)
* [Angular Material Widgets and Design](https://material.angular.io/)
* [NGRX for State Management](https://ngrx.io/)
* [Loopback SDK generator for Angular](https://github.com/mean-expert-official/loopback-sdk-builder)


### Optional tools
This section lisrt additional tools and materials that might be used in some of the instances of SciCat
#### Messaging/Streaming/Processing
* [Apache Kafka](https://kafka.apache.org/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Nodered Browser-based flow programming](https://nodered.org/)
