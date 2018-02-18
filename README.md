# SciCat

## What?

A project to catalogue and provide access to metdatdata and raw experimental data.

<<<<<<< HEAD
## How?

Scicat is made up of the following technologies:

* Web based frontend - [Catanie](https://github.com/SciCatProject/catanie): An Angular \(2+\) based application that uses ngrx to communicate with the SciCat API and provide a searchable interface for datasets, as well as the option to carry out actions \(i.e. archiving\) and acts as a place to reference datasets used in publications.

* API Server - [Catamel: ](https://github.com/SciCatProject/catamel)A NodeJS application that uses the Loopback framework to generate RESTful APIs from JSON files that define models \(such as: Users, Datasets, Instruments etc\). Follows the Swagger API format and SDKs can be generated in almost any language.

* Database - MongoDB
* Data Ingesting - NODE-RED: A NodeJS based visual programming tool to handle flows of data from one source to another.
* 


=======
## Building and Editing Locally

`npm i -g gitbook-cli`

`gitbook install`

`gitbook build . docs/`
The command above could be useful to put into a git hook to ensure that a build is made on each push.

## Summaries

The TOC for a Gitbook is read from the `Summary.md`, this can be handled by the python script: `summary_generator.py`

## Pre Commit Hook

```
#!/bin/sh

cd $DACATHOME/docs
python summary_generator.py
gitbook build . docs/
git add .
```
>>>>>>> 1af3b1299dcbad649fd24c7b9eb5b956c964a138
