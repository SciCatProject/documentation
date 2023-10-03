# Configuration

When using the official release image, Backend configuration can be achieved by setting the environmental variables listed below through an orchestration/containerization system, the .env file or with a suitable method compatible with your environment.  
The current source code contains an example .env file, named _.env.sample_ listing all the environment variable available to configure the backend.

If you are compiling the application from source, you can edit the file _serc/config/configuration.ts_ with the correct values for your infrastructure. This option is still undocumented, although it is our intention to provide a detailed how-to guide as soon as we can.

## Environment Variables

This is complete the list of environment variable that can be used to configure SciCat backend.
The list is compiled according to the configuration class defined in _src/config/configuration.ts_

- ADMIN\_GROUPS:  
  list of groups that have admin priviliges
  _default_: ""  
  _format_: comma separated list of strings. Leading and trailing spaces are trimmed

- DELETE_GROUPS:  
  list of groups that are allowed to delete content  
  _default_: ""  
  _format_: comma separated list of strings. Leading and trailing spaces are trimmed

- CREATE_DATASET_GROUPS:  
  list of non admin groups that are allowed to create datasets. If set to "all", all users can create a dataset belonging to any of the groups they belong to.
  _default_: "all"  
  _format_: comma separated list of strings. Leading and trailing spaces are trimmed

- ACCESS_GROUPS_STATIC_VALUES:
  List of groups assigned by default to all users. Used in the vanilla implementation for easy configuration.   
  If you do not want or need to assign any default group, it should be set to empty string "".  
  Default value: ""  
  _format_: Comman separated list of strings.  Leading and trailing spaces are trimmed
  _example_: "group1,group2,group3,..."  

- ACCESS_GROUP_SERVICE_TOKEN
  Access token needed to access the API specified in ACCESS_GROUP_SERVICE_API_URL, used to
  retrieve access groups from a third party system.  
  _format_: string  

- ACCESS_GROUP_SERVICE_API_URL
  Well formed url of the service API used to provide access groups. Only one value is allowed.  
  _example_: "https://my.access.group/service/api/url"   
  _format_: string  

- DOI_PREFIX  
  The facility DOI prefix, with trailing slash.  
  _default_: ""  
  _format_: string  

- EXPRESS_SESSION_SECRET
  Secret used to set up express session.  
  _default_: ""  
  _format_: string  

- LOGOUT_URL  
  URL specified upon successful logout. It is returned in the json object for the frontend, or third party UI, to be used locally.  
  _default_: ""
  _format_: string

- HTTP_MAX_REDIRECTS  
  Max number of redirects for http requests.  
  _default_: 5  
  _format_: integer  

- HTTP_TIMEOUT
  Timeout from http requests in ms.  
  _default_: 5000  
  _format_: integer    
  
- JWT_SECRET  
  The secret used to create any JWT token, used for authorization.  
  _default_: ""  
  _format_: string  

- JWT_EXPIRES_IN  
  Expiration time of any JWT token in seconds.  
  _default_: 3600 (s)   
  _format_: integer  

- JWT_NEVER_EXPIRES
  Set if the jwt secret never expires or not.
  _default_: 100y
  _format_: string as in number of years

- LDAP_URL  
  Full URI (including port) of your local LDAP server, if this is your selected authentication method.  
  _default_: No default  
  _example_: ldaps://ldap.server.com:636/  
  _format_: string  

- LDAP_BIND_DN  
  Bind DN to access information on your LDAP server.  
  _default_: No default  
  _format_: string  

- LDAP_BIND_CREDENTIALS  
  Credentials associated with your bind DN to acccess your LDAP server.  
  _default_: No default  
  _format_: string  

- LDAP_SEARCH_BASE  
  Search base for your LDAP server.  
  _default_: No default  
  _format_: string  

- LDAP_SEARCH_FILTER  
  Search filter for you LDAP server.  
  _default_: No default  
  _format_: string  
  _example_: "(LDAPUsername={{username}})"  

- LDAP_MODE
  type of ldap server we are communicating with
  _default_: ad
  _format_: string
  acceptable values: ad, 
  ___NEEDS TO BE UPDATED. Not sure which other values are accepted___

- LDAP_EXTERNAL_ID
  LDAP matching field that provides the external id
  _default_: sAMAccountName
  _format_: string

- LDAP_USERNAME
  LDAP field providing the username
  _default_: displayName
  _format_: string

- OIDC_ISSUER  
  Full URL of your OIDC identity provider  
  _default_: No default  
  _format_: string  
  _example_: "https://identity.your.facility/your/realm"  

- OIDC_CLIENT_ID  
  Client id used to convert OIDC code to OIDC token. This is assigned in the OIDC service when the token is generated  
  _default_: No default  
  _format_: string  
  _example_: "scicat"  

- OIDC_CLIENT_SECRET  
  Token used to convert OIDC code to OIDC token. This is assigned in the OIDC service when the token is generated  
  _example_: "90f1268..."  

- OIDC_CALLBACK_URL  
  URL of the endpoint that is called when the authentication has been executed with the OIDC service.  
  _default_: No default  
  _format_: string  
  _example_: "http://localhost:3000/api/v3/oidc/callback"  

- OIDC_SCOPE
  Information returned by the OIDC service together with token  
  _default_: No default  
  _format_: string  
  _example_: "openid profile email"  

- OIDC_SUCCESS_URL   
  Frontend URL that the user is directed to after a successful authentication. It must be a valid frontend URL.
  _default_: No default  
  _format_: string  
  _example_: "http://localhost:3000/Datasets"

- OIDC_ACCESS_GROUPS  
  field used to retrieve access groups from the OIDC service. It is not used in the vanilla implementation.  
  _default_: No default  
  _format_: string  
  _example_: "access_groups"  

- OIDC_ACCESS_GROUPS_PROPERTY
  name of the OIDC property used to retrieve the users groups from OIDC
  _default_: none
  _format_: string

- OIDC_AUTO_LOGOUT
  if enabled, when login out from SciCat, we logout from OIDC also.
  _default_: false
  _format_: boolean

- OIDC_RETURN_URL
  URL the user is redirected after a successful logout
  _default_: none
  _format_: string

- LOGBOOK_ENABLED
  Flag to enable/disable the Logbook endpoints.  
  accept values: "yes", "no"  
  _default_: no  
  _format_: string  

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
  _default_: No default
  _format_: string "mongodb://<USERNAME>:<PASSWORD>@<HOST>:27017/<DB_NAME>"
  
- OAI_PROVIDER_ROUTE  
  URI to OAI provider, which is used in the `/publisheddata/:id/resync` endpoint.  
  _default_: no default  
  _format_: string  

- PID_PREFIX   
  The facility PID prefix, with trailing slash.
  _default_: no default  
  _format_: string  

- PUBLIC_URL_PREFIX   
  The base URL to the facility Landing Page.  
  _default_: No default  
  _format_: string  
  _example_: "https://doi.ess.eu/detail/"  

- PORT  
  The port on which the backend listen on.  
  _default_: 3000  
  _format_: integer  

- RABBITMQ_ENABLED  
  Flag to enable/disable RabbitMQ consumer.  
  accepted values: "yes", "no"  
  _default_: no  
  _format_: string  
  
- RABBITMQ_HOSTNAME  
  The hostname of the RabbitMQ message broker. Only required if RabbitMQ is enabled.  
  _default_: no default  
  _default_: string  

- RABBITMQ_USERNAME  
  The username used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.  
  _default_: no default  
  _format_: string  

- RABBITMQ_PASSWORD  
  The password used to authenticate to the RabbitMQ message broker. Only required if RabbitMQ is enabled.  
  _default_: no default  
  _format_: string  

- REGISTER_DOI_URI
  URI to the organization that registers the facilities DOIs.  
  _default_: no default  
  _format_: string  
  _example_: "https://mds.test.datacite.org/doi"

- REGISTER_METADATA_URI  
  URI to the organization that registers the facilities published data metadata.  
  _default_: no default  
  _format_: string  
  _example_: ="https://mds.test.datacite.org/metadata"  

- DOI_USERNAME
  Username used to authenticate on the DOI site
  _default_: no default
  _format_: string

- DOI_PASSWORD
  Password used to authenticate on the DOI site
  _default_: no default
  _format_: string

- SITE  
  The name of your site.  
  _default_: no default  
  _format_: string  

- SMTP_HOST  
  Host of SMTP server.   
  _default_: no default    
  _format_: string  

- SMTP_MESSAGE_FROM  
  Email address that emails should be sent from.  
  _default_: no default  
  _format_: string, email  

- SMTP_PORT  
  Port of SMTP server.  
  _default_: no default  
  _format_: string  

- SMTP_SECURE  
  Secure of SMTP server.
  _default_: no default  
  _format_: string  

- POLICY_PUBLICATION_SHIFT
  Number of years that needs to elapse before the dataset is made publicly acceessible
  _default_: 3
  _format_: integer

- POLICY_RETENTION_SHIFT
  Number of years that the datasets are kept online before are archived or deleted. A negative value means that they are never archived/deleted
  _default_: -1
  _format_: integer
