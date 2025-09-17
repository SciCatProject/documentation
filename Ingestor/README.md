# Ingesting Data into SciCat

## Using pyscicat (recommended)
Pyscicat is python client for working with the SciCat API, which provides an easy mechanism to ingest data. See  https://www.scicatproject.org/pyscicat/howto/ingest.html to get started. 

For an example of the full workflow, please see the `pyscicat.ipynb` Jupyter notebook in SciCat live: https://github.com/SciCatProject/scicatlive/blob/main/services/jupyter/config/notebooks/pyscicat.ipynb. This includes how to authenticate, create a dataset, add datablocks and upload an attachment.

## Manual ingestion

The following steps will add a dataset to your system using the API with the Linux program curl.

1.
Login to the backend. The default password for the ingestor user is aman. Running the command below in the terminal will yield an access token.

```
 curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"username":"ingestor", "password":"<your_password>"}' 'http://localhost:3000/api/v3/Users/login'
 ```

2.
Create a json file with the contents below and name it metadata.json
```
{
    "creationLocation": "/PSI/SLS/TOMCAT",
    "sourceFolder": "/scratch/devops",
    "type": "raw",
    "ownerGroup":"p16623"
}
```

3.
cat the metadata.json file and pipe it to a curl command. Insert your access token in the command below and run it in the terminal:

```
cat metadata.json | curl -X POST --header 'Content-Type: application/json'  --header 'Accept: application/json'  -d @-  'http://localhost:3000/api/v3/Datasets?access_token=YOUR_TOKEN_HERE'
```

There should now be a dataset in your mongoDB instance.



# Site Specific Examples

For site specific examples see the following links:
* [ESS](IngesManual_ESS.md)
* [PSI](ingestManual.md)


#