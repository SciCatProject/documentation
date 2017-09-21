# An Introduction to the Data Model

When you have an instance of the data catalog running, the data model can be visualised at the following URLS:

* <CATAMEL_URL>/modeldiagram/ 
* <CATAMEL_URL>/explorer/
* <CATAMEL_URL>/visualize

## Explorer

The API explorer is a feature of Loopback and allows one to test various endpoints. This section outlines the core functionality. The first point to note is that requests require a token. You can use the `login` route under the `User` tab to obtain one of these, or use a CURL command.

### Main Screen

The top right entry field is where the token should be included. The token will define your access rights, so not all routes will be accessible. Each model has a tab which relates to its endpoint. Expanding the tab shows the routes section below.

![explorer](img/explorer.png)

### Routes

Each section outlines the routes for the chosen model. This is configurable but the HTTP verbs are supported here for most routes and conform to the standards. Error codes are also consistent. Expanding the chosen route allows one to test the response with sample data, or their own.


![routes](img/explorer_routes.png)

### Single Route

Selecting a route shows the expected JSON object and provides an editor to allow you to test the route. Response information is shown below.
Clicking the `data type` box will insert it into your request for easy testing.

![route](img/explorer_single_route.png)

### Model

The model view can be accessed by clicking the link next to `Example Value` and shows the fields that Loopback is expecting to receive, as well as their type and whether they are required.

![model](img/explorer_model.png)
