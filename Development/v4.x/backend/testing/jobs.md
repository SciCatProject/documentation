# 1100-1180: Jobs

Jobs test that the functionalities for creating, updating, deleting and retrieving jobs are working correctly.

Tests are built around assuming the following owner, access and public information:

| Groups | Dataset 1 | Dataset 2 | Dataset 3 |
| --- | --- | --- | --- |
| admin | Admin | Admin | Admin |
| adminingestor | Admin | Admin | Admin |
| archivemanager | | | Access | 
| datasetingestor | | | |
| proposalingestor | | | | 
| sampleingestor | | | |
| group1 | Owner | | Access |
| group2 | | Owner | |
| group3 | | | |
| group4 | | | |
| group5 | Access | | Owner | 

Users are contained in file `functionalAccount.json.test` and are the following:

| User | Group | Permission Group |
| --- | --- | --- |
| admin | admin | Admin Groups, Delete Job Groups |
| adminIngestor | adminingestor | Admin Groups |
| archiveManager | archivemanager | Delete Groups, Delete Job Groups |
| datasetIngestor | datasetingestor | Create Dataset Privileged Groups |
| proposalIngestor | proposalingestor | Proposal Groups |
| sampleIngestor | sampleingestor | Sample Privileged Groups |
| user1 | group1 | Create Job Groups, Update Job Groups, Create Dataset Groups, Sample Groups |
| user2 | group2 | Create Job Groups, Create Dataset Groups, Create Dataset with Pid Groups |
| user3 | group3 | Create Dataset Groups, Create Dataset Privileged Groups |
| user4 | group4 | _none_ |
| user5.1 | group5 | _none_ |
| user5.2 | group5 | _none_ |

## Tests List
File `Jobs.js` performs tests with job configurations mimicking a real configuration, such as "archive/retrieve/public". Test suite 1115 additionally tests if entered job parameters are valid.
Other jobs test files are separated into distinct ones based on the authorization value for "_create_" entry in the job configuration file and test if specific user is authorized to do the CRUD operations. Not all files test PATCH and DELETE methods, as these would be redundant. 
### 1110: Jobs: Test New Job Model: possible real configurations

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new public job as a normal user himself/herself with a published dataset | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new public job as a normal user himself/herself with unpublished datasets, which should fail | POST | /api/v3/Jobs | user5.1 | 409 | ```ConflictStatusCode``` |
| 0060 | Add a new archive job as a normal user himself/herself with an archivable dataset | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new retrieve job as a normal user himself/herself with a non retrievable dataset, which should fail | POST | /api/v3/Jobs | user5.1 | 409 | ```ConflictStatusCode``` |
| 0080 | Add a new public job as a normal user himself/herself with unknown files, which should fail | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0090 | Add a new public job as a normal user himself/herself choosing only specific files | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |


### 1115: Validate Job Action

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Create validate job fails without required parameters | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0020 | Create validate job fails with the wrong types | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0030 | Create validate job fails with the wrong types | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0040 | Create validate job fails with the wrong types | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0050 | Create validate succeeds with the right types | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Update validate fails without the required parameters | PATCH | /api/v3/Jobs/${encodedJobIdValidate1} | admin | 400 | ```BadRequestStatusCode``` |
| 0070 | Update validate fails with incorrect types | PATCH | /api/v3/Jobs/${encodedJobIdValidate1} | admin | 400 | ```BadRequestStatusCode``` |
| 0080 | Updating validate succeeds with the required parameters | PATCH | /api/v3/Jobs/${encodedJobIdValidate1} | admin | 200 | ```SuccessfulPatchStatusCode``` |


### 1120: Jobs: Test New Job Model Authorization for #all jobs

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with no datasets in job parameters, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with not existing dataset IDs, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with no jobParams parameter, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with empty jobParams parameter | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for another user in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from ADMIN_GROUPS for undefined user from another group user in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0115 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#all' configuration without contactEmail, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0120 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#all' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a user from CREATE_JOB_GROUPS for his/her group in '#all' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0140 | Add a new job as a user from CREATE_JOB_GROUPS for another user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0150 | Add a new job as a user from CREATE_JOB_GROUPS for another group in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0160 | Add a new job as a user from CREATE_JOB_GROUPS for anonymous user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0170 | Add a new job as a normal user for himself/herself in '#all' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0180 | Add a new job as a normal user for his/her group in '#all' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0190 | Add a new job as a normal user for another user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0200 | Add a new job as a normal user for another group in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0210 | Add a new job as a normal user for anonymous user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0220 | Add a new job as unauthenticated user in '#all' configuration | POST | /api/v3/Jobs | unauthenticated | 201 | ```EntryCreatedStatusCode``` |
| 0230 | Add a new job as unauthenticated user for another user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | unauthenticated | 400 | ```BadRequestStatusCode``` |
| 0240 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0250 | Add a Status update to a job as a user from ADMIN_GROUPS for another user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0260 | Add a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0280 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByUser1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0290 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByUser51} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0300 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByGroup1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0310 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByGroup5} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0320 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByAnonym} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0330 | Add a Status update to a job as a normal user  for his/her job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0340 | Add a Status update to a job as a normal user for another user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByUser1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0350 | Add a Status update to a job as a normal user for his/her group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0360 | Add a Status update to a job as a normal user for another user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByGroup1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0370 | Add a Status update to a job as a normal user for anonymous user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByAnonym} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0380 | Add a Status update to a job as unauthenticated user for anonymous job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByAnonym} | unauthenticated | 200 | ```SuccessfulPatchStatusCode``` |
| 0390 | Add a Status update to a job as unauthenticated user for another group's job in '#all' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByGroup1} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0400 | Adds a Status update to a job as unauthenticated user for another user's job in '#all' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedAllJobOwnedByUser1} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0410 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '#all' configuration with non-existing jobId, which should fail as bad request | PATCH | /api/v3/Jobs/${badJobId} | admin | 400 | ```BadRequestStatusCode``` |
| 0420 | Access jobs as a user from ADMIN_GROUPS | GET | /api/v3/Jobs | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0430 | Access jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0440 | Access jobs as a user from ADMIN_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0450 | Access jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v3/Jobs?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0460 | Access jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0470 | Access jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v3/Jobs?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0480 | Access jobs as a user from CREATE_JOB_GROUPS | GET | /api/v3/Jobs | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0490 | Access jobs as a user from CREATE_JOB_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0500 | Access jobs as a user from CREATE_JOB_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0510 | Access jobs as a normal user | GET | /api/v3/Jobs | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0520 | Access jobs as a normal user (user5.1) that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0530 | Access jobs as another normal user (user5.2) | GET | /api/v3/Jobs | user5.2 | 200 | ```SuccessfulGetStatusCode``` |
| 0540 | Access jobs as unauthenticated user, which should be forbidden | GET | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0550 | Get admin's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAdmin} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0560 | Get user1's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser1} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0570 | Get group1's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup1} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0580 | Get admin's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0590 | Get admin's job as user from CREATE_JOB_GROUP, which should be forbidden | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAdmin} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0600 | Get his/her own job as user from CREATE_JOB_GROUP | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser1} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0610 | Get a job from his/her own group as user from CREATE_JOB_GROUP | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup1} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0620 | Get other user's job as user from CREATE_JOB_GROUP, which should be forbidden | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser51} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0630 | Get anonymous user's job as user from CREATE_JOB_GROUP, which should be forbidden | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0640 | Get admin's job as normal, which should be forbidden | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAdmin} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0650 | Get other user's job as normal user, which should be forbidden | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0660 | Get his/her own job as normal user | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0670 | Get anonymous user's job as normal user, which should be forbidden | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0680 | Get anonymous user's job as anonymous user, which should be forbidden | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0690 | Delete job created by admin as Archive Manager | DELETE | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAdmin} | archiveManager | 200 | ```SuccessfulDeleteStatusCode``` |
| 0700 | Delete job created by admin as Admin | DELETE | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser1} | admin | 200 | ```SuccessfulDeleteStatusCode``` |
| 0710 | Delete job created by admin as CREATE_JOB_GROUPS user, which should fail | DELETE | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup1} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0720 | Delete job created by admin as normal user, which should fail | DELETE | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0730 | Delete job not existing in database as Archive Manager, which should fail | DELETE | /api/v3/Jobs/${fakeJobId} | archiveManager | 400 | ```BadRequestStatusCode``` |
| 0740 | Access jobs as a user from ADMIN_GROUPS, which should be one less than before proving that delete works | GET | /api/v3/Jobs | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0750 | Fullquery jobs as a user from ADMIN_GROUPS, limited by 5 | GET | /api/v3/Jobs?limit=5 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0760 | Fullquery jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0770 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0780 | Fullquery jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v3/Jobs?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0790 | Fullquery jobs as a user from CREATE_JOB_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0800 | Fullquery jobs as a user from CREATE_JOB_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0810 | Fullquery jobs as a normal user | GET | /api/v3/Jobs | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0820 | Fullquery jobs as a normal user (user5.1) that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0830 | Fullquery jobs as unauthenticated user, which should be forbidden | GET | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0840 | Fullfacet jobs as unauthenticated user, which should be forbidden | GET | /api/v3/Jobs/facet | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0850 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v3/Jobs/facet?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0860 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User1 | GET | /api/v3/Jobs/facet?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0870 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v3/Jobs/facet?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0880 | Fullfacet jobs as a user from CREATE_JOB_GROUPS that were created by admin | GET | /api/v3/Jobs/facet?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0890 | Fullfacet jobs as a user from CREATE_JOB_GROUPS that were created by User1 | GET | /api/v3/Jobs/facet?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0900 | Fullfacet jobs as a normal user | GET | /api/v3/Jobs/facet | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0910 | Fullfacet jobs as a normal user (user5.1) that were created by admin | GET | /api/v3/Jobs/facet?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |


### 1130: Jobs: Test New Job Model Authorization for #all jobs


| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#authenticated' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a normal user for himself/herself in '#authenticated' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as unauthenticated user in '#authenticated' configuration, which should fail as forbidden | POST | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |


### 1140: Jobs: Test New Job Model Authorization for #dataset_access jobs configuration

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetAccess' configuration with access to datasets | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetAccess' configuration with no access to datasets | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as user1 for user5.1 ownerUser and group5 ownerGroup for #datasetAccess, which should fail | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0120 | Add a new job as a normal user for himself/herself in '#datasetAccess' configuration with access to datasets | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a normal user for himself/herself in '#datasetAccess' configuration with no access to datasets, which should fail as forbidden | POST | /api/v3/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0140 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0150 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0160 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0170 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0180 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByUser1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0190 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByUser51} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0200 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByGroup1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0210 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByGroup5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0220 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByAnonym} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0230 | Adds a Status update to a job as a normal user  for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0240 | Adds a Status update to a job as a normal user for another user's job in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByUser1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0250 | Adds a Status update to a job as a normal user for his/her group in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0260 | Adds a Status update to a job as a normal user for another user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByGroup1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0270 | Adds a Status update to a job as a normal user for anonymous user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByAnonym} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0280 | Adds a Status update to a job as unauthenticated user for anonymous user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByAnonym} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |


### 1150: Jobs: Test New Job Model Authorization for #dataset_owner jobs configuration

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetOwner' configuration with datasets owned by his/her group | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetOwner' configuration with datasets owned by his/her group | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0120 | Add a new job as a normal user for himself/herself in '#datasetOwner' configuration with datasets owned by his/her group | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a normal user for himself/herself in '#datasetOwner' configuration with datasets not owned by his/her group, which should fail as forbidden | POST | /api/v3/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0140 | Add a new job as a user from ADMIN_GROUPS for group2 and user1 in '#datasetOwner' configuration | POST | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByAdmin} | admin | 200 | ```SuccessfulPostStatusCode``` |
| 0150 | Add a new job as a user from ADMIN_GROUPS for group1 and user2 in '#datasetOwner' configuration | POST | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByUser1} | admin | 200 | ```SuccessfulPostStatusCode``` |
| 0160 | Add a new job as a user from ADMIN_GROUPS for group1 and user3 in '#datasetOwner' configuration | POST | /api/v3/Jobs/${encodedDatasetOwnerJobOwnedByGroup1} | admin | 200 | ```SuccessfulPostStatusCode``` |
| 0170 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0180 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0190 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0200 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0210 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0220 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser51} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0230 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0240 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0250 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0260 | Adds a Status update to a job as a normal user  for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Adds a Status update to a job as a normal user for another user's job in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByUser1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0280 | Adds a Status update to a job as a normal user for his/her group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup5} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0290 | Adds a Status update to a job as a normal user for another user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0300 | Adds a Status update to a job as a normal user for anonymous user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0310 | Adds a Status update to a job as unauthenticated user for anonymous user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByAnonym} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0320 | Access jobs as a User1 | GET | /api/v3/Jobs/ | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0330 | Access jobs as a User1 | GET | /api/v3/Jobs/ | user2 | 200 | ```SuccessfulGetStatusCode``` |
| 0340 | Access jobs as a User1 | GET | /api/v3/Jobs/ | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0350 | Access jobs as a User5.1 | GET | /api/v3/Jobs/ | user51 | 200 | ```SuccessfulGetStatusCode``` |

### 1160: Jobs: Test New Job Model Authorization for #dataset_public jobs configuration

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with all published datasets | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetPublic' configuration with all published datasets | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a normal user himself/herself in '#datasetPublic' configuration with a published dataset | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0120 | Add a new job as a normal user himself/herself in '#datasetPublic' configuration with unpublished datasets, which should fail as forbidden | POST | /api/v3/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0130 | Add a new job as anonymous user in '#datasetPublic' configuration with all published datasets | POST | /api/v3/Jobs | unauthenticated | 201 | ```EntryCreatedStatusCode``` |
| 0140 | Add a new job as anonymous user in '#datasetPublic' configuration with one unpublished dataset, which should fail as forbidden | POST | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |


### 1170: Jobs: Test New Job Model Authorization for configuration set to a specific group: @group5

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for another user in '@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_GROUPS for another group in '#@group5' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_GROUPS for user 5.1 in '#@group5' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0120 | Add a new job as a user 5.1 for himself/herself in '#@group5' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a user 5.1 for another user in his/her group in '#@group5' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0140 | Add a new job as a user 5.2 for himself/herself in '#@group5' configuration | POST | /api/v3/Jobs | user5.2 | 201 | ```EntryCreatedStatusCode``` |
| 0150 | Add a new job as user3 for himself/herself in #@group5 configuration, which should fail as forbidden | POST | /api/v3/Jobs | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0160 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0170 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0180 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0190 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0200 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0210 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser51} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0220 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByGroup1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0230 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByGroup5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0240 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByAnonym} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0250 | Adds a Status update to a job as user5.1 for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0260 | Adds a Status update to a job as user5.1 for another user's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Adds a Status update to a job as user5.1 for his/her group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0280 | Adds a Status update to a job as user5.1 for another user's group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0290 | Adds a Status update to a job as user5.1 for anonymous user's group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByAnonym} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0300 | Adds a Status update to a job as user5.2 for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser52} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 0310 | Adds a Status update to a job as user5.2 for user's 5.1 in same group job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser51} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 0320 | Adds a Status update to a job as user5.2 for another user in his/her group job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByGroup5} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 0330 | Adds a Status update to a job as user3 for his/her job in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser3} | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0340 | Adds a Status update to a job as user3 for user's 5.1 job in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedGroupSpecJobOwnedByUser51} | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0350 | Access jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0360 | Get job of another user in his/her group as normal user | GET | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser52} | user5.1 | 403 | ```SuccessfulGetStatusCode``` |
| 0370 | Get job from his/her own group as normal user | GET | /api/v3/Jobs/${encodedDatasetAccessJobOwnedByGroup5} | user5.1 | 403 | ```SuccessfulGetStatusCode``` |
| 0380 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0390 | Fullquery jobs as another normal user (user5.2) | GET | /api/v3/Jobs | user5.2 | 200 | ```SuccessfulGetStatusCode``` |
| 0400 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v3/Jobs/facet?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0410 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs/facet?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0420 | Fullfacet jobs as another normal user (user5.2) | GET | /api/v3/Jobs/facet | user5.2 | 200 | ```SuccessfulGetStatusCode``` |


### 1180: Jobs: Test New Job Model Authorization for configuration set to a specific user: USER5.1

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for another user in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself user in '#USER5.1' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_GROUPS for user5.1 in '#USER5.1' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0120 | Add a new job as user5.1 himself/herself in '#USER5.1' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as user5.1 for no ownerUser and group5 ownerGroup in #USER5.1 configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0140 | Add a new job as user5.2 for himself/herself in #USER5.1, which should fail as forbidden | POST | /api/v3/Jobs | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0150 | Adds a Status update to a job as a user from ADMIN_GROUPS for his/her job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0160 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0170 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0180 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0190 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0200 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser51} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0210 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByGroup1} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0220 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByGroup5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0230 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByAnonym} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0240 | Adds a Status update to a job as user5.1 for his/her job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0250 | Adds a Status update to a job as user5.1 for another user's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0260 | Adds a Status update to a job as user5.1 for his/her group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Adds a Status update to a job as user5.1 for another user's group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0280 | Adds a Status update to a job as user5.1 for anonymous user's group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByAnonym} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0290 | Adds a Status update to a job as user5.2 for his/her job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser52} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0300 | Adds a Status update to a job as user5.2 for user's 5.1 in same group job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByUser51} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0310 | Adds a Status update to a job as user5.2 for another user in his/her group job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedUserSpecJobOwnedByGroup5} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0320 | Access jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v3/Jobs?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0330 | Access jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0340 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.1, limited by 5 | GET | /api/v3/Jobs?createdBy=user5.1&limit=5 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0350 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0360 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v3/Jobs/facet?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
