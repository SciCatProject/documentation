# Users Authorization
## CASL ability actions
This is the list of the permissions methods available for datasets and all their endpoints
##### Endpoint authorization
- UserLogin
- UserRead
- UserCreate
- UserUpdate
- UserPassword
- UserDelete

##### Instance authorization
- UserReadOwn
- UserReadAny
- UserCreateOwn
- UserCreateAny
- UserUpdateOwn
- UserUpdateAny
- UserPasswordOwn
- UserPasswordAny
- UserDeleteAny

#### Priority
```mermaid
graph TD;
    UserLogin(E)
    UserCreate(E)-->UserCreateOwn(I)-->UserCreateAny(I);
    UserRead(E)-->UserReadOwn(I)-->UserReadAny(I);
    UserUpdate(E)-->UserUpdateOwner(I)-->UserUpdateAny(I);
    UserPassword(E)-->UserPasswordOwner(I)-->UserPasswordAny(I);
    UserDelete(E)-->UserDeleteOwn(I)-->UserDeleteAny(I);
```



#### Authorization table:
| HTTP method | Endpoint | Endpoint Authorization | Anonymous | Authenticated User | User Privileged Groups | Admin Groups | User Delete Groups |  
| ----------- | -------- | --------- | ------------------ | ---------------------- | ------------ |  ------------- | ------------- | 
| POST | Users/jwt | _UserRead_ | __no__ | Own<br/>_UserReadOwn_ | __no__ | __no__ | __no__ |
| POST | Users/login | _UserLogin_ | __no__ | __no__ | __no__ | __no__ | __no__ |
| GET | Users/_id_ | _UserRead_ | __no__ | Own<br/>_UserReadOwn_ | Any<br/>_UserReadAny_ | Any<br/>_UserReadAny_ | __no__ |
| GET | Users/_id_/userIdentity | _UserRead_ | __no__ | Own<br/>_UserReadOwn_ | Any<br/>_UserReadAny_ | Any<br/>_UserReadAny_ | __no__ |
| POST | Users/_id_/settings | _UserCreate_ | __no__ | Own<br/>_UserCreateOwn_ | Any<br/>_UserCreateAny_ | Any<br/>_UserCreateAny_ | __no__ |
| GET | Users/_id_/settings | _UserUpdate_ | __no__ | Own<br/>_UserReadOwn_ | Any<br/>_UserReadAny_ | Any<br/> _UserReadAny_ | __no__ |
| PUT | Users/_id_/settings | _UserUpdate_ | __no__ | Own<br/>_UserUpdateOwn_ | Any<br/>_UserUpdateAny_ | Any<br/>_UserUpdateAny_ | __no__ |
| PATCH | Users/_id_/settings | _UserUpdate_ | __no__ | Own<br/>_UserUpdateOwn_ | Any<br/>_UserUpdateAny_ | Any<br/>_UserUpdateAny_ | __no__ |
| PATCH | Users/_id_/password | _UserPassword_ | __no__ | Own<br/>_UserPasswordOwn_ | Any<br/>_UserPasswordAny_ | Any<br/>_UserPasswordAny_ | __no__ |
| DELETE | Users/_id_ | _UserDelete_ | __no__ | __no__ | __no__ | __no__ | Any<br/>_UserDeleteAny_ |
| DELETE | Users/_id_/settings | _UserDelete_ | __no__ | __no__ | __no__ | __no__ | Any<br/>_UserDeleteAny_ |
| GET | Users/_id_/authorization/dataset/create | _UserRead_ | __no__ | Own<br/>_UserReadOwn_ | Own<br/>_UserReadOwn_ | Any<br/>_UserReadAny_ | __no__ |
| GET | Users/logout | _UserLogout_ | __no__ | Own<br/>_UserLogoutOwn_ | __no__ | __no__ | __no__ |
| GET | useridentities/findOne | _UserRead_ | __no__ | Own<br/>_UserReadOwn_ | Any<br/>_UserReadAny_ | Any<br/>_UserReadAny_ | __no__ |


