# Samples Authorization
## CASL ability actions
This is the list of the permissions methods available for Samples and all their endpoints

### Endpoint Authorization
- SampleCreate
- SampleRead
- SampleUpdate
- SampleDelete
- SampleAttachmentCreate
- SampleAttachmentRead
- SampleAttachmentUpdate
- SampleAttachmentDelete
- SampleDatasetRead

### (Data) Instance Authorization
- SampleCreateOwner
- SampleCreateAny
- SampleReadManyPublic
- SampleReadManyAccess
- SampleReadManyOwner
- SampleReadOnePublic
- SampleReadOneAccess
- SampleReadOneOwner
- SampleReadAny
- SampleUpdateOwner
- SampleUpdateAny
- SampleDeleteOwner
- SampleDeleteAny
- SampleAttachmentCreateOwner
- SampleAttachmentCreateAny
- SampleAttachmentReadManyPublic
- SampleAttachmentReadManyAccess
- SampleAttachmentReadManyOwner
- SampleAttachmentReadManyAny
- SampleAttachmentUpdateOwner
- SampleAttachmentUpdateAny
- SampleAttachmentDeleteOwner
- SampleAttachmentDeleteAny
- SampleDatasetReadPublic
- SampleDatasetReadAccess
- SampleDatasetReadOwner
- SampleDatasetReadAny

#### Priority
```mermaid
graph LR;
    SampleCreate-->SampleCreateOwner;
    SampleCreateOwner-->SampleCreateAny;
    SampleRead-->SampleReadManyPublic;
    SampleReadManyPublic-->SampleReadManyAccess;
    SampleReadManyAccess-->SampleReadManyOwner;
    SampleReadManyOwner-->SampleReadAny;
    SampleRead-->SampleReadOnePublic;
    SampleReadOnePublic-->SampleReadOneAccess;
    SampleReadOneAccess-->SampleReadOneOwner;
    SampleReadOneOwner-->SampleReadAny;
    SampleUpdate-->SampleUpdateOwner;
    SampleUpdateOwner-->SampleUpdateAny;
    SampleDelete-->SampleDeleteOwner;
    SampleDeleteOwner-->SampleDeleteAny;
    SampleAttachmentCreate-->SampleAttachmentCreateOwner;
    SampleAttachmentCreateOwner-->SampleAttachmentCreateAny;
    SampleAttachmentRead-->SampleAttachmentReadManyPublic;
    SampleAttachmentReadManyPublic-->SampleAttachmentReadManyAccess;
    SampleAttachmentReadManyAccess-->SampleAttachmentReadManyOwner;
    SampleAttachmentReadManyOwner-->SampleAttachmentReadManyAny;
    SampleAttachmentUpdate-->SampleAttachmentUpdateOwner;
    SampleAttachmentUpdateOwner-->SampleAttachmentUpdateAny;
    SampleAttachmentDelete-->SampleAttachmentDeleteOwner;
    SampleAttachmentDeleteOwner-->SampleAttachmentDeleteAny;
    SampleDatasetRead-->SampleDatasetReadPublic;
    SampleDatasetReadPublic-->SampleDatasetReadAccess;
    SampleDatasetReadAccess-->SampleDatasetReadOwner;
    SampleDatasetReadOwner-->SampleDatasetReadAny;
```

#### Authorization table
| HTTP method | Endpoint | Endpoint Authentication | Anonymous | Authenticated User | Sample Groups | Sample Privileged Groups | Admin Groups | Delete Groups | Notes |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| POST | Samples | _SampleCreate_ | __no__ | __no__ | Owner<br>_SampleCreateOwner_ | Any<br>_SampleCreateAny_ | Any<br>_SampleCreateAny_ | __no__ |  |
| GET | Samples | _SampleRead_ | Public<br/>_SampleReadManyPublic_ | Has Access<br/>_SampleReadManyAccess_ | Has Access<br/>_SampleReadManyAccess_ | Has Access<br/>_SampleReadManyAccess_ | Any<br/>_SampleReadAny_ |  __no__  |  |
| GET | Samples/fullquery | _SampleRead_ | Public<br/>_SampleReadManyPublic_ | Has Access<br/>_SampleReadManyAccess_ | Has Access<br/>_SampleReadManyAccess_ | Has Access<br/>_SampleReadManyAccess_ | Any<br/>_SampleReadAny_ |  __no__  |  |
| GET | Samples/fullfacet | _SampleRead_ | Public<br/>_SampleReadManyPublic_ | Has Access<br/>_SampleReadManyAccess_ | Has Access<br/>_SampleReadManyAccess_ | Has Access<br/>_SampleReadManyAccess_ | Any<br/>_SampleReadAny_ |  __no__  |  |
| GET | Samples/_pid_ | _SampleRead_ | Public<br/>_SampleReadOnePublic_ | Has Access<br/>_SampleReadOneAccess_ | Has Access<br/>_SampleReadOneAccess_ | Has Access<br/>_SampleReadOneAccess_ | Any<br/>_SampleReadAny_ |  __no__  |  |
| GET | Samples/fullquery | _SampleRead_ | Public<br/>_SampleReadOnePublic_ | Has Access<br/>_SampleReadOneAccess_ | Has Access<br/>_SampleReadOneAccess_ | Has Access<br/>_SampleReadOneAccess_ | Any<br/>_SampleReadAny_ |  __no__  |  |
| PATCH | Samples/_pid_ | _SampleUpdate_ | __no__ | __no__ | Owner<br/>_SampleUpdateOwn_ | Owner<br/>_SampleUpdateOwn_ | Any<br/>_SampleUpdateAny_ | __no__ | |
| DELETE | Samples/_pid_ | _SampleDelete_ | __no__ | __no__ | __no__ | __no__ | __no__ | Any<br/>_SampleDeleteAny_ |  |
|||||
| POST | Samples/_pid_/Attachments | _SampleAttachmentCreate_ | __no__ | __no__ | Owner<br>_SampleAttachmentCreateOwner_ | Any<br>_SampleAttachmentCreateAny_ | Any<br>_SampleAttachmentCreateAny_ | __no__ |  |
| GET | Samples/_pid_/Attachments | _SampleAttachmentRead_ | Public<br/>_SampleAttachmentReadManyPublic_ | Has Access<br/>_SampleAttachmentReadManyAccess_ | Has Access<br/>_SampleAttachmentReadManyAccess_ | Has Access<br/>_SampleAttachmentReadManyAccess_ | Any<br/>_SampleAttachmentReadManyAny_ | __no__ | |
| DELETE | Samples/_pid_/attachment/_aid_ | _SampleAttachmentDelete_ | __no__ | __no__ | Owner<br/>_SampleAttachmentDeleteOwner_ | Owner<br/>_SampleAttachmentDeleteOwner_ | Any<br/>_SampleAttachmentDeleteAny_ | Any<br/>_SampleAttachmentDeleteAny_ | |
|||||
| GET | Samples/_pid_/datasets | _SampleDatasetRead_ | Public<br/>_SampleDatasetReadOnePublic_ | Has Access<br/>_SampleDatasetReadOneAccess_ | Has Access<br/>_SampleDatasetReadOneAccess_ | Has Access<br/>_SampleDatasetReadOneAccess_ | Any<br/>_SampleDatasetReadOneAny_ | __no__ | |
