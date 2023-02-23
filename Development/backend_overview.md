## Backend Overview

This page provides a brief introduction on SciCat backend, its components and how it works.

The backend is the key component which implements all the functionalities to manage, save and retrieve all the user data, interact with the database and develop relationships between entities of the data.
We suggest that you get familiar with all the tools and technologies that are used in SciCat backend.

SciCat backend stores all data in a MongoDB instance. The database is completely managed by the backend through the mongoose library and the nestjs connector to mongoose.

The backend source files are organized by functionalities/endpoints. the main `src` folder contains the main and app files, and a series of folders, each one implementing all the endpoints related to a specific model/entity defined in SciCat, simply called _endpoint folders_.  Each endpoint folder contains all the necessary fiels to implement the REST api, the database intagration, the data model and DTOs. Usually a normal endpoint folder will contain the following files and folders:
* dto: folder containing all the DTOs used with this model. 
* interceptors: nestjs implementation of functions that always need to be run before or after a specific endpoint or function. Please visit the [interceptor](https://docs.nestjs.com/interceptors) documentation to learn more on nestjs interceptors
* interfaces: javascript interfaces implementation for various data structures used in the module
* schemas: schema files used by nestjs and mongoose to create entries in the database
* controller: controller file with all the endpoints available for the current model
* module: main module file containing the nestjs definition of the current model with its endpoints, services and data structures. Please visit this [module](https://docs.nestjs.com/modules) documentation to learn more about nestjs modules
* service: service file containing all the functionalities to store and retrieve all the instances of the current model. Please visit the [service](https://docs.nestjs.com/providers#services) documentation to learn more about nestjs services


#### Running the backend

In order to run the backend locally, the configuration needs to be customized. You can do that by editing directly the file 
```
src/config/configuration.ts
``` 
or, follow the preferred solution, define the configuration values through environment variables as specified in the backend [Configuration]() page.
Once the configuration is set, and a mongo instance is accessible, you can run the backend locally using the command:
```
npm run start
```

#### Testing the backend

All tests for the backend are in the `test` folder in the root of the repo.
To run the tests, make sure that the backend is running (please the previous section for a quick how-to) and than run the following command at the terminal:
```
npm run test
```

## Python Client API
__to be reviewed__
The python API can be generated automatically running the command below and using the Swagger/openAPI (http://swagger.io/) specification created from the data model using the [Swagger Codegen code](https://github.com/swagger-api/swagger-codegen)

```
java -jar ./swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i swagger.json -l python -o scicat-backend/client/python
```

