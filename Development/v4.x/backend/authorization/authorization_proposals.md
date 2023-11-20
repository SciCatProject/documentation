# Proposals Authorization
## CASL ability actions
This is the list of the permissions methods available for Proposals and all their endpoints

### Endpoint Authorization
- ProposalCreate
- ProposalRead
- ProposalUpdate
- ProposalDelete
- ProposalAttachmentCreate
- ProposalAttachmentRead
- ProposalAttachmentUpdate
- ProposalAttachmentDelete
- ProposalDatasetRead


### (Data) Instance Authorization
- ProposalCreateOwner
- ProposalCreateAny
- ProposalReadManyPublic
- ProposalReadManyAccess
- ProposalReadManyOwner
- ProposalReadOnePublic
- ProposalReadOneAccess
- ProposalReadOneOwner
- ProposalReadAny
- ProposalUpdateOwner
- ProposalUpdateAny
- ProposalDeleteOwner
- ProposalDeleteAny
- ProposalAttachmentCreateOnwer
- ProposalAttachmentCreateAny
- ProposalAttachmentReadManyPublic
- ProposalAttachmentReadManyAccess
- ProposalAttachmentReadManyOwner
- ProposalAttachmentReadManyAny
- ProposalAttachmentUpdateOwner
- ProposalAttachmentUpdateAny
- ProposalAttachmentDeleteOwner
- ProposalAttachmentDeleteAny
- ProposalDatasetReadPublic
- ProposalDatasetReadAccess
- ProposalDatasetReadOwner
- ProposalDatasetReadAny


#### Priority
```mermaid
graph LR;
    ProposalCreate-->ProposalsCreateOwner;
    ProposalCreateOwner-->ProposalCreateAny;
    ProposalRead-->ProposalReadManyPublic;
    ProposalReadManyPublic-->ProposalReadManyAccess;
    ProposalReadManyAccess-->ProposalReadManyOwner;
    ProposalReadManyOwner-->ProposalReadAny;
    ProposalRead-->ProposalReadOnePublic;
    ProposalReadOnePublic-->ProposalReadOneAccess;
    ProposalReadOneAccess-->ProposalReadOneOwner;
    ProposalReadOneOwner-->ProposalReadAny;
    ProposalUpdate-->ProposalUpdateOwner;
    ProposalUpdateOwner-->ProposalUpdateAny;
    ProposalDelete-->ProposalDeleteOwner;
    ProposalDeleteOwner-->ProposalDeleteAny;
    ProposalAttachmentCreate-->ProposalAttachmentCreateOnwer;
    ProposalAttachmentCreateOnwer-->ProposalAttachmentCreateAny;
    ProposalAttachmentRead-->ProposalAttachmentReadManyPublic;
    ProposalAttachmentReadManyPublic-->ProposalAttachmentReadManyAccess;
    ProposalAttachmentReadManyAccess-->ProposalAttachmentReadManyOwner;
    ProposalAttachmentReadManyOwner-->ProposalAttachmentReadManyAny;
    ProposalAttachmentUpdate-->ProposalAttachmentUpdateOwner;
    ProposalAttachmentUpdateOwner-->ProposalAttachmentUpdateAny;
    ProposalAttachmentDelete-->ProposalAttachmentDeleteOwner;
    ProposalAttachmentDeleteOwner-->ProposalAttachmentDeleteAny;
    ProposalDatasetRead-->ProposalDatasetReadPublic;
    ProposalDatasetReadPublic-->ProposalDatasetReadAccess;
    ProposalDatasetReadAccess-->ProposalDatasetReadOwner;
    ProposalDatasetReadOwner-->ProposalDatasetReadAny;
```

#### Authorization table
| HTTP method | Endpoint | Endpoint Authentication | Anonymous | Authenticated User | Proposals Groups | Admin Groups | Delete Groups | Notes |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | 
| POST | Proposals | _ProposalCreate_ | __no__ | __no__ | Any<br>_ProposalCreateAny_ | Any<br>_ProposalCreateAny_ | __no__ |  |
| GET | Proposals | _ProposalRead_ | Public<br/>_ProposalReadManyPublic_ | Has Access<br/>_ProposalReadManyAccess_ | Has Access<br/>_ProposalReadManyAccess_ | Any<br/>_ProposalReadAny_ |  __no__  |  |
| GET | Proposals/fullquery | _ProposalRead_ | Public<br/>_ProposalReadManyPublic_ | Has Access<br/>_ProposalReadManyAccess_ | Has Access<br/>_ProposalReadManyAccess_ | Any<br/>_ProposalReadAny_ |  __no__  |  |
| GET | Proposals/fullfacet | _ProposalRead_ | Public<br/>_ProposalReadManyPublic_ | Has Access<br/>_ProposalReadManyAccess_ | Has Access<br/>_ProposalReadManyAccess_ | Any<br/>_ProposalReadAny_ |  __no__  |  |
| GET | Proposals/_pid_ | _ProposalRead_ | Public<br/>_ProposalReadOnePublic_ | Has Access<br/>_ProposalReadOneAccess_ | Has Access<br/>_ProposalReadOneAccess_ | Any<br/>_ProposalReadAny_ |  __no__  |  |
| GET | Proposals/fullquery | _ProposalRead_ | Public<br/>_ProposalReadOnePublic_ | Has Access<br/>_ProposalReadOneAccess_ | Has Access<br/>_ProposalReadOneAccess_ | Any<br/>_ProposalReadAny_ |  __no__  |  |
| PATCH | Proposals/_pid_ | _ProposalUpdate_ | __no__ | __no__ | Owner<br/>_ProposalUpdateOwn_ | Any<br/>_ProposalUpdateAny_ | __no__ | |
| DELETE | Proposals/_pid_ | _ProposalDelete_ | __no__ | __no__ | __no__ | __no__ | Any<br/>_ProposalDeleteAny_ |  |
|||||
| POST | Proposals/_pid_/attachements | _ProposalAttachementCreate_ | __no__ | __no__ | Any<br>_ProposalAttachmentCreateAny_ | Any<br>_ProposalAttachmentCreateAny_ | __no__ |  |
| GET | Proposals/_pid_/attachements | _ProposalAttachmentRead_ | Public<br/>_ProposalAttachmentReadManyPublic_ | Has Access<br/>_ProposalAttachmentReadManyAccess_ | Has Access<br/>_ProposalAttachmentReadManyAccess_ | Any<br/>_ProposalAttachmentReadManyAny_ | __no__ | |
| PATCH | Proposals/_pid_/attachments/_aid_ | _ProposalAttachmentUpdate_ | __no__ | __no__ | Owner<br/>_ProposalAttachmentUpdateOwner_ | Any<br/>_ProposalAttachmentUpdateAny_ | __no__ | |
| DELETE | Proposals/_pid_/attachment/_aid_ | _ProposalAttachmentDelete_ | __no__ | __no__ | Onwer<br/>_ProposalAttachmentDeleteOwner_ | Any<br/>_ProposalAttachmentDeleteAny_ | __no__ | |
|||||
| GET | Proposals/_pid_/datasets | _ProposalDatasetRead_ | Public<br/>_ProposalDatasetReadOnePublic_ | Has Access<br/>_ProposalDatasetReadOneAccess_ | Has Access<br/>_ProposalDatasetReadOneAccess_ | Any<br/>_ProposalDatasetReadOneAny_ | __no__ | |
