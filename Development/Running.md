# Running locally


```
git clone https://github.com/SciCatProject/catamel.git 
cd catamel
npm install
npm start
```

```
git clone https://github.com/SciCatProject/frontend.git 
cd frontend
npm install
npx ng serve
```

For convenience, this has been added to the `package.json` so you can run `npm start` as an alias.

Access [here](http://localhost:4200) once running.

# Running with Docker

The containers in our repos are based on alpine linux to ensure a minimal size with almost nothing but the required packages. Most standard \*nix commands are available.

The recommend way is to use [scicatlive](https://github.com/SciCatProject/scicatlive#readme) . This does all for you automatically.

If you want to do things manually instead:

`git clone https://github.com/SciCatProject/frontend.git && cd frontend`

`docker build -t <tag> .`

`docker run <tag>`

You should see the container begin and print out the URL, this is retrieved dynamically based on the IP of the container. Changing it to localhost or 0.0.0.0 **will** break it.

# Running with Kubernetes

Creating a Kubernetes environment takes some expertise but the SciCat repo [localdeploy](https://github.com/SciCatProject/localdeploy) contains all the necessary configuration for deploying SciCat to a cluster with a simple readme.
