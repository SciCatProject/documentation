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
| admin | admin | Admin Groups |
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

**Tests List:**

| Test Number | Description | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Expected Request Code |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | adds dataset 1 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0020 | adds dataset 2 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0030 | adds dataset 3 as Admin Ingestor | POST | /api/v3/Datasets | adminIngestor | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0040 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with no datasets in job parameters, which should fail | POST | /api/v3/Jobs | admin | 400 | ```TestData.BadRequestStatusCode``` |
| 0050 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#all' configuration with not existing dataset IDs, which should fail | POST | /api/v3/Jobs | admin | 400 | ```TestData.BadRequestStatusCode``` |
| 0060 | Add a new job as a user from ADMIN_GROUPS for himself/herself in '#datasetPublic' configuration with no jobParams parameter, which should fail | POST | /api/v3/Jobs | admin | 400 | ```TestData.BadRequestStatusCode``` |
<!-- | 0065 | POST | /api/v3/Jobs | admin | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0070 | POST | /api/v3/Jobs | admin | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0080 | POST | /api/v3/Jobs | admin | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0090 | POST | /api/v3/Jobs | admin | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0100 | POST | /api/v3/Jobs | admin | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0110 | POST | /api/v3/Jobs | user1 | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0120 | POST | /api/v3/Jobs | user1 | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0130 | POST | /api/v3/Jobs | user1 | 400 | ```TestData.BadRequestStatusCode``` |
| 0140 | POST | /api/v3/Jobs | user1 | 400 | ```TestData.BadRequestStatusCode``` |
| 0150 | POST | /api/v3/Jobs | user1 | 400 | ```TestData.BadRequestStatusCode``` |
| 0160 | POST | /api/v3/Jobs | user5.1 | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0170 | POST | /api/v3/Jobs | user5.1 | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0180 | POST | /api/v3/Jobs | user5.1 | 400 | 400 | ```TestData.BadRequestStatusCode``` |
| 0190 | POST | /api/v3/Jobs | user5.1 | 400 | 400 | ```TestData.BadRequestStatusCode``` |
| 0200 | POST | /api/v3/Jobs | user5.1 | 400 | 400 | ```TestData.BadRequestStatusCode``` |
| 0210 | POST | /api/v3/Jobs | unauthenticated | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0220 | POST | /api/v3/Jobs | unauthenticated | 400 | 400 | ```TestData.BadRequestStatusCode``` |
| 0230 | POST | /api/v3/Jobs | admin | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0240 | POST | /api/v3/Jobs | admin | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0250 | POST | /api/v3/Jobs | admin | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0260 | POST | /api/v3/Jobs | admin | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0270 | POST | /api/v3/Jobs | admin | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0280 | POST | /api/v3/Jobs | user1 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0290 | POST | /api/v3/Jobs | user1 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0300 | POST | /api/v3/Jobs | user5.1 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0310 | POST | /api/v3/Jobs | user5.1 | 403 | ```TestData.AccessForbiddenStatusCode``` |
| 0311 | POST | /api/v3/Jobs | user5.1 | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0312 | POST | /api/v3/Jobs | user5.1 | 409 | ```TestData.ConflictStatusCode``` |
| 0313 | POST | /api/v3/Jobs | user5.1 | 201 | ```archiveJob``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0314 | POST | /api/v3/Jobs | user5.1 | 409 | ```retrieveJob``` | ```TestData.ConflictStatusCode``` |
| 0315 | POST | /api/v3/Jobs | user5.1 | 400 | 400 | ```TestData.BadRequestStatusCode``` |
| 0316 | POST | /api/v3/Jobs | user5.1 | 201 | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0320 | POST | /api/v3/Jobs | unauthenticated | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0330 | POST | /api/v3/Jobs | unauthenticated | 403 | ```TestData.AccessForbiddenStatusCode``` |
| 0340 | POST | /api/v3/Jobs | admin | 201 | ```jobAuthenticated``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0350 | POST | /api/v3/Jobs | admin | 201 | ```jobAuthenticated``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0360 | POST | /api/v3/Jobs | admin | 201 | ```jobAuthenticated``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0370 | POST | /api/v3/Jobs | admin | 201 | ```jobAuthenticated``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0380 | POST | /api/v3/Jobs | user1 | 201 | ```jobAuthenticated``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0390 | POST | /api/v3/Jobs | user5.1 | 201 | ```jobAuthenticated``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0400 | POST | /api/v3/Jobs | unauthenticated | 403 | ```jobAuthenticated``` | ```TestData.AccessForbiddenStatusCode``` |
| 0410 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0420 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0430 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0435 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0440 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0450 | POST | /api/v3/Jobs | user1 | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0460 | POST | /api/v3/Jobs | user1 | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0470 | POST | /api/v3/Jobs | user1 | 400 | ```jobDatasetAccess``` | 400 | ```TestData.BadRequestStatusCode``` |
| 0480 | POST | /api/v3/Jobs | user5.1 | 201 | ```jobDatasetAccess``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0490 | POST | /api/v3/Jobs | user5.1 | 403 | ```jobDatasetAccess``` | ```TestData.AccessForbiddenStatusCode``` |
| 0500 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0510 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0520 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0530 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0535 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0540 | POST | /api/v3/Jobs | admin | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0550 | POST | /api/v3/Jobs | user1 | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0560 | POST | /api/v3/Jobs | user1 | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0570 | POST | /api/v3/Jobs | user5.1 | 201 | ```jobDatasetOwner``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0580 | POST | /api/v3/Jobs | user5.1 | 403 | ```jobDatasetOwner``` | ```TestData.AccessForbiddenStatusCode``` |
| 0590 | POST | /api/v3/Jobs | admin | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0600 | POST | /api/v3/Jobs | admin | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0610 | POST | /api/v3/Jobs | admin | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0615 | POST | /api/v3/Jobs | admin | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0616 | POST | /api/v3/Jobs | admin | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0620 | POST | /api/v3/Jobs | admin | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0630 | POST | /api/v3/Jobs | user1 | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0640 | POST | /api/v3/Jobs | user1 | 400 | ```jobUser51``` | 400 | ```TestData.BadRequestStatusCode``` |
| 0650 | POST | /api/v3/Jobs | user5.1 | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0660 | POST | /api/v3/Jobs | user5.1 | 201 | ```jobUser51``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0670 | POST | /api/v3/Jobs | user5.2 | 403 | ```jobUser51``` | ```TestData.AccessForbiddenStatusCode``` |
| 0680 | POST | /api/v3/Jobs | admin | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0690 | POST | /api/v3/Jobs | admin | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0700 | POST | /api/v3/Jobs | admin | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0705 | POST | /api/v3/Jobs | admin | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0706 | POST | /api/v3/Jobs | admin | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0710 | POST | /api/v3/Jobs | admin | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0720 | POST | /api/v3/Jobs | user1 | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0730 | POST | /api/v3/Jobs | user1 | 400 | ```jobGroup5``` | 400 | ```TestData.BadRequestStatusCode``` |
| 0740 | POST | /api/v3/Jobs | user5.1 | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0750 | POST | /api/v3/Jobs | user5.1 | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0760 | POST | /api/v3/Jobs | user5.2 | 201 | ```jobGroup5``` | 201 | ```TestData.EntryCreatedStatusCode``` |
| 0770 | POST | /api/v3/Jobs | user3 | 403 | ```jobGroup5``` | ```TestData.AccessForbiddenStatusCode``` |
| 0780 | PATCH | /api/v3/Jobs/${encodedJobId1} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0790 | PATCH | /api/v3/Jobs/${encodedJobId2} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0800 | PATCH | /api/v3/Jobs/${encodedJobId3} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0810 | PATCH | /api/v3/Jobs/${encodedJobId6} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0820 | PATCH | /api/v3/Jobs/${encodedJobId2} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0830 | PATCH | /api/v3/Jobs/${encodedJobId4} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0840 | PATCH | /api/v3/Jobs/${encodedJobId3} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0850 | PATCH | /api/v3/Jobs/${encodedJobId5} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0860 | PATCH | /api/v3/Jobs/${encodedJobId6} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0870 | PATCH | /api/v3/Jobs/${encodedJobId4} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0880 | PATCH | /api/v3/Jobs/${encodedJobId2} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0890 | PATCH | /api/v3/Jobs/${encodedJobId5} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0900 | PATCH | /api/v3/Jobs/${encodedJobId3} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0910 | PATCH | /api/v3/Jobs/${encodedJobId6} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0920 | PATCH | /api/v3/Jobs/${encodedJobId6} | unauthenticated | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0930 | PATCH | /api/v3/Jobs/${encodedJobId3} | unauthenticated | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 0940 | PATCH | /api/v3/Jobs/${encodedJobId2} | unauthenticated | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 0950 | PATCH | /api/v3/Jobs/${encodedJobIdUser1} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0960 | PATCH | /api/v3/Jobs/${encodedJobIdUser2} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0970 | PATCH | /api/v3/Jobs/${encodedJobIdUser3} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0980 | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 0990 | PATCH | /api/v3/Jobs/${encodedJobIdUser2} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1000 | PATCH | /api/v3/Jobs/${encodedJobIdUser4} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1010 | PATCH | /api/v3/Jobs/${encodedJobIdUser3} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1020 | PATCH | /api/v3/Jobs/${encodedJobIdUser5} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1030 | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1040 | PATCH | /api/v3/Jobs/${encodedJobIdUser4} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1050 | PATCH | /api/v3/Jobs/${encodedJobIdUser2} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1060 | PATCH | /api/v3/Jobs/${encodedJobIdUser5} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1070 | PATCH | /api/v3/Jobs/${encodedJobIdUser3} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1080 | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1090 | PATCH | /api/v3/Jobs/${encodedJobIdUser6} | unauthenticated | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1100 | PATCH | /api/v3/Jobs/${encodedJobIdGroup1} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1110 | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1120 | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1130 | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1140 | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1150 | PATCH | /api/v3/Jobs/${encodedJobIdGroup4} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1160 | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1170 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1180 | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1190 | PATCH | /api/v3/Jobs/${encodedJobIdGroup4} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1200 | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1210 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1220 | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1230 | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1240 | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | unauthenticated | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1250 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec1} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1260 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec2} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1270 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec3} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1280 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec6} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1290 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec2} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1300 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1310 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec3} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1320 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec5} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1330 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec6} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1340 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1350 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec2} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1360 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec5} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1370 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1380 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec6} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1390 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user5.2 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1400 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec2} | user5.2 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1410 | PATCH | /api/v3/Jobs/${encodedJobIdUserSpec4} | user5.2 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1420 | PATCH | /api/v3/Jobs/${encodedJobIdGroup1} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1430 | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1440 | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1450 | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | admin | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1460 | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1470 | PATCH | /api/v3/Jobs/${encodedJobIdGroup4} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1480 | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | user1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1490 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1500 | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | user1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1510 | PATCH | /api/v3/Jobs/${encodedJobIdGroup4} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1520 | PATCH | /api/v3/Jobs/${encodedJobIdGroup2} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1530 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user5.1 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1540 | PATCH | /api/v3/Jobs/${encodedJobIdGroup3} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1550 | PATCH | /api/v3/Jobs/${encodedJobIdGroup6} | user5.1 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1560 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user5.2 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1570 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user5.2 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1580 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user5.2 | 200 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.SuccessfulPatchStatusCode``` |
| 1590 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user3 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1600 | PATCH | /api/v3/Jobs/${encodedJobIdGroup5} | user3 | 403 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | ```TestData.AccessForbiddenStatusCode``` |
| 1610 | PATCH | /api/v3/Jobs/nonExistingJobId | admin | 400 | ```{ statusMessage: "update status of a job", statusCode: "job finished/blocked/etc" }``` | 400 | ```TestData.BadRequestStatusCode``` |
| 1620 | GET | /api/v3/Jobs | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1630 | GET | /api/v3/Jobs?createdBy=admin | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1640 | GET | /api/v3/Jobs?createdBy=user1 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1650 | GET | /api/v3/Jobs?createdBy=user5.1 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1660 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1670 | GET | /api/v3/Jobs?createdBy=anonymous | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1680 | GET | /api/v3/Jobs | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1690 | GET | /api/v3/Jobs?createdBy=admin | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1700 | GET | /api/v3/Jobs?createdBy=user1 | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1710 | GET | /api/v3/Jobs | user5.1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1720 | GET | /api/v3/Jobs?createdBy=admin | user5.1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1730 | GET | /api/v3/Jobs | user5.2 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1740 | GET | /api/v3/Jobs | unauthenticated | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1750 | GET | /api/v3/Jobs/${jobId1} | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1760 | GET | /api/v3/Jobs/${jobId1} | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1770 | GET | /api/v3/Jobs/${jobId1} | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1780 | GET | /api/v3/Jobs/${jobId1} | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1790 | GET | /api/v3/Jobs/${jobId1} | user1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1800 | GET | /api/v3/Jobs/${jobId1} | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1810 | GET | /api/v3/Jobs/${jobId1} | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1820 | GET | /api/v3/Jobs/${jobId1} | user1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1830 | GET | /api/v3/Jobs/${jobId1} | user1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1840 | GET | /api/v3/Jobs/${jobId1} | user5.1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1850 | GET | /api/v3/Jobs/${jobId1} | user5.1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1860 | GET | /api/v3/Jobs/${jobId1} | user5.1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1870 | GET | /api/v3/Jobs/${jobId1} | user5.1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1880 | GET | /api/v3/Jobs/${jobId1} | user5.1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1890 | GET | /api/v3/Jobs/${jobId1} | user5.1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1900 | GET | /api/v3/Jobs/${jobId1} | unauthenticated | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1910 | DELETE | /api/v3/Jobs/${jobId1} | archiveManager | 200 | ```null``` | ```TestData.SuccessfulDeleteStatusCode``` |
| 1920 | DELETE | /api/v3/Jobs/${jobId1} | admin | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1930 | DELETE | /api/v3/Jobs/${jobId1} | user1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1940 | DELETE | /api/v3/Jobs/${jobId1} | user5.1 | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 1950 | DELETE | /api/v3/Jobs/nonExistingJobId | archiveManager | 400 | ```null``` | 400 | ```TestData.BadRequestStatusCode``` |
| 1960 | GET | /api/v3/Jobs | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1970 | GET | /api/v3/Jobs?limit=5 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1980 | GET | /api/v3/Jobs?createdBy=admin | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 1990 | GET | /api/v3/Jobs?createdBy=user1 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2000 | GET | /api/v3/Jobs?createdBy=user5.1&limit=5 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2010 | GET | /api/v3/Jobs?createdBy=user5.2 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2020 | GET | /api/v3/Jobs?createdBy=anonymous | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2040 | GET | /api/v3/Jobs?createdBy=admin | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2050 | GET | /api/v3/Jobs?createdBy=user1 | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2060 | GET | /api/v3/Jobs | user5.1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2070 | GET | /api/v3/Jobs?createdBy=admin | user5.1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2080 | GET | /api/v3/Jobs | user5.2 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2090 | GET | /api/v3/Jobs | unauthenticated | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 2100 | GET | /api/v3/Jobs/facet | unauthenticated | 403 | ```null``` | ```TestData.AccessForbiddenStatusCode``` |
| 2110 | GET | /api/v3/Jobs/facet?createdBy=admin | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2120 | GET | /api/v3/Jobs/facet?createdBy=user1 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2130 | GET | /api/v3/Jobs/facet?createdBy=user5.1 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2140 | GET | /api/v3/Jobs/facet?createdBy=user5.2 | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2150 | GET | /api/v3/Jobs/facet?createdBy=anonymous | admin | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2160 | GET | /api/v3/Jobs/facet?createdBy=admin | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2170 | GET | /api/v3/Jobs/facet?createdBy=user1 | user1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2180 | GET | /api/v3/Jobs/facet | user5.1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2190 | GET | /api/v3/Jobs/facet?createdBy=admin | user5.1 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` |
| 2200 | GET | /api/v3/Jobs/facet | user5.2 | 200 | ```null``` | ```TestData.SuccessfulGetStatusCode``` | -->