# Job Configuration

- [Overview](#overview)
- [Quick-start](#quick-start)
- [Details](#details)
  - [Job lifecycle](#job-lifecycle)
  - [Referencing datasets](#referencing-datasets)
  - [Status Codes](#status-codes)
  - [Actions](#actions)
  - [Migration Notes](#migration-notes)
- [Configuration](#configuration)
  - [Configuration overview](#configuration-overview)
  - [Authorization](#authorization)
  - [Templates](#templates)
  - [Actions Configuration](#actions-configuration)
    - [URLAction](#urlaction)
    - [Validate](#validate)
      - [Example 1: Require extra template data](#example-1-require-extra-template-data)
      - [Example 2: Enforce datasetLifecycle state](#example-2-enforce-datasetlifecycle-state)
      - [Example 3: Define statusCodes](#example-3-define-statuscodes)
    - [Email](#email)
    - [RabbitMQ](#rabbitmq)
    - [Switch](#switch)
    - [Error](#error)
    - [Log](#log)


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

## Quick-start

To start using jobs:

1. Copy
   [`jobConfig.recommended.yaml`](https://github.com/SciCatProject/scicat-backend-next/blob/master/jobConfig.recommended.yaml)
   to `jobConfig.yaml`
2. Update the configuration. See
   [jobConfig.example.yaml](https://github.com/SciCatProject/scicat-backend-next/blob/master/jobConfig.example.yaml)
   and the [Actions Configuration](#actions-configuration) section below for examples.
3. Set `JOB_CONFIGURATION_FILE=jobConfig.yaml` in your .env file or environment

## Details

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
   users. Only members of groups listed in the `DELETE_JOB_GROUPS` env variable can
   delete jobs.

### Referencing datasets

Many (but not all) jobs relate to datasets. These are specified during job creation in
the `jobParams.datasetList` array. The array should contain objects with a `pid` string
and a `files` array listing individual files that the job should be applied to. An empty
`files` array indicates that the job should apply to all files.

```json
{
  "type": ...,
  "jobParams": {
    "datasetList": [
      {
        "pid": "12.3456...",
        "files": []
      }
    ]
  }
}
```

### Status Codes

External systems can provide updates to the user by updating the job via the REST API.
- `statusCode` is a machine readable status code. Values can be customized for different
  job types, but are usually single-word strings in camel-case. Some example values are
  given below.
- `statusMessage` is a human-readable description of the job state. This string is
  displayed to the user.
- `jobResultObject` is a json object with additional machine-readable state information.

Newly created jobs will have `"statusCode": "jobSubmitted"` and `"statusMessage": "Job
Submitted."`. These values can be customized using the `JOB_DEFAULT_STATUS_CODE` and
`JOB_DEFAULT_STATUS_MESSAGE` environmental variables.

Status codes can be used to implement state machine logic in an external system, such as
an archive infrastructure. The archive system can be notified about new and updated jobs
through *actions* (see below) which might call a URL or post to a message broker. The
archive system then sends a `PATCH` request to update the job, triggering further
actions. While status codes can be customized for each institute, the following statuses
are given as examples for archive and retrieve jobs:

| statusCode                | Meaning                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| jobSubmitted              | Freshly created job                                                                                                                              |
| inProgress                | The archive system is working on the job                                                                                                         |
| finishedSuccessful        | Success!                                                                                                                                         |
| finishedWithDatasetErrors | A user error occurred relating to one or more datasets; see `datasetlifecycle.archiveStatusMessage` of any related datasets for more information |
| finishedUnsuccessful      | A system error occurred                                                                                                                          |

Additional status changes may be associated with datasets referenced in
`jobParams.datasetList`, for example in the `datasetlifecycle.archiveStatusMessage`
field.

It is recommended that values of `statusCode` be configured for each job type using a
[`validate`](#validate) action (see below).

### Actions

After *create* and *update* stages, a series of actions can be performed by SciCat. This
can be things like sending an email, posting a message to a message broker, or calling
an API. The `jobParams` and `jobResultObject` are used to provide additional information
that the actions may need, such as the list of datasets the job refers to.

A full list of built-in actions is given below. A plugin mechanism for registering new
actions is also planned for a future SciCat release.

### Migration Notes

For general information about migrating from v3.x, see [Migration](../../Migration.md).

In v3.x the `archive`, `retrieve`, and `public` jobs were hard-coded. In v4.x the job
types can be arbitrary strings; however we recommend using the standard job names to
avoid confusion.

The data transfer objects for job endpoints have changed in v4.x. We recommend migrating
tools to use the new `/api/v4/jobs` endpoints. Old `/api/v3/Jobs` endpoints are still
available using the old models, but may have some restrictions.

<!-- TODO: Add a table mapping the old schemas to the new ones -->

Also note that some checks that were performed by default in v3.x for certain job types
must now be configured explicitly as actions. These are included in the provided
`jobConfig.recommended.yaml` file and are also noted below.

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

Production configuration files may contain duplicate actions. Using yaml
[aliases](https://yaml.org/spec/1.2.2/#alias-nodes) is recommended to avoid unneccessary
duplication.

### Authorization

Values for `auth` are described in [JobsAuthorization](../authorization/authorization_jobs.md).
Some authorization values may require certain information to be passed in the request body;
for instance, `"#datasetOwner"` requires that a dataset be passed.

> **Caution** Setting `auth` to a permissive value (eg `#all`) could expose archiving
> services to external users. Please consider the security model carefully when
> configuring jobs.

### Templates

Many actions can be configured using templates, which get filled when the action runs.
Template strings use [Handlebars](https://handlebarsjs.com/) syntax. The following
top-level variables are availabe in the handlebars context:

{% raw %}
| Top-level variable | Type                                 | Examples                                       | Description                                                             |
| ------------------ | ------------------------------------ | ---------------------------------------------- | ----------------------------------------------------------------------- |
| `request`          | `CreateJobDto` or<br/>`UpdateJobDto` | `{{{request.type}}}`<br/>`{{{request.jobParams}}}` | HTTP Request body                                                       |
| `job`              | `JobClass`                           | `{{{job.id}}}`                                   | The job. During the validate phase this is the previous job values (if any); during the perform phase it will be the current database value. |
| `datasets`         | `DatasetClass[]`                     | `{{#each datasets}}{{{pid}}}{{/each}}`           | Array of all datasets referenced in `job.jobParams.datasetList`.        |
| `env`              | `object`                             | `{{{env.SECRET_TOKEN}}}`                         | Access environmental variables                                          |
{% endraw %}

Environmental variables are particularly useful for secrets that should not be stored in
the config file.

{% raw %}
Most variables should use handlebars "triple-stash" (`{{{ var }}}`) to disable html
escaping. Use double-brackets (`{{ var }}`) for HTML email bodies where special
characters should be escaped. Templates that expect JSON should use `{{{ jsonify var
}}}` to ensure correct quoting. In addition to the built-in handlebars functions, the
following additional helpers are defined:
{% endraw %}

- `unwrapJSON`: convert a json object to HTML (arrays become `<ul>`, objects are formatted as key:value lines, etc)
- `keyToWord`: convert camelCase to space-separated words
- `eq`: test exact equality (`===`)
- `jsonify`: Convert an object to JSON
- `job_v3`: Convert a JobClass object to the old JobClassV3
- `urlencode`: urlencode input
- `base64enc`: base64enc input

Not all variables may be available at all times. Actions run either before job is saved
to the database (`validate` phase) or after (`perform` phase). The following table
indicates what values can be expected in the context during each phase.

| Operation | Phase    | request        | job                          | datasets         |
| --------- | -------- | -------------- | ---------------------------- | ---------------- |
| create    | validate | `CreateJobDto` | *undefined*                  | `DatasetClass[]` |
| create    | perform  | `CreateJobDto` | `JobClass`                   | `DatasetClass[]` |
| update    | validate | `UpdateJobDto` | `JobClass` (previous values) | `DatasetClass[]` |
| update    | perform  | `UpdateJobDto` | `JobClass` (updated values)  | `DatasetClass[]` |

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
  url: http://localhost:3000/api/v3/health?jobid={{{request.id}}}
  method: GET
  headers:
    accept: application/json
    Authorization: "Bearer {{{env.ARCHIVER_AUTH_TOKEN}}}",
  body: "{{{jsonify job}}}
```

Where:

- `url` (required): The URL for the request.This can include template variables.
- `method` (optional): The HTTP method for the request, e.g. "GET", "POST".
- `headers` (optional): An object containing HTTP headers to be included in the request.
- `body` (optional): The body of the request, for methods like "POST" or "PUT".

It is recommended that authorization tokens be stored as environmental variables rather
than included directly in the jobConfig.yaml file.

#### Validate

The `validate` action is used to validate requests to the job endpoints. It is used to
enforce custom constraints on `jobParams` or `jobResultObject` for each job type. If
other actions rely on custom fields in their templates they should first be validated
with this action.

ValidateAction is configured with a series of `<path>: <typecheck>` pairs which describe
a constraint to be validated. These can be applied to different contexts:

- **`request`** - Checks the incoming request body (aka the DTO).
- **`datasets`** - requires that a list of datasets be included in
  `jobParams.datasetList`. Checks are applied to each dataset.

Validation occurs before the job gets created in the database, while most other actions
are performed after the job is created. This means that correctly configuring validation
is important to detect user errors early.

Configuration is described in detail below. However, a few illustrative examples are
provided first.

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

In this case an [`email` action](#email) would be configured using handlebars to insert the
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
          to: "{{{job.contactEmail}}}"
          subject: "[SciCat] {{{job.jobParams.subject}}}"
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

##### Example 3: Define statusCodes

This example restricts the permitted statusCodes to a fixed list. This can help detect
typos and ill-defined states.

```
jobs:
  - jobType: archive
    create:
      auth: "#datasetOwner"
      actions: ...
    update:
      auth: archivemanager
      actions:
        - actionType: validate
          requests:
            statusCode:
              enum:
                - jobSubmitted
                - inProgress
                - finishedSuccessful
                - finishedWithDatasetErrors
                - finishedUnsuccessful
```

#### Email

The `email` action responds to a Job event by sending an email.

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
  to: "{{{job.contactEmail}}}"
  from: "sender@example.com",
  subject: "[SciCat] Your {{{job.type}}} job was submitted successfully."
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
      Your {{{job.type}}} job with id {{{job.id}}} has been submitted ...
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
  phase: validate | perform | all
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
  Properties are selected from the same context used for templates; see
  [templates](#templates) above for a description of the values available
- `phase` (required) Determines which phases the switch statement runs. Some properties
  may be unavailable in some phases (see [templates](#templates)), requiring limiting
  when the switch statement is evaluated. Actions listed within the `cases` section will
  also be run only in the phase listed here.
  - `validate`: Evaluated before the request is accepted and written to the database;
    useful for `validate` actions.
  - `perform`: Evaluated after the request is written to the database; most actions
    run in this phase.
  - `all`: Evaluate the switch condition in both phases
- `cases`: one or more conditions to match the property against. Conditions are tested in
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

Some JSON paths may return multiple values. For instance, accessing dataset properties
should use array paths such as `datasets[*].storageLocation`. If multiple unique values
are returned then the request will return a 400 error. If the property doesn't match
any values then a value of `undefined` will be used, which can be handled by a default
case.

**Examples**:

Switch can be used as a simple 'if' statement. For instance, it could be used to respond
to different statusCodes (this case could also be handled with handlebars templates):

```yaml
  - jobType: retrieve
    create:
      auth: '#datasetAccess'
    update:
      auth: archiveManager
      actions:
        - actionType: switch
          phase: perform
          property: job.statusCode
          cases:
            - match: finishedSuccessful
              actions:
              - actionType: email
                to: {{{job.contactEmail}}}
                subject: "[SciCat] Your {{{job.type}}} job was successful!"
                bodyTemplateFile: retrieve-success.html
            - actions:
              - actionType: email
                to: {{{job.contactEmail}}}
                subject: "[SciCat] Your {{{job.type}}} job has state {{{job.statusCode}}}"
                bodyTemplateFile: retrieve-failure.html
```

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
Usually the entry is added after the job request has been processed (`perform`),
but it can also be configured to log messages during initialization or when validating
an incoming job.

**Configuration**:

```yaml
- actionType: log
  init: "Job initialized with params {{{ jsonify this }}}"
  validate: "Request body received: {{{ jsonify this }}}"
  perform: "Job saved: {{{ jsonify this }}}"
```

All arguments are optional.

{% raw %}
- `init` (optional): Log message to print during startup. The actions's configuration
  section from jobConfig.yaml is available as a Handlebars context. Default: ""
- `validate` (optional): Log message to print when the job request is received. The
  request body (aka DTO) is available as a Handlebars context. Default: ""
- `perform` (optional): Log message to print after the job is saved to the database.
  The updated job object is available as a Handlebars context.
  Default: `"Performing job for {{{job.type}}}"`
{% endraw %}