# Catanie Environment file

This is the configuration file for the catanie client. The environment file allows the systems administrator to configure every aspect of the client including switching on/off almost all non essential features.

An example is shown below

```
catanie/src/environment:

import { TableColumn } from "state-management/models";

export const environment = {
  production: false,
  lbBaseURL: "http://127.0.0.1:3000",
  fileserverBaseURL: "http://127.0.0.1:8889",
  synapseBaseUrl: "https://scitest.esss.lu.se",
  riotBaseUrl: "http://scitest.esss.lu.se/riot",
  jupyterHubUrl: "https://jupyterhub.esss.lu.se/",
  externalAuthEndpoint: "",
  addDatasetEnabled: true,
  archiveWorkflowEnabled: true,
  columnSelectEnabled: true,
  datasetReduceEnabled: true,
  editMetadataEnabled: true,
  editSampleEnabled: true,
  editPublishedData: true,
  facility: "PSI",
  fileColorEnabled: true,
  localColumns: [
    { name: "select", order: 0, type: "standard", enabled: true },
    { name: "datasetName", order: 1, type: "standard", enabled: true },
    { name: "runNumber", order: 2, type: "standard", enabled: true },
    { name: "sourceFolder", order: 3, type: "standard", enabled: true },
    { name: "size", order: 4, type: "standard", enabled: true },
    { name: "creationTime", order: 5, type: "standard", enabled: true },
    { name: "type", order: 6, type: "standard", enabled: true },
    { name: "image", order: 7, type: "standard", enabled: true },
    { name: "metadata", order: 8, type: "standard", enabled: true },
    { name: "proposalId", order: 9, type: "standard", enabled: true },
    { name: "ownerGroup", order: 10, type: "standard", enabled: false },
    { name: "dataStatus", order: 11, type: "standard", enabled: false },
    { name: "derivedDatasetsNum", order: 12, type: "standard", enabled: false }
  ] as TableColumn[],
  landingPage: "doi2.psi.ch/detail/",
  logbookEnabled: true,
  metadataPreviewEnabled: true,
  fileDownloadEnabled: true,
  multipleDownloadEnabled: true,
  maxDirectDownloadSize: 5000000000000,
  multipleDownloadAction: "http://localhost:3011/zip",
  scienceSearchEnabled: true,
  scienceSearchUnitsEnabled: true,
  searchProposals: true,
  searchPublicDataEnabled: true,
  searchSamples: true,
  sftpHost: "login.esss.dk",
  shoppingCartEnabled: true,
  shoppingCartOnHeader: true,
  tableSciDataEnabled: true,
  userNamePromptEnabled: true,
  userProfileImageEnabled: true
};

```


# Catamel Configuration

The following 4 files provide the minimum confifuration for catamel.

catamel/server:
* datasources.json - This sets up your connection to Mongo and should follow the syntax outlined in loopback
* config.local.js - These are site specific settings for your install, such as the prefix to use for IDs
* providers.json - Contains connection information to LDAP or other authentication sources
* component-config.json - This file defines the connection to RabbitMQ or other message que
