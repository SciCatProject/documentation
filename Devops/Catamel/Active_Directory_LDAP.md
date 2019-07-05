# Active Directory LDAP

SciCat uses loopback passport-ldapauth

Your confiuration files should replace the default providers.json

It should look similar to the template below, with the appropriate LDAP url, bindDn, bindCredentials, searchBase and searchFilter added.

```
{
        "local": {
                "provider": "local",
                "module": "passport-local",
                "usernameField": "username",
                "passwordField": "password",
                "authPath": "/auth/local",
                "successRedirect": "/auth/account",
                "failureRedirect": "/local",
                "failureFlash": true
        },
        "ldap": {
                "provider": "ldap",
                "authScheme": "ldap",
                "module": "passport-ldapauth",
                "authPath": "/auth/msad",
                "successRedirect": "/auth/account",
                "failureRedirect": "/msad",
                "session": true,
                "json": true,
                "failureFlash": true,
                "profileAttributesFromLDAP": {
                        "displayName": "displayName",
                        "email": "mail"
                },
                "server": {
                        "url": "ldaps://myldapserver:ldap_port/",
                        "bindDn": "myldapuser@mydomain.com",
                        "bindCredentials": "mycredentials",
                        "searchBase": "OU=My org unit,DC=my domain,DC=etc,DC=etc",
                        "searchFilter": "(&(samAccountType=myaccountetails)(sAMAccountName={{username}}))"
                }
        }
```
