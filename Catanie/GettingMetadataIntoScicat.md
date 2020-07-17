
# Getting Metadata Into SciCat.




## Manual ingestion

The following steps will add a dataset to you system using the API with the linux program curl. Windows users will need an alternative method.

1.
Login to catamel. The default password for the inestor user is aman. Runnign the command below in the terminal will yeild an access token.

 curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"username":"ingestor", "password":"<your_password>"}' 'http://localhost:3000/api/v3/Users/login'

2. 
Create a json file with the contents below and name it data

```
{
  "owner": "string",
  "ownerEmail": "string",
  "orcidOfOwner": "string",
  "contactEmail": "string",
  "sourceFolder": "string",
  "sourceFolderHost": "string",
  "size": 0,
  "packedSize": 0,
  "numberOfFiles": 0,
  "numberOfFilesArchived": 0,
  "creationTime": "2020-07-17T09:12:59.775Z",
  "type": "string",
  "validationStatus": "string",
  "keywords": [
    "string"
  ],
  "description": "string",
  "datasetName": "string",
  "classification": "string",
  "license": "string",
  "version": "string",
  "isPublished": true,
  "ownerGroup": "string",
  "accessGroups": [
    "string"
  ],
  "datasetlifecycle": {
    "archivable": false,
    "retrievable": false,
    "publishable": false,
    "dateOfDiskPurging": "2020-07-17T09:12:59.776Z",
    "archiveRetentionTime": "2020-07-17T09:12:59.776Z",
    "dateOfPublishing": "2020-07-17T09:12:59.776Z",
    "isOnCentralDisk": true,
    "archiveReturnMessage": {},
    "retrieveReturnMessage": {},
    "exportedTo": "string",
    "retrieveIntegrityCheck": true

  },
  "history": [
    {
      "id": "string"
    }
  ]
}
```

3. 
cat the data file and pipe it to a curl command. Insert your access token in the command below and run it in the terminal:

cat data | curl -X POST --header 'Content-Type: application/json'  --header 'Accept: application/json'  -d @-  'http://localhost:3000/api/v3/Datasets?access_token=YOUR_TOKEN_HERE'


```

