# Job Configuration

## Overview

The SciCat job system is used for any interactions between SciCat and external services.

Example jobs include:

- Request an **archive system** to *archive* or *retrieve* data from tape storage
- Move data to a *public* location (e.g. to access data from a [DOI landing
  page](https://github.com/SciCatProject/LandingPageServer))
- Run maintenance tasks such as emailing users

If you just plan to use SciCat for cataloging data and don't plan to use its data
management features then you may not need any job types. If no job types are configured
then SciCat will reject any backend requests to create jobs. In this case [frontend
features](../../frontend/configuration.md) for archiving (`archiveWorkflowEnabled:
false`) and retrieval should be disabled.

### Migration Notes

In v3.x the `archive`, `retrieve`, and `public` jobs were hard-coded. In v4.x the job
types can be arbitrary strings; however we recommend using the standard job names to
avoid confusion.

Also note that some checks that were performed by default in v3.x for certain job types
must now be configured explicitly as actions. These are included in the provided
`jobConfig.example.yaml` file and are also noted below.

### Job lifecycle

Jobs follow a standard Create-Read-Update-Delete (CRUD) lifecycle:

1. Jobs are *created* via a `POST` request to `/jobs`. This can be the result of a frontend
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

2. Jobs can be *read* via a `GET` request to `/jobs/:id` or through the `/jobs/fullquery`
   search endpoint. The frontend uses this to display the list of jobs.
3. Jobs are *updated* via a `PATCH` or `PUT` request to `/jobs/:id`. This is usually
   used by facility services to update the job status and provide feedback.

   The body of the request should follow the UpdateJobDto:

   ```json
   {
     "statusCode": "string",
     "statusMessage": "string",
     "jobResultObject": {}
   }
   ```

4. Jobs may be *deleted* periodically during maintenance. This is usually not done by
   users.

### Actions

After *create* and *update* stages, a series of actions can be performed by SciCat. This
can be things like sending an email, posting a message to a message broker, or calling
an API. The `jobParams` and `jobResultObject` are used to provide additional information
that the actions may need, such as the list of datasets the job refers to.

A full list of built-in actions is given below. A plugin mechanism for registering new
actions is also planned for a future SciCat release.

## Configuration

In SciCat v3.x, a limited number of jobs were hard-coded into the code base. This was
changed in v4.x to allow each site to configure their own set of jobs and customize
actions based on the job status.

The available jobs are configured in the file `jobConfig.yaml` (or can be overridden
with the `JOB_CONFIGURATION_FILE` [environment
variable](../configuration.md#environment-variables)). An example
`jobConfig.example.yaml` file is available
[here](https://github.com/SciCatProject/scicat-backend-next/blob/master/jobConfig.example.yaml).

### Configuration overview

The top-level configuration is structured like this:

```yaml
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
  lifecycle. The actions are defined in the [job actions
  section](#actions-configuration).
- `auth` configures the roles authorized to use the endpoint for each job operation.
- `actions` give a list of actions to run when the endpoint is called.

### Authorization

Values for `auth` are described in [JobsAuthorization](../authorization/authorization_jobs.md).
Some authorization values may require certain information to be passed in the request body;
for instance, `"#datasetOwner"` requires that a dataset be passed.

> **Caution** Setting `auth` to a permissive value (eg `#all`) could expose archiving
> services to external users. Please consider the security model carefully when
> configuring jobs.

### Actions Configuration

The following actions are built-in to SciCat and can be included in the `actions` array.

#### URLAction

The `URL` action responds to a Job event by making an HTTP call.

**Configuration**:
The *URL action*, per job stage (*create*, *update*) if defined, must be configured in
`jobConfig.yaml`. It supports templating, by extracting the values from the job schema.

For example:

```yaml
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

The `validate` action is used to validate requests to the job endpoints. It is used to
enforce custom constraints on `jobParams` or `jobResultObject` for each job type. If
other actions rely on custom fields in their templates they should first be validated
with this action.

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

```yaml
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

```yaml
jobs:
  - jobType: archive
    create:
      auth: "#datasetOwner"
      actions:
        - actionType: validate
          datasets:
            datasetlifecycle.archivable:
              const: true
    update:
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
    update:
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
    update:
      auth: archivemanager
```

**Configuration**:
The config file for a validate action will look like this:

```yaml
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

```yaml
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
The *Mail service* must first be configured through environmental variables, as described in the [configuration](../configuration.md).
There you can define the `EMAIL_TYPE`, which can be either `smtp` or `ms365`, along with the type's respective configuration values.
While SMTP is the default, MS365 adds support for [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0) for sending emails.
This is an alternative to SMTP for MS365 accounts that would otherwise require interactive OAuth logins, making it useful for automated emails.
To use MS365, you (or your azure admin) will need to generate a `tenantId`, `clientId`, and `clientSecret` with permissions to send email.
The process is described [here](https://docs.emailengine.app/setting-up-oauth2-with-outlook/).
Upon instantiation, the service will create the configured transporter, ready to sent emails upon request.

The *Email action*, per job stage (*create*, *update*) if defined, must be configured in `jobConfig.yaml`.
It supports templating, by extracting the values from the job schema.

Example:

```yaml
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

```html
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
The *RabbitMQ service* must first be configured through environmental variables, as described in the [configuration](../configuration.md).
Upon instantiation, it will create a RabbitMQ connection and channel.

The *RabbitMQ action*, per job stage (*create*, *update*) if defined, must be configured in `jobConfig.yaml`, for example:

```yaml
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

#### Switch

Switch which actions are performed based on a condition, similar to a 'switch' or 'case'
statement. It is added to the 'actions' list of a job, and itself contains a list of
sub-actions that will be performed conditionally.

**Configuration**:
The action is added to the `actions` section of a job in `jobConfig.yaml` as follows:

```yaml
- actionType: switch
  scope: request | datasets
  property: some.property
  cases:
  - match: exact value match
    actions: [...]
  - regex: /^regex$/i
    actions: [...]
  - schema: {JSON schema}
    actions: [...]
  - # default
    actions: [...]
```

- `property` (required) Name of a variable to test against. This is specified as a
  JSONPath+ spec; the most common case is a simple dot-delimited list of keys.
- `scope` (required) Determines where the property is looked up. The following values
  are supported:
  - `request`: Read properties from the job request body (validation phase) or the job
    as stored in the database (perform phase).
  - `datasets`: Valid only for `create` jobs, properties will be read from the dataset
    referenced in `jobParams.datasetList`. If multiple datasets are listed, all should
    resolve to a single value; otherwise the job will return a 400 error.
- cases: one or more conditions to match the property against. Conditions are tested in
  order. No "fall through" behavior is implemented; this can be approximated using yaml
  anchors and aliases if needed. The following types of conditions are available:
  - `match`: match the property against a string or literal value. This use javascript
    `==` for equality; use a JSON schema with a `const` term if deep equality is needed.
  - `regex`: Match a string property against a regular expression. Delimiting slashes
    are required. The regex is matched using javascript `RegExp.test`. Flags are
    supported.
  - `schema`: Match the property against a JSON schema.
  - If no condition is included then the case will always match. This is useful for
    adding a terminal 'default' condition (eg with an `error` action).

**Examples**:

Switch can be used as a simple if statement. For instance, it could be used to respond
to different statusCodes (this case could also be handled with handlebars templates):

```yaml
  - jobType: retrieve
    create:
      auth: '#datasetAccess'
    update:
      auth: archiveManager
      actions:
        - actionType: switch
          scope: request
          property: statusCode
          cases:
            - match: finishedSuccessful
              actions:
              - actionType: email
                to: {{contactEmail}}
                subject: "[SciCat] Your {{type}} job was successful!"
                bodyTemplateFile: retrieve-success.html
            - actions:
              - actionType: email
                to: {{contactEmail}}
                subject: "[SciCat] Your {{type}} job has state {{statusCode}}"
                bodyTemplateFile: retrieve-failure.html
```

**Valid properties**:

Generally speaking, actions may be applied either to the request body sent by the client
(such as the `validate` action) or to the job after it is successfully created or
updated in the database (most actions). Currently these are implemented independently,
meaning that, in the request scope, `property` will be matched once against the request
body and then a second time on the updated property from the database. For instance, it
is not possible to use a `switch` action with the job `id` property, since this is not
available in the request body (although it may be present in the URL parameters for
update jobs). This limitation may be relaxed in the future.

#### Error

Throw a custom HTTP error. This can be useful for testing or in combination with a
`switch` action to detect error conditions. The error is thrown before making any
database changes.

**Configuration**:

```yaml
- actionType: error
  message: An error has occurred!
  status: 418
```

- `message`: Error message. The response will include this message in the JSON body.
  The message can contain handlebars template variables, which are passed the incoming
  request body as a context.
- `status` (optional): HTTP error code

#### Log

This is a dummy action, useful for debugging. It adds a log entry when executed.
Usually the entry is added after the job request has been processed (`performJob`),
but it can also be configured to log messages during initialization or when validating
an incoming job.

**Configuration**:

```yaml
- actionType: log
  init: "Job initialized with params {{{ jsonify this }}}"
  validate: "Request body received: {{{ jsonify this }}}"
  performJob: "Job saved: {{{ jsonify this }}}"
```

All arguments are optional.

- `init` (optional): Log message to print during startup. The actions's configuration
  section from jobConfig.yaml is available as a Handlebars context. Default: ""
- `validate` (optional): Log message to print when the job request is received. The
  request body (aka DTO) is available as a Handlebars context. Default: ""
- `performJob` (optional): Log message to print after the job is saved to the database.
  The updated job object is available as a Handlebars context. Default: "Performing job
  for {{{type}}}"
