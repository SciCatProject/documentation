# Authorization
### aka permissions aka who can do what

SciCat backend v4.x rely on [CASL](https://casl.js.or) to manage permissions.  
The default vanilla installation of the backend is configured with the permissions described below.   
To avoid confusion and clarify the terminology used below, the term _User_ indicates a normal authenticated user with no elevated permissions, while _Admin_ indicates any user who belongs to a group that it is listed in the environmental variable ADMIN_GROUPS.  
By default ADMIN_GROUPS is set to groups: admin, ingestor, archivemanager.
Special case is for deleting items in SciCat. Users with groups listed in DELETE_GROUPS, are allowed to perform delete. Default value is archivemanager.

In V3.x, permissions were managed through roles. In V4.x, roles are not used, and they are converted to user group.

By default, the default functional accounts are assigned to groups as follow:
- user: admin  
  group: admin  

- user: ingestor  
  group: ingestor  

- user: archiveManager  
  group: archivemanager

This allow for the flexibility required by many installations in different facilities with different needs.  

Authorization (permissions) are listed by endpoint groups  

## Datasets
| HTTP method | Endpoint | Anonymous | User | Admin | Delete Admin | Permissions Methods |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- |
| POST | Datasets | no | _Own_ | _Any_ | n/a | DatasetCreateOwn, DatasetCreateAny |
| POST | Datasets/isValid | no | _Own_ | _Any_ | n/a | DatasetCreateOwn, DatasetCreateAny | 
| GET | Datasets | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| GET | Datasets/fullquery | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| GET | Datasets/fullfacet | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| GET | Datasets/metadataKeys | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| GET | Datasets/findOne | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| GET | Datasets/count | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| GET | Datasets/_pid_ | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| PATCH | Datasets/_pid_ | no | _Own_ | _Any_ | n/a | DatasetUpdateOwn, DatasetUpdateAny | 
| PUT | Datasets/_pid_ | no | _Own_ | _Any_ | n/a | DatasetUpdateOwn, DatasetUpdateAny | 
| DELETE | Datasets/_pid_ | no | no | no | _Any_ | DatasetDeleteOwn, DatasetDeleteAny | 
| POST | Datasets/_pid_/appendToArrayField | no | _Own_ | _Any_ | n/a | DatasetUpdateOwn, DatasetUpdateAny | 
| GET | Datasets/_pid_/thumbnail | _Public_ | _Own_ | _Any_ | n/a | DatasetReadOwn, DatasetReadAny | 
| POST | Datasets/_pid_/attachments | no | _Own\_dataset_ | _Any_ | n/a | DatasetAttachmentCreateOwn, DatasetAttachmentCreateAny | 
| GET | Datasets/_pid_/attachments | _Public_ | _Own_ | _Any_ | n/a | DatasetAttachmentReadOwn, DatasetAttachmentReadAny | 
| PUT | Datasets/_pid_/attachments/_aid_ | no | _Own_ | _Any_ | n/a | DatasetAttachmentUpdateOwn, DatasetAttachmentUpdateAny | 
| DELETE | Datasets/_pid_/attachments/_aid_ | no | _Own_ | _Any_ | _Any_ | DatasetAttachmentDeleteOwn, DatasetAttachmentDeleteAny | 
| POST | Datasets/_pid_/origdatablocks | no | _Own\_dataset_ | _Any_ | n/a | DatasetOrigdatablockCreateOwn, DatasetOrigdatablockCreateAny | 
| POST | Datasets/_pid_/origdatablocks/isValid | no | _Own\_dataset_ | _Any_ | n/a | DatasetOrigdatablockCreateOwn, DatasetOrigdatablockCreateAny | 
| GET | Datasets/_pid_/origdatablocks | _Public_ | _Own_ | _Any_ | n/a | DatasetOrigdatablockReadOwn, DatasetOrigdatablockReadAny | 
| PATCH | Datasets/_pid_/origdatablocks/_oid_ | no | _Own_ | _Any_ | n/a | DatasetOrigdatablockUpdateOwn, DatasetOrigdatablockUpdateAny | 
| DELETE | Datasets/_pid_/origdatablocks/_oid_ | no | _Own_ | _Any_ | _Any_ | DatasetOrigdatablockDeleteOwn, DatasetOrigdatablockDeleteAny | 
| POST | Datasets/_pid_/datablocks | no | _Own\_dataset_ | _Any_ | n/a | DatasetDatablockCreateOwn, DatasetDatablockCreateAny | 
| GET | Datasets/_pid_/datablocks | _Public_ | _Own_ | _Any_ | n/a | DatasetDatablockReadOwn, DatasetDatablockReadAny | 
| PATCH | Datasets/_pid_/datablocks/_oid_ | no | _Own_ | _Any_ | n/a | DatasetDatablockUpdateOwn, DatasetDatablockUpdateAny | 
| DELETE | Datasets/_pid_/datablocks/_oid_ | no | _Own_ | _Any_ | _Any_ | DatasetDatablockDeleteOwn, DatasetDatablockDeleteAny | 
| GET | Datasets/_pid_/logbook | no | _Own_ | _Any_ | n/a | DatasetLogbookReadOwn, DatasetLogbookReadAny | 


## Users

List of available actions:
- UserReadOwn
- UserReadAny
- UserCreateOne
- UserCreateAny
- UserUpdateOwn
- UserUpdateAny
- UserDeleteOwn
- UserDeleteAny


Authorization table:

| HTTP method | Endpoint | Anonymous | User | Admin | Delete | Permissions Methods |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- |
| POST | Users/jwt | yes | yes | n/a | n/a | n/a |
| POST | Users/login | no | _Own_ | n/a | n/a | n/a |
| GET | Users/_id_ | no | _Own_ | _Any_ | n/a | UserReadOwn, UserReadAny |
| GET | Users/_id_/userIdentity | no | _Own_ | _Any_ | n/a | UserReadOwn, UserReadAny |
| POST | Users/_id_/settings | no | _Own_ | _Any_ | n/a | UserCreateOwn, UserCreateAny |
| GET | Users/_id_/settings | no | _Own_ | _Any_ | n/a | UserReadOwn, UserReadAny |
| PUT | Users/_id_/settings | no | _Own_ | _Any_ | n/a | UserUpdateOwn, UserUpdateAny |
| PATCH | Users/_id_/settings | no | _Own_ | _Any_ | n/a | UserUpdateOwn, UserUpdateAny |
| DELETE | Users/_id_/settings | no | _Own_ | _Any_ | n/a | UserDeleteOwn, UserDeleteAny |
| GET | Users/_id_/authorization/dataset/create | no | _Own_ | _Any_ | n/a | UserReadOwn, UserReadAny |
| GET | Users/logout | no | _if logged in_ | n/a | n/a | n/a |
| GET | useridentities/findOne | no | _Own_ | _Any_ | n/a | UserReadOwn, UserReadAny |

