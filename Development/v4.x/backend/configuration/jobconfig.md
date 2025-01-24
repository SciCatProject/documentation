# Job Configuration

> _**Development Feature**. This section documents features that are still under
> development as part of the `release-jobs` branch._

## Overview

The SciCat job system is used for any interactions between SciCat and external services.

Example jobs include:

- Request an **archive system** to *archive* or *retrieve* data from tape storage
- Move data to a *public* location (e.g. to access data from a [DOI landing
  page](https://github.com/SciCatProject/LandingPageServer))
- Run maintenance tasks such as emailing users.

If you just plan to use SciCat for cataloging data and don't plan to use its data
management features then you may not need any job types. If no job types are configured then SciCat will reject any backend requests to create jobs. In this case [frontend features](../../frontend/configuration.md) for archiving (`archiveWorkflowEnabled: false`) and retrieval should be disabled.

### Migration Notes

In v3.x the `archive`, `retrieve`, and `public` jobs were hard-coded. In v4.x the job
types can be arbitrary strings; however we recommend using the standard job names to
avoid confusion.

Also note that some checks that were preformed by default in v3.x for certain job types
must now be configured explicitly as actions. These are included in the provided
`jobConfig.example.yaml` file and are also noted below.

### Job lifecycle

Jobs follow a standard Create-Read-Update-Delete (CRUD) lifecycle:

1. Jobs are _created_ via a `POST` request to `/jobs`. This can be the result of a frontend
   interaction (eg selecting a dataset for publishing) or through the REST API.

   The body of the request should follow the CreateJobDto (Data Transfer Object):
   ```json
   {
     "type": "archive",
     "ownerUser": "owner",
     "ownerGroup": "group",
     "contactEmail": "email@example.com"
     "jobParams": {}
   }
   ```
2. Jobs can be _read_ via a `GET` request to `/jobs/:id` or through the `/jobs/fullquery`
   search endpoint. The frontend uses this to display the list of jobs.
3. Jobs are _updated_ via a `PATCH` or `PUT` request to `/jobs/:id`. This is usually
   used by facility services to update the job status and provide feedback.

   The body of the request should follow the UpdateJobDto:
   ```
   {
     "statusCode": "string",
     "statusMessage": "string",
     "jobResultObject": {}
   }
   ```
4. Jobs may be _deleted_ periodically during maintenance. This is usually not done by
   users.

### Actions

After _create_ and _update_ stages, a series of actions can be performed by SciCat. This
can be things like sending an email, posting a message to a message broker, or calling
an API. The `jobParams` and `jobResultObject` are used to add additional information
that the actions may need, such as the list of datasets the job refers to.

A full list of built-in actions is given below. A plugin mechanism for registering new
actions is also planned for a future SciCat release.

## Configuration

In SciCat v3.x, a limited number of jobs were hard-coded into the code base. This was
changed in v4.x to allow each site to configure their own set of jobs and customize
actions based on the job status.

The available jobs are configured in the file `jobConfig.yaml` (or can be overridden
with the `JOB_CONFIGURATION_FILE` [environment
variable](../configuration.md#environment-variables)). An example `jobConfig.example.yaml` file
is available
[here](https://github.com/SciCatProject/scicat-backend-next/blob/release-jobs/jobConfig.example.yaml).

### Configuration overview
The top-level configuration is structured like this:

```
configVersion: v1.0
jobs:
  - jobType: archive
    create:
      auth: "#datasetOwner"
      actions:
        - ...
    update:
      auth: archivemanager
      actions:
        - ...
```

- `configVersion` is a string that indicates the version of this configuration file. It
  is not used by SciCat itself, but is useful for migrating jobs if the configuration
  changes. SciCat will log a warning if a job was updated with a different config
  version than it was created with.
- `jobs` is an array allowing the configuration of different job types
- `jobType` can be defined for each SciCat instance, but the names `archive`,
  `retrieve`, and `public` are traditionally the most common jobs. Only jobs matching a
  configured jobType will be accepted by the backend.
- `create` and `update` correspond to `POST` and `PATCH` requests to the `/jobs`
  endpoint. These configure 'actions' which are run when at different phases of the job
  lifecycle. The actions are defined in the [job actions section](#job-actions).
- `auth` configures the roles authorized to use the endpoint for each job operation.
- `actions` give a list of actions to run when the endpoint is called.

### Authorization

Values for `auth` are described in [Jobs Authorization](../authorization/authorization_jobs.md). Some authorization values may require certain information to be passed in the request body; for instance, `"#datasetOwner"` requires that a dataset be passed.

> **Caution** Setting `auth` to a permissive value (eg `#all`) could expose archiving services to external users. Please consider the security model carefully when configuring jobs.

### Actions Configuration

The following actions are built-in to SciCat and can be included in the `actions` array.

#### URLAction

The `URL` action responds to a Job event by making an HTTP call.

**Configuration**:
The _URL action_, per job stage (_create_, _update_) if defined, must be configured in `jobConfig.yaml`.
It supports templating, by extracting the values from the job schema.

For example:
```yml
- actionType: url
  url: http://localhost:3000/api/v3/health?jobid={{id}}
  method: GET
  headers:
    accept: application/json
```

Where:
  - `url` (required): The URL for the request.This can include template variables.
  - `method` (optional): The HTTP method for the request, e.g. "GET", "POST".
  - `headers` (optional): An object containing HTTP headers to be included in the request.
  - `body` (optional): The body of the request, for methods like "POST" or "PUT".

#### Validate

The `validate` action is used to check validate requests to the job endpoints. It is
used to enforce custom constraints on `jobParams` or `jobResultObject` for each job
type. If other actions rely on custom fields in their templates they should first be
validated with this action.

ValidateAction is configured with a series of `<path>: <typecheck>` pairs which describe
a constraint to be validated. These can be applied to different contexts:
- **`request`** - Checks the incoming request body (aka the DTO).
- **`datasets`** - (CREATE only) requires that a list of datasets be included in
  `jobParams.datasetList`. Checks are applied to each dataset

Validation occurs before the job gets created in the database, while most other actions
are performed after the job is created. This means that correctly configuring validation
is important to detect user errors early.

Configuration is described in detail below. However, a few illustrative examples are
provided first.

##### Example 1: Require extra template data

Consider a case where you want to pass a value from the request body through to other
actions. For example, you want to allow the requestor to specify the subject of an email
to be sent in the request body like this:

```json
POST /jobs
{
  "type": "email_demo",
  "jobParams": {
    "subject": "Thanks for using scicat!"
  }
}
```

In this case an `email` action would be configured using handlebars to insert the
`jobParams.subject` value. However, a `validate` action should also be configured to
catch errors early where the subject is not specified:

`jobConfig.yaml`:
```
jobs:
  - jobType: email_demo
    create:
      auth: admin
      actions:
        - actionType: validate
          request:
            jobParams.subject:
              type: string
        - actionType: email
          to: "{{contactEmail}}"
          subject: "[SciCat] {{jobParams.subject}}"
          bodyTemplate: demo_email.html
    update:
      auth: admin
      actions: []
```

##### Example 2: Enforce datasetLifecycle state

Many job types require a dataset to be included. These are specified in
`jobParams.datasetList` like this:

```json
POST /jobs
{
  "owner"...
  "jobParams": {
    "datasetList": [
      {
        "pid": "examplePID",
        "files": []
      }
    ]
  }
}
```

Permission to access to the datasets is checked with the `#dataset*` authentication
methods, but other properties need to be enforced with a `validate` action.

The following validate actions are recommended for `archive`, `retrieve` and `publish`
jobs:

`jobConfig.yaml`:
```yml
jobs:
  - jobType: archive
    create:
      auth: "#datasetOwner"
      actions:
        - actionType: validate
          datasets:
            datasetlifecycle.archivable:
              const: true
    statusUpdate:
      auth: archivemanager
      actions: []
  - jobType: retrieve
    create:
      auth: "#datasetOwner"
      actions:
        - actionType: validate
          datasets:
            datasetlifecycle.retrievable:
              const: true
    statusUpdate:
      auth: archivemanager
      actions: []
  - jobType: public
    create:
      auth: "#all"
      actions:
        - actionType: validate
          datasets:
            isPublished:
              const: true
    statusUpdate:
      auth: archivemanager
```

**Configuration**:
The config file for a validate action will look like this:

```yml
- actionType: validate
  request:
    <path>: <typecheck>
  datasets:
    <path>: <typecheck>
```

Usually `<path>` will be a dot-delimited field in the DTO, eg. "jobParams.name".
Technically it is a [JSONPath-Plus](https://github.com/JSONPath-Plus/JSONPath)
expression, which is applied to the request body or dataset to extract any matching
items. When writing a jobconfig file it may be helpful to test an expected request body
against the [JSONPath demo](https://jsonpath-plus.github.io/JSONPath/demo/).

The `<typecheck>` expression is a JSON Schema. While complicated schemas are possible,
the combination with JSONPath makes common type checks very concise and legible.
Here are some example `<typecheck>` expressions:

```
- actionType: validate
  request: # applies to the request body
    jobParams.stringVal: # match simple types
      type: string
    jobParams.enumVal: # literal values
      enum: ["yes", "no"]
    jobResultObject.mustBeTrue: # enforce a value
      const: true
    "jobParams": # Apply external JSON Schema to all params
      $ref: https://json.schemastore.org/schema-org-thing.json
  dataset: # applies to all datasets
    datasetLifecycle.archivable:
      const: true
```

Validation will result in a `400 Bad Request` response if either the path is not found
or if any values matching the path do not validate against the provided schema.

#### Email

The `Email` action responds to a Job event by sending an email.

**Configuration**:
The _Mail service_ must first be configured through environmental variables, as described in the [configuration](../configuration.md).
There you can define the `EMAIL_TYPE`, which can be either `smtp` or `ms365`, along with the type's respective configuration values.
While SMTP is the default, MS365 adds support for [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0) for sending emails.
This is an alternative to SMTP for MS365 accounts that would otherwise require interactive OAuth logins, making it useful for automated emails.
To use MS365, you (or your azure admin) will need to generate a `tenantId`, `clientId`, and `clientSecret` with permissions to send email.
The process is described [here](https://docs.emailengine.app/setting-up-oauth2-with-outlook/).
Upon instantiation, the service will create the configured transporter, ready to sent emails upon request.

The _Email action_, per job stage (_create_, _update_) if defined, must be configured in `jobConfig.yaml`.
It supports templating, by extracting the values from the job schema.

Example:
```
- actionType: email
  to: "{{contactEmail}}"
  from: "sender@example.com",
  subject: "[SciCat] Your {{type}} job was submitted successfully."
  bodyTemplateFile: "path/to/job-template-file.html"
```

Where:
- `to`: The recipient's email address. This can include template variables.
- `from`: The sender's email address. If no value is provided, then the default sender email address will be used, as defined in [configuration](../configuration.md).
- `subject`: The subject of the email. This can include template variables.
- `bodyTemplateFile`: The path to the HTML template file for the email body.

You can create your own template for the email's body, which should be a valid html file - for example:
```
<html>
<head>
  <style type="text/css">
  ...
  </style>
</head>
  <body>
    <p>
      Your {{type}} job with id {{id}} has been submitted ...
    </p>
  </body>
</html>
```

#### RabbitMQ

The `RabbitMQ` action implements a way for the backend to connect to a Message Broker.
It publishes the new or updated Job entry to a messaging queue, from where it can be picked up by any program willing to react to this Job.

**Configuration**:
The _RabbitMQ service_ must first be configured through environmental variables, as described in the [configuration](../configuration.md). 
Upon instantiation, it will create a RabbitMQ connection and channel.

The _RabbitMQ action_, per job stage (_create_, _update_) if defined, must be configured in `jobConfig.yaml`, for example:
```
- actionType: rabbitmq
  exchange: jobs.write
  key: jobqueue
  queue: client.jobs.write
```
Where:
- An `exchange` is a routing mechanism that receives messages and routes them to the appropriate queues.
- A routing `key` is a string used to label messages, to specify the message's purpose or destination.
- A `queue` is a storage buffer where messages are held until they are consumed.

If needed, different queues can be defined for different purposes.
Exchanges and keys can be reused for different queues. 

Trying to configure a RabbitMQ action, when the service is not enabled, will throw an error that will prevent the application from running.

#### Log

This is a dummy action, useful for debugging. It adds a log entry when executed.

**Configuration**:
```
- actionType: log
```

The log action does not have any configuration options.
