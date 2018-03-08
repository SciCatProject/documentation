## CI

The primary repositories for the SciCat code is hosted at `gitlab.psi.ch`. However, these repositories are also mirrored to [https://github.com/scicatproject. ](https://github.com/scicatproject)

NOTE: \*NEVER\* push to the Github repos, your remote should \*always\* be the Gitlab repository.

## Travis \(Github\)

Travis CI is a build system available to Github repositories and provides email feedback \(among other options\). It has been enabled for Catanie and the details of the build can be seen in `.travis-ci.yml` in the root of the repository.

## Jenkins

Jenkins is running inside the Kubernetes cluster and uses dynamic pod provisioning for builds; this means that there are no Jenkins slaves constantly available.

There are currently 2 main build jobs:

1. Catanie-GL
2. Catamel-GL

Each of these jobs is triggered every evening at 8pm and can also be triggered by a webhook.

#### Git hooks





