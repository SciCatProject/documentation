# OIDC Integration
SciCat can integrate with one or more OIDC servers to provide Authentication. Integration requires configuration of both Catamel and Catanie in order to setup the redirecting and handshaking that the OAuth2 code flow requires. Additionally, it may involve writing [custom code hooks](catamel-code-hooks)  in catamel in order to properly handle profile information obtained by the OIDC Auth Provider.

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
        "scope": ["email", "profile", "openid"],
        "loginCallback": "sampleLoginCallback"
    }
```
> Note that information about Google sign in can be found [here](https://developers.google.com/identity/protocols/oauth2/openid-connect), details are beyond the scope of this document.


> Note that OIDC authentication services publish their specific settings in a Discovery document.. To find the settings for, say, google, see <https://accounts.google.com/.well-known/openid-configuration>.

Details about the fields in this provider configuration:
* **provider** is used by the loopback-passport-configurator to build a strategy
* **authScheme** is used by the loopback-passport-configurator to build a strategy
* **module** describes the passport module to use. passport-openidconnect is already included in Catamel
* **authPath** is the path that Catamel will create (with the help of loopback-passport-configurator) to begin the authentication process. Catamel will redirect users to this path (once it is configured, of course!)
* **successRedirect** is the URL passed to the OIDC provider instructing it to redirect the user on success. Here we set it to the a development environment's user page.
* **failureRedirect** is the URL passed to the OIDC provider instructing it to redirect the user on failed authentication. Here we set it to the a development environment's user page login page.
* **failureFlash** is currently unsupported.
* **session** is not needed, since Catanie authenticates outside of sessions.
* **authorizationURL** is specific to your OIDC provider
* **tokenURL** is specific to your OIDC provider
* **userInfoURL** is specific to your OIDC provider
* **clientID** is specific to your OIDC provider
* **clientSecret** is specific to your OIDC provider
* **scope** is specific to your OIDC provider
* **loginCallback** optional name of a [callback](#configure-callback) function to run to add profile information to the UserIdentity


## Catanie Configuration 

The default login page in Catanie provides a username/password form that is used both for local and LDAP/AD authentication. When using and OIDC authentication provider, SciCat will not ask the user for credential directly. Instead, the user will be redirected to the OIDC provider to authenticate. So, Catanie provides two configuration settings to modify the login page appropriately.

These setting are accomplished by modifying the catanie [environment document](./Environment.md). 

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

## Catamel Code Hooks

Configuring Catamel and Catanie to authenticate through OIDC is very useful for providing a third party authentication. However, there two issues that come up that can be addressed with Catamel code hooks:

* By default, the system will authenticate all users who pass come in through the OAuth Provider. 
* By default, the users profile in the application will contain information gathered from the OAuth Provider, and nothing more.

### Prevent Authenticating Unkown Users

In [Catamel Configuration](#catamel-configuration), we configured the loginCallback. The value of this file is the name of a function that must be defined and exported. See [login-call.js](https://github.com/SciCatProject/catamel/blob/develop/server/boot/login-callbacks.js) for details.

Code snippet is presented for as an example, omitting the particular details about communicating with an external system:

```javascript

module.exports.sampleLoginCallback = function(req, done) {
  return function(err, user, identity, token) {

    var authInfo = {
      identity: identity,
    };
    if (token) {
      authInfo.accessToken = token;
    }

    const requestURL = getUserURL(identity);
    if (!requestURL){
      logger.logError(`unexpected authenticator type: ${identity.provider}`);
      done();
      return;
    }
    request(requestURL, function (error, response, body) {
      // ask external system for the user's profile information
      if (error){
        // and error occurred talking to the external system (possibly from a connection issue)...deny login
        logger.logError(`error talking to external ${error.message}`);
        done(err, null, null);
        return;
      }
      if (response.statusCode == 200) {
        const bodyObj = JSON.parse(body);
        logger.logInfo("user service returned", bodyObj);
      }
      else{
        logger.logError(`external system replied with an error ${response.statusCode} - ${body}.`);
        // external system replied with a negative response...deny login
        done(err, null, null);
        return;
      }
      //accept login
      done(err, user, authInfo);
    });
  };
};
```
### Add information to User's Profile 

By default profile information from the Authentication Provider will be added to the user's profile. This profile is stored in the DaCat database `UserIdentity` collection. This collection is created by the loopback-component-passport library, and is also used for LDAP authentication. Catamel LDAP integrations populate this collection with the user's LDAP profile information automatically with a callback. One of the most important things that is added to the profile is the user's accessGroups field, which is critical to calculating a user's privilege in SciCat.

One way to mimic this with an OAuth2 provider is to use a `before save` [Loopback Operation Hook](https://loopback.io/doc/en/lb3/Operation-hooks.html). This hook will get called as the user logs in and allows you to add information to the `UserIdentity` collection, which will be used in a variety of places, including access controls.

The following code snippet is presented for as an example, omitting the particular details about communicating with an external system:

```javascript
// Observe saving UserIdentity. This gives us the ability to update the user profile with facility-specific groups
module.exports = function (app) {
  app.models.UserIdentity.observe("before save", function(ctx, next) {
    if (!ctx.data){
      logger.logInfo("No context data from UserIdentity");
      next();
      return;
    }
    request(userURL, function (error, response, _body) {
      // ask external system for user information so we can get group info
      if (error){
        logger.logError(`error talking to external system ${error.message}`);
        next();
        return;
      }
      if (response.statusCode == 200){
        // add groups to profile, saving in the UserIdentity model
        ctx.data.profile.accessGroups = JSON.parse(response.body).groups;
      }
      next();
    });
  });
};
```
