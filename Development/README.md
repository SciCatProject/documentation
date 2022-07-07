# SciCat Data Catalogue Developer Guide

This guide aims to help developers understand the overall structure of the software and therefore enables people to contribute to the development of the software. See also the [Overview in the Operator Manual](../Operator/) for a helicopter view of the involved components.

If you want to contribute to the software you should also read the [Contributing](../Development/Development_Methods.html) section, which among others links to the git workflow to be used.


# Getting an development environment set up
The easiest is to follow [this description](https://github.com/SciCatProject/scicatlive#readme) to get a fully running frontend and backend setup automatically using docker. Otherwise follow the [Running section](Running.html)

# Architecture
SciCat is built on micro services using the following stack:

## API (Catamel)

* [Node 12.x](https://nodejs.org/en/)
* [Loopback 3](https://loopback.io/lb3)
* [MongoDB 3.6 or later](https://www.mongodb.com)

The most important part to understand is how loopback works, because it is the platform which is directly addressed as part of the development. Please check the corresponding Loopback 3 documentation for all details

## Web Browser Client (Frontend)

* [Angular 9+](https://angular.io/) 
* [Angular Material Widgets and Design](https://material.angular.io/) 
* [NGRX for State Management](https://ngrx.io/)
* [Loopback SDK generator for Angular](https://github.com/mean-expert-official/loopback-sdk-builder)


Again please of a look at the original documentation to understand how these tools and frameworks work.

## Optional Messaging/Streaming/Processing tools

* [Apache Kafka](https://kafka.apache.org/) or [RabbitMQ](https://www.rabbitmq.com/)
* [Nodered Browser-based flow programming](https://nodered.org/)
