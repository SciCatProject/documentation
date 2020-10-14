# Documentation

## Overview
The documentation consists of two main parts.

* The "Home Webgpage" of the project , describing the purpose and use cases for the software. The source is located at https://github.com/SciCatProject/scicatproject.github.io 
* The documentation proper, split into User,Operator,Ingestor and Developer manual. The source is located at https://github.com/SciCatProject/documentation .  It covers all components of the software, i.e  frontend and backend. The documentation tool [honkit](https://honkit.netlify.app/) (successor of gitbook) is used.

Both documentation parts are hosted on the [GitHub Pages platform](https://pages.github.com/). The documentation part is "injected" into the GitHub pages automatically by a travis job, which runs after each commit to the documentation repository

The live web site is then visible on the following URLs respectively
* https://scicatproject.github.io/
* https://scicatproject.github.io/documentation

## Changes and Deployment of Home Webpage

```
git clone https://github.com/SciCatProject/scicatproject.github.io`
cd scicatproject.github.io

# make your changes, git add and git commit as usual

git push origin master
```

After pushing the changes they will immediately become visible at the URL https://scicatproject.github.io/

## Changes and Deployment of Manuals

```
git clone https://github.com/SciCatProject/documentation.git`
cd documentation

# make your edit/add/commit cycle

npm install honkit --save
npx honkit build
```

### Serving the Documentation locally

`npx honkit serve --port 4040`

### Publishing the documentation

`git push origin master`

The push to the origin repo will trigger a travis job, which will publish the resulting documentation to https://scicatproject.github.io/documentation

