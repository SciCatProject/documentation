# OIDC Integration
SciCat can integrate with one or more OIDC servers to provide Authentication. Integration requires configuration of both backend and frontend in order to set up the redirecting and handshaking that the OAuth2 code flow requires. Additionally, it may involve writing [custom code hooks](#backend-code-hooks)  in the backend in order to properly handle profile information obtained by the OIDC Auth Provider.

## Backend Configuration
Configuration of the backend for OIDC involves adding the following environmental variables to `scicat-backend-next`:


* `OIDC_ISSUER` - the URL of your OIDC issuer e.g. https://keycloak.myorg.com/realm/myrealm
* `OIDC_AUTHORIZATION_URL` - the URL of your authorization provider e.g. "https://keycloak.myorg.com/"
* `OIDC_CLIENT_ID` - the client id that the OIDC issuer recognises
* `OIDC_CLIENT_SECRET` - the client secret associated with the above id
* `OIDC_CALLBACK_URL` - the URL which will be called by the OIDC after authentication e.g https://scicat.myorg.com/api/v3/auth/oidc/callback
* `OIDC_SCOPE` - the scopes required by Scicat from the OIDC provider 
* `OIDC_SUCCESS_URL` - the URL to redirect to after a successful login e.g "https://scicat.myorg.com/auth-callback"
* `OIDC_ACCESS_GROUPS` - the scope name for access groups in your OIDC provider 
    

A minimal .env for OIDC may look like this:
```angular2html
OIDC_ISSUER=https://keycloak.myorg.com/realm/myrealm
OIDC_AUTHORIZATION_URL=https://keycloak.myorg.com/
OIDC_CLIENT_ID=scicat
OIDC_CLIENT_SECRET=my-super-scicat-secret-123
OIDC_CALLBACK_URL=https://scicat.myorg.com/api/v3/auth/oidc/callback
OIDC_SCOPE='openid profile email'
OIDC_SUCCESS_URL=https://scicat.myorg.com/auth-callback
OIDC_ACCESS_GROUPS=accessgroups
```

> Note that information about Google sign in can be found [here](https://developers.google.com/identity/protocols/oauth2/openid-connect), details are beyond the scope of this document.


> Note that OIDC authentication services publish their specific settings in a Discovery document. To find the settings for, say, google, see <https://accounts.google.com/.well-known/openid-configuration>.

