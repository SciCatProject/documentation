# OIDC Integration
SciCat can integrate with one or more OIDC servers to provide Authentication. Integration requires configuration of both Catamel and Catanie in order to setup the redirecting and handshaking required. Additionally, it may writing custom code in catamel in order to properly handle projefile information obtained by the OIDC Auth Provider.

## Catamel Configuration
Configuration of Catamel for OIDC involves adding a provider to `providers.json` file. See [Start Here](./StartHere.md) for more information on configuring this file.

Here is an example of a provider that uses Google as an authenticator. Google is used here because it is well-documented and commonly available.

```json
    "google": {
        "provider": "oidc",
        "authScheme": "openid connect",
        "module": "passport-openidconnect",
        "authPath": "/auth/google",
        "successRedirect": "http://localhost/user",
        "failureRedirect": "http://localhost/login",
        "failureFlash": true,
        "session": false,
        "issuer": "https://accounts.google.com",
        "authorizationURL": "https://accounts.google.com/o/oauth2/v2/auth",
        "tokenURL": "https://oauth2.googleapis.com/token",
        "userInfoURL": "https://openidconnect.googleapis.com/v1/userinfo",
        "clientID": "...",
        "clientSecret": "...",
        "callbackURL": "http://localhost:3000/auth/google/callback",
        "scope": ["email", "profile", "openid"]
    }
```
> Note that information about Google sign in can be found [here](https://developers.google.com/identity/protocols/oauth2/openid-connect), details are beyond the scope of this document.


> Note that OIDC authentication services publish their specific settings in a Discovery document.. To find the settings for, say, google, see <https://accounts.google.com/.well-known/openid-configuration>.

A couple of things to note about this provider example:
* **provider** is used by the loopback-passport-configurator to build a strategy
* **authsheme** is used by the loopback-passport-configurator to build a strategy
* **module** describes the passport module to use. passport-openidconnect is already included in Catamel
* **authPath** is the path that Catamel will create (with the help of loopback-passport-configurator) to begin the authentication process. Catamel will redirect users to this path (once it is configured, of course!)
* **successRedirect** is the URL passed to the OIDC provider instructing it to rediect the user on success. Here we set it to the a development enviornment's user page.
* **failureRedirect** is the URL passed to the OIDC provider instructing it to rediect the user on failed authentication. Here we set it to the a development enviornment's user page login page.
* **failureFlash** is currently unsupported.
* **session** is not needed, since Catanie authenticates outside of sessions.
* **authorizationURL** is specific to your OIDC provider
* **tokenURL** is specific to your OIDC provider
* **userInfoURL** is specific to your OIDC provider
* **clientID** is specific to your OIDC provider
* **clientSecret** is specific to your OIDC provider
* **scope** is specific to your OIDC provider


## Catanie Configuration 

The default login page in Catanie provides a userne/passowrd form that is used both for local and LDAP/AD authentication. When using and OIDC authentication provider, Scicat will not ask the user for credientials directly. Instead, the user will be redirected to the OIDC provider to authetnicate. So, Catanie provides two configuration settings to modify the login page appropriately.

These setting are accomplihsed by modifying the catanie [environmnet document](./Environment.md). 

```javascript
  
  loginFormEnabled: false,
  oAuth2Endpoints: [
    {displayText: "Google", displayImage: "../../../assets/images/btn_google_light_normal_ios.svg", authURL: "auth/google"}]

```


* **loginFormEnabled** sets whether to display the username/password form in the login page
* **oAuth2Endpoints** provides information that Catanie uses to display "Sign in with ..." buttons. Note that this is an array, multiple buttons for multiple OIDC providers can be configured.
  * **displayText** sets the name of the provider to display in the button. In this case, the button will show "Sign In With Google"
  * **displayImage** defines an image to display in the button. The image will end up being 24px tall. It is recommended that the image be in SVG format.
  * **authURL** defines the relative path that the user will be redirected to when they click the button. Note that this maps to the `authPath` setting described above.
