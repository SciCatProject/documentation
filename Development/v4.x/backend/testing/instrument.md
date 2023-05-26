# Instrument

Instrument test that the functionalities for creating, updating, deleting and retrieving instruments are working correctly

| Test Number | HTTP Method | Endpoint | Authenticated User | Expected Request Status | Input | Results |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0010 | POST | Instruments | ingestor | 201 | ```TestData.InstrumentCorrect1``` | ```TestData.InstrumentCorrect1``` |
| 0020 | POST | Instruments | ingestor | 201 | ```TestData.InstrumentCorrect2``` | ```TestData.InstrumentCorrect2``` |
| 0030 | POST | Instruments | ingestor | 201 | ```TestData.InstrumentCorrect3``` | ```TestData.InstrumentCorrect3``` |
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


