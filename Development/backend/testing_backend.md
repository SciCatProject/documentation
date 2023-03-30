# Testing

## Packages

* [Chai](https://github.com/chaijs/chai) - Assertion
* [Supertest](https://github.com/visionmedia/supertest) - NodeJS testing for HTTP calls
* [Mocha](https://github.com/mochajs/mocha) - Test runner framework

## API tests

SciCat backend v4.x comes with many API tests. They are locate in the `/test` folder

In order to run the tests you need to have the backend running.  
In a different terminal, you can run one of the following two commands:

`npm run test`

or 

`mocha --config ./test/config/.mocharc.json --timeout=5000 --reporter=nyan`

If you are interested in a specific subset of tests, you can add the _--grep_ option to the mocha command.  
For example if you are interested in running only the test named _Authorization functionalities_, you can use the following command:  
`mocha --config ./test/config/.mocharc.json --grep \"Authorization functionalities\ --timeout=5000 --reporter=nyan`

## Coverage

The following is the list of the current tests groups. We are trying to cover all the different components and endpoints of SciCat backend v4.x and we keep adding new tests every release cycle.
The coverage might not be complete. If you find any use case  that is not covered by our tests, feel free to open an issue or, even better, to write a new set of tests and submit a PR.

List of tests:
- Auth.js
- CheckDifferentDatasetTypes.js
- DatasetAuthorization.js
- DatasetFilter.js
- DatasetLifecycle.js
- DerivedDatasetDatablock.js
- DerivedDataset.js
- DerivedDatasetOrigDatablock.js
- Instrument.js
- InstrumentsFilter.js
- jest-e2e-tests
- Jobs.js
- LoginUtils.js
- Policy.js
- ProposalAuthorization.js
- Proposal.js
- PublishedData.js
- RandomizedDatasetPermissions.js
- RawDatasetDatablock.js
- RawDataset.js
- RawDatasetOrigDatablock.js
- ResetDataset.js
- Sample.js
- UserAuthorization.js
- Users.js

We are trying to save all the test data in the file `TestData.js`.  
In some cases, we need to code variation of the data directly in the test file.

## Test Details

### Datasets

### User Authorization
