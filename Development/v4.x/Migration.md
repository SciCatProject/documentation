# Migrating from the old SciCat Backend

SciCat v4.x is a major rewrite from [v3.x](https://github.com/SciCatProject/backend-v3). The backend has been rewritten in typescript. It uses NestJS rather than Loopback 3 for the API, and includes a large number of new features. Version 3 is now considered deprecated and will receive only maintenance updates.

This document is intended to help users of backend-v3 migrate to v4. It also describes major breaking changes between the two versions that will need to be updated in scicat clients or scripts.

## Database changes

Where the [current SciCat Backend](https://github.com/SciCatProject/backend) accepts id fields in the database named `pid`, `doi`, or similar, this implementation requires there to be an id field of the form `_id` on every document. It is therefore necessary to run a database migration script towards MongoDB instance from a place where you have access to it and can install `migrate-mongo` package.

All database [migration scripts](https://github.com/SciCatProject/scicat-backend-next/tree/master/migrations) are located in the [migrations](https://github.com/SciCatProject/scicat-backend-next/tree/master/migrations) folder.
* To run the migrations locally you just need to install all dependencies and run `npm run start` which will run the migrations first and start the application. If you want to run the migrations manually you can install `migrate-mongo` package globally and run `migrate-mongo up` or if it is already installed locally because is part of the dependencies it is possible to just run: `node ./node_modules/migrate-mongo/bin/migrate-mongo.js up`.
* To run the migrations on the server you will need to copy the [migration scripts](https://github.com/SciCatProject/scicat-backend-next/tree/master/migrations) together with [`migrate-mongo-config.js`](https://github.com/SciCatProject/scicat-backend-next/blob/master/migrate-mongo-config.js) file to a location were you can access your MongoDB instance and have `migrate-mongo` package installed either globally(which is preferred) or locally if global installation is not possible. Then modify the config file to contain your MongoDB instance details like database name and url. Once modified, start the migration by running

```sh
migrate-mongo up
```

if `migrate-mongo` is installed globally at the location where you want to run it from or if it is locally installed just run

```sh
./node_modules/migrate-mongo/bin/migrate-mongo.js up
```

## API changes

### Base URL

The scicat API was previously served at `/api/v3`. Many of the endpoints are backwards
compatible and are still served at the same address. However, several schemas have added
non-backwards-compabible features (eg. `Datasets`, `Attachements`, and `Jobs`). For
these it is recommended to access the new `/api/v4` endpoints. Old `/api/v3` endpoints
are still available for backwards compatibility, but will be removed in a future
version.

<!-- TODO: provide more details about the updated DTOs -->

### Authorization

Version 3 endpoints were authenticated by including an `access_token` query parameter in
the URL. Following best practices, this has been changed to use the HTTP `Authorization:
Bearer` header to pass the access token. All scicat clients must be updated for this
change, even those using the otherwise backwards-compatible `/api/v3` endpoints.

## Migration documentation and NestJs resources
Following are the post that I found useful working on the migration:
- Schema and DTOs: https://betterprogramming.pub/how-to-use-data-transfer-objects-dto-for-validation-in-nest-js-7ff95309f650
- Validation:
  - [Official documentation](https://docs.nestjs.com/techniques/validation)
  - [Custom validation with datasbase in NestJs](https://dev.to/avantar/custom-validation-with-database-in-nestjs-gao)
  - [Validating nested objects with class-validator in NestJs](https://dev.to/avantar/validating-nested-objects-with-class-validator-in-nestjs-1gn8)
  - [Validating numeric query parameters in NestJS](https://dev.to/avantar/validating-numeric-query-parameters-in-nestjs-gk9)
  - [Injecting request object to a custom validation class in NestJS](https://dev.to/avantar/injecting-request-object-to-a-custom-validation-class-in-nestjs-5dal)
- Swagger and OpenAPI:
  - https://docs.nestjs.com/openapi/introduction
  - https://docs.nestjs.com/openapi/types-and-parameters
  - https://docs.nestjs.com/openapi/decorators
---

For the full documentation please go to the [SciCat home page](https://scicatproject.github.io/) and follow the [documentation link](https://scicatproject.github.io/documentation)
