## So, you have just started working on SciCat?

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

