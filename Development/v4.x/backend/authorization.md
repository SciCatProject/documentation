# Authorization
### aka permissions 
### aka who can do what

SciCat backend v4.x rely on [CASL](https://casl.js.or) to manage permissions.  
The default vanilla installation of the backend is configured with the permissions described and linked below.   
To avoid confusion and clarify the terminology used below, the term _User_ indicates a normal authenticated user with no elevated permissions, while _Admin_ indicates any user who belongs to a group that it is listed in the environmental variable ADMIN_GROUPS.  
By default ADMIN_GROUPS is set to groups: admin, ingestor, archivemanager.
Special case is for deleting items in SciCat. Users with groups listed in DELETE_GROUPS, are allowed to perform delete. Default value is archivemanager.

___IMPORTANT___ In V3.x, permissions were managed through roles. In V4.x, roles are not used, and they are converted to user group.

In the vanilla installation, the default functional accounts are assigned to groups as follow:
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
| CREATE_DATASET_PRIVILEGED_GROUPS | Users of the listed groups can create datasets for any group, but can only modify datasets belong to one of the group they belong to. They are allowed to specify pids for new datasets. This settings are suggested for ingestion functional accounts | DatasetCreateAll , DatasetReadOwn , DatasetUpdateOwn |
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
| DELETE_GROUPS | Users whose group is listed here are allowed to delete datasets, origdatablock or datablock | DatasetDeleteAny , DatasetOrigdatablockDeleteAny , DatasetDatablockDeleteAny |

## Subsystems
- [Datasets](authorization/authorization_datasets.md)
- [OrigDatablocks](authorization/authorization_origdatablocks.md)
- [Jobs](authorization/authorization_jobs.md)
- [Users](authorization/authorization_users.md)

___N.B.___: we know that many subsystems are still missing. We are working on reviewing the authorization model for each one of them and producing the relative documentation. We welcome any contribution.

