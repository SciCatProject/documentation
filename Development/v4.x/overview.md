# Overview of SciCat

___This page needs to be updated___

This page provides a brief introduction to the overall workings of the SciCat data model, how things connect and links to more details on each component.

## Backend

The SciCat backend provides the REST API of the all system. It uses MongoDB to store all persistent information and leverages individual dtos to validate the information provided in input.

### Model Definitions:

* Properties: These are the values, types and other information. None of these are mongo specific and can all map to a relational database just as easily.
* Relations: These link models, i.e. allowing a DatasetLifecycle to be linked to a Dataset. The mongo connector handles this by embedding the datasetId in the document for you.
* ACLs: These are access control limitations and these are very powerful. You can give a user full control of a model, some users can only have read access etc.
* Methods: When you create a model, loopback will automagically generate API endpoints that allows users to PUT, POST, PATCH, GET etc for all the models. However, sometimes this is not enough. For example, you may want to be able to generate a monthly report of all datasets created, so you define the method here, the name of the endpoint and the expected parameters. You will implement the method in the next section we cover now.

### Model Implementation:

SciCat backend leverages nest.js and each endpoint is implemented by a specific function in the controller component of the associated model.
The models are defined in the model folder of each endpoint/model.
It leverages nest.js interface to Mongoose.
Mode details are found in each individual page

### Running the backend

The backend can be run as it is, provided that a number of environmental variables are defined.
For the list of the environment variables available please see the [Backend Configuration page](Documentation/v4.x/backend/configuration.md).

To start the backend is as simple as running the following command:
```
npm start
```

### Testing the backend
There are multiple type of tests that can be run on the backend:
- unit tests
  They can be run using the command:
  ```
  npm run tests
  ```
- api tests
  These tests are defined in the `test` folder and tests the endpoint. 
  To run them use the command:
  ```
  npm run test:api:mocha
  ```

