# Testing

## Packages
Following is the list of hte main packages used to build, run and manage testing for the project

* [Chai](https://github.com/chaijs/chai) - Assertion
* [Supertest](https://github.com/visionmedia/supertest) - NodeJS testing for HTTP calls
* [Mocha](https://github.com/mochajs/mocha) - Test runner framework

## API tests

SciCat backend v4.x comes with many API tests. They are locate under the `/test` folder in the backend repository

In order to run the tests you need to have the backend running with an accessible mongodb instance.
The backend can be run from terminl with the command:

`npm run dev`

In a different terminal, you can run all the following tests:
- unit tests:   
  `npm run test`
- linting tests:  
  `npm run lint`
- api tests based on mocha
  `npm run test:api:mocha`

If you would like to run the mocha tests directly, you can use the following command: 

`mocha --config ./test/config/.mocharc.json --timeout=5000 --reporter=nyan`

If you are interested in a specific subset of API tests, you can add the _--grep_ option to the mocha command.  
For example if you are interested in running only the test named _Authorization functionalities_, you can use the following command:  
`mocha --config ./test/config/.mocharc.json --grep \"Authorization functionalities\ --timeout=5000 --reporter=nyan`

## Coverage

The following is the list of the current tests groups. We are trying to cover all the different components and endpoints of SciCat backend v4.x and we keep adding new tests every release cycle.
The coverage might not be complete. If you find any use case  that is not covered by our tests, feel free to open an issue or, even better, to write a new set of tests and submit a PR.

**List of tests:**  
  
| test file | main code | title | description |  
| ----- | ----- | ----- | ----- |  
| Auth.js | 0100 | Authorization functionalities | Test login and logout for functional accounts |  
| CheckDifferentDatasetTypes.js | 0200 | Check Different Dataset Types | Check different dataset types and their inheritance |   
| DatasetAuthorization.js | 0300 | Test access to dataset | Test different use cases with different user and restricted access |  
| DatasetFilter.js | 0400 | Test retrieving datasets using filtering capabilities | Leverage fullquery endpoint to retrieve different group of datasets  |  
| DatasetLifecycle.js | 0500 | Test facet and filter queries |  |  
| DatasetTypes.js | 0550 |  |  |  
| DerivedDatasetDatablock.js | 0600 |  |  |  
| DerivedDataset.js | 0700 | Derived Datasets | test derived datasets functionalities |  
| DerivedDatasetOrigDatablock.js | 0800 | DerivedDatasetOrigDatablock | Test OrigDatablocks and their relation to derived Datasets |  
| Instrument.js | 0900 | Instrument | instrument management, creation, update, deletion and search |  
| InstrumentsFilter.js | 1000 | Test retrieving instruments using filtering capabilities  |  |  
| Jobs.js | 1100 | Test New Job Model | Test authorization and CRUD operations for jobs |  
| OrigDatablockForRawDataset | 1200 | Test OrigDatablocks and their relation to raw Datasets using origdatablocks endpoint | |
| Policy.js | 1300 | Simple Policy tests |  |  
| ProposalAuthorization.js | 1400 | Test access to proposal |  |  
| Proposal.js | 1500 | Simple Proposal |  |  
| PublishedData.js | 1600 | Test of access to published data |  |  
| RandomizedDatasetPermissions.js | 1700 | permission test with bigger amount of data |  |  
| RawDatasetDatablock.js | 1800 | Test Datablocks and their relation to raw Datasets |  |  
| RawDataset.js | 1900 | Raw Datasets |  |  
| RawDatasetOrigDatablock.js | 2000 | Test OrigDatablocks and their relation to raw Datasets |  |  
| ResetDataset.js | 2100 | Create Dataset and its Datablocks, then reset Datablocks and embedded Datasetlifecycle status |  |  
| Sample.js | 2200 | Simple Sample | Samples functionality tests, like create, update and delete |  
| SampleAuthorization.js | 2250 | Sample Authorization | Test authorization for all samples operations |  
| UserAuthorization.js | 2300 | User Authorization | test that user authorization are correct |  
| Users.js | 2400 | Login with functional accounts |  |  

## Test data

It is our intention to save all test data in the file `TestData.js`.  
In some cases, we need to code variation of the data directly in the test file.

## Functional and Test accounts

All tests are performed assuming the following user accounts, groups and configuration are present.
Users and groups can be defined in the configuration structure defined in ```src/config/configuration.ts```, although the preferred method for configuring functional/tests accounts is through the `functional_accounts.json` file present in the following folder ``
These settings are meant only for testing and to demonstrate the capabilities of backend V4.x. IT is highly recommended to remove accounts that are not needed and change passwords and group affiliations as needed.

### Default Accounts
The following table lists the accounts that are provided by default in a vanilla installation.
Please make sure to change them, update their password or remove them entirely in your production environment.

| Account | Groups | Admin Group | Delete Group | Create Dataset w/o pid | Create Dataset w/ pid | Create Dataset Privileged | Create Job | Update Job | Delete Job |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| admin | admin, global | yes | no | Any |  |  | Any | Any | no |
| ingestor | ingestor | yes | no | Any |  |  | Any | Any | no |
| archiveManager | archivemanager | yes | yes | no |  |  | Any | Any | Any |
| proposalIngestor | proposalingestor | no | no | no |  |  | no | no | no |
| user 1 | group1 | no | no | Own |  |  | Own | Own | no |
| user 2 | group2 | no | no | Own |  |  | Own | Own | no |
| user 3 | group3 | no | no | Own |  |  | Own | Own | no |
| user 4 | group4 | no | no | no |  |  | no | no | no |

### Group permissions
| Environmental variable | List of groups |
| ----- | ----- | 
| ADMIN_GROUPS | admin, ingestor, archivemanager |
| DELETE_GROUPS | archivemanager |
| CREATE_DATASET_GROUPS | group1, group2, group3 |


## Test Details

This section provides details on how all the tests files listed above are organized. Each subsection, provides a list of the test included in each file and the details of each one of them.

- [Dataset Types](./testing/dataset_types.md) 
- [Dataset Authorization](./testing/dataset_authorization.md) 
- [Instrument](./testing/instrument.md)
- [Jobs](./testing/jobs.md)
- [Sample Authorization](./testing/sample_authorization.md)
- [User Authorization](./testing/user_authorization.md)
