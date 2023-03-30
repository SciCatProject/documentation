# Configuration

When using the official release image, Backend configuration can be achieved by defining the needed environmental variables either through an orchestration/containerization system, the .env file or with a suitable method compatible with your environment.  
The current source code contains an example .env file, named _.env.sample_ listing all the environment variable available to configure the backend.

If you are compiling the application from source, you can edit the file _serc/config/configuration.ts_ with the correct values for your infrastructure.

### Environement Variables

This is complete the list of environment variable that can be used to configure SciCat backend.
The list is compiled according to the configuration class defined in _src/config/configuration.ts_

- ADMIN_GROUPS:  
  list of groups that have admin priviliges in SciCat  
  Default: admin  
  Format: comma separated list of strings  

- ACCESS_GROUPS_STATIC_VALUES:  
  List of groups assigned by default as groups to all users. Used in the vanilla implementation.   
  If you do not want to want or need to assign default group, it should be set to empty string "".  
  Default value: ""  
  Format: Comman separated list of strings.   
  Example: "group1,group2,group3,..."  

- ACCESS_GROUP_SERVICE_TOKEN
  Access token needed to access the API specified in ACCESS_GROUP_SERVICE_API_URL, used to
  retrieve access groups from a third party system.  
  Format: string  

- ACCESS_GROUP_SERVICE_API_URL
  Well formed url of the service API used to provide access groups. Only one value is allowed.  
  Example: "https://my.access.group/service/api/url"   
  Format: string  

- DOI_PREFIX  
  The facility DOI prefix, with trailing slash.  
  Default: ""  
  Format: string  

- EXPRESS_SESSION_SECRET
  Secret used to set up express session.  
  Default: ""  
  Format: string  

- LOGOUT_URL  
  Local SciCat URL to redirect users after a successfull logout
  Default: none
  Format: string

- HTTP_MAX_REDIRECTS  
  Max redirects for http requests.  
  Default: 5  
  Fromat: integer  

- HTTP_TIMEOUT
  Timeout from http requests in ms.  
  Default: 5000  
  Format: integer  
  
JWT_SECRET=<JWT_SECRET>  // The secret for your JWT token, used for authorization.
JWT_EXPIRES_IN=3600  // *Optional*  How long, in seconds, the JWT token is valid. Defaults to `3600`.
LDAP_URL="ldaps://ldap.server.com:636/"  // *Optional* The URL (and port) to your LDAP server.
LDAP_BIND_DN="<USERNAME>@server.com"  // *Optional* Bind_DN for your LDAP server.
LDAP_BIND_CREDENTIALS=<PASSWORD>  // *Optional* Credentials for your LDAP server.
LDAP_SEARCH_BASE=<SEARCH_BASE>  // *Optional* Search base for your LDAP server.
LDAP_SEARCH_FILTER="(LDAPUsername={{username}})"  // *Optional* Search filter for you LDAP server.
OIDC_ISSUER="https://identity.your.facility/your/realm" // Full URL of the identity provider
OIDC_CLIENT_ID= "scicat" // Client id used to convert OIDC code to OIDC token. This is assigned in the OIDC service when the token is generated
OIDC_CLIENT_SECRET="90f126864824ede0e22f7b4407aa1a5cd8158e6cabbce39aaf091937589f1750" // Token used to convert OIDC code to OIDC token. This is assigned in the OIDC service when the token is generated
OIDC_CALLBACK_URL="http://localhost:3000/api/v3/oidc/callback" // URL of the endpoint that is called when the authentication has been executed with the OIDC service.
OIDC_SCOPE="openid profile email" // Information returned by the OIDC service together with token"
OIDC_SUCCESS_URL="http://localhost:3000/explorer" // URL of the endpoint that is called after a successful authentication. IT is not used in the vanilla implementaation.
OIDC_ACCESS_GROUPS="access_groups" // field used to retrieve access groups from the OIDC service. It is not used in the vanilla implementation.
LOGBOOK_ENABLED=<"yes"|"no">  // *Optional* Flag to enable/disable the Logbook endpoints. Values "yes" or "no". Defaults to "no".
LOGBOOK_BASE_URL="http://localhost:3030/scichatapi"  // *Optional* The base URL to the SciChat wrapper API. Only required if Logbook is enabled.
LOGBOOK_USERNAME="<LOGBOOK_USERNAME>"  // *Optional* The username used to authenticate to the SciChat wrapper API. Only required if Logbook is enabled.
LOGBOOK_PASSWORD="<LOGBOOK_PASSWORD>"  // *Optional* The password used to authenticate to the SciChat wrapper API. Only required if Logbook is enabled.
METADATA_KEYS_RETURN_LIMIT=100  // *Optional* The return limit for the `/Datasets/metadataKeys` endpoint.
METADATA_PARENT_INSTANCES_RETURN_LIMIT=100  // *Optional* The return limit of Datasets to extract metadata keys from for the `/Datasets/metadataKeys` endpoint.
MONGODB_URI="mongodb://<USERNAME>:<PASSWORD>@<HOST>:27017/<DB_NAME>"  // The URI for your MongoDB instance.
OAI_PROVIDER_ROUTE="<OAI_PROVIDER_ROUTE>"  // *Optional* URI to OAI provider, used for the `/publisheddata/:id/resync` endpoint.
PID_PREFIX="<PID_PREFIX>"  // The facility PID prefix, with trailing slash.
PUBLIC_URL_PREFIX="https://doi.ess.eu/detail/"  // The base URL to the facility Landing Page.
PORT=3000  // *Optional* The port on which you want to access the app. Defaults to `3000`.
RABBITMQ_ENABLED=<"yes"|"no">  *Optional* Flag to enable/disable RabbitMQ consumer. Values "yes" or "no". Defaults to "no".
RABBITMQ_HOSTNAME="localhost"  // *Optional* The hostname of the RabbitMQ message broker. Only required if RabbitMQ is enabled.
RABBITMQ_USERNAME="rabbitmq"  // *Optional* The username used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.
RABBITMQ_PASSWORD="rabbitmq"  // *Optional* The password used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.
REGISTER_DOI_URI="https://mds.test.datacite.org/doi"  // URI to the organization that registers the facilities DOIs.
REGISTER_METADATA_URI="https://mds.test.datacite.org/metadata"  // URI to the organization that registers the facilities published data metadata.
SITE=<SITE>  // The name of your site.
SMTP_HOST=<SMTP_HOST>  // Host of SMTP server.
SMTP_MESSAGE_FROM=<SMTP_MESSAGE_FROM>  // Email address that emails should be sent from.
SMTP_PORT=<SMTP_PORT>  // Port of SMTP server.
SMTP_SECURE=<SMTP_SECURE>  // Secure of SMTP server.

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
