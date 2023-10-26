# OrigDatablock Authorization
## CASL ability actions
This is the list of the permissions methods available for origdatablock and all their endpoints
### Endpoint Authorization
- OrigdatablockCreate
- OrigdatablockRead
- OrigdatablockUpdate
- OrigdatablockDelete

### (Data) Instance Authorization
- OrigdatablockCreateOwner
- OrigdatablockCreateAny
- OrigdatablockReadPublic
- OrigdatablockReadAccess
- OrigdatablockReadOwner
- OrigdatablockReadAny
- OrigdatablockUpdateOwner
- OrigdatablockUpdateAny
- OrigdatablockDeleteAny

#### Priority
```mermaid
%%{init: {'theme' : 'base', 'themeVariables': { 'fontSize': '11px', 'fontFamily' : 'monospace'}}}%%
graph LR;
    DatasetOrigdatablockCreate-->DatasetOrigdatablockCreateOwner;
    DatasetOrigdatablockCreateOwner-->DatasetOrigdatablockCreateAny;
    DatasetOrigdatablockRead-->DatasetOrigdatablockReadPublic;
    DatasetOrigdatablockReadPublic-->DatasetOrigdatablockReadAccess;
    DatasetOrigdatablockReadAccess-->DatasetOrigdatablockReadAny;
    DatasetOrigdatablockUpdate-->DatasetOrigdatablockUpdateOwner;
    DatasetOrigdatablockUpdateOwner-->DatasetOrigdatablockUpdateAny;
    DatasetOrigdatablockDelete-->DatasetOrigdatablockDeleteOwner;
    DatasetOrigdatablockDeleteOwner-->DatasetOrigdatablockDelteAny;
```

#### Authorization table
| HTTP method | Endpoint | Endpoint Authentication | Anonymous | Authenticated User | Create Dataset Groups | Create Dataset with Pid Groups | Create Dataset Privileged Groups | Admin Groups | Delete Groups | Notes |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| POST | origdatablocks | _OrigdatablockCreate_ | __no__ | __no__ | Owner<br>_OrigdatablockCreateOwn_ | Owner<br>_OrigidatablockCreateOwn_ | Any<br>_OrigdatablockCreateAny_ | Any _OrigdatablockCreateAny_ | __no__ |  
| POST | origdatablocks/isValid | _OrigdatablockCreate_ | __no__ | __no__ | Owner<br>_OrigdatablockCreateOwn_ | Owner<br>_OrigdatablockCreateOwn_ | Any<br>_OrigdatablockCreateAny_ | Any<br>_OrigdatablockCreateAny_ | __no__ | 
| GET | origdatablocks | _OrigdatablockRead_ | Public _OrigdatablockReadPublic_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Any<br>_OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/_oid_ | _OrigdatablockRead_ | Public<br>_OrigdatablockReadPublic_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Any<br>_OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/fullquery | _OrigdatablockRead_ | Public<br>_OrigdatablockReadPublic_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Any<br>_OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/fullquery/files | _OrigdatablockRead_ | Public<br>_OrigdatablockReadPublic_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Any<br>_OrigdatablockReadAny_ | __no__ | 
| GET | origdatablocks/fullfacet | _OrigdatablockRead_ | Public<br>_OrigdatablockReadPublic_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Has Access<br>_OrigdatablockReadAccess_ | Any<br>_OrigdatablockReadAny_ | __no__ | 
| PATCH | origdatablocks/_oid_ | _OrigdatablockUpdate_ | __no__ | __no__ | Owner<br>_OrigdatablockUpdateOwner_ | Owner<br>_OrigdatablockUpdateOwner_ | Owner<br>_OrigdatablockUpdateOwner_ | Any<br>_OrigdatablockUpdateAny_ | __no__ | 
| DELETE | origdatablocks/_oid_ | _OrigdatablockDelete_ | __no__ | __no__ | __no__ |  __no__ | __no__ |  __no__ | Any<br>_OrigdatablockDeleteAny_ | 

