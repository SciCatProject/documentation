# Proposals Authorization
## CASL ability actions
This is the list of the permissions methods available for Proposals and all their endpoints

### Endpoint Authorization
- ProposalsCreate
- ProposalsRead
- ProposalsUpdate
- ProposalsDelete

### (Data) Instance Authorization
- ProposalsCreateOwner
- ProposalsCreateAny
- ProposalsReadManyPublic
- ProposalsReadManyAccess
- ProposalsReadManyOwner
- ProposalsReadOnePublic
- ProposalsReadOneAccess
- ProposalsReadOneOwner
- ProposalsReadAny
- ProposalsUpdateOwner
- ProposalsUpdateAny
- ProposalsDeleteOwner
- ProposalsDeleteAny

#### Priority
```mermaid
graph LR;
    ProposalsCreate(E)-->ProposalsCreateOwner(I);
    ProposalsCreateOwner(I)-->ProposalsCreateAny(I)
    ProposalsRead(E)-->ProposalsReadManyPublic(I);
    ProposalsReadManyPublic(I)-->ProposalsReadManyAccess(I);
    ProposalsReadManyAccess(I)-->ProposalsReadManyOwner(I);
    ProposalsReadManyOwner(I)-->ProposalsReadAny(I);
    ProposalsRead(E)-->ProposalsReadOnePublic(I);
    ProposalsReadOnePublic(I)-->ProposalsReadOneAccess(I);
    ProposalsReadOneAccess(I)-->ProposalsReadOneOwner(I);
    ProposalsReadOneOwner(I)-->ProposalsReadAny(I);
    ProposalsUpdate(E)-->ProposalsUpdateOwner(I);
    ProposalsUpdateOwner(I)-->ProposalsUpdateAny(I);
    ProposalsDelete(E)-->ProposalsDeleteOwner(I);
    ProposalsDeleteOwner(I)-->ProposalsDeleteAny(I);
```

#### Authorization table
| HTTP method | Endpoint | Endpoint Authentication | Anonymous | Authenticated User | Proposals Groups | Admin Groups | Delete Groups | Notes |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | 
| POST | Proposals | _ProposalsCreate_ | __no__ | __no__ | Any<br>_ProposalsCreateAny_ | Any<br>_ProposalsCreateAny_ | __no__ |  |
| GET | Proposals | _ProposalsRead_ | Public<br/>_ProposalsReadManyPublic_ | Has  Access<br/>_ProposalsReadManyAccess_ | Has Access<br/>_ProposalsReadManyAccess_ | Any<br/>_ProposalsReadAny_ |  __no__  |  |
| GET | Proposals/_pid_ | _ProposalsRead_ | Public<br/>_ProposalsReadOnePublic_ | Has Access<br/>_ProposalsReadOneAccess_ | Has Access<br/>_ProposalsReadOneAccess_ | Any<br/>_ProposalsReadAny_ |  __no__  |  |
| GET | Proposals/fullquery | _ProposalsRead_ | Public<br/>_ProposalsReadOnePublic_ | Has Access<br/>_ProposalsReadOneAccess_ | Has Access<br/>_ProposalsReadOneAccess_ | Any<br/>_ProposalsReadAny_ |  __no__  |  |
| POST | Proposals/_pid_ | _ProposalsUpdate_ | __no__ | __no__ | Owner<br/>_ProposalsUpdateOwn_ | Any<br/>_ProposalsUpdateAny_ | __no__ | |
| DELETE | Proposals/_pid_ | _ProposalsDelete_ | __no__ | __no__ | __no__ | Any<br/>_ProposalsDeleteAny_ | __no__ |  |

