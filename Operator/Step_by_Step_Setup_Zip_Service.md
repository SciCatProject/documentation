# Step by Step manual to Setup the Zip Service

## Setup Zip Service

The zip service repository can be found [here](https://github.com/SciCatProject/zip-service).
To install it, you first have to add a configuration file (local.config.json) to the source directory. A sample for this file can be found in CI/ESS or in the description of the repository.
Then build the image and run it.


### JWT

In order for SciCat to authenticate against the zip service, the jwt secret has to be configured the same in both services. The jwt secret for the zip service can be configured in the file local.config.json. The configuration file containing the jwt secret for the SciCat backend can be found under the catamel filepath:
/home/node/app/server/config.json


### Volumes

The data volumes have to be mounted to the zip service in order for it to access the files, zip them and offer them for download. The filepath, stored in the OriginalDatablock and Datafile objects, have to match a valid path on the zip service.
