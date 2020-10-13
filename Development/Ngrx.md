# State Management in Angular

Almost all external requests made by the client (catanie) are done so via `NGRX effects` within the state management components.

Loopback within catamel provies a generated SDK that is used by catanie to define all requests to the API. The SDK folder should not be edited because it will just overwrite it when a new one is generated.

The SDK is updated by running the following in the catamel source code root:
`./node_modules/.bin/lb-sdk server/server.js  ../catanie/src/app/shared/sdk`
and this is necessary when making any changes to endpoints in catamel.

[NGRX](https://ngrx.io/) is Redux for Angular and is heavily used in the client to manage state.


