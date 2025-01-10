# 1100: Jobs

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

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | Add dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0020 | Add dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0030 | Add dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with no datasets in job parameters, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with not existing dataset IDs, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with no jobParams parameter, which should fail | POST | /api/v3/Jobs | admin | 400 | ```BadRequestStatusCode``` |
| 0065 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with empty jobParams parameter | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0070 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0080 | Add a new job as a user from ADMIN_GROUPS for another user in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0090 | Add a new job as a user from ADMIN_GROUPS for undefined user from another group user in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0100 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#all' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0110 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#all' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0120 | Add a new job as a user from CREATE_JOB_GROUPS for his/her group in '#all' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0130 | Add a new job as a user from CREATE_JOB_GROUPS for another user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0140 | Add a new job as a user from CREATE_JOB_GROUPS for another group in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0150 | Add a new job as a user from CREATE_JOB_GROUPS for anonymous user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0160 | Add a new job as a normal user for himself/herself in '#all' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0170 | Add a new job as a normal user for his/her group in '#all' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0180 | Add a new job as a normal user for another user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0190 | Add a new job as a normal user for another group in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0200 | Add a new job as a normal user for anonymous user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0210 | Add a new job as unauthenticated user in '#all' configuration | POST | /api/v3/Jobs | unauthenticated | 201 | ```EntryCreatedStatusCode``` |
| 0220 | Add a new job as unauthenticated user for another user in '#all' configuration, which should fail as bad request | POST | /api/v3/Jobs | unauthenticated | 400 | ```BadRequestStatusCode``` |
| 0230 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with all published datasets | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0240 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0250 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0260 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0270 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0280 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetPublic' configuration with all published datasets | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0290 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetPublic' configuration with one unpublished dataset | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0300 | Add a new job as a normal user himself/herself in '#datasetPublic' configuration with a published dataset | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0310 | Add a new job as a normal user himself/herself in '#datasetPublic' configuration with unpublished datasets, which should fail as forbidden | POST | /api/v3/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0311 | Add a new public job as a normal user himself/herself with a published dataset | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0312 | Add a new public job as a normal user himself/herself with unpublished datasets, which should fail | POST | /api/v3/Jobs | user5.1 | 409 | ```ConflictStatusCode``` |
| 0313 | Add a new archive job as a normal user himself/herself with an archivable dataset | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0314 | Add a new retrieve job as a normal user himself/herself with a non retrievable dataset, which should fail | POST | /api/v3/Jobs | user5.1 | 409 | ```ConflictStatusCode``` |
| 0315 | Add a new public job as a normal user himself/herself with unknown files, which should fail | POST | /api/v3/Jobs | user5.1 | 400 | ```BadRequestStatusCode``` |
| 0316 | Add a new public job as a normal user himself/herself choosing only specific files | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0320 | Add a new job as anonymous user in '#datasetPublic' configuration with all published datasets | POST | /api/v3/Jobs | unauthenticated | 201 | ```EntryCreatedStatusCode``` |
| 0330 | Add a new job as anonymous user in '#datasetPublic' configuration with one unpublished dataset, which should fail as forbidden | POST | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0340 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0350 | Add a new job as a user from ADMIN_GROUPS for another user in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0360 | Add a new job as a user from ADMIN_GROUPS for another group in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0370 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#authenticated' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0380 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#authenticated' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0390 | Add a new job as a normal user for himself/herself in '#authenticated' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0400 | Add a new job as unauthenticated user in '#authenticated' configuration, which should fail as forbidden | POST | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0410 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0420 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0430 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0435 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0440 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetAccess' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0450 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetAccess' configuration with access to datasets | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0460 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetAccess' configuration with no access to datasets | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0470 | Add a new job as user1 for user5.1 ownerUser and group5 ownerGroup for #datasetAccess, which should fail | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0480 | Add a new job as a normal user for himself/herself in '#datasetAccess' configuration with access to datasets | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0490 | Add a new job as a normal user for himself/herself in '#datasetAccess' configuration with no access to datasets, which should fail as forbidden | POST | /api/v3/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0500 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0510 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0520 | Add a new job as a user from ADMIN_GROUPS for another user in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0530 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0535 | Add a new job as a user from ADMIN_GROUPS for another group in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0540 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#datasetOwner' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0550 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetOwner' configuration with datasets owned by his/her group | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0560 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself in '#datasetOwner' configuration with datasets owned by his/her group | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0570 | Add a new job as a normal user for himself/herself in '#datasetOwner' configuration with datasets owned by his/her group | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0580 | Add a new job as a normal user for himself/herself in '#datasetOwner' configuration with datasets not owned by his/her group, which should fail as forbidden | POST | /api/v3/Jobs | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 0590 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0600 | Add a new job as a user from ADMIN_GROUPS for another user in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0610 | Add a new job as a user from ADMIN_GROUPS for another group in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0615 | Add a new job as a user from ADMIN_GROUPS for another group in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0616 | Add a new job as a user from ADMIN_GROUPS for another user in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0620 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#USER5.1' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0630 | Add a new job as a user from CREATE_JOB_GROUPS for himself/herself user in '#USER5.1' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0640 | Add a new job as a user from CREATE_JOB_GROUPS for user5.1 in '#USER5.1' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0650 | Add a new job as user5.1 himself/herself in '#USER5.1' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0660 | Add a new job as user5.1 for no ownerUser and group5 ownerGroup in #USER5.1 configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0670 | Add a new job as user5.2 for himself/herself in #USER5.1, which should fail as forbidden | POST | /api/v3/Jobs | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 0680 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0690 | Add a new job as a user from ADMIN_GROUPS for another user in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0700 | Add a new job as a user from ADMIN_GROUPS for another group in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0705 | Add a new job as a user from ADMIN_GROUPS for another group in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0706 | Add a new job as a user from ADMIN_GROUPS for another user in '@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0710 | Add a new job as a user from ADMIN_GROUPS for anonymous user in '#@group5' configuration | POST | /api/v3/Jobs | admin | 201 | ```EntryCreatedStatusCode``` |
| 0720 | Add a new job as a user from CREATE_JOB_GROUPS for another group in '#@group5' configuration | POST | /api/v3/Jobs | user1 | 201 | ```EntryCreatedStatusCode``` |
| 0730 | Add a new job as a user from CREATE_JOB_GROUPS for user 5.1 in '#@group5' configuration, which should fail as bad request | POST | /api/v3/Jobs | user1 | 400 | ```BadRequestStatusCode``` |
| 0740 | Add a new job as a user 5.1 for himself/herself in '#@group5' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0750 | Add a new job as a user 5.1 for another user in his/her group in '#@group5' configuration | POST | /api/v3/Jobs | user5.1 | 201 | ```EntryCreatedStatusCode``` |
| 0760 | Add a new job as a user 5.2 for himself/herself in '#@group5' configuration | POST | /api/v3/Jobs | user5.2 | 201 | ```EntryCreatedStatusCode``` |
| 0770 | Add a new job as user3 for himself/herself in #@group5 configuration, which should fail as forbidden | POST | /api/v3/Jobs | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 0780 | Add a status update to a job as a user from ADMIN_GROUPS for his/her job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0790 | Add a Status update to a job as a user from ADMIN_GROUPS for another user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId2} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0800 | Add a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId3} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0810 | Add a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId6} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0820 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId2} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0830 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId4} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0840 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId3} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0850 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId5} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0860 | Add a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId6} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0870 | Add a Status update to a job as a normal user  for his/her job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId4} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0880 | Add a Status update to a job as a normal user for another user's job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId2} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0890 | Add a Status update to a job as a normal user for his/her group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0900 | Add a Status update to a job as a normal user for another user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId3} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0910 | Add a Status update to a job as a normal user for anonymous user's group in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId6} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 0920 | Add a Status update to a job as unauthhenticated user for anonymous job in '#all' configuration | PATCH | /api/v3/Jobs/${encodedJobId6} | unauthenticated | 200 | ```SuccessfulPatchStatusCode``` |
| 0930 | Add a Status update to a job as unauthhenticated user for anouther group's job in '#all' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobId3} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0940 | Adds a Status update to a job as unauthhenticated user for another user's job in '#all' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobId2} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 0950 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUser1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0960 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUser2} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0970 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUser3} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0980 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 0990 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUser2} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1000 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser4} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1010 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUser3} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1020 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1030 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1040 | Adds a Status update to a job as a normal user  for his/her job in '#jobOwnerUser' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUser4} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1050 | Adds a Status update to a job as a normal user for another user's job in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser2} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1060 | Adds a Status update to a job as a normal user for his/her group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser5} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1070 | Adds a Status update to a job as a normal user for another user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser3} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1080 | Adds a Status update to a job as a normal user for anonymous user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1090 | Adds a Status update to a job as unauthhenticated user for anonymous user's group in '#jobOwnerUser' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 1100 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1110 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1120 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1130 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1140 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1150 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroup4} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1160 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1170 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1180 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1190 | Adds a Status update to a job as a normal user  for his/her job in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup4} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1200 | Adds a Status update to a job as a normal user for another user's job in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1210 | Adds a Status update to a job as a normal user for his/her group in '#jobOwnerGroup' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1220 | Adds a Status update to a job as a normal user for another user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1230 | Adds a Status update to a job as a normal user for anonymous user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1240 | Adds a Status update to a job as unauthhenticated user for anonymous user's group in '#jobOwnerGroup' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 1250 | Adds a Status update to a job as a user from ADMIN_GROUPS for his/her job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1260 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec2} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1270 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec3} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1280 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec6} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1290 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec2} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1300 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1310 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec3} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1320 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1330 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec6} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1340 | Adds a Status update to a job as user5.1 for his/her job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1350 | Adds a Status update to a job as user5.1 for another user's job in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec2} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1360 | Adds a Status update to a job as user5.1 for his/her group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1370 | Adds a Status update to a job as user5.1 for another user's group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1380 | Adds a Status update to a job as user5.1 for anonymous user's group in 'USER5.1' configuration | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec6} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1390 | Adds a Status update to a job as user5.2 for his/her job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec7} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 1400 | Adds a Status update to a job as user5.2 for user's 5.1 in same group job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 1410 | Adds a Status update to a job as user5.2 for another user in his/her group job in 'USER5.1' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec5} | user5.2 | 403 | ```AccessForbiddenStatusCode``` |
| 1420 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec1} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1430 | Adds a Status update to a job as a user from ADMIN_GROUPS for another group's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec2} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1440 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec3} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1450 | Adds a Status update to a job as a user from ADMIN_GROUPS for anonymous user's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec6} | admin | 200 | ```SuccessfulPatchStatusCode``` |
| 1460 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec2} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1470 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's job in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec4} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1480 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for his/her group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec3} | user1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1490 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for another user's group in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec5} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1500 | Adds a Status update to a job as a user from UPDATE_JOB_GROUPS for anonymous user's group in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec6} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1510 | Adds a Status update to a job as user5.1 for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec4} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1520 | Adds a Status update to a job as user5.1 for another user's job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec2} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1530 | Adds a Status update to a job as user5.1 for his/her group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec5} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1540 | Adds a Status update to a job as user5.1 for another user's group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec4} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1550 | Adds a Status update to a job as user5.1 for anonymous user's group in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec6} | user5.1 | 200 | ```SuccessfulPatchStatusCode``` |
| 1560 | Adds a Status update to a job as user5.2 for his/her job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec5} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 1570 | Adds a Status update to a job as user5.2 for user's 5.1 in same group job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec2} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 1580 | Adds a Status update to a job as user5.2 for another user in his/her group job in '@group5' configuration | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec3} | user5.2 | 200 | ```SuccessfulPatchStatusCode``` |
| 1590 | Adds a Status update to a job as user3 for his/her job in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec4} | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 1600 | Adds a Status update to a job as user3 for user's 5.1 job in '@group5' configuration, which should fail as forbidden | PATCH | /api/v3/Jobs/${encodedJobIdGroupSpec2} | user3 | 403 | ```AccessForbiddenStatusCode``` |
| 1610 | Adds a status update to a job as a user from ADMIN_GROUPS for his/her job in '#all' configuration with non-existing jobId, which should fail as bad request | PATCH | /api/v3/Jobs/${badJobId} | admin | 400 | ```BadRequestStatusCode``` |
| 1620 | Access jobs as a user from ADMIN_GROUPS | GET | /api/v3/Jobs | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1630 | Access jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1640 | Access jobs as a user from ADMIN_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1650 | Access jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v3/Jobs?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1660 | Access jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1670 | Access jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v3/Jobs?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1680 | Access jobs as a user from CREATE_JOB_GROUPS | GET | /api/v3/Jobs | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 1690 | Access jobs as a user from CREATE_JOB_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 1700 | Access jobs as a user from CREATE_JOB_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 1710 | Access jobs as a normal user | GET | /api/v3/Jobs | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 1720 | Access jobs as a normal user (user5.1) that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 1730 | Access jobs as another normal user (user5.2) | GET | /api/v3/Jobs | user5.2 | 200 | ```SuccessfulGetStatusCode``` |
| 1740 | Access jobs as unauthenticated user, which should be forbidden | GET | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 1750 | Get admin's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedJobIdUser1} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1760 | Get user1's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedJobIdUser2} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1770 | Get group1's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedJobIdUser3} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1780 | Get admin's job as user from ADMIN_GROUP | GET | /api/v3/Jobs/${encodedJobIdUser6} | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1790 | Get admin's job as user from CREATE_JOB_GROUP, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser1} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1800 | Get his/her own job as user from CREATE_JOB_GROUP | GET | /api/v3/Jobs/${encodedJobIdUser2} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 1810 | Get a job from his/her own group as user from CREATE_JOB_GROUP | GET | /api/v3/Jobs/${encodedJobIdUser3} | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 1820 | Get other user's job as user from CREATE_JOB_GROUP, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser4} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1830 | Get anonymous user's job as user from CREATE_JOB_GROUP, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser6} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1840 | Get admin's job as normal, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser1} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1850 | Get other user's job as normal user, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser2} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1860 | Get his/her own job as normal user | GET | /api/v3/Jobs/${encodedJobIdUser4} | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 1870 | Get job of another user in his/her group as normal user, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUserSpec7} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1880 | Get job from his/her own group as normal user, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser5} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1890 | Get anonymous user's job as normal user, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser6} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1900 | Get anonymous user's job as anonymous user, which should be forbidden | GET | /api/v3/Jobs/${encodedJobIdUser6} | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 1910 | Delete job 1 as Archive Manager | DELETE | /api/v3/Jobs/${encodedJobIdUser1} | archiveManager | 200 | ```SuccessfulDeleteStatusCode``` |
| 1920 | Delete job 1 as Admin | DELETE | /api/v3/Jobs/${encodedJobIdUser2} | admin | 200 | ```SuccessfulDeleteStatusCode``` |
| 1930 | Delete job 1 as CREATE_JOB_GROUPS user, which should fail | DELETE | /api/v3/Jobs/${encodedJobIdUser3} | user1 | 403 | ```AccessForbiddenStatusCode``` |
| 1940 | Delete job 1 as normal user, which should fail | DELETE | /api/v3/Jobs/${encodedJobIdUser3} | user5.1 | 403 | ```AccessForbiddenStatusCode``` |
| 1950 | Delete job not existing in database as Archive Manager, which should fail | DELETE | /api/v3/Jobs/${fakeJobId} | archiveManager | 400 | ```BadRequestStatusCode``` |
| 1960 | Access jobs as a user from ADMIN_GROUPS, which should be one less than before proving that delete works | GET | /api/v3/Jobs | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1970 | Fullquery jobs as a user from ADMIN_GROUPS, limited by 5 | GET | /api/v3/Jobs?limit=5 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1980 | Fullquery jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 1990 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2000 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.1, limited by 5 | GET | /api/v3/Jobs?createdBy=user5.1&limit=5 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2010 | Fullquery jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2020 | Fullquery jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v3/Jobs?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2040 | Fullquery jobs as a user from CREATE_JOB_GROUPS that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 2050 | Fullquery jobs as a user from CREATE_JOB_GROUPS that were created by User1 | GET | /api/v3/Jobs?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 2060 | Fullquery jobs as a normal user | GET | /api/v3/Jobs | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 2070 | Fullquery jobs as a normal user (user5.1) that were created by admin | GET | /api/v3/Jobs?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 2080 | Fullquery jobs as another normal user (user5.2) | GET | /api/v3/Jobs | user5.2 | 200 | ```SuccessfulGetStatusCode``` |
| 2090 | Fullquery jobs as unauthenticated user, which should be forbidden | GET | /api/v3/Jobs | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 2100 | Fullfacet jobs as unauthenticated user, which should be forbidden | GET | /api/v3/Jobs/facet | unauthenticated | 403 | ```AccessForbiddenStatusCode``` |
| 2110 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by admin | GET | /api/v3/Jobs/facet?createdBy=admin | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2120 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User1 | GET | /api/v3/Jobs/facet?createdBy=user1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2130 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.1 | GET | /api/v3/Jobs/facet?createdBy=user5.1 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2140 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by User5.2 | GET | /api/v3/Jobs/facet?createdBy=user5.2 | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2150 | Fullfacet jobs as a user from ADMIN_GROUPS that were created by anonymous user | GET | /api/v3/Jobs/facet?createdBy=anonymous | admin | 200 | ```SuccessfulGetStatusCode``` |
| 2160 | Fullfacet jobs as a user from CREATE_JOB_GROUPS that were created by admin | GET | /api/v3/Jobs/facet?createdBy=admin | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 2170 | Fullfacet jobs as a user from CREATE_JOB_GROUPS that were created by User1 | GET | /api/v3/Jobs/facet?createdBy=user1 | user1 | 200 | ```SuccessfulGetStatusCode``` |
| 2180 | Fullfacet jobs as a normal user | GET | /api/v3/Jobs/facet | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 2190 | Fullfacet jobs as a normal user (user5.1) that were created by admin | GET | /api/v3/Jobs/facet?createdBy=admin | user5.1 | 200 | ```SuccessfulGetStatusCode``` |
| 2200 | Fullfacet jobs as another normal user (user5.2) | GET | /api/v3/Jobs/facet | user5.2 | 200 | ```SuccessfulGetStatusCode``` |

### 3120: Validate Job Action

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
