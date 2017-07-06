# Running locally

`git clone git@gitlab.psi.ch:MELANIE/catanie.git && cd catanie`

`npm install`

Note: Now that Angular cli has reached V1, it has been recommended to keep the module local to each project. This means that you will need to access it here:

`./node_modules/@angular/cli/bin/ng serve`

For convenience, this has been added to the `package.json` so you can run `npm start` as an alias.

Access [here](http://localhost:4200) once running.

# Running with Docker

The container is based on alpine linux to ensure a minimal size with almost nothing but the required packages. Most standard \*nix commands are available.

`git clone git@gitlab.psi.ch:MELANIE/catanie.git && cd catanie`

`docker built -t <tag> .`

`docker run <tag>`

You should see the container begin and print out the URL, this is retrieved dynamically based on the IP of the container. Changing it to localhost or 0.0.0.0 **will** break it.

# Running with Kubernetes

For kubernetes, you will need the `kubectl` binary., which can be found [here.](https://kubernetes.io/docs/tasks/tools/install-kubectl/) The configuration for the binary should be found in the `secrets` repo for your organisation and you will need to export it as `KUBECONFIG`, you can check this with `kubectl version` and ensure both client and server have versions.

The docker image for Angular can either contain the Angular CLI development server, or an Nginx server that serves static files built by webpack.

Using the default nginx docker image means that all URLs are not mapped, this means one needs to provide a custom config file:

```
server {
    listen 80;
    root /usr/share/html;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

1. Build the dist with `ng build -prod -op dist/prod`
2. `sudo docker build -t registry.psi.ch:5000/egli/catanie:$CATANIE_IMAGE_VERSION .`
3. `sudo docker push registry.psi.ch:5000/egli/catanie:$CATANIE_IMAGE_VERSION`





## Locally with Minikube

TODO

## On a cluster

TODO

