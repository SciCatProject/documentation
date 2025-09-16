![SciCatLogo.png](SciCatLogo.png)

# SciCat Metadata Catalogue
[![Build Status](https://travis-ci.org/SciCatProject/documentation.svg?branch=master)](https://travis-ci.org/SciCatProject/documentation)

## Why SciCat ?

See the [SciCat Home Webpage](https://scicatproject.github.io) for an overview of how SciCat can help to manage scientific data.

## Structure of Documentation

SciCat documentation is split into the following chapters:

* [User Guide](Users) - Users of the system can come here to see screen captures, FAQs and find resources on how to better understand SciCat.
* [Operator Guide](Operator) - System admins read this part to set up SciCat for their location
* [Ingestor Guide](Ingestor) - Instrument responsibles read this to understand how data can ge ingested into SciCat either manually or in an automated fashion
* [Developer Guide](Development) - Developers who want to contribute to the project should read this chapter.

## Talks

[SciCat Project: Data Catalog System (2017)](https://icatproject.org/wp-content/uploads/2017/12/ICAT_F2F_2017_PSI.pdf)
[SciCat talk from Luke Gorman on Joint ExPaNDS and PaNOSC Meeting Feb 2020](https://indico.esss.lu.se/event/1373/contributions/10773/attachments/9761/15638/Lund2020.pdf)

## Building

Docs are built using [honkit](https://honkit.netlify.app/). This can either be installed locally using npm or run via docker.

### Serving documentation with docker

```
docker compose up -d
```

This should start the honkit server on http://localhost:4040. Honkit will watch for changes in the source files and automatically re-build them.

### Serving the Documentation locally

You can also run the honkit server locally using npm:

```
npm install
npm run start
```

## Publishing the documentation

The [website](https://scicatproject.github.io/documentation) will be automatically
rebuilt after each change to the `master` branch by a github action.