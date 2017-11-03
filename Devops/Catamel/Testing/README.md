# Testing

## Packages

* [Chai](https://github.com/chaijs/chai) - Assertion
* [Supertest](https://github.com/visionmedia/supertest) - NodeJS testing for HTTP calls
* [Mocha](https://github.com/mochajs/mocha) - Test runner framework

## Running

`npm run test`

or 

`mocha --timeout=5000 --reporter=nyan`

## Tests

Some tests to cover the Users API and the RawDataset API have been written but more are needed. There is a LoginUtils file that supports the retrieval of tokens and everything else is documented in the Swagger file

## Environment

If this is being run independently of an infrastructure then you should provide the `NODE_ENV` to be `test`.