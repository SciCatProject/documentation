# SciCat Data Catalogue Developer Guide

SciCat is a data catalogue web application that provides a searchable interface for datasets, a method of publishing DOIs, as well as the option to carry out actions (i.e. archiving and publishing) and acts as a place to reference datasets used in publications.

This guide aims to help developers and system admins understand some of the SciCat components.

SciCat is built on micro services using the following stack:

## Web Browser Client (Catanie)

* node
* npm
* typescript
* angular
* NGRX
* loopback SDK generator

## API (Catamel)

* node
* js
* loopback
* mongoDB


![systen_components](img/micro.png)

Unit tests are explained in this page
[Testing](Testing)

Ngrx is the Angular implementation of Redux state management
[Ngrx](Ngrx)

Users can archive data  using the Archive interface1
[Archiving](Archiving)
