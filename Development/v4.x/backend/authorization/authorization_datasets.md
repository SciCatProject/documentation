# Datasets Authoorization
## CASL ability actions
This is the list of the permissions methods available for datasets and all their endpoints
### Endpoint authorization
- DatasetCreate
- DatasetRead
- DatasetUpdate
- DatasetDelete
- DatasetAttachmentCreate
- DatasetAttachmentRead
- DatasetAttachmentUpdate
- DatasetAttachmentDelete
- DatasetOrigdatablockCreate
- DatasetOrigdatablockRead
- DatasetOrigdatablockUpdate
- DatasetOrigdatablockDelete
- DatasetDatablockCreate
- DatasetDatablockRead
- DatasetDatablockUpdate
- DatasetDatablockDelete
- DatasetLogbookRead
### Instance authorization
- DatasetCreateOwnerNoPid
- DatasetCreateOwnerWithPid
- DatasetCreateAny
- DatasetReadPublic
- DatasetReadAccess
- DatasetReadOwner
- DatasetReadAny
- DatasetUpdateOwner
- DatasetUpdateAny
- DetasetDeleteOwner
- DatasetDeleteAny
- DatasetAttachmentCreateOwner
- DatasetAttachmentCreateAny
- DatasetAttachmentReadPublic
- DatasetAttachmentReadAccess
- DatasetAttachmentReadOwner
- DatasetAttachmentReadAny
- DatasetAtatchementUpdateOwner
- DatasetAtatchementUpdateAny
- DatasetAttachmentDeleteOwner
- DatasetAttachmentDeleteAny
- DatasetOrigdatablockCreateOwner
- DatasetOrigdatablockCreateAny
- DatasetOrigdatablockReadPublic
- DatasetOrigdatablockReadAccess
- DatasetOrigdatablockReadOwner
- DatasetOrigdatablockReadAny
- DatasetOrigdatablockUpdateOwner
- DatasetOrigdatablockUpdateAny
- DatasetOrigdatablockDeleteAny
- DatasetDatablockCreateOwner
- DatasetDatablockCreateAny
- DatasetDatablockReadPublic
- DatasetDatablockReadAccess
- DatasetDatablockReadOwner
- DatasetDatablockReadAny
- DatasetDatablockUpdateOwner
- DatasetDatablockUpdateAny
- DatasetDatablockDeleteOwner
- DatasetDatablockDeleteAny
- DatasetLogbookReadOwn
- DatasetLogbookReadAny

### Priority
```mermaid
graph TD;
    DatasetCreate_(E)_-->DatasetCreateOwnerNoPid_(I)_-->DatasetCreateOwnerWithPid(I)-->DatasetCreateAny(I);
    DatasetRead_(E)_-->DatasetReadPublic_(I)_-->DatasetReadAccess_(I)_-->DatasetReadOwner_(I)_-->DatasetReadAny_(I)_;
    DatasetUpdate_(E)_-->DatasetUpdateOwner_(I)_-->DatasetUpdateAny_(I)_;
    DatasetDelete_(E)_-->DatasetDeleteOwner_(I)_-->DatasetDelteAny_(I)_;
```

### Authorization table
| HTTP method | Endpoint | Endpoint Authorization | Anonymous | Authenticated User | Create Dataset Groups | Create Dataset with Pid Groups | Create Dataset Privileged Groups | Admin Groups | Delete Groups | Notes |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| POST | Datasets | _DatasetCreate_ | __no__ | __no__ | Owner, w/o PID<br/>_DatasetCreateOwnerNoPid_ | Owner, w/ PID<br/>_DatasetCreateOwnerWithPid_ | Any<br/>_DatasetCreateAny_ | Any<br/>_DatasetCreateAny_ | __no__ | 
| POST | Datasets/isValid | _DatasetCreate_ | __no__ | __no__ | Owner, w/o PID<br/>_DatasetCreateOwnerNoPid_ | Owner, W/ PID<br/>_DatasetCreateOwnerWithPid_ | Any<br/>_DatasetCreateAny_ | Any<br/>_DatasetCreateAny_ | __no__ | 
| GET | Datasets | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadyAny_ | __no__ | 
| GET | Datasets/fullquery | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadAny_ | __no__ | 
| GET | Datasets/fullfacet | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadAny_ | __no__ | 
| GET | Datasets/metadataKeys | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadAny_ | __no__ | 
| GET | Datasets/findOne | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadAny_ | __no__ | 
| GET | Datasets/count | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadAny_ | __no__ | 
| GET | Datasets/_pid_ | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadAny_ | __no__ | 
| PATCH | Datasets/_pid_ | _DatasetUpdate_ | __no__ | __no__ | Owner<br/>_DatasetUpdateOwner_ | Owner<br/>_DatasetUpdateOwner_ | Owner<br/>_DatasetUpdateOwner_ | Any<br/>_DatasetUpdateAny_ | __no__ | 
| PUT | Datasets/_pid_ |  _DatasetUpdate_ |__no__ | __no__ | Owner<br/>_DatasetUpdateOwner_ | Owner<br/>_DatasetUpdateOwner_ | Owner<br/>_DatasetUpdateOwner_ | Any<br/>_DatasetUpdateAny_ | __no__ | 
| POST | Datasets/_pid_/appendToArrayField |  _DatasetUpdate_ |__no__ | __no__ | Owner<br/>_DatasetUpdateOwner_ |  Owner<br/>_DatasetUpdateOwner_ | Owner<br/>_DatasetUpdateOwner_ | Any<br/>_DatasetUpdateAny_ | __no__ | 
| | | | | | | | | |
| DELETE | Datasets/_pid_ | _DatasetDelete_ | __no__ | __no__ | __no__ | __no__ | __no__ | __no__ | Any<br/>_DatasetDeleteAny_ | 
| | | | | | | | | |
| GET | Datasets/_pid_/thumbnail | _DatasetRead_ | Public<br/>_DatasetReadPublic_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Has Access<br/>_DatasetReadAccess_ | Any<br/>_DatasetReadAny_ | __no__ | 
| | | | | | | | | |
| POST | Datasets/_pid_/attachments | _DatasetAttachmentCreate_ | __no__ | __no__ | Owner<br/>_DatasetAttachmentCreateOwner_ | Owner<br/>_DatasetAttachmentCreateOwner_ | Any<br/>_DatasetAttachmentCreateAny_ | Any<br/>_DatasetAttachmentCreateAny_ | __no__ | 
| GET | Datasets/_pid_/attachments | _DatasetAttachmemntRead_ | Public<br/>_DatasetAttachmentReadPublic_ | Has Access<br/>_DatasetAttachmentReadAccess_ | Has Access<br/>_DatasetAttachmentReadAccess_ | Has Access<br/>_DatasetAttachmentReadAccess_ | Has Access<br/>_DatasetAttachmentReadAccess_ | Any<br/>_DatasetAttachmentReadAny_ | __no__ | 
| PUT | Datasets/_pid_/attachments/_aid_ | _DatasetAttachmemntUpdate_ | __no__ | __no__ | Owner<br/>_DatasetAttachmentUpdateOwner_ | Owner<br/>_DatasetAttachmentUpdateOwner_ | Owner<br/>_DatasetAttachmentUpdateOwner_ |  Any<br/>_DatasetAttachmentCreateAny_ | __no__ | 
| DELETE | Datasets/_pid_/attachments/_aid_ | _DatasetAttachmemntDelete_ | __no__ | __no__ | Owner<br/>_DatasetAttachmentDeleteOwner_ | Owner<br/>_DatasetAttachmentDeleteOwner_ | Owner<br/>_DatasetAttachmentDeleteOwner_ | Any<br/>_DatasetAttachmentDeleteAny_ | __no__ | 
| | | | | | | | | |
| POST | Datasets/_pid_/origdatablocks | _DatasetOrigdatablocksCreate_ | __no__ | __no__ | Owner<br/>_DatasetOrigdatablockCreateOwner_ | Owner<br/>_DatasetOrigdatablockCreateOwner_ | Any<br/>_DatasetOrigdatablockCreateAny_ | Any<br/>_DatasetOrigdatablockCreateAny_ | __no__ | 
| POST | Datasets/_pid_/origdatablocks/isValid | _DatasetOrigdatablocksCreate_ |  __no__ | __no__ | Owner<br/>_DatasetOrigdatablockCreateOwner_ | Owner<br/>_DatasetOrigdatablockCreateOwner_ | Any<br/>_DatasetOrigdatablockCreateAny_ | Any<br/>_DatasetOrigdatablockCreateAny_ | __no__ | 
| GET | Datasets/_pid_/origdatablocks | _DatasetOrigdatablocksRead_ | Public<br/>_DatasetOrigdatablockReadPublic_ | Has Access<br/>_DatasetOrigdatablockReadOAccess_ | Has Access<br/>_DatasetOrigdatablockReadAccess_ | Has Access<br/>_DatasetOrigdatablockReadAccess_ | Has Access<br/>_DatasetOrigdatablockReadAccess_ | Any<br/>_DatasetOrigdatablockReadAny_ | __no__ | 
| PATCH | Datasets/_pid_/origdatablocks/_oid_ | _DatasetOrigdatablocksUpdate_ | __no__ | __no__ | Owner<br/>_DatasetOrigdatablockUpdateOwner_ | Owner<br/>_DatasetOrigdatablockUpdateOwner_ | Owner<br/>_DatasetOrigdatablockUpdateOwner_ | Any<br/>_DatasetOrigdatablockCreateAny_ | __no__ | 
| DELETE | Datasets/_pid_/origdatablocks/_oid_ | _DatasetOrigdatablocksDelete_ | __no__ | __no__ | __no__ |  __no__ | __no__ |  __no__ | Any<br/>_DatasetOrigdatablockDeleteAny_ | 
| | | | | | | | | |
| POST | Datasets/_pid_/datablocks | _DatasetDatablocksCreate_ | __no__ | __no__ | Owner<br/>_DatasetDatablockCreateOwner_ | Owner<br/>_DatasetDatablockCreateOwner_ | Owner<br/>_DatasetDatablockCreateOwner_ | Any<br/>_DatasetDatablockCreateAny_ | __no__ | 
| GET | Datasets/_pid_/datablocks | _DatasetOrigdatablocksRead_ | Public<br/>_DatasetDatablockReadPublic_ | Has Access<br/>_DatasetDatablockReadAccess_ | Has Access<br/>_DatasetDatablockReadAccess_ | Has Access<br/>_DatasetDatablockReadAccess_ | Has Access<br/>_DatasetDatablockReadAccess_ | Any<br/>_DatasetDatablockReadAny_ | __no__ | 
| PATCH | Datasets/_pid_/datablocks/_oid_ | _DatasetDatablocksUpdate_ | __no__ | __no__ | Owner<br/>_DatasetDatablockUpdateOwner_ | Owner<br/>_DatasetDatablockUpdateOwner_ | Owner<br/>_DatasetDatablockUpdateOwner_ | Any<br/>_DatasetDatablockCreateAny_ | __no__ | 
| DELETE | Datasets/_pid_/datablocks/_oid_ | _DatasetDatablocksDelete_ | __no__ | __no__ | __no__ |  __no__ | __no__ | __no__ | Any<br/>_DatasetDatablockDeleteAny_ | 
| | | | | | | | | |
| GET | Datasets/_pid_/logbook | _DatasetLogbookRead_ | __no__ | Owner<br/>_DatasetLogbookReadOwner_ |  Owner<br/>_DatasetLogbookReadOwner_ | Owner<br/>_DatasetLogbookReadOwner_ |  Any<br/>_DatasetLogbookReadAny_ | __no__ | 

