# SciCat Frontend Configuration file

This is the configuration file for the frontend client. The configuration file allows the systems administrator to configure every aspect of the client including switching on/off almost all non essential features. The configuration file can either be served from the backend, via the `/client/config.json` endpoint or mounted into `/usr/share/nginx/html/assets/config.json`.

An example is shown below

```
frontend/src/assets/config.json:

{
  "accessTokenPrefix": "",  // Set the backend token prefix. Should be empty string for current backend or "Bearer " if using scicat-backend-next.
  "addDatasetEnabled": true,  // Show/hide the "Create Dataset" button in the Datasets Dashboard.
  "archiveWorkflowEnabled": true,  // Enable/disable the archive/retrieve workflow.
  "datasetReduceEnabled": true,  // Enable/disable the automatic Dataset reduction/analysis workflow.
  "editDatasetSampleEnabled": true,  // Enable/disable editing of which Sample a Dataset belongs to.
  "editMetadataEnabled": true,  // Enable/disable editing of Scientific Metadata.
  "editPublishedData": true,  // Enable/disable editing of Published Data.
  "editSampleEnabled": true,  // Enable/disable editing of Samples.
  "externalAuthEndpoint": "/auth/msad",  // Endpoint used for third party authentication, e.g, LDAP.
  "facility": "ESS",  // Facility running the SciCat instance.
  "fileColorEnabled": true,  // Enable/disable file size color representation in the Datasets Dashboard.
  "fileDownloadEnabled": true,  // Enable/disable download workflow for Dataset datafiles.
  "gettingStarted": null,  // URL to Getting Started guide for SciCat, displayed on the Help page.
  "ingestManual": null,  // URL to Ingest Manual for SciCat, displayed on the Help page.
  "jobsEnabled": true,  // Enable/disable Job workflow.
  "jsonMetadataEnabled": true,  // Show/hide the "Show Metadata" button on the details pages, allowing users to see the JSON represantion of the current document.
  "jupyterHubUrl": "https://jupyterhub.esss.lu.se/",  // URL to Jupyter Hub instance used for data analysis.
  "landingPage": "doi2.psi.ch/detail/",  // URL to the facility's Landing Page for Published Data.
  "lbBaseURL": "http://127.0.0.1:3000",  // URL to the SciCat Backend.
  "localColumns": [                      // Default columns to be displayed in the table on the Datasets Dashboard.
    {
      "name": "select",
      "order": 0,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "datasetName",
      "order": 1,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "runNumber",
      "order": 2,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "sourceFolder",
      "order": 3,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "size",
      "order": 4,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "creationTime",
      "order": 5,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "type",
      "order": 6,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "image",
      "order": 7,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "metadata",
      "order": 8,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "proposalId",
      "order": 9,
      "type": "standard",
      "enabled": true
    },
    {
      "name": "ownerGroup",
      "order": 10,
      "type": "standard",
      "enabled": false
    },
    {
      "name": "dataStatus",
      "order": 11,
      "type": "standard",
      "enabled": false
    }
  ],
  "logbookEnabled": true,  // Enable/disable SciChat Logbook integration.
  "loginFormEnabled": true,  // Enable/disable the local Login form. Should be disabled if using oAuth2 for authentication.
  "maxDirectDownloadSize": 5000000000,  // Set a maximum allowed file size for downloading datafiles over HTTP.
  "metadataPreviewEnabled": true,  // Enable/disable Scientific Metadata preview on the Datasets Dashboard.
  "metadataStructure": "tree", // Allow tree structure for Scientific Metadata. Set to empty string for flat structure.
  "multipleDownloadAction": "http://localhost:3012/zip",  // URL to service handling direct download of datafiles.
  "multipleDownloadEnabled": true,  // Enable/disable ability to download multiple datafiles.
  "oAuth2Endpoints": [],  // List of endpoints used for oAuth2 authentication.
  "policiesEnabled": true,  // Enable/disable Dataset Policies workflow.
  "retrieveDestinations": [],  // List of destinations for Dataset retrievals.
  "riotBaseUrl": "http://scitest.esss.lu.se/riot",  // URL to SciChat client.
  "scienceSearchEnabled": true,  // Enable/disable filtering documents on Scientific Metadata.
  "scienceSearchUnitsEnabled": true,  // Enable/disable filtering documents on Scientific Metadata using units.
  "searchPublicDataEnabled": true,  // Enable/disable filtering Datasets on public or non-public data.
  "searchSamples": true,  // Enable/disable searching Samples on Samples Dashboard.
  "sftpHost": "login.esss.dk",  // URL to SFTP service used for downloading files exceeding maximum allowed file size.
  "shareEnabled": true,  // Enable/disable workflow for sharing Datasets with other users using their email address.
  "shoppingCartEnabled": true,  // Enable/disable the Dataset cart used for bulk actions.
  "shoppingCartOnHeader": true,  // Toggle Dataset cart placement, either on header or to the left on the Datasets Dashboard.
  "tableSciDataEnabled": true  // Enable/disable Scientific Metadata table view on details pages. If disabled, Scientific Metadata is displayed as raw JSON.
}

```


