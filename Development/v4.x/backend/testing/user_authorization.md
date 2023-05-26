# User Authorization

User authorization tests access to the Users endpoints according to the default configuration provided in the vanilla installation and illustrated at the beginning of this document.

| Test Number | HTTP Method | Endpoint | Authenticated User | User to be checked | Request Status | Results |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | GET | Users/_uid_/authorization/dataset/create | ingestor | _herself_ | 200 | ```{authorization: true}``` |
| 0020 | GET | Users/_uid_/authorization/dataset/create | admin | _herself_ | 200 | ```{authorization: true}``` |
| 0030 | GET | Users/_uid_/authorization/dataset/create | admin | user1 | 200 | ```{authorization: true}``` |
| 0040 | GET | Users/_uid_/authorization/dataset/create | admin | user2 | 200 | ```{authorization: true}``` |
| 0050 | GET | Users/_uid_/authorization/dataset/create | admin | user3 | 200 | ```{authorization: true}``` |
| 0060 | GET | Users/_uid_/authorization/dataset/create | admin | user4 | 200 | ```{authorization: false}``` |
| 0070 | GET | Users/_uid_/authorization/dataset/create | user1 | _herself_ | 200 | ```{authorization: true}``` |
| 0080 | GET | Users/_uid_/authorization/dataset/create | user1 | admin | 403 | n/a |
| 0090 | GET | Users/_uid_/authorization/dataset/create | user1 | user2 | 403 | n/a |
| 0100 | GET | Users/_uid_/authorization/dataset/create | user1 | user3 | 403 | n/a |
| 0110 | GET | Users/_uid_/authorization/dataset/create | user1 | user4 | 403 | n/a |
| 0120 | GET | Users/_uid_/authorization/dataset/create | user2 | _herself_ | 200 | ```{authorization: true}``` |
| 0130 | GET | Users/_uid_/authorization/dataset/create | user3 | _herself_ | 200 | ```{authorization: true}``` |
| 0140 | GET | Users/_uid_/authorization/dataset/create | user4 | _herself_ | 200 | ```{authorization: false}``` |
| 0144 | GET | Users/_uid_/authorization/dataset/create | _anonymous_ | admin | 401 | n/a |
| 0146 | GET | Users/_uid_/authorization/dataset/create | _anonymous_ | user1 | 401 | n/a |
| 0150 | POST | Users/jwt | _anonymous_ | n/a | 201 | ```{jwt: <NEW_JWT>}``` |
| 0160 | POST | Users/jwt | admin | n/a | 201 | ```{jwt: <NEW_JWT>}``` |
| 0170 | POST | Users/jwt | user1 | n/a | 201 | ```{jwt: <NEW_JWT>}``` |
| 0180 | GET | Users/_uid_ | admin | _herself_ | 200 | ```Admin user model without password``` |
| 0190 | GET | Users/_uid_ | admin | user1 | 200 | ```User1 user model without password``` |
| 0200 | GET | Users/_uid_ | user1 | _herself_ | 200 | ```User1 user model without password``` |
| 0210 | GET | Users/_uid_ | user1 | admin | 403 | n/a |
| 0220 | GET | Users/_uid_ | user1 | user2 | 403 | n/a |
| 0230 | GET | Users/_uid_ | _anonymous_ | admin | 401 | n/a |
| 0240 | GET | Users/_uid_ | _anonymous_ | user1 | 401 | n/a |
| 0250 | GET | Users/_uid_/userIdentity | admin | _herself_ | 200 | ```Admin user identity model``` |
| 0260 | GET | Users/_uid_/userIdentity | admin | user1 | 200 | ```User1 user identity model``` |
| 0270 | GET | Users/_uid_/userIdentity | user1 | _herself_ | 200 | ```User1 user identity model``` |
| 0280 | GET | Users/_uid_/userIdentity | user1 | admin | 403 | n/a |
| 0290 | GET | Users/_uid_/userIdentity | user1 | user2 | 403 | n/a |
| 0300 | GET | Users/_uid_/userIdentity | _anonymous_ | admin | 401 | n/a |
| 0310 | GET | Users/_uid_/userIdentity | _anonymous_ | user1 | 401 | n/a |
| 0320 | GET | Users/_uid_/settings | admin | _herself_ | 200 | ```Admin user settings model``` |
| 0330 | GET | Users/_uid_/settings | admin | user1 | 200 | ```User1 user settings model``` |
| 0340 | GET | Users/_uid_/settings | user1 | _herself_ | 200 | ```User1 user settings model``` |
| 0350 | GET | Users/_uid_/settings | user1 | admin | 403 | n/a |
| 0360 | GET | Users/_uid_/settings | user1 | user2 | 403 | n/a |
| 0370 | GET | Users/_uid_/settings | _anonymous_ | admin | 401 | n/a |
| 0380 | GET | Users/_uid_/settings | _anonymous_ | user1 | 401 | n/a |
| 0390 | GET | Users/userIdentities/findOne | admin | _herself_ | 200 | ```Admin user identity model``` |
| 0400 | GET | Users/userIdentities/findOne | admin | user1 | 200 | ```User1 user identity model``` |
| 0410 | GET | Users/userIdentities/findOne | user1 | _herself_ | 200 | ```User1 user identity model``` |
| 0420 | GET | Users/userIdentities/findOne | user1 | admin | 403 | n/a |
| 0430 | GET | Users/userIdentities/findOne | user1 | user2 | 403 | n/a |
| 0440 | GET | Users/userIdentities/findOne | _anonymous_ | admin | 401 | n/a |
| 0450 | GET | Users/userIdentities/findOne | _anonymous_ | user1 | 401 | n/a |
| 0460 | POST | Users/_uid_/jwt | admin | _herself_ | 201 | ```{ "jwt" : "<JWT-TOKEN>"}``` |
| 0470 | POST | Users/_uid_/jwt | admin | user1 | 201 | ```{ "jwt" : "<JWT-TOKEN>"}``` |
| 0480 | POST | Users/_uid_/jwt | user1 | _herself_ | 403 | n/a |
| 0490 | POST | Users/_uid_/jwt | user1 | admin | 403 | n/a |
| 0500 | POST | Users/_uid_/jwt | user1 | user2 | 403 | n/a |
| 0510 | POST | Users/_uid_/jwt | _anonymous_ | admin | 401 | n/a |
| 0520 | POST | Users/_uid_/jwt | _anonymous_ | user1 | 401 | n/a |