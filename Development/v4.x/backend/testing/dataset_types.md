# 0200: Dataset Types

Dataset types tests that over all functionalities regarding creating, updating, deleting and retrieving datasets both raw and derived.  
They are the original datasets tests. _In the near future, they should be reviewed and updated or removed_.  

| Test Number | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Input | Results |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | GET | Datasets/count | admin | 201 | n/a | ```{ count: 0 }``` |
| 0020 | GET | Datasets/count | admin | 201 | ```{ "type" : "raw" }``` | ```{ count: 0 }``` |
| 0030 | GET | Datasets/count | admin | 201 | ```{ "type" : "derived" }``` | ```{ count: 0 }``` |
| ---- |
| 0040 | POST | Instruments | ingestor | 400 | ```TestData.InstrumentCorrect2``` | ```Error: duplicate entry``` |
| 0050 | POST | Instruments | ingestor | 400 | ```TestData.InstrumentWrong1``` | ```Validation Error``` |
| 0060 | POST | Instruments | user1 | 400 | ```TestData.InstrumentCorrect2``` | ```Unauthorized``` |
| 0070 | GET | Instruments/_instrumentId1_ | ingestor | 200 | n/a | ```TestData.InstrumentCorrect1``` |
| 0080 | GET | Instruments/_instrumentId2_ | ingestor | 200 | n/a | ```TestData.InstrumentCorrect2``` |
| 0090 | GET | Instruments | ingestor | 200 | n/a | ```TestData.InstrumentCorrect 1,2,3``` |
| 0100 | GET | Instruments | ingestor | 200 | ```{where: {customMetadata: { main_user: "ESS"}}}``` | ```TestData.InstrumentCorrect 1,2``` |
| 0110 | GET | Instruments/findOne | ingestor | 200 | n/a | ```TestData.InstrumentCorrect1``` |
| 0120 | GET | Instruments/findOne | ingestor | 200 | ```{where: {customMetadata: { main_user: "ESS"}}}``` | ```TestData.InstrumentCorrect 1``` |
| 0130 | GET | Instruments/findOne | ingestor | 200 | ```{where: {customMetadata: { main_user: { like : "somebody"}}}}``` | ```TestData.InstrumentCorrect 3``` |
| 0140 | GET | Instruments | user1 | 200 | n/a | ```TestData.InstrumentCorrect 1,2,3``` |
| 0150 | PATCH | Instruments/_instrumentId2_ | ingestor | 200 | ```{ name: newName }```  | ```TestData.InstrumentCorrect2 with name as newName``` |
| 0160 | GET | Instruments/_instrumentId2_ | ingestor | 200 | n/a  | ```TestData.InstrumentCorrect2 with name as newName``` |
| 0170 | GET | Instruments/ | ingestor | 200 | ```{where: {name: "newName"}}```  | ```TestData.InstrumentCorrect2 with name as newName``` |
| 0180 | DELETE | Instruments/_instrumentId1_ | ingestor | 400 | n/a  | n/a |
| 0190 | DELETE | Instruments/_instrumentId1_ | archiveManager | 200 | n/a  | n/a |
| 0200 | DELETE | Instruments/_instrumentId2_ | archiveManager | 200 | n/a  | n/a |
| 0210 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |
| 0220 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |
| 0230 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |
| 0240 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |
| 0250 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |
| 0260 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |
| 0270 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |
| 0280 | DELETE | Instruments/_instrumentId3_ | archiveManager | 200 | n/a  | n/a |


