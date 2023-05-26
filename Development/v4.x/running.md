# Run SciCat

There are multiple ways to run SciCat, which are listed and described below.

## Run locally

### Backend

To run the backend successfully, you need to have a mongodb instance accessible.
First we need to get the latest code available from the repo

```
git clone https://github.com/SciCatProject/backend.git 
cd backend
npm install
```

Before you csan run the backend successfully, you need to configure it.
Please refer to the configuration page for more details.
Once the configuration is set, you can start the backend with the command:

```
npm start
```

The backend api will be accessible at the addess `http://localhost:3000`

### Frontend
Same as the backend, we need to get the code from the repo:

```
git clone https://github.com/SciCatProject/frontend.git 
cd frontend
npm install
```

Make sure that you have the proper configuration and than you are ready to start the UI with the command:
```
npx ng serve
```
For convenience, this command has been added to the `package.json` so you can run `npm start` as an alias.

The frontend application can be accessed at the URL http://localhost:4200.


## Running with Docker

The recommend way is to use [scicatlive](https://github.com/SciCatProject/scicatlive#readme), althought it is not completely up-to-date.  
SciCatLive provides an all-in-one bundle containing all the necessary pieces to run an instance of SciCat successfully.

If you would like to run the latest versions, or a specific version of backend and frontend, you can find the images ready at the following URLs:
- Backend: https://github.com/SciCatProject/frontend/pkgs/container/frontend
- Frontend: https://github.com/SciCatProject/scicat-backend-next/pkgs/container/backend-next


# Running with Kubernetes

Creating a Kubernetes environment takes some expertise. There is an effort in the community to provide examples and use cases on how to run SciCat on Kubernetes. Stay tuned and check back soon.
