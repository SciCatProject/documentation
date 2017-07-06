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

For kubernetes, you will need the `kubectl` binary., which can be found [here.](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Locally with Minikube

TODO

## On a cluster

TODO

