# Configuration

- [SciCat Frontend](#scicat-frontend)
- [SciCat Backend](#scicat-backend)
  - [Dotenv Config](#dotenv-config)
  - [DOI Config](#doi-config)

## SciCat Frontend

This is the configuration file for the frontend client. The configuration file allows the systems administrator to configure every aspect of the client including switching on/off almost all non essential features. The configuration file can either be served from the backend, via the `/client/config.json` endpoint or mounted into `/usr/share/nginx/html/assets/config.json`.

An example is shown below

```
frontend/src/assets/config.json:

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

An example is shown below

```
backend/.env
// Required
DOI_PREFIX="<DOI_PREFIX>"  // The facility DOI prefix, with trailing slash.
JWT_SECRET=<JWT_SECRET>  // The secret for your JWT token, used for authorization.
MONGODB_URI="mongodb://<USERNAME>:<PASSWORD>@<HOST>:27017/<DB_NAME>"  // The URI for your MongoDB instance.
PID_PREFIX="<PID_PREFIX>"  // The facility PID prefix, with trailing slash.
PUBLIC_URL_PREFIX="https://doi.ess.eu/detail/"  // The base URL to the facility Landing Page.

//*Optional* - Redirect and security
JWT_EXPIRES_IN=3600  // *Optional*  How long, in seconds, the JWT token is valid. Defaults to `3600`.
HTTP_MAX_REDIRECTS=5  // *Optional* Max redirects for http requests. Defaults to 5.
HTTP_TIMEOUT=5000  // *Optional* Timeout from http requests in ms. Defaults to 5000.
EXPRESS_SESSION_SECRET="<EXPRESS_SESSION_SECRET>"  // *Optional* Secret used to set up express session.
PORT=3000  // *Optional* The port on which you want to access the app. Defaults to `3000`.

// *Optional* - Include  for authentication via LDAP
LDAP_URL="ldaps://ldap.server.com:636/"  // The URL (and port) to your LDAP server.
LDAP_BIND_DN="<USERNAME>@server.com"  // Bind_DN for your LDAP server.
LDAP_BIND_CREDENTIALS=<PASSWORD>  //  Credentials for your LDAP server.
LDAP_SEARCH_BASE=<SEARCH_BASE>  //  Search base for your LDAP server.
LDAP_SEARCH_FILTER="(LDAPUsername={{username}})"  // Search filter for you LDAP server.

// *Optional* - Include for authentication via keycloak
OIDC_ISSUER="https://keycloak.myorg.com/realm/myrealm" // The URL for OIDC issuer if you want to do OIDC login
OIDC_AUTHORIZATION_URL=https://keycloak.myorg.com/ // The URL for the the OIDC authorization
OIDC_CLIENT_ID=scicat // Client ID to communicate with the OIDC Issuer
OIDC_CLIENT_SECRET=my-super-scicat-secret-123 // Client Secret to go with the above id
OIDC_CALLBACK_URL=https://scicat.myorg.com/api/v3/auth/oidc/callback // callback URL for OIDC
OIDC_SCOPE='openid profile email' // Scopes as required by Scicat
OIDC_SUCCESS_URL=https://scicat.myorg.com/auth-callback // The URL to redirect to after a successful login
OIDC_FAILURE_URL=https://scicat.myorg.com/login // *Optional* The URL to redirect to after a unsuccessful login
OIDC_ACCESS_GROUPS=accessgroups // *Optional* scopes to retrieve access groups from OIDC

//*Optional* - for adding a logbook to Scicat
LOGBOOK_ENABLED=<"yes"|"no">  // *Optional* Flag to enable/disable the Logbook endpoints. Values "yes" or "no". Defaults to "no".
LOGBOOK_BASE_URL="http://localhost:3030/scichatapi"  // *Optional* The base URL to the SciChat wrapper API. Only required if Logbook is enabled.
LOGBOOK_USERNAME="<LOGBOOK_USERNAME>"  // *Optional* The username used to authenticate to the SciChat wrapper API. Only required if Logbook is enabled.
LOGBOOK_PASSWORD="<LOGBOOK_PASSWORD>"  // *Optional* The password used to authenticate to the SciChat wrapper API. Only required if Logbook is enabled.

//*Optional* - for data
METADATA_KEYS_RETURN_LIMIT=100  // *Optional* The return limit for the `/Datasets/metadataKeys` endpoint.
METADATA_PARENT_INSTANCES_RETURN_LIMIT=100  // *Optional* The return limit of Datasets to extract metadata keys from for the `/Datasets/metadataKeys` endpoint.
OAI_PROVIDER_ROUTE="<OAI_PROVIDER_ROUTE>"  // *Optional* URI to OAI provider, used for the `/publisheddata/:id/resync` endpoint.
REGISTER_DOI_URI="https://mds.test.datacite.org/doi"  // URI to the organization that registers the facilities DOIs.
REGISTER_METADATA_URI="https://mds.test.datacite.org/metadata"  // URI to the organization that registers the facilities published data metadata.

//*Optional* - for connecting to AMQP service RabbitMQ
RABBITMQ_ENABLED=<"yes"|"no">  *Optional* Flag to enable/disable RabbitMQ consumer. Values "yes" or "no". Defaults to "no".
RABBITMQ_HOSTNAME="localhost"  // *Optional* The hostname of the RabbitMQ message broker. Only required if RabbitMQ is enabled.
RABBITMQ_USERNAME="rabbitmq"  // *Optional* The username used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.
RABBITMQ_PASSWORD="rabbitmq"  // *Optional* The password used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.

//*Optional* - for adding SMTP to Scicat
SITE=<SITE>  // The name of your site.
SMTP_HOST=<SMTP_HOST>  // Host of SMTP server.
SMTP_MESSAGE_FROM=<SMTP_MESSAGE_FROM>  // Email address that emails should be sent from.
SMTP_PORT=<SMTP_PORT>  // Port of SMTP server.
SMTP_SECURE=<SMTP_SECURE>  // Secure of SMTP server.

```
> Note for more information about using OIDC to authenticate please see  [OIDC connection](#OIDC).

### DOI Config

This config file contains the username and password for authenicating against your DOI provider, e.g., DataCite, which is used when registering the DOI and metadata of your published data.

```
backend/src/config/doiconfig.local.json

{
  "username": "<DOI_CONFIG_USERNAME>",
  "password": "<DOI_CONFIG_PASSWORD>"
}

```
