## Overview of Backend and Model

This page provides a brief introduction to the overall workings of the SciCat data model, how things connect and links to more details on each component.

### Catamel

First off, the backend is the key component here and you will see there is next to hand written code here \(aside from some tests\). The folder you will be working in most is: `common/models` and this is NodeJS application based on the Loopback framework. Go away and read the docs for Loopback \(3\) and come back here when you are fairly comfortable. I'll wait.

Got it? Good. OK, so, SciCat stores all of its data in a MongoDB but you will almost never need to perform any admin on the database. The connection between loopback and Mongo is handled by the loopback-mongo-connector. The only thing you need to provide is the file in `server/datasources.json` , this provides the connection string and any connection specific info.

If you take a look at a model, you will see that some of them have a datasource of `transient` and others are specified as MongoDB. The `transient` models are not stored or handled by the mongo connector. You will see some other sections, so let's go through them:

#### Model Definitions:

* Properties: These are the values, types and other information. None of these are mongo specific and can all map to a relational database just as easily.
* Relations: These link models, i.e. allowing a DatasetLifecycle to be linked to a Dataset. The mongo connector handles this by embedding the datasetId in the document for you.
* ACLs: These are access control limitations and these are very powerful. You can give a user full control of a model, some users can only have read access etc.
* Methods: When you create a model, loopback will automagically generate API endpoints that allows users to PUT, POST, PATCH, GET etc for all the models. However, sometimes this is not enough. For example, you may want to be able to generate a monthly report of all datasets created, so you define the method here, the name of the endpoint and the expected parameters. You will implement the method in the next section we cover now.

#### Model Implementation:

As just mentioned, Loopback handles all the basic RESTful commands for a model for you but there are two ways to extend this:

* Custom methods: You can extend your model with methods that allow you to implement logic beyond what loopback provides
* Remote hooks: Before a particular endpoint \(or all endpoints\) are called, or before a document is saved/edited/accessed, then you can use these hooks to implement some logic. For example, you may want to inject some extra information into a JSON object before it is saved or ensure the user has some access control that is outside of your Loopback system.

For the best example of these, take a look at the Dataset JS and JSON files, this also shows how relations work between models.

#### Running Catamel

Catamel has some core files missing that are required in order for it to run. Below, we list these files and what they should contain. Ideally, there will be a minimal install of Catamel in the source repo that includes minimal config files to remove this barrier.

* `datasources.json` - This sets up your connection to Mongo and should follow the syntax outlined in [loopback](https://loopback.io/doc/en/lb3/datasources.json.html) . 
* `config.local.js` - These are site specific settings for your install, such as the prefix to use for IDs, messages to store in the dataset and the facilities you have
* `providers.json` - Contains connection information to LDAP or other authentication sources
* `component-config.json` - This file connects to RabbitMQ or (in the case of testing) connects to a local rabbitmq, but this file should not be required in the future so the queuing system used is not fixed. 

#### Editing the Configs

##### datasources.json
Make sure that the host field of the json is configured to your mongo hostname e.g. for a local instance of mongo with hostname "mongodb":
```
   "mongo": {
      "host": "mongodb",
      "port": 27017,
      "url": "",
      "database": "dacat",
      "name": "mongo",
      "connector": "mongodb",
      "useNewUrlParser": true,
      "allowExtendedOperators":true
    }

```
##### config.local.js
Here you can configure many aspects of scicat for your institute. Here is an example config file, where you delete parts to turn off certain features:
```
var p = require('../package.json');
var version = p.version.split('.').shift();
module.exports = {
    restApiRoot: '/api' + (version > 0 ? '/v' + version : ''),
    host: process.env.HOST || '0.0.0.0',
    port: process.env.PORT || 3000,
    pidPrefix: 'PutYourPIDPrefixHere',
    policyPublicationShiftInYears: 3,
    policyRetentionShiftInYears: 10,
    site: 'YOUR-SITE',
    facilities: ["Facility1", "Facility2"],
    metadataKeysReturnLimit: 100,
    registerMetadataUri : "https://mds.test.datacite.org/metadata",
    registerDoiUri : "https://mds.test.datacite.org/doi",
    grayLog: {
      enabled: false,
      host: "my.graylog.host",
      port: 0000,
      facility: "facility",
      owner: "owner",
      service: "service"
    },
	# Add to this section if you want to use RabbitMQ for the Proposals mechanism
    rabbitmq: {
      enabled: false,
      host: null,
      port: null,
      queue: null
    },
	# Remove this if you want to use the Jobs mechanism without SMTP or configure for your SMTP service.
    smtpSettings: {
      host: 'SMTP.YOUR.DOMAIN',
      port: 25,
      secure: false    },
    smtpMessage: {
      from: 'scicatarchivemanager@YOUR.DOMAIN',
      to: undefined,
      subject: '[SciCat '+process.env.NODE_ENV+']',
      text: undefined // can also set html key and this will override this
    },
	# Keep this if you want to set your queue service to rabbitmq, remove if you are not using a messaging service
    queue: 'rabbitmq'
};

```
##### component-config.json

If you want to use RabbitMQ to reach out to a microservice through the Jobs mechanism in Scicat you will need to edit the component-config.json file. You will also need to add the `queue: "rabbitmq"` line in the 
config.local.js file for this to work (see above section.) In order to connect to rabbitMQ you will need a user and password already defined in a rabbitMQ service to connect and the service should be up and running.
To set this up add the following to the component-config.json and change the username and password to those you have defined in your rabbitMQ service. Also edit the hostname in the `uri` field to be the hostname of your RabbitMQ service. 

```
"../node_modules/loopback-component-mq/lib":{
"options":{
"restPort":15672,
"acls":[
{
"accessType":"*",
"principalType":"ROLE",
"principalId":"$unauthenticated",
"permission":"DENY"
}
]
},
"topology":{
"connection":{
"uri":"amqp://<username>:<password>@<rabbitmqhost>:5672/"
},
"exchanges":[
{
"name":"jobs.write",
"type":"topic",
"persistent":true
}
],
"queues":[
{
"name":"client.jobs.write",
"subscribe":true
}
],
"bindings":[
{
"exchange":"jobs.write",
"target":"client.jobs.write",
"keys":[
"jobqueue"
]
}
]
}
}

```
For more info on setting up RabbitMQ see the Deploy with Docker Compose section.


#### Testing Catamel

All tests for catamel are in the `test` folder in the root of the repo and can be run with `npm run test`. 

## Python Client API
The API is automatically created from the Swagger/openAPI (http://swagger.io/) specificication created from the data model using the [Swagger Codegen code](https://github.com/swagger-api/swagger-codegen)

```
java -jar ./swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i swagger.json -l python -o dacat-api/client/python
```

