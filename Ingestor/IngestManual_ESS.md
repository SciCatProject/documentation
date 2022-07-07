# Ingest Instructions ESS

![Kafka flow](screenshots/kafka.png)

As shown in the picture above the detector and the data collection software is writing into kafka topics. The topics is then being read by a filewriter that in turn writes the dataset to storage and sends back an event when the file is written that contains metadata about the file and the experiment. There is then an ingestion program that will parse the event from the filewriter and gather additional information before triggering REST calls into the backend. 

### How the ingestion program works:

#### 1. Parse Event

The ingestor is subscribing to a topic in Kafka where the filewriter creates an event when a file has been written. This event contains information about location, proposal id and metadata that exist on the file in the form of nexus data. 

#### 2. Login  

 Login and get a access token that can be used for interfacing with the backend. We advise to create a special ingestor account to be used when doing automatic ingestion. 

#### 3. Gather more metadata

The ingestor contacts the User Office and get's additional information regarding the experiment, the principal investigator and the sample.

#### 4. Create dataset

![dataset](screenshots/dataset.png)

Using the information from the filewriter event with the additional information gathered from the user office a dataset request can be constructed and sent to the backend.

#### 5. Create OrigDatablocks

![datablock](screenshots/datablock.png)

After a dataset has been created we attach the files that relate, this is done by creating datablocks that attaches to the dataset

#### 6. Create Sample

![sample](screenshots/sample.png)

If sample information is available a sample record can be created and attached to the dataset. This is an important step as it makes the data available to a wider audience of people. 
