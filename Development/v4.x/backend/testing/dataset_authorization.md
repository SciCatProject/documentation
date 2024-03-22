# 0300: Dataset Authorization

Dataset Authorization tests that authorization is correctly set for all the dataset endpoints for all the different type of users.  

| Test Number | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Input | Results |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | POST | Datasets | ingestor | 200 | ```test public dataset 1``` | ```test dataset 1 with scicat pid``` |
| 0020 | POST | Datasets | ingestor | 200 | ```test private dataset 2``` | ```test dataset 2 with scicat pid``` |
| 0030 | POST | Datasets | ingestor | 200 | ```test private dataset 3``` | ```test dataset 3 with scicat pid``` |
| 0040 | POST | Datasets/_PidDataset1_/origdatablocks | ingestor | 201 | ```TestData.OrigDatablockCorrect1``` | ```OrigDatablock 1 with SciCat id``` |
| 0050 | POST | Datasets/_PidDataset1_/datablocks | ingestor | 201 | ```TestData.DatablockCorrect1``` | ```Datablock 1 with SciCat id``` |
| 0060 | POST | Datasets/_PidDataset1_/attachements | ingestor | 201 | ```TestData.AttachementCorrect``` | ```Attachment 1 with SciCat id``` |
| 0070 | GET | Datasets | _anonymous_ | 200 | n/a | ```dataset 1``` |
| 0080 | GET | Datasets/_PidDataset1_ | _anonymous_ | 200 | n/a | ```dataset 1``` |
| 0090 | GET | Datasets/_PidDataset2_ | _anonymous_ | 403 | n/a | ```Error 403, not authorized``` |
| 0100 | GET | Datasets | ingestor | 200 | n/a | ```datasets 1,2,3``` |
| 0110 | GET | Datasets/count | ingestor | 200 | n/a | ```{ count: 3 }``` |
| 0120 | GET | Datasets/_PidDataset1_ | ingestor | 200 | n/a | ```dataset 1``` |
| 0130 | GET | Datasets/fullquery | ingestor | 200 | n/a | ```dataset 1,2,3``` |
| 0140 | GET | Datasets/_PidDataset2_ | ingestor | 200 | n/a | ```dataset 2``` |
| 0150 | GET | Datasets/_PidDataset3_ | ingestor | 200 | n/a | ```dataset 3``` |
| 0160 | GET | Datasets | user1 | 200 | n/a  | ```dataset 1, 2``` |
| 0170 | GET | Datasets/count | user1 | 200 | n/a  | ```{ count: 2 }``` |
| 0180 | GET | Datasets/_PidDataset1_ | user1 | 200 | n/a  | ```dataset 1``` |
| 0190 | GET | Datasets/_PidDataset2_ | user1 | 200 | n/a  | ```dataset 2``` |
| 0200 | GET | Datasets/_PidDataset3_ | user1 | 200 | n/a  | ```Error 403``` |
| 0210 | GET | Datasets/fullquery | user1 | 200 | n/a  | ```dataset 1,2``` |
| 0220 | GET | Datasets | user2 | 200 | n/a  | ```dataset 1,3``` |
| 0230 | GET | Datasets/count | user2 | 200 | n/a  | ```{ count: 2 }``` |
| 0240 | GET | Datasets/_PidDataset1_ | user2 | 200 | n/a  | ```dataset 1``` |
| 0250 | GET | Datasets/_PidDataset2_ | user2 | 403 | n/a  | ```Error 403, not authorized``` |
| 0260 | GET | Datasets/_PidDataset3_ | user2 | 200 | n/a  | ```dataset 3``` |
| 0270 | GET | Datasets/fullquery | user2 | 200 | n/a  | ```dataset 1,3``` |
| 0280 | GET | Datasets | user3 | 200 | n/a  | ```dataset 1,2,3``` |
| 0290 | GET | Datasets/count | user3 | 200 | n/a  | ```{ count: 3 }``` |
| 0300 | GET | Datasets/_PidDataset1_ | user3 | 200 | n/a  | ```dataset 1``` |
| 0310 | GET | Datasets/_PidDataset2_ | user3 | 200 | n/a  | ```dataset 2``` |
| 0320 | GET | Datasets/_PidDataset3_ | user3 | 200 | n/a  | ```dataset 3``` |
| 0330 | GET | Datasets/fullquery | user3 | 200 | n/a  | ```dataset 1,2,3``` |
| 0340 | POST | Datasets/_PidDataset2_ | ingestor | 200 | ```{ isPublished: true }``` | ```public dataset 2``` |
| 0350 | GET | Datasets/fullquery | user2 | 200 | ```{ fields: { isPublished: true}}``` | ```dataset 1,2``` |
| 0360 | GET | Datasets/fullfacet | user2 | 200 | ```{ fields: { isPublished: true}}``` | ```{ totalSets: 2 }``` |
| 0370 | GET | Datasets/_PidDataset1_/origdatablocks | user3 | 200 | n/a | ```1 origdatablock dataset 1``` |
| 0380 | GET | Datasets/_PidDataset1_/datablocks | user3 | 200 | n/a | ```1 datablock dataset 1``` |
| 0390 | GET | Datasets/_PidDataset1_/attachments | user3 | 200 | n/a | ```1 attachment dataset 1``` |
| 0400 | GET | Datasets/_PidDataset1_/thumbnail | user3 | 200 | n/a | ```thumbnail dataset 1``` |
| 0410 | DELETE | Datasets/_PidDataset1_/attachment | archiveManager | 200 | n/a | n/a |
| 0420 | DELETE | Datasets/_PidDataset1_/origdatablock | archiveManager | 200 | n/a | n/a |
| 0430 | DELETE | Datasets/_PidDataset3_/datablock | archiveManager | 200 | n/a | n/a |
| 0440 | DELETE | Datasets/_PidDataset1_ | archiveManager | 200 | n/a | n/a |
| 0450 | DELETE | Datasets/_PidDataset2_ | archiveManager | 200 | n/a | n/a |
| 0460 | DELETE | Datasets/_PidDataset3_ | archiveManager | 200 | n/a | n/a |

