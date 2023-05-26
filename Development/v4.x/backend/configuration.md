# Configuration

When using the official release image, Backend configuration can be achieved by setting the environmental variables listed below through an orchestration/containerization system, the .env file or with a suitable method compatible with your environment.  
The current source code contains an example .env file, named _.env.sample_ listing all the environment variable available to configure the backend.

If you are compiling the application from source, you can edit the file _serc/config/configuration.ts_ with the correct values for your infrastructure. This option is still undocumented, although it is our intention to provide a detailed how-to guide as soon as we can.

## Environment Variables

This is complete the list of environment variable that can be used to configure SciCat backend.
The list is compiled according to the configuration class defined in _src/config/configuration.ts_

- ADMIN_GROUPS:  
  list of groups that have admin priviliges
  Default: ""  
  Format: comma separated list of strings. Leading and trailing spaces are trimmed

- DELETE_GROUPS:  
  list of groups that are allowed to delete content  
  Default: ""  
  Format: comma separated list of strings. Leading and trailing spaces are trimmed

- CREATE_DATASET_GROUPS:  
  list of non admin groups that are allowed to create datasets. If set to "all", all users can create a dataset belonging to any of the groups they belong to.
  Default: "all"  
  Format: comma separated list of strings. Leading and trailing spaces are trimmed

- ACCESS_GROUPS_STATIC_VALUES:
  List of groups assigned by default to all users. Used in the vanilla implementation for easy configuration.   
  If you do not want or need to assign any default group, it should be set to empty string "".  
  Default value: ""  
  Format: Comman separated list of strings.  Leading and trailing spaces are trimmed
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
  URL specified upon successful logout. It is returned in the json object for the frontend, or third party UI, to be used locally.  
  Default: ""
  Format: string

- HTTP_MAX_REDIRECTS  
  Max number of redirects for http requests.  
  Default: 5  
  Fromat: integer  

- HTTP_TIMEOUT
  Timeout from http requests in ms.  
  Default: 5000  
  Format: integer    
  
- JWT_SECRET  
  The secret used to create any JWT token, used for authorization.  
  default: ""  
  format: string  

- JWT_EXPIRES_IN  
  EXpiration time of any JWT token in seconds.  
  default: 3600 (s)   
  format: integer  

- LDAP_URL  
  Full URI (including port) of your local LDAP server, if this is your selected authentication method.  
  default: No default  
  example: ldaps://ldap.server.com:636/  
  format: string  

- LDAP_BIND_DN  
  Bind DN to access information on your LDAP server.  
  default: No default  
  format: string  

- LDAP_BIND_CREDENTIALS  
  Credentials associated with your bind DN to acccess your LDAP server.  
  default: No default  
  format: string  

- LDAP_SEARCH_BASE  
  Search base for your LDAP server.  
  default: No default  
  format: string  

- LDAP_SEARCH_FILTER  
  Search filter for you LDAP server.  
  default: No default  
  format: string  
  example: "(LDAPUsername={{username}})"  

- OIDC_ISSUER  
  Full URL of your OIDC identity provider  
  default: No default  
  format: string  
  example: "https://identity.your.facility/your/realm"  

- OIDC_CLIENT_ID  
  Client id used to convert OIDC code to OIDC token. This is assigned in the OIDC service when the token is generated  
  default: No default  
  format: string  
  example: "scicat"  

- OIDC_CLIENT_SECRET  
  Token used to convert OIDC code to OIDC token. This is assigned in the OIDC service when the token is generated  
  example: "90f1268..."  

- OIDC_CALLBACK_URL  
  URL of the endpoint that is called when the authentication has been executed with the OIDC service.  
  default: No default  
  format: string  
  example: "http://localhost:3000/api/v3/oidc/callback"  

- OIDC_SCOPE
  Information returned by the OIDC service together with token  
  default: No default  
  format: string  
  example: "openid profile email"  

- OIDC_SUCCESS_URL   
  URL of the endpoint that is called after a successful authentication. It is not used in the vanilla implementation.  
  default: No default  
  format: string  
  example: "http://localhost:3000/explorer"

- OIDC_ACCESS_GROUPS  
  field used to retrieve access groups from the OIDC service. It is not used in the vanilla implementation.  
  default: No default  
  format: string  
  example: "access_groups"  

- LOGBOOK_ENABLED
  Flag to enable/disable the Logbook endpoints.  
  accept values: "yes", "no"  
  default: no  
  format: string  

- LOGBOOK_BASE_URL  
  The base URL to the SciChat wrapper API. Only required if Logbook is enabled.  
  _default_: "http://localhost:3030/scichatapi"    
  _format_: string  

- LOGBOOK_USERNAME  
  The username used to authenticate to the SciChat wrapper API. Only required if Logbook is enabled.  
  _default_: No default  
  _format_: string  

- LOGBOOK_PASSWORD  
  The password used to authenticate to the SciChat wrapper API. Only required if Logbook is enabled.  
  _default_: No default  
  _format_: string  

- METADATA_KEYS_RETURN_LIMIT  
  The maximum number of keys returned by the `/Datasets/metadataKeys` endpoint.  
  _default_: No default  
  _format_: integer  

- METADATA_PARENT_INSTANCES_RETURN_LIMIT  
  The maximum number of Datasets used to extract metadata keys in the `/Datasets/metadataKeys` endpoint.  
  _default_: No default  
  _format_: integer  

- MONGODB_URI
  The URI for your MongoDB instance.
  default: No default
  _format_: string "mongodb://<USERNAME>:<PASSWORD>@<HOST>:27017/<DB_NAME>"
  
- OAI_PROVIDER_ROUTE  
  URI to OAI provider, which is used in the `/publisheddata/:id/resync` endpoint.  
  default: no default  
  format: string  

- PID_PREFIX   
  The facility PID prefix, with trailing slash.
  default: no default  
  format: string  

- PUBLIC_URL_PREFIX   
  The base URL to the facility Landing Page.  
  default: No default  
  format: string  
  example: "https://doi.ess.eu/detail/"  

- PORT  
  The port on which the backend listen on.  
  default: 3000  
  format: integer  

- RABBITMQ_ENABLED  
  Flag to enable/disable RabbitMQ consumer.  
  accepted values: "yes", "no"  
  default: no  
  format: string  
  
- RABBITMQ_HOSTNAME  
  The hostname of the RabbitMQ message broker. Only required if RabbitMQ is enabled.  
  default: no default  
  default: string  

- RABBITMQ_USERNAME  
  The username used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.  
  default: no default  
  format: string  

- RABBITMQ_PASSWORD  
  The password used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.  
  default: no default  
  format: string  

- REGISTER_DOI_URI
  URI to the organization that registers the facilities DOIs.  
  default: no default  
  format: string  
  example: "https://mds.test.datacite.org/doi"

- REGISTER_METADATA_URI  
  URI to the organization that registers the facilities published data metadata.  
  default: no default  
  format: string  
  example: ="https://mds.test.datacite.org/metadata"  

- DOI_USERNAME
  Username used to authenticate on the DOI site
  default: no default
  format: string

- DOI_PASSWORD
  Password used to authenticate on the DOI site
  default: no default
  format: string

- SITE  
  The name of your site.  
  default: no default  
  format: string  

- SMTP_HOST  
  Host of SMTP server.   
  default: no default    
  format: string  

- SMTP_MESSAGE_FROM  
  Email address that emails should be sent from.  
  default: no default  
  format: string, email  

- SMTP_PORT  
  Port of SMTP server.  
  default: no default  
  format: string  

- SMTP_SECURE  
  Secure of SMTP server.
  default: no default  
  format: string  


