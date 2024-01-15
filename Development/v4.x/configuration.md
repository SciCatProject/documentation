# Configuration

- [SciCat Frontend](#scicat-frontend)
- [SciCat Backend](#scicat-backend)
  - [Dotenv Config](#dotenv-config)
  - [DOI Config](#doi-config)

## SciCat Frontend

This is the configuration file for the frontend client. The configuration file allows the systems administrator to configure every aspect of the client including switching on/off almost all non essential features. 

The configuration file can be served from the backend, via the `admin/client/config.json` endpoint. The frontend would expect the backend to be served on port 3000 in a routing configuration for this  to work.  The configuration file can also be mounted to the volume `/home/node/app/dist/config/frontend.config.json` for it to be served through this endpoint. 


An example is shown below

```
frontend.config.json:

{
  "accessTokenPrefix": "",  // Set the backend token prefix. Should be empty string for current backend or "Bearer " if using scicat-backend-next.
  "addDatasetEnabled": true,  // Show/hide the "Create Dataset" button in the Datasets Dashboard.
  "archiveWorkflowEnabled": true,  // Enable/disable the archive/retrieve workflow.
  "datasetReduceEnabled": true,  // Enable/disable the automatic Dataset reduction/analysis workflow.
  "editDatasetSampleEnabled": true,  // Enable/disable editing of which Sample a Dataset belongs to.
  "editMetadataEnabled": true,  // Enable/disable editing of Scientific Metadata.
  "editPublishedData": true,  // Enable/disable editing of Published Data.
  "editSampleEnabled": true,  // Enable/disable editing of Samples.
  "externalAuthEndpoint": "/auth/msad",  // Endpoint used for third party authentication, e.g, LDAP.
  "facility": "ESS",  // Facility running the SciCat instance.
  "fileColorEnabled": true,  // Enable/disable file size color representation in the Datasets Dashboard.
  "fileDownloadEnabled": true,  // Enable/disable download workflow for Dataset datafiles.
  "gettingStarted": null,  // URL to Getting Started guide for SciCat, displayed on the Help page.
  "ingestManual": null,  // URL to Ingest Manual for SciCat, displayed on the Help page.
  "jobsEnabled": true,  // Enable/disable Job workflow.
  "jsonMetadataEnabled": true,  // Show/hide the "Show Metadata" button on the details pages, allowing users to see the JSON represantion of the current document.
  "jupyterHubUrl": "https://jupyterhub.esss.lu.se/",  // URL to Jupyter Hub instance used for data analysis.
  "landingPage": "doi2.psi.ch/detail/",  // URL to the facility's Landing Page for Published Data.
  "lbBaseURL": "http://127.0.0.1:3000",  // URL to the SciCat Backend.
  "localColumns": [                      // Default columns to be displayed in the table on the Datasets Dashboard.
    {
      "name": "select",
      "order": 0,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "datasetName",
      "order": 1,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "runNumber",
      "order": 2,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "sourceFolder",
      "order": 3,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "size",
      "order": 4,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "creationTime",
      "order": 5,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "type",
      "order": 6,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "image",
      "order": 7,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "metadata",
      "order": 8,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "proposalId",
      "order": 9,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "ownerGroup",
      "order": 10,
      "type": "standard",
      "enabled": false
    },
    {
      "name": "dataStatus",
      "order": 11,
      "type": "standard",
      "enabled": false
    }
  ],
  "logbookEnabled": true,  // Enable/disable SciChat Logbook integration.
  "loginFormEnabled": true,  // Enable/disable the local Login form. Should be disabled if using oAuth2 for authentication.
  "maxDirectDownloadSize": 5000000000,  // Set a maximum allowed file size for downloading datafiles over HTTP.
  "metadataPreviewEnabled": true,  // Enable/disable Scientific Metadata preview on the Datasets Dashboard.
  "metadataStructure": "tree", // Allow tree structure for Scientific Metadata. Set to empty string for flat structure.
  "multipleDownloadAction": "http://localhost:3012/zip",  // URL to service handling direct download of datafiles.
  "multipleDownloadEnabled": true,  // Enable/disable ability to download multiple datafiles.
  "oAuth2Endpoints": [],  // List of endpoints used for oAuth2 authentication.
  "policiesEnabled": true,  // Enable/disable Dataset Policies workflow.
  "retrieveDestinations": [],  // List of destinations for Dataset retrievals.
  "riotBaseUrl": "http://scitest.esss.lu.se/riot",  // URL to SciChat client.
  "scienceSearchEnabled": true,  // Enable/disable filtering documents on Scientific Metadata.
  "scienceSearchUnitsEnabled": true,  // Enable/disable filtering documents on Scientific Metadata using units.
  "searchPublicDataEnabled": true,  // Enable/disable filtering Datasets on public or non-public data.
  "searchSamples": true,  // Enable/disable searching Samples on Samples Dashboard.
  "sftpHost": "login.esss.dk",  // URL to SFTP service used for downloading files exceeding maximum allowed file size.
  "shareEnabled": true,  // Enable/disable workflow for sharing Datasets with other users using their email address.
  "shoppingCartEnabled": true,  // Enable/disable the Dataset cart used for bulk actions.
  "shoppingCartOnHeader": true,  // Toggle Dataset cart placement, either on header or to the left on the Datasets Dashboard.
  "tableSciDataEnabled": true  // Enable/disable Scientific Metadata table view on details pages. If disabled, Scientific Metadata is displayed as raw JSON.
}

```

## SciCat Backend

### Dotenv config

This is the configuration file for the backend. This file allows the systems administrator to configure connected services, like authentication services and message queues, and also switching on/off almost all non essential features. The configuration file is a [dotenv](https://www.npmjs.com/package/dotenv) file and is read by the backend at runtime.

There are currently many configurable additions to SciCat which makes it very flexible these are:
- OIDC for authenticatoin
- LDAP for authentication
- Elastic Search 
- SMTP for sending emails to notify users of SciCat jobs
- AMQP to provide a message queue for the jobs 

An minimal example is shown below followed by a full example:

#### Minimal Backend Config Example
```
   ADMIN_GROUPS [string] Optional Comma separated list of admin groups with admin permission assigned to the listed users. Example: "admin, ingestor". For more details check: Scicat Documentation

   EXPRESS_SESSION_SECRET [string] Optional Secret used to set up express session.

   HTTP_MAX_REDIRECTS [number] Optional Max redirects for http requests. Defaults to 5.

   HTTP_TIMEOUT [number] Optional Timeout from http requests in ms. Defaults to 5000.

   JWT_SECRET [string] The secret for your JWT token, used for authorization.

   JWT_EXPIRES_IN [number] Optional How long, in seconds, the JWT token is valid. Defaults to 3600.

   MONGODB_URI [string] The URI for your MongoDB instance.

```


#### Full Backend Config Example

```
backend/.env

Valid environment variables for the .env file. See .env.example for examples value formats.

## Data Management

    ADMIN_GROUPS [string] Optional Comma separated list of admin groups with admin permission assigned to the listed users. Example: "admin, ingestor". For more details check: Scicat Documentation

    CREATE_DATASET_GROUPS [string] Optional Comma seperated list of create dataset groups. Users belong to the listed groups can create dataset with/without PID. Example: "group1, group2". For more details check: Scicat Documentation

    CREATE_DATASET_WITH_PID_GROUPS [string] Optional Comma seperated list of create dataset with pid groups. Users belong to the listed groups can create dataset with PID. Example: "group1, group2". For more details check: Scicat Documentation

    DELETE_GROUPS [string] Optional Comma seperated list of delete groups. Users belong to the listed groups can delete any dataset, origDatablocks, datablocks etc. For more details check: Scicat Documentation

    DATASET_CREATION_VALIDATION_ENABLED [boolean] Flag to enable/disable dataset validation to validate if requested new dataset is valid with given regular expression. Preconfigure DATASET_CREATION_VALIDATION_REGEX variable is required. Default value: false

    DATASET_CREATION_VALIDATION_REGEX [string] Regular expression validation for new dataset request. Default value: ""

    PROPOSAL_GROUPS [string] Optional Comma separated list of proposal groups with permission to create any proposals. Example: "proposaladmin, proposalingestor". For more details check: Scicat Documentation

    SAMPLE_GROUPS [string] Optional Comma separated list of sample groups with permission to create any samples. Example: "sampleadmin, sampleingestor". For more details check: Scicat Documentation
    
## Access groups from external administration systems

    ACCESS_GROUPS_STATIC_VALUES [string] Optional Comma separated list of access groups automatically assigned to all users. Example: "scicat, user"

    ACCESS_GROUPS_SERVICE_TOKEN [string] Optional Authentication token used if access groups are obtained from a third party service. This value is not used by the vanilla installation, but only if the instance is customized to use an external service to provide user groups, like the ESS example

    ACCESS_GROUP_SERVICE_API_URL [string] Optional URL of the service providing the users' access groups. This value is not used by the vanilla installation, but only if the instance is customized to use an external service to provide user groups, like the ESS example
   
## Secrets, tokens and http settings

    EXPRESS_SESSION_SECRET [string] Optional Secret used to set up express session.

    HTTP_MAX_REDIRECTS [number] Optional Max redirects for http requests. Defaults to 5.

    HTTP_TIMEOUT [number] Optional Timeout from http requests in ms. Defaults to 5000.

    JWT_SECRET [string] The secret for your JWT token, used for authorization.

    JWT_EXPIRES_IN [number] Optional How long, in seconds, the JWT token is valid. Defaults to 3600.

## LDAP Settings - only required for authentication using LDAP

    LDAP_URL [string] Optional The URL to your LDAP server.

    LDAP_BIND_DN [string] Optional Bind_DN for your LDAP server.

    LDAP_BIND_CREDENTIALS [string] Optional Credentials for your LDAP server.

    LDAP_SEARCH_BASE [string] Optional Search base for your LDAP server.

    LDAP_SEARCH_FILTER [string] Optional Search filter for you LDAP server.

## OIDC Settings - only required for OIDC authentication

    OIDC_ISSUER [string] Optional URL of the oidc server providing the authentication service. Example: https://identity.esss.dk/realm/ess.

    OIDC_CLIENT_ID [string] Optional Identity of the client that we want to use to obtain the user token. Example: scicat

    OIDC_CLIENT_SECRET [string] Optional Secret to provide to the oidc service to obtain the user token. Example: Aa1JIw3kv3mQlGFWhRrE3gOdkH6xreAwro

    OIDC_CALLBACK_URL [string] Optional SciCat callback URL that we want th eoidc service to redirect to, in case of successful login. Example: http://myscicat/api/v3/oidc/callback

    OIDC_SCOPE [string] Optional Space separated list of the info returned by the oidc service. Example: "openid profile email"

    OIDC_SUCCESS_URL [string] Optional SciCat Frontend auth-callback URL. Required in order to pass user credentials to SciCat Frontend after OIDC login. Example: https://myscicatfrontend/auth-callback

    OIDC_ACCESS_GROUPS [string] Optional Functionality is still unclear.

## Scicat metadata settings

    PID_PREFIX [string] The facility PID prefix, with trailing slash.

    LOGBOOK_ENABLED [string] Optional Flag to enable/disable the Logbook endpoints. Values "yes" or "no". Defaults to "no".

    LOGBOOK_BASE_URL [string] Optional The base URL to the Logbook API. Only required if Logbook is enabled.

    METADATA_KEYS_RETURN_LIMIT [number] Optional The return limit for the /Datasets/metadataKeys endpoint.

    METADATA_PARENT_INSTANCES_RETURN_LIMIT Optional The return limit of Datasets to extract metadata keys from for the /Datasets/metadataKeys endpoint.

    MONGODB_URI [string] The URI for your MongoDB instance.

    SITE [string] The name of your site.

    POLICY_PUBLICATION_SHIFT [integer] Optional Embargo period expressed in years. Default value: 3 years

    POLICY_RETENTION_SHIFT [integer] Optional Retention period (aka how long the facility will hold on to data) expressed in years. Default value: -1 (data will be hold indefinitely)

## Settings for publishing data sets

    OAI_PROVIDER_ROUTE [string] Optional URI to OAI provider, used for the /publisheddata/:id/resync endpoint.

    DOI_PREFIX [string] The facility DOI prefix, with trailing slash.

    PUBLIC_URL_PREFIX [string] The base URL to the facility Landing Page.

    PORT [number] Optional The port on which you want to access the app. Defaults to 3000.
    REGISTER_DOI_URI [string] URI to the organization that registers the facilities DOI's.

    REGISTER_METADATA_URI [string] URI to the organization that registers the facilities published data metadata.

## Message queue settings - only required when using the jobs settings. This currently does not work in release 4.4 but will be released soon 
<!-- 
    RABBITMQ_ENABLED [string] Optional Flag to enable/disable RabbitMQ consumer. Values "yes" or "no". Defaults to "no".

    RABBITMQ_HOSTNAME [string] Optional The hostname of the RabbitMQ message broker. Only required if RabbitMQ is enabled.

    RABBITMQ_USERNAME [string] Optional The username used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.

    RABBITMQ_PASSWORD [string] Optional The password used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled. -->

## SMTP Settings - need this option if you require Scicat to send emails.     

    SMTP_HOST [string] Optional Host of SMTP server.

    SMTP_MESSAGE_FROM [string] Optional Email address that emails should be sent from.

    SMTP_PORT [string] Optional Port of SMTP server.

    SMTP_SECURE [string] Optional Secure of SMTP server.
    

## Elastic Search settings - use these to enable elastic search 

    ELASTICSEARCH_ENABLED [string] Flag to enable/disable the Elasticsearch endpoints. Values "yes" or "no". Defaults to "no"

    ES_HOST [string] Host of Elasticsearch server instance

    ES_USERNAME [string] Optional Elasticsearch username that can be customized when loads Elasticsearch server. Default value: 'elastic'

    ES_PASSWORD [string] Elasticsearch password that can be customized when loads Elasticsearch server.

    MONGODB_COLLECTION [string] Collection name to be mapped into specified Elasticsearch index. Used for data synchronization between mongoDB and Elasticsearch index.

    ES_MAX_RESULT [number] Maximum records can be indexed into Elasticsearch. Default value: 10000

    ES_FIELDS_LIMIT [number] The total number of fields in an index. Default value: 1000

    ES_REFRESH [string] If set to wait_for Elasticsearch will wait till data is insereted to specificied index then return response. Unless you have a good reason to wait for the change to become visible, always use false (the default setting).


```

### DOI Config

This config file contains the username and password for authenicating against your DOI provider, e.g., DataCite, which is used when registering the DOI and metadata of your published data.

```
backend/src/config/doiconfig.local.json

{
  "username": "<DOI_CONFIG_USERNAME>",
  "password": "<DOI_CONFIG_PASSWORD>"
}

```
