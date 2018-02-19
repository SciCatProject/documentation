## So, you have just started working on SciCat?

This page provides a brief introduction to the overall workings of the SciCat data model, how things connect and links to more details on each component.

### Catamel

First off, the backend is the key component here and you will see there is next to hand written code here \(aside from some tests\). The folder you will be working in most is: `common/models` and this is NodeJS application based on the Loopback framework. Go away and read the docs for Loopback \(3\) and come back here when you are fairly comfortable. I'll wait.

Got it? Good. OK, so, SciCat stores all of its data in a MongoDB but you will almost never need to perform any admin on the database. The connection between loopback and Mongo is handled by the loopback-mongo-connector. The only thing you need to provide is the file in `server/datasources.json` , this provides the connection string and any connection specific info.

