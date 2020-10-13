# Documentation

The bulk of the documentation is stored in a dedicated *documentation* repository. It covers
all components of the software, i.e  frontend and backend. It is structured into different capters.
The documentation tool [honkit](https://honkit.netlify.app/) (successor of gitbook) is used.

## Building and Editing Locally

```
git clone https://github.com/SciCatProject/documentation.git`
cd documentation
npm install honkit --save
npx honkit build
```

## Serving the Documentation locally

`npx honkit serve --port 4040`

## Publishing the documentation

`git push origin master`

The push to the origin repo will trigger a travis job, which will publish the resulting documentation to https://scicatproject.github.io/documentation

