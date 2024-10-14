# Job Configuration

> _**Development Feature**. This section documents features that are still under
> development as part of the `release-jobs` branch._

## Overview

The SciCat job system is used for any interactions between SciCat and external services.

Example jobs include:

- Request an **archive system** to *archive* or *retrieve* data from tape storage
- Move data to a *public* location (e.g. to access data from a [DOI landing
  page](https://github.com/SciCatProject/LandingPageServer))
- Run maintenance tasks such as emailing users

### Job lifecycle

Jobs follow a standard Create-Read-Update-Delete (CRUD) lifecycle:

1. Jobs are _created_ via a `POST` request. This can be the result of a frontend
   interaction (eg selecting a dataset for publishing) or through the REST API.

   The body of the request should follow the CreateJobDto (Data Transfer Object):
   ```
   {
    "type": "archive",
    "ownerUser": "owner",
    "ownerGroup": "group",
    "contactEmail": "email"
    "jobParams": {},
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

After _create_ and _update_ stages a series of actions can be performed by SciCat. This
can be things like sending an email, posting a message to a message broker, or calling
an API. The `jobParams` and `jobResultObject` are used to add additional information
that the actions may need, such as the list of datasets the job refers to.

A full list of built-in actions is given below. A plugin mechanism for registering new
actions is also planned for a future SciCat release.

## Configuration

In SciCat v3.x, a limited number of jobs were hard-coded into the code base. This was
changed in v4.x to allow each site to configure their own set of jobs and customize
actions based on the job status.

The available jobs are configured in the file `jobConfig.json` (or can be overridden
with the `JOB_CONFIGURATION_FILE` [environment
variable](../configuration.md#environment-variables)). An example `jobConfig.json` file
is available
[here](https://github.com/SciCatProject/scicat-backend-next/blob/release-jobs/src/jobs/config/jobConfig.example.json).

### Configuration overview
The top-level configuration is structured like this:

```
{
  "configVersion": "v1.0",
  "jobs": [
    {
      "jobType": "archive",
      "create": {
        "auth": "#all",
        "actions": [...]
      },
      "update": {
        "auth": "archivemanager",
        "actions": [...]
      }
    }
  ]
}
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

### Authorization

Values for `auth` are described in [Jobs Authorization](../authorization/authorization_jobs.md). Some authorization values may require certain information to be passed in the request body; for instance, `"#datasetOwner"` requires that a dataset be passed.

### Actions Configuration


#### URLAction

**Configuration**:
```
{
  "actionType": "url",
  "url": "http://localhost:3000/api/v3/health?jobid={{id}}",
  "method": "GET",
  "headers": {
    "accept": "application/json"
  }
},
```

#### Validate

**Configuration**:
```
{
  "actionType": "validate",
  "request": {
    "jobParams.datasetIds[*]": {
      "type": "object",
      "required": ["pid","files"]
    }
  }
}
```

#### Email

**Configuration**:
```
{
  "actionType": "email",
  "auth": {
    "user": "user",
    "password": "password"
  },
  "to": "{{contactEmail}}",
  "from": "from",
  "subject": "[SciCat] Your {{type}} job was submitted successfully",
  "bodyTemplateFile": "src/common/email-templates/job-template-simplified.html"
}
```

#### RabbitMQ

**Configuration**:
```
{
  "actionType": "rabbitmq",
  "hostname": "rabbitmq",
  "port": 5672,
  "username": "guest",
  "password": "guest",
  "exchange": "jobs.write",
  "queue": "client.jobs.write",
  "key": "jobqueue"
}
```

#### Log

**Configuration**:
```
{
  "actionType": "log"
}
```

This is a dummy action, useful for debugging. It adds a log entry when executed.
