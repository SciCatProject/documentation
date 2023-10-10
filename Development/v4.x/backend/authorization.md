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


## Group Lists available in Vanilla Configuration 
The permissions in the vanilla installation provides a set of user groups which acquires specific set of permissions. In order to assign a set of permissions to a specific group of user, add such group to the correct list indicated below.

| Configuration Group List | Description | CASL ability actions |
| ------------------------ | ----------- | ------------------- |
| _authenticated users_ | Authenticated users can view/access all datasets that belong to one of the groups they belong to |  DatasetReadOwn |
| | Users can view attachments for datasets belonging to one of their group |  DatasetAttachmentReadOwn  |
| | Users are allowed to view origdatablocks for datasets belonging to one of their group | DatasetOrigdatablockReadOwn |
| | Users are allowed to view datablocks for datasets belonging to one of their group |  DatasetDatablockReadOwn |
| | Users can view the logbook of the datasets that belong to one of their group | DatasetLogbookReadOwn |
| | |
| CREATE_DATASET_GROUPS | Users of the listed groups can create and modify datasets for any of the groups they belong to. At creation time, the system assignes a pid to the new datasets. If the user assigns one, the system will ignore it. |  DatasetCreateOwn , DatasetReadOwn , DatasetUpdateOwn |
| | Users are allowed to perform all operations on attachments for datasets belonging to one of their group | DatasetAttachmentCreateOwn , DatasetAttachmentReadOwn , DatasetAtatchementUpdateOwn , DatasetAttachmentDeleteOwn  |
| | Users are allowed to create and update origdatablocks for datasets belonging to one of their group | DatasetOrigdatablockCreateOwn , DatasetOrigdatablockReadOwn , DatasetOrigdatablockUpdateOwn |
| | Users are allowed to create and update datablocks for datasets belonging to one of their group | DatasetDatablockCreateOwn , DatasetDatablockReadOwn , DatasetDatablockUpdateOwn |
| | Users can view the logbook of the datasets that belong to one of their group | DatasetLogbookReadOwn |
| | |
| CREATE_DATASET_WITH_PID_GROUPS | Users of the listed groups can create and modify datasets for any of the groups they belong to. They are allowed to specify the dataset pid. If they decided not to specify a pid, the system will assign one. | DatasetCreateOwn , DatasetReadOwn , DatasetUpdateOwn |
| | Users are allowed to perform all operations on attachments for datasets belonging to one of their group | DatasetAttachmentCreateOwn , DatasetAttachmentReadOwn , DatasetAtatchementUpdateOwn , DatasetAttachmentDeleteOwn  |
| | Users are allowed to create and update origdatablocks for datasets belonging to one of their group | DatasetOrigdatablockCreateOwn , DatasetOrigdatablockReadOwn , DatasetOrigdatablockUpdateOwn |
| | Users are allowed to create and update datablocks for datasets belonging to one of their group | DatasetDatablockCreateOwn , DatasetDatablockReadOwn , DatasetDatablockUpdateOwn |
| | Users can view the logbook of the datasets that belong to one of their group | DatasetLogbookReadOwn |
| | |
| CREATE_DATASET_PRIVELEGED_GROUPS | Users of the listed groups can create datasets for any group, but can only modify datasets belong to one of the group they belong to. They are allowed to specify pids for new datasets. This settings are suggessted for ingestion functional accounts | DatasetCreateAll , DatasetReadOwn , DatasetUpdateOwn |
| | Users are allowed to perform all operations on attachments for datasets belonging to one of their group | DatasetAttachmentCreateOwn , DatasetAttachmentReadOwn , DatasetAtatchementUpdateOwn , DatasetAttachmentDeleteOwn  |
| | Users are allowed to create origdatablocks for any datasets, but can only update them for datasets belonging to one of their group | DatasetOrigdatablockCreateAny , DatasetOrigdatablockReadOwn , DatasetOrigdatablockUpdateOwn |
| | Users are allowed to create and update datablocks for datasets belonging to one of their group | DatasetDatablockCreateOwn , DatasetDatablockReadOwn , DatasetDatablockUpdateOwn |
| | Users can view the logbook of the datasets that belong to one of their group | DatasetLogbookReadOwn |
| | |
| ADMIN_GROUPS | Users of the listed groups can create and modify datasets belonging to any group. They are allowed to specify the dataset's pid at creation time | DatasetCreateAny , DatasetReadAny , DatasetUpdateAny |
| | Users are allowed to perform all operations on attachments for any datasets | DatasetAttachmentCreateAny , DatasetAttachmentReadAny , DatasetAtatchementUpdateAny , DatasetAttachmentDeleteAny  |
| | Users are allowed to perform all operations on origdatablocks for any datasets, except delete | DatasetOrigdatablockCreateAny , DatasetOrigdatablockReadAny , DatasetOrigdatablockUpdateAny |
| | Users are allowed to perform all operations on datablocks for any datasets, except delete | DatasetDatablockCreateAny , DatasetDatablockReadAny , DatasetDatablockUpdateAny |
| | Users can view logbook for any datasets| DatasetLogbookReadAny | 
| | |
| DELETE_GROUPS | Users whos group is listed here are allowed to delete datasets, origdatablock or datablock | DatasetDeleteAny , DatasetOrigdatablockDeleteAny , DatasetDatablockDeleteAny |

## Users Authorization
Authorization (permissions) are listed by endpoint groups. They are expressed for each type of user group. A user is an Authenticated User if he/she is logged in but it does not belong to any of the group listed in the Configuration Group Lists

### Datasets
#### CASL ability actions
This is the list of the permissions methods available for datasets and all their endpoints
- DatasetCreateOwn
- DatasetCreateAny
- DatasetReadOwn
- DatasetReadAny
- DatasetUpdateOwn
- DatasetUpdateAny
- DatasetDeleteAny
- DatasetAttachmentCreateOwn
- DatasetAttachmentCreateAny
- DatasetAttachmentReadOwn
- DatasetAttachmentReadAny
- DatasetAtatchementUpdateOwn
- DatasetAtatchementUpdateAny
- DatasetAttachmentDeleteOwn
- DatasetAttachmentDeleteAny
- DatasetOrigdatablockCreateOwn
- DatasetOrigdatablockCreateAny
- DatasetOrigdatablockReadOwn
- DatasetOrigdatablockReadAny
- DatasetOrigdatablockUpdateOwn
- DatasetOrigdatablockUpdateAny
- DatasetOrigdatablockDeleteAny
- DatasetDatablockCreateOwn
- DatasetDatablockCreateAny
- DatasetDatablockReadOwn
- DatasetDatablockReadAny
- DatasetDatablockUpdateOwn
- DatasetDatablockUpdateAny
- DatasetDatablockDeleteOwn
- DatasetLogbookReadOwn
- DatasetLogbookReadAny

#### Authorization table
| HTTP method | Endpoint | Anonymous | Authenticated User | Create Dataset Groups | Create Dataset with Pid Groups | Create Dataset Privileged Groups | Admin Groups | Delete Groups |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| POST | Datasets | __no__ | __no__ | Own _DatasetCreateOwn_ |  Own _DatasetCreateOwn_ | Any _DatasetCreateAny_ |  Any _DatasetCreateAny_ | __no__ | 
| POST | Datasets/isValid | __no__ | __no__ | Own  _DatasetCreateOwn_ |  Own _DatasetCreateOwn_ | Any _DatasetCreateAny_ |  Any _DatasetCreateAny_ | __no__ | 
| GET | Datasets | Public | Own _DatasetReadOwn_ | Own  _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ |  Any _DatasetReadyAny_ | __no__ | 
| GET | Datasets/fullquery | Public | Own _DatasetReadOwn_ | Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ | __no__ | 
| GET | Datasets/fullfacet | Public | Own _DatasetReadOwn_ | Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ | __no__ | 
| GET | Datasets/metadataKeys |Public | Own _DatasetReadOwn_ | Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ | __no__ | 
| GET | Datasets/findOne | Public | Own _DatasetReadOwn_ | Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ | __no__ | 
| GET | Datasets/count | Public | Own _DatasetReadOwn_ | Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ | __no__ | 
| GET | Datasets/_pid_ | Public | Own _DatasetReadOwn_ | Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ | __no__ | 
| PATCH | Datasets/_pid_ | __no__ | __no__ | Own _DatasetUpdateOwn_ |  Own _DatasetUpdateOwn_ |  Own _DatasetUpdateOwn_ | Any _DatasetUpdateAny_ | __no__ | 
| PUT | Datasets/_pid_ | __no__ | __no__ | Own _DatasetUpdateOwn_ |  Own _DatasetUpdateOwn_ |  Own _DatasetUpdateOwn_ | Any _DatasetUpdateAny_ | __no__ | 
| POST | Datasets/_pid_/appendToArrayField | __no__ | __no__ | Own _DatasetUpdateOwn_ |  Own _DatasetUpdateOwn_ |  Own _DatasetUpdateOwn_ | Any _DatasetUpdateAny_ | __no__ | 
| | | | | | | | | |
| DELETE | Datasets/_pid_ | __no__ | __no__ | __no__ | __no__ |  __no__ | Any _DatasetDeleteAny_ | 
| | | | | | | | | |
| GET | Datasets/_pid_/thumbnail | Public | Own _DatasetReadOwn_ | Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ |  Own _DatasetReadOwn_ | Any _DatasetReadAny_ | __no__ | 
| | | | | | | | | |
| POST | Datasets/_pid_/attachments |  __no__ | __no__ | Own  _DatasetAttachmentCreateOwn_ |  Own _DatasetAttachmentCreateOwn_ | Any _DatasetAttachmentCreateAny_ |  Any _DatasetAttachmentCreateAny_ | __no__ | 
| GET | Datasets/_pid_/attachments | Public | Own _DatasetAttachmentReadOwn_ | Own  _DatasetAttachmentReadOwn_ |  Own _DatasetAttachmentReadOwn_ | Own _DatasetAttachmentReadOwn_ |  Any _DatasetAttachmentCreateAny_ | __no__ | 
| PUT | Datasets/_pid_/attachments/_aid_ | __no__ | __no__ | Own  _DatasetAttachmentUpdateOwn_ |  Own _DatasetAttachmentUpdateOwn_ | Own _DatasetAttachmentUpdateOwn_ |  Any _DatasetAttachmentCreateAny_ | __no__ | 
| DELETE | Datasets/_pid_/attachments/_aid_ | __no__ | __no__ | Own  _DatasetAttachmentDeleteOwn_ |  Own _DatasetAttachmentDeleteOwn_ | Own _DatasetAttachmentDeleteOwn_ |  Any _DatasetAttachmentDeleteAny_ | __no__ | 
| | | | | | | | | |
| POST | Datasets/_pid_/origdatablocks |  __no__ | __no__ | Own  _DatasetOrigdatablockCreateOwn_ |  Own _DatasetOrigdatablockCreateOwn_ | Any _DatasetOrigdatablockCreateAny_ |  Any _DatasetOrigdatablockCreateAny_ | __no__ | 
| POST | Datasets/_pid_/origdatablocks/isValid |  __no__ | __no__ | Own  _DatasetOrigdatablockCreateOwn_ |  Own _DatasetOrigdatablockCreateOwn_ | Any _DatasetOrigdatablockCreateAny_ |  Any _DatasetOrigdatablockCreateAny_ | __no__ | 
| GET | Datasets/_pid_/origdatablocks | Public | Own _DatasetOrigdatablockReadOwn_ | Own _DatasetOrigdatablockReadOwn_ |  Own _DatasetOrigdatablockReadOwn_ | Own _DatasetOrigdatablockReadOwn_ |  Any _DatasetOrigdatablockReadAny_ | __no__ | 
| PATCH | Datasets/_pid_/origdatablocks/_oid_ | __no__ | __no__ | Own  _DatasetOrigdatablockUpdateOwn_ |  Own _DatasetOrigdatablockUpdateOwn_ | Own _DatasetOrigdatablockUpdateOwn_ |  Any _DatasetOrigdatablockCreateAny_ | __no__ | 
| DELETE | Datasets/_pid_/origdatablocks/_oid_ | __no__ | __no__ | __no__ |  __no__ | __no__ |  __no__ | Any _DatasetOrigdatablockDeleteAny_ | 
| | | | | | | | | |
| POST | Datasets/_pid_/datablocks |  __no__ | __no__ | Own  _DatasetDatablockCreateOwn_ |  Own _DatasetDatablockCreateOwn_ | Own _DatasetDatablockCreateOwn_ |  Any _DatasetDatablockCreateAny_ | __no__ | 
| GET | Datasets/_pid_/datablocks | Public | Own _DatasetDatablockReadOwn_ | Own  _DatasetDatablockReadOwn_ |  Own _DatasetDatablockReadOwn_ | Own _DatasetDatablockReadOwn_ |  Any _DatasetDatablockReadAny_ | __no__ | 
| PATCH | Datasets/_pid_/datablocks/_oid_ | __no__ | __no__ | Own _DatasetDatablockUpdateOwn_ |  Own _DatasetDatablockUpdateOwn_ | Own _DatasetDatablockUpdateOwn_ |  Any _DatasetDatablockCreateAny_ | __no__ | 
| DELETE | Datasets/_pid_/datablocks/_oid_ | __no__ | __no__ | __no__ |  __no__ | __no__ | __no__ | Any _DatasetDatablockDeleteAny_ | 
| | | | | | | | | |
| GET | Datasets/_pid_/logbook | __no__ | Own  _DatasetLogbookReadOwn_ |  Own _DatasetLogbookReadOwn_ | Own _DatasetLogbookReadOwn_ |  Any _DatasetLogbookReadAny_ | __no__ | 

### OrigDatablock
#### CASL ability actions
- OrigdatablockCreateOwn
- OrigdatablockCreateAny
- OrigdatablockReadOwn
- OrigdatablockReadAny
- OrigdatablockUpdateOwn
- OrigdatablockUpdateAny
- OrigdatablockDeleteAny

#### Authorization table
| HTTP method | Endpoint | Anonymous | Authenticated User | Create Dataset Groups | Create Dataset with Pid Groups | Create Dataset Privileged Groups | Admin Groups | Delete Groups |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| POST | origdatablocks |  __no__ | __no__ | Own  _OrigdatablockCreateOwn_ |  Own _OrigidatablockCreateOwn_ | Any _OrigdatablockCreateAny_ |  Any _OrigdatablockCreateAny_ | __no__ | 
| POST | origdatablocks/isValid |  __no__ | __no__ | Own  _OrigdatablockCreateOwn_ |  Own _OrigdatablockCreateOwn_ | Any _OrigdatablockCreateAny_ |  Any _OrigdatablockCreateAny_ | __no__ | 
| GET | origdatablocks | Public | Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Any _OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/_oid_ | Public | Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Any _OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/fullquery | Public | Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Any _OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/fullquery/files | Public | Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Any _OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/fullfacet | Public | Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Own _OrigdatablockReadOwn_ | Own _OrigdatablockReadOwn_ |  Any _OrigdatablockReadAny_ | __no__ | 
| PATCH | origdatablocks/_oid_ | __no__ | __no__ | Own  _OrigdatablockUpdateOwn_ |  Own _OrigdatablockUpdateOwn_ | Own _OrigdatablockUpdateOwn_ |  Any _OrigdatablockCreateAny_ | __no__ | 
| DELETE | origdatablocks/_oid_ | __no__ | __no__ | __no__ |  __no__ | __no__ |  __no__ | Any _OrigdatablockDeleteAny_ | 


### Users
#### CASL ability actions
- UserReadOwn
- UserReadAny
- UserCreateOwn
- UserCreateAny
- UserUpdateOwn
- UserUpdateAny
- UserUpdatePasswordOwn
- UserUpdatePasswordAny
- UserDeleteAny


#### Authorization table:
| HTTP method | Endpoint | Anonymous | Authenticated User | User Privileged Groups | Admin Groups | Delete Groups |
| ----------- | -------- | --------- | ------------------ | ---------------------- | ------------ |  ------------- |
| POST | Users/jwt | __no__ | Own | __no__ | __no__ | __no__ |
| POST | Users/login | Any | __no__ | __no__ | __no__ | __no__ |
| GET | Users/_id_ | __no__ | Own _UserReadOwn_ | Any _UserReadAny_ | Any _UserReadAny_ | __no__ |
| GET | Users/_id_/userIdentity | __no__ | Own _UserReadOwn_ | Any _UserReadAny_ | Any _UserReadAny_ | __no__ |
| POST | Users/_id_/settings | __no__ | Own _UserCreateOwn_ | Any _UserCreateAny_ | Any _UserCreateAny_ | __no__ |
| GET | Users/_id_/settings | __no__ | Own _UserReadOwn_ | Any _UserReadAny_ | Any _UserReadAny_ | __no__ |
| PUT | Users/_id_/settings | __no__ | Own _UserUpdateOwn_ | Any _UserUpdateAny_ | Any _UserUpdateAny_ | __no__ |
| PATCH | Users/_id_/settings | __no__ | Own _UserUpdateOwn_ | Any _UserUpdateAny_ | Any _UserUpdateAny_ | __no__ |
| PATCH | Users/_id_/password | __no__ | Own _UserUpdatePasswordOwn_ | Any _UserUpdatePasswordAny_ | Any _UserUpdatePasswordAny_ | __no__ |
| DELETE | Users/_id_ | __no__ | __no__ | __no__ | __no__ | Any _UserDeleteAny_ |
| DELETE | Users/_id_/settings | __no__ | __no__ | __no__ | __no__ | Any _UserDeleteAny_ |
| GET | Users/_id_/authorization/dataset/create | __no__ | Own _UserReadOwn_ | Own _UserReadOwn_ | Any _UserReadAny_ | __no__ |
| GET | Users/logout | __no__ | Own | __no__ | __no__ | __no__ |
| GET | useridentities/findOne | __no__ | Own _UserReadOwn_ | Any _UserReadAny_ | Any _UserReadAny_ | __no__ |


