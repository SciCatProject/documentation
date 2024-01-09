# OIDC Integration
SciCat can integrate with one or more OIDC servers to provide Authentication. Integration requires configuration of both backend and frontend in order to setup the redirecting and handshaking that the OAuth2 code flow requires. Additionally, it may involve writing [custom code hooks](#backend-code-hooks)  in the backend in order to properly handle profile information obtained by the OIDC Auth Provider if you are using a specialised provider.

## Backend Configuration

The backend configuration requires the following to be set as environmental variables in order to work with OIDC.
```
OIDC_ISSUER = https://oidc-issuer-address.org # the URL of your OIDC issuer
OIDC_CLIENT_ID = myClient # The client you use to access it
OIDC_CLIENT_SECRET = mySciCatSecret # the secret belonging to the client
OIDC_CALLBACK_URL = https://scicat.myinstitute.org/api/v3/auth/oidc/callback  # the callback url, the root is your scicat url with the suffix api/v3/auth/oidc/callback
OIDC_SCOPE = email profile openid # the scopes from your oidc provider that are required by SciCat
OIDC_SUCCESS_URL = https://scicat.myinstitute.org/login # the success URL is your scicat url with the suffix login 
```

## Frontend Configuration

The `frontend.config.json` requires the following variables to be set to work with OIDC.
```
 
      "accessTokenPrefix": "Bearer ", # make sure there is a whitespce between Bearer and the end quotes
      "lbBaseURL": "https://scicat.myinstitute.org" # the address you are returning to after authentication if it is not 127.0.0.1:3000
      "oAuth2Endpoints": [
       {"displayText": "My Institute SSO", "authURL": "api/v3/auth/oidc"}
      ]

```
SciCat requires you to specify the `accesstokenprefix` in order to find the the token in the OAuth response. 

`lbBaseURL` configures the base URL that the SciCat frontend-to-backend (API) service that the frontend will communicate with. It will therefore match the roots of the `OIDC_CALLBACK_URL` and the `OIDC_SUCCESS_URL` in the backend OIDC configurations.

In the `oAuth2Endpoints` include the display text you want to see on the Login button and the suffix of the authURL which is `api/v3/auth/oidc` (the preffix is set as the `lbBaseURL`).

