# 1100-1190: Jobs

Jobs test that the functionalities for creating, updating, deleting and retrieving jobs are working correctly.

Tests are built assuming the following owner, access and public information:

| Groups | Dataset 1 | Dataset 2 | Dataset 3 |
| --- | --- | --- | --- |
| admin | Admin | Admin | Admin |
| adminingestor | Admin | Admin | Admin |
| archivemanager | | | Access | 
| datasetingestor | | | |
| proposalingestor | | | | 
| sampleingestor | | | |
| group1 | Owner | | Access |
| group2 | | | |
| group3 | | Owner | |
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
| user1 | group1 | Create Job Privileged Groups, Create Dataset Groups, Sample Groups |
| user2 | group2 | Create Job Privileged Groups, Create Dataset Groups, Create Dataset with Pid Groups |
| user3 | group3 | Update Privileged Job Groups, Create Dataset Groups, Create Dataset Privileged Groups |
| user4 | group4 | _none_ |
| user5.1 | group5 | _none_ |
| user5.2 | group5 | _none_ |

## Tests List

Tests use their own job configuration file `config/jobconfig.yaml`. This file defines familiar "archive", "retrieve", "public" jobs, but also "validate" job or new types that are used here to test the authorization model.
File `Jobs.js` performs tests with job configurations mimicking a real configuration, such as "archive/retrieve/public". Test suite 1115 additionally tests if entered job parameters are valid.
Other jobs' test files are separated into distinct ones based on the authorization value for "_create_" entry in the job configuration file and test if specific user is authorized to do the CRUD operations.
Not all files test PATCH and DELETE methods, as these would be redundant.

### 1110: Jobs: Test New Job Model: possible real configurations

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new public job as a normal user himself/herself with a published dataset | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new public job as a normal user himself/herself with unpublished datasets, which should fail | POST | /api/v4/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0060 | Add a new archive job as a normal user himself/herself with an archivable dataset | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new retrieve job as a normal user himself/herself with a non retrievable dataset, which should fail | POST | /api/v4/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0080 | Add a new public job as a normal user himself/herself with unknown files, which should fail | POST | /api/v4/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0090 | Add a new public job as a normal user himself/herself choosing only specific files | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |


### 1115: Validate Job Action

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Create validate job fails without required parameters | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0020 | Create validate job fails with the wrong types | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0030 | Create validate job fails with the wrong types | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0040 | Create validate job fails with the wrong types | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0050 | Create validate fails without datasetList | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0060 | Create validate succeeds with the right types | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Update validate fails without the required parameters | PATCH | /api/v4/Jobs/${encodedJobIdValidate1} | admin | 400 | ```BadRequestStatusCode``` |
| 0080 | Update validate fails with incorrect types | PATCH | /api/v4/Jobs/${encodedJobIdValidate1} | admin | 400 | ```BadRequestStatusCode``` |
| 0090 | Updating validate succeeds with the required parameters | PATCH | /api/v4/Jobs/${encodedJobIdValidate1} | admin | 200 | ```SuccessfulPatchStatusCode``` |


### 1120: Jobs: Test New Job Model Authorization for all_access jobs type

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with no datasets in job parameters, which should fail | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with not existing dataset IDs, which should fail | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with no jobParams parameter, which should fail | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with empty jobParams parameter | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for another user in '#all' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from ADMIN_GROUPS for undefined user from another group user in '#all' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#all' configuration without contactEmail, which should fail | POST | /api/v4/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0120 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#all' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#all' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0140 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for his/her group in '#all' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0150 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for another user in '#all' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0160 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for another group in '#all' configuration (the user has no access to the dataset)| POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0170 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for anonymous user in '#all' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0180 | Add a new job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for anonymous user in '#all' configuration, which should be forbidden | POST | /api/v4/Jobs | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0190 | Add a new job as a normal user for himself/herself in '#all' configuration | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0200 | Add a new job as a normal user for his/her group in '#all' configuration | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0210 | Add a new job as a normal user for another user in '#all' configuration, which should fail as bad request | POST | /api/v4/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0220 | Add a new job as a normal user for another group in '#all' configuration, which should fail as bad request | POST | /api/v4/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0230 | Add a new job as a normal user for anonymous user in '#all' configuration, which should fail as bad request | POST | /api/v4/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0240 | Add a new job as unauthenticated user in '#all' configuration | POST | /api/v4/Jobs | unauthenticated | 201 | ```EntryCreatedStatusCode``` |
| 0250 | Add a new job as unauthenticated user for another user in '#all' configuration, which should fail as bad request | POST | /api/v4/Jobs | unauthenticated | 400 | ```BadRequestStatusCode``` |
| 0260 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Add a status update to a job as a user from ADMIN_GROUPS for another user's job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0280 | Add a status update to a job as a user from ADMIN_GROUPS for another group's job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0290 | Add a status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0300 | Add a status update to a job as a user from CREATE_JOB_PRIVILEGED_GROUPS for anonymous user's job in '#all' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser3} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0310 | Add a status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS his/her group in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup3} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0320 | Add a status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0330 | Add a status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for admin's job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0340 | Add a status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's group in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0350 | Add a status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for anonymous user's group in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0360 | Add a status update to a job as a normal user  for his/her job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0370 | Add a status update to a job as a normal user for another user's job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0380 | Add a status update to a job as a normal user for his/her group in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0390 | Add a status update to a job as a normal user for another user's group in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0400 | Add a status update to a job as a normal user for anonymous user's group in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0410 | Add a status update to a job as unauthenticated user for anonymous job in '#all' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | unauthenticated | 200 | ```SuccessfulPatchStatusCode``` |
| 0420 | Add a status update to a job as unauthenticated user for another group's job in '#all' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0430 | Add a status update to a job as unauthenticated user for another user's job in '#all' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0440 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '#all' configuration with non-existing jobId, which should fail as bad request | PATCH | /api/v4/Jobs/${badJobId} | admin | 400 | ```BadRequestStatusCode``` |
| 0450 | Access jobs as a user from ADMIN_GROUPS | GET | /api/v4/Jobs | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0460 | Access jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v4/Jobs?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0470 | Access jobs as a user from ADMIN_GROUPS that were created by user in CREATE_JOB_PRIVILEGED_GROUPS | GET | /api/v4/Jobs?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0480 | Access jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v4/Jobs?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0490 | Access jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v4/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0500 | Access jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v4/Jobs?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0510 | Access jobs as a user from CREATE_JOB_PRIVILEGED_GROUPS | GET | /api/v4/Jobs | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0520 | Access jobs as a user from CREATE_JOB_PRIVILEGED_GROUPS that were created by admin | GET | /api/v4/Jobs?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0530 | Access jobs as a user from CREATE_JOB_PRIVILEGED_GROUPS that were created by user1 | GET | /api/v4/Jobs?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0540 | Access jobs as a user from UPDATE_JOB_PRIVILEGED_GROUPS | GET | /api/v4/Jobs | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0550 | Access jobs as a normal user | GET | /api/v4/Jobs | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0560 | Access jobs as a normal user (user5.1) that were created by admin | GET | /api/v4/Jobs?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0570 | Access jobs as another normal user (user5.2) | GET | /api/v4/Jobs | user5.2 | 200 | ```SuccessfulGetStatusCode``` |
| 0580 | Access jobs as unauthenticated user, which should be forbidden | GET | /api/v4/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0590 | Get admin's job as user from ADMIN_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0600 | Get user1's job as user from ADMIN_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByUser1} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0610 | Get group1's job as user from ADMIN_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByGroup1} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0620 | Get admin's job as user from ADMIN_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByAnonym} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0630 | Get admin's job as user from CREATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByAdmin} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0640 | Get his/her own job as user from CREATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByUser1} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0650 | Get a job from his/her own group as user from CREATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0660 | Get other user's job as user from CREATE_JOB_GROUP| GET | /api/v4/Jobs/${encodedJobOwnedByUser51} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0670 | Get anonymous user's job as user from CREATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0680 | Get admin's job as user from UPDATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByAdmin} | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0690 | Get his/her own job as user from UPDATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByUser1} | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0700 | Get a job from his/her own group as user from UPDATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByGroup3} | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0710 | Get other user's job as user from UPDATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByUser51} | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0720 | Get anonymous user's job as user from UPDATE_JOB_GROUP | GET | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0730 | Get admin's job as normal user, which should be forbidden | GET | /api/v4/Jobs/${encodedJobOwnedByAdmin} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0740 | Get other user's job as normal user, which should be forbidden | GET | /api/v4/Jobs/${encodedJobOwnedByUser1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0750 | Get his/her own job as normal user | GET | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0760 | Get anonymous user's job as normal user, which should be forbidden | GET | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0770 | Get anonymous user's job as anonymous user, which should be forbidden | GET | /api/v4/Jobs/${encodedJobOwnedByAnonym} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0780 | Delete job created by admin as Archive Manager | DELETE | /api/v4/Jobs/${encodedJobOwnedByAdmin} | archiveManager | 200 | ```SuccessfulDeleteStatusCode``` |
| 0790 | Delete job created by admin as Admin | DELETE | /api/v4/Jobs/${encodedJobOwnedByUser1} | admin | 200 | ```SuccessfulDeleteStatusCode``` |
| 0800 | Delete job created by admin as CREATE_JOB_PRIVILEGED_GROUPS user, which should be forbidden | DELETE | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user1 | 403 | ```DeleteForbiddenStatusCode``` |
| 0810 | Delete job created by admin as normal user, which should be forbidden | DELETE | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user5.1 | 403 | ```DeleteForbiddenStatusCode``` |
| 0820 | Delete job not existing in database as Archive Manager, which should fail | DELETE | /api/v4/Jobs/${fakeJobId} | archiveManager | 400 | ```BadRequestStatusCode``` |
| 0830 | Access jobs as a user from ADMIN_GROUPS, which should be one less than before proving that delete works | GET | /api/v4/Jobs | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0840 | Fullquery jobs as a user from ADMIN_GROUPS, limited by 2 | GET | /api/v4/Jobs?limit=2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0850 | Fullquery jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v4/Jobs/fullquery?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0860 | Fullquery jobs as a user from ADMIN_GROUPS that were created by user1 | GET | /api/v4/Jobs/fullquery?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0870 | Fullquery jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v4/Jobs/fullquery?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0880 | Fullquery jobs as a user from CREATE_JOB_PRIVILEGED_GROUPS that were created by admin | GET | /api/v4/Jobs/fullquery?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0890 | Fullquery jobs as a user from CREATE_JOB_PRIVILEGED_GROUPS that were created by user1 | GET | /api/v4/Jobs/fullquery?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0900 | Fullquery jobs as a user from UPDATE_JOB_PRIVILEGED_GROUPS that were created by admin | GET | /api/v4/Jobs/fullquery?createdBy=admin | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0910 | Fullquery jobs as a user from UPDATE_JOB_PRIVILEGED_GROUPS that were created by user1 | GET | /api/v4/Jobs/fullquery?createdBy=user1 | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0920 | Fullquery jobs as a normal user | GET | /api/v4/Jobs/fullquery | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0930 | Fullquery jobs as a normal user (user5.1) that were created by admin | GET | /api/v4/Jobs/fullquery?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0940 | Fullquery jobs as unauthenticated user, which should be forbidden | GET | /api/v4/Jobs/fullquery | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0950 | Fullfacet jobs as unauthenticated user, which should be forbidden | GET | /api/v4/Jobs/fullfacet | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0960 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v4/Jobs/fullfacet?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0970 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by user1 | GET | /api/v4/Jobs/fullfacet?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0980 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v4/Jobs/fullfacet?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0990 | Fullfacet jobs as a user from CREATE_JOB_PRIVILEGED_GROUPS that were created by admin | GET | /api/v4/Jobs/fullfacet?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 1000 | Fullfacet jobs as a user from CREATE_JOB_PRIVILEGED_GROUPS that were created by user1 | GET | /api/v4/Jobs/fullfacet?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 1010 | Fullfacet jobs as a user from UPDATE_JOB_PRIVILEGED_GROUPS that were created by admin | GET | /api/v4/Jobs/fullfacet?createdBy=admin | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 1020 | Fullfacet jobs as a user from UPDATE_JOB_PRIVILEGED_GROUPS that were created by user1 | GET | /api/v4/Jobs/fullfacet?createdBy=user1 | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 1030 | Fullfacet jobs as a normal user | GET | /api/v4/Jobs/fullfacet | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 1040 | Fullfacet jobs as a normal user (user5.1) that were created by admin | GET | /api/v4/Jobs/fullfacet?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |


### 1130: Jobs: Test New Job Model Authorization for authenticated_access jobs type

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#authenticated' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#authenticated' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#authenticated' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#authenticated' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#authenticated' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a normal user for himself/herself in '#authenticated' configuration | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as unauthenticated user in '#authenticated' configuration, which should be forbidden | POST | /api/v4/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |


### 1140: Jobs: Test New Job Model Authorization for dataset_access jobs type

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetAccess' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetAccess' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetAccess' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetAccess' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetAccess' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetAccess' configuration with access to datasets | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetAccess'  with no access to datasets, which should be forbidden | POST | /api/v4/Jobs | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetAccess' configuration with access to datasets | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0120 | Add a new job as user from CREATE_JOB_PRIVILEGED_GROUPS for another user ownerGroup for #datasetAccess | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as user from CREATE_JOB_PRIVILEGED_GROUPS for different ownerUser and ownerGroup for #datasetAccess, which should be forbidden | POST | /api.v4/Jobs | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0140 | Add a new job as a normal user for himself/herself in '#datasetAccess' configuration with access to datasets | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0150 | Add a new job as a normal user for himself/herself in '#datasetAccess' configuration with no access to datasets, which should be forbidden | POST | /api/v4/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0160 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0170 | Add a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0180 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0190 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0200 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser3} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0210 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0220 | AAdd a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for admin's job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | user3 | 403 | ```SuccessfulPatchStatusCode``` |
| 0230 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for anonymous user's group in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user3 | 403 | ```SuccessfulPatchStatusCode``` |
| 0240 | Add a Status update to a job as a normal user  for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0250 | Add a Status update to a job as a normal user for another user's job in '#jobOwnerGroup' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0260 | Add a Status update to a job as a normal user for his/her group in '#jobOwnerGroup' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Add a Status update to a job as a normal user for another user's group in '#jobOwnerGroup' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0280 | Add a Status update to a job as a normal user for anonymous user's group in '#jobOwnerGroup' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0290 | Add a Status update to a job as unauthenticated user for anonymous user's group in '#jobOwnerGroup' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |


### 1150: Jobs: Test New Job Model Authorization for owner_access jobs type

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetOwner' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetOwner' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetOwner' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetOwner' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetOwner' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetOwner' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetOwner' configuration with dataset owned by his/her group | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetOwner' configuration with only one of two datasets owned by his/her group, which should be forbidden | POST | /api/v4/Jobs | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0120 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for another user in '#datasetOwner' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a normal user for himself/herself in '#datasetOwner' configuration with datasets owned by his/her group | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0140 | Add a new job as a normal user for himself/herself in '#datasetOwner' configuration with datasets not owned by his/her group, which should be forbidden | POST | /api/v4/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0150 | Add a new job as a user from ADMIN_GROUPS for group2 and user1 in '#datasetOwner' configuration | POST | /api/v4/Jobs| admin | 200 | ```EntryCreatedStatusCode``` |
| 0160 | Add a new job as a user from ADMIN_GROUPS for group1 and user2 in '#datasetOwner' configuration | POST | /api/v4/Jobs | admin | 200 | ```EntryCreatedStatusCode``` |
| 0170 | , where the user is not an owner of some of these datasets, which should be forbidden | POST | /api/v4/Jobs | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0180 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for another user in '#datasetOwner' configuration, where the user is owner of these datasets | POST | /api/v4/Jobs | user1 | 200 | ```EntryCreatedStatusCode``` |
| 0190 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for group1 and user3 in '#datasetOwner' configuration, which should be forbidden | POST | /api/v4/Jobs | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0200 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0210 | Add a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0220 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0230 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0240 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser3} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0250 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's job in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0260 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for job owned by CREATE_JOB_PRIVILEGED_GROUPS in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's group in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0280 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for anonymous user's group in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0290 | Add a Status update to a job as a user from CREATE_JOB_PRIVILEGED_GROUPS for other group in '#jobOwnerUser' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0300 | Add a Status update to a job as a normal user  for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0310 | Add a Status update to a job as a normal user for another user's job in '#jobOwnerUser' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0320 | Add a Status update to a job by his group with no ownerUser as a normal user in '#jobOwnerUser' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0330 | Add a Status update to his/her job as a normal user in '#jobOwnerUser' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0340 | Add a Status update to a job by his group but another user as a normal user in '#jobOwnerUser' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser52} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0350 | Add a Status update to a job as a normal user for another user's group in '#jobOwnerUser' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0360 | Add a Status update to a job as a normal user for anonymous user's group in '#jobOwnerUser' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0370 | Add a Status update to a job as unauthenticated user for anonymous user's group in '#jobOwnerUser' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0380 | Access jobs as a User1 | GET | /api/v4/Jobs/ | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 0390 | Access jobs as a User2 | GET | /api/v4/Jobs/ | user2 | 200 | ```SuccessfulGetStatusCode``` |
| 0400 | Access jobs as a User3 | GET | /api/v4/Jobs/ | user3 | 200 | ```SuccessfulGetStatusCode``` |
| 0410 | Access jobs as a User5.1 | GET | /api/v4/Jobs/ | user51 | 200 | ```SuccessfulGetStatusCode``` |

### 1160: Jobs: Test New Job Model Authorization for public_access jobs type

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with all published datasets | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetPublic' configuration with all published datasets | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetPublic' configuration with published dataset for another group | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#datasetPublic' configuration with one unpublished dataset for another group, which should be forbidden | POST | /api/v4/Jobs | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0120 | Add a new job as a normal user himself/herself in '#datasetPublic' configuration with a published dataset | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a normal user himself/herself in '#datasetPublic' configuration with unpublished datasets, which should be forbidden | POST | /api/v4/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0140 | Add a new job as anonymous user in '#datasetPublic' configuration with all published datasets | POST | /api/v4/Jobs | unauthenticated | 201 | ```EntryCreatedStatusCode``` |
| 0150 | Add a new job as anonymous user in '#datasetPublic' configuration with one unpublished dataset, which should be forbidden | POST | /api/v4/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |


### 1170: Jobs: Test New Job Model Authorization for job_admin jobs type
| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#jobAdmin' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#jobAdmin' configuration  POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#jobAdmin' configuration  POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#jobAdmin' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#jobAdmin' configuration with dataset owned by his/her group | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#jobAdmin' configuration with only one of two datasets owned by his/her group | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for another user in '#jobAdmin' configuration  POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a normal user for himself/herself in '#jobAdmin' configuration with datasets owned by his/her group, which should be forbidden  POST | /api/v4/Jobs | user51 | 403 | ```AccessForbiddenStatusCode``` |
| 0120 | Add a new job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for himself/herself in '#jobAdmin' configuration with datasets owned by his/her group, which should be forbidden | POST | /api/v4/Jobs | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0130 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '#jobAdmin' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | Admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0140 | Add a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#jobAdmin' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | Admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0150 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobAdmin' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup3} | Admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0160 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for his/her job in '#jobAdmin' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup3} | User3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0170 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's job in '#jobAdmin' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | User3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0180 | Add a Status update to a job as a user from CREATE_JOB_PRIVILEGED_GROUPS for his group's in '#jobAdmin' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | User1 | 403 | ```AccessForbiddenStatusCode``` |
| 0190 | Add a Status update to a job as a normal user  for his/her job in '#jobAdmin' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | User51 | 403 | ```AccessForbiddenStatusCode``` |




### 1180: Jobs: Test New Job Model Authorization for group_access type: configuration set to a specific group - @group5

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#@group5' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#@group5' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#@group5' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#@group5' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for another user in '@group5' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#@group5' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for his/her own group in '#@group5' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for user 5.1 in '#@group5' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0120 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for user 4 in '#@group5' configuration | POST | /api/v4/Jobs/ user1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for user 5.1 in '#@group5' configuration, which should be forbidden | POST | /api/v4/Jobs | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0140 | Add a new job as a user 5.1 for himself/herself in '#@group5' configuration | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0150 | Add a new job as a user 5.1 for another user in his/her group in '#@group5' configuration | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0160 | Add a new job as a user 5.2 for himself/herself in '#@group5' configuration | POST | /api/v4/Jobs | user5.2 | 201 | ```EntryCreatedStatusCode``` |
| 0170 | Add a new job as a user 5.1 for another user in '#@group5' configuration, which should fail as bad request | POST | /api/v4/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0180 | Add a new job as user from UPDATE_JOB_PRIVILEGED_GROUPS for himself/herself in #@group5 configuration, which should fail as forbidden | POST | /api/v4/Jobs | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0190 | Add a new job as a normal user not in group5 for himself/herself in #@group5 configuration, which should be forbidden | POST | /api/v4/Jobs | user4 | 403 | ```AccessForbiddenStatusCode``` |
| 0200 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0210 | Add a Status update to a job as a user from ADMIN_GROUPS for another group's job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0220 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0230 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0240 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for his/her job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0250 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0260 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for his/her group in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | 0260: Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's group in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0280 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for anonymous user's group in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0290 | Add a Status update to a job as a user from CREATE_JOB_PRIVILEGED_GROUPS for anonymous user's group in '@group5' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0300 | Add a Status update to a job as user5.1 for his/her job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0310 | Add a Status update to a job as user5.1 for another user's job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0320 | Add a Status update to a job as user5.1 for his/her group in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0330 | Add a Status update to a job as user5.1 for another user's group in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0340 | Add a Status update to a job as user5.1 for anonymous user's group in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0350 | Add a Status update to a job as user5.2 for his/her job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser52} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 0360 | Add a Status update to a job as user5.2 for user's 5.1 in same group job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 0370 | Add a Status update to a job as user5.2 for another user in his/her group job in '@group5' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 0380 | Add a Status update to a job as a normal user for his/her job in '@group5' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser4} | user4 | 403 | ```AccessForbiddenStatusCode``` |
| 0390 | Add a Status update to a job as a normal user for user 5.1 job in '@group5' configuration, which should fail as forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user4 | 403 | ```AccessForbiddenStatusCode``` |
| 0400 | Access jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v4/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0410 | Get job of another user in his/her group as normal user | GET | /api/v4/Jobs/${encodedJobOwnedByUser52} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0420 | Get job from his/her own group as normal user | GET | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0430 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v4/Jobs/fullquery?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0440 | Fullquery jobs as another normal user (user5.2) | GET | /api/v4/Jobs/fullquery | user5.2 | 200 | ```SuccessfulGetStatusCode``` |
| 0450 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v4/Jobs/fullfacet?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0460 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v4/Jobs/fullfacet?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0470 | Fullfacet jobs as another normal user (user5.2) | GET | /api/v4/Jobs/fullfacet | user5.2 | 200 | ```SuccessfulGetStatusCode``` |


### 1190: Jobs: Test New Job Model Authorization for user_access type: configuration set to a specific user: USER5.1

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#USER5.1' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for another user in '#USER5.1' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for another group in '#USER5.1' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for another group in '#USER5.1' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for another user in '#USER5.1' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#USER5.1' configuration | POST | /api/v4/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for himself/herself user in '#USER5.1' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for user5.1 in '#USER5.1' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0120 | Add a new job as a user from CREATE_JOB_PRIVILEGED_GROUPS for another user in '#USER5.1' configuration | POST | /api/v4/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user in '#USER5.1' configuration, which should be forbidden | POST | /api/v4/Jobs | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0140 | Add a new job as user5.1 himself/herself in '#USER5.1' configuration | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0150 | Add a new job as user5.1 for no ownerUser and group5 ownerGroup in #USER5.1 configuration | POST | /api/v4/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0160 | Add a new job as user5.2 for himself/herself in #USER5.1, which should be forbidden | POST | /api/v4/Jobs | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0170 | Add a Status update to a job as a user from ADMIN_GROUPS for his/her job in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0180 | Add a Status update to a job as a user from ADMIN_GROUPS for another group's job in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0190 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0200 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0210 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for his/her job in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0220 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's job in 'USER5.1' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0230 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for his/her group in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup1} | user3 | 200 | ```SuccessfulPatchStatusCode``` |
| 0240 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for another user's group in 'USER5.1' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0250 | Add a Status update to a job as a user from UPDATE_JOB_PRIVILEGED_GROUPS for anonymous user's group in 'USER5.1' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 0260 | Add a Status update to a job as user5.1 for his/her job in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0270 | Add a Status update to a job as user5.1 for another user's job in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser1} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0280 | Add a Status update to a job as user5.1 for his/her group in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0290 | Add a Status update to a job as user5.1 for another user's group in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0300 | Add a Status update to a job as user5.1 for anonymous user's group in 'USER5.1' configuration | PATCH | /api/v4/Jobs/${encodedJobOwnedByAnonym} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0310 | Add a Status update to a job as user5.2 for his/her job in 'USER5.1' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser52} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0320 | Add a Status update to a job as user5.2 for user's 5.1 in same group job in 'USER5.1' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByUser51} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0330 | Add a Status update to a job as user5.2 for another user in his/her group job in 'USER5.1' configuration, which should be forbidden | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0340 | Access jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v4/Jobs?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0350 | Access jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v4/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0360 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.1, limited by 5 | GET | /api/v4/Jobs/fullquery?createdBy=user5.1&limit=1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0370 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v4/Jobs/fullquery?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0380 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v4/Jobs/fullfacet?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |

### 1200: Jobs: Test Backwards Compatibility

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add via /api/v3 a new job without datasetList, as a user from ADMIN_GROUPS, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0040 | Add via /api/v3 a new job ignoring datasetList from jobParams, as a user from ADMIN_GROUPS, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0050 | Add via /api/v3 an anonymous job as a user from ADMIN_GROUPS | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0060 | Get via /api/v4 the anonymous job as a user from ADMIN_GROUPS | GET | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0070 | Get via /api/v3 the anonymous job as user5.1, which should fail | GET | /api/v3/Jobs/${encodedJobOwnedByAdmin} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0080 | Get via /api/v4 the anonymous job as user5.1, which should fail | GET | /api/v4/Jobs/${encodedJobOwnedByAdmin} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0090 | Add via /api/v3 a new job with emailJobInitiator for user5.11, as a user from ADMIN_GROUPS | POST | /api/v3/Jobs |admin |  ```EntryCreatedStatusCode ``` |
| 0100 | Get via /api/v4 the job added for user5.1, as a user from ADMIN_GROUPS | GET | /api/v4/Jobs/${encodedJobOwnedByGroup5} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0110 | Get via /api/v4 the job added for user5.1, as user5.1, which should fail because ownerUser does not exist | GET | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0120 | Get via /api/v3 the job added for user5.1, as user5.1, which should fail because ownerUser does not exist | GET | /api/v3/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0130 | Add via /api/v3 a new job with a complete dto for user5.1 and other contactEmail, as a user from ADMIN_GROUPS | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0140 | Get via /api/v4 the job added for user5.1, as a user from ADMIN_GROUPS | GET | /api/v4/Jobs/${encodedJobOwnedByGroup5} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0150 | Get via /api/v4 the job added for user5.1, as user5.1 | GET | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0160 | Get via /api/v3 the job added for user5.1, as user5.1 | GET | /api/v3/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0170 | Add via /api/v3 a new job without specifying username for user5.1, as user5.1, which should fail | POST | /api/v3/Jobs |  user51 | 400 | ```BadRequestStatusCode``` |
| 0180 | Add via /api/v3 a new job specifying only emailJobInitiator for user5.1, as user5.1, which should fail | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0190 | Add via /api/v3 a new job with complete dto for user5.1, as user5.1 | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0200 | Get via /api/v4 the job added for user5.1, as user5.1 | GET | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0210 | Get via /api/v3 the job added for user5.1, as user5.1 | GET | /api/v3/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0220 | Add a status update via /api/v3 without jobStatusMessage to a job, as a user from ADMIN_GROUPS, which should fail | PATCH | /api/v3/Jobs/${encodedJobOwnedByAdmin} | admin | 400 | ```BadRequestStatusCode``` |
| 0230 | Add a status update via /api/v3 to a job as a user from ADMIN_GROUPS for his/her job | PATCH | /api/v3/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0240 | Get via /api/v4 the previously updated job as a user from ADMIN_GROUPS | GET | /api/v4/Jobs/${encodedJobOwnedByAdmin} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0250 | Add a status update via /api/v4 to a job that was created via /api/v3, as user5.1 for his/her job | PATCH | /api/v4/Jobs/${encodedJobOwnedByGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0260 | Get via /api/v3 the job that was previously updated via /api/v4, as user5.1 for his/her job | GET | /api/v3/Jobs/${encodedJobOwnedByGroup5} | user5 | 200 | ```SuccessfulGetStatusCode``` |
| 0270 | Get via /api/v3 all accessible jobs as user5.1 | GET | /api/v3/Jobs | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0280 | Get via /api/v3 all accessible jobs as a user from ADMIN_GROUPS | GET | /api/v3/Jobs | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0290 | Fullquery via /api/v3 all jobs that were created by user5.1, as user5.1 | GET | /api/v3/Jobs/fullquery?createdBy=user5.1 | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 0300 | Fullfacet via /api/v3 jobs that were created by admin, as a user from ADMIN_GROUPS | GET | /api/v3/Jobs/fullfacet?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0310 | Fullfacet via /api/v3 jobs that were created by user5.1, as a user from ADMIN_GROUPS | GET | /api/v3/Jobs/fullfacet?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0320 | Delete via /api/v3 a job created by admin, as a user from ADMIN_GROUPS | DELETE | /api/v3/Jobs/${encodedJobOwnedByAdmin} | admin |  200 | ```SuccessfulDeleteStatusCode``` |
| 0330 | Get via /api/v3 all accessible jobs as a user from ADMIN_GROUPS, which should be one less than before, proving that delete works | GET | /api/v3/Jobs/ | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0340 | Add via /api/v3 an anonymous job as user5.1, which should fail | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0350 | Add via /api/v3 an anonymous job as user51, providing another contactEmail, which should fail | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0360 | Add via /api/v3 a job for another user, as user5.1, which should fail | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0370 | Add a new job as anonymous user with all published datasets | POST | /api/v3/Jobs | unauthenticated | 201 | ```EntryCreatedStatusCode``` |
| 0380 | Get via /api/v4 the anonymous job as a user from ADMIN_GROUPS | GET | /api/v4/Jobs/${encodedJobAnonymous} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 0390 | Get via /api/v3 the anonymous job as user5.1, which should fail | GET | /api/v3/Jobs/${encodedJobAnonymous} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0400 | Get via /api/v3 the anonymous job as the normal user in its contactEmail, which should fail | GET | /api/v3/Jobs/${encodedJobAnonymous} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0410 | Get via /api/v3 the anonymous job as a user in CREATE_JOB_PRIVILEGED_GROUPS | GET | /api/v3/Jobs/${encodedJobAnonymous} | user2 | 200 | ```SuccessfulGetStatusCode``` |