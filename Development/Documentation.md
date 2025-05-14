# Documentation

## Overview
The documentation consists of three main parts.

* The "Home Webpage" of the project , describing the purpose and use cases for the software. The source is located at https://github.com/SciCatProject/scicatproject.github.io
* The documentation proper, split into User,Operator,Ingestor and Developer manual. The source is located at https://github.com/SciCatProject/documentation . It covers all components of the software, i.e  frontend and backend. The documentation tool [honkit](https://honkit.netlify.app/) (successor of gitbook) is used.
* The documentation of the REST API of the backend. This is generated from the OpenAPI description, which itself is generated from the model descriptions in the backend code.

All parts are hosted on the [GitHub Pages platform](https://pages.github.com/). The documentation part is "injected" into the GitHub pages automatically by a travis job, which runs after each commit to the documentation repository

The live web site is then visible on the following URLs respectively
* https://scicatproject.github.io/
* https://scicatproject.github.io/documentation
* The REST API not generated statically but is available from each running SciCat
  backend (for example, the public [ESS instance](https://scicat.ess.eu/explorer)).
  <!-- TODO update following completion of https://github.com/SciCatProject/documentation/issues/42 -->

## Changes and Deployment of Home Webpage

The homepage is built using [Jekyll](https://jekyllrb.com/) and hosted on GitHub pages.
The source is located in the repository
[SciCatProject/scicatproject.github.io](https://github.com/SciCatProject/scicatproject.github.io).

After pushing the changes they will become visible at the URL https://scicatproject.github.io/

## Changes and Deployment of Manuals

Manuals are built using [honkit](https://honkit.netlify.app/) from the
[SciCatProject/documentation](https://github.com/SciCatProject/documentation)
repository. After pushing the changes they will become visible at the URL
https://scicatproject.github.io/documentation.
