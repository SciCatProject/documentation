
# [Testing](https://angular.io/docs/ts/latest/guide/testing.html)

All components of SciCat include unit test coverage and catanie has additional end to end user interface testing. Tests are run by CI before any change request is approved.


# E2E ([Protractor](http://www.protractortest.org/#/))

Initially Protractor was used for end to end testing but this was abandoned in favour of the far more robust and flexible [Cypress](https://www.cypress.io/).

# Cypress E2E

Cypress is not based on Selenium. 

`npx cypress run` runs all tests headless (without displaying the browser).

`npx cypress open` opens the Cypress GUI in the browser.

`npx cypress run --spec /home/encima/dev/melanie/catanie/cypress/integration/policy-delegate.spec.js` will run the single test file policy-delegate.spec.js.

# Unit (Jasmine, run by Karma)

`ng test` runs all unit tests.


### Mocking Services

Create a mock service and implement only what you need

```
class MockUserApi {

  getCurrentId() {
    return 123;
  }
}
```

Now, set your testbed to override the service you are mocking.

```
TestBed.overrideComponent(AppComponent, {
    set: {
      providers: [
        { provide: UserApi, useClass: MockUserApi }
      ]
    }
```

The practice I have followed is to create a `MockStubs` file that contains only the necessary mocked methods for services or pipes or components. This file can be added to to allow almost complete coverage of the app.


# Anatomy of a Unit Test 

## BeforeEach

These are called to set up the test and involve 2 important methods.

### `configureTestingModule`

This should include imports for all the modules used in the component. If the component also includes other components, then they should be included. This is also true for any pipes that may be used in the template. I am not sure if there is a fix for this but that does mean that, if a subcomponent uses a pipe then it should be included in all the specs.

### `overrideComponent`

Test cases for a component should test as few things outside of the component as possible (services etc should have their own tests), but this causes problems for the services implemnted in each component. This is especially true for the loopback services, but also HTTP and Router. In the `overrideComponent` method, you can specify the service names and provide an alternative class to use.

For every service your component uses, there should be a `Mock` equivalent that provides hardcoded data in response to their calls. First, check the service exists in `MockStubs.ts` in the root of the `app` folder. If it is not in there, please implement it only in that file.  You do **not** need to implement every method, others can add to these when they are needed.

The format in the `spec` file should be as follows:
```
{ provide: RawDatasetApi, useClass: MockDatasetApi }
```

The default test merely tests the creation of a component. This is merely opinion but a component should not be considered complete on a branch until the initial tests pass. A release should not go live untilthe coverage of the tests covers more than just basic functionality, i.e. 80% coverage.


## State management/NGRX testing 


Tests of ngrx state management should test e.g. if a new state object is returned.

Sample ngrx reducer test:
```javascript
  describe('SelectDatasetAction', () => {
    it('should return the state', () => {
      const data:DatasetInterface = {owner: '', contactEmail: '', sourceFolder: '', creationTime: new Date(), type: '', ownerGroup: ''};
      const payload = new Dataset({pid: 'pid 1', ...data});
      const action = new fromActions.SelectDatasetAction(payload);
      const state = fromDatasets.datasetsReducer(initialDatasetState, action);
      expect(state.selectedSets2).toEqual([payload]);
      expect(state.selectedSets2.constructor).toBe(Array);
    });
  });
```
