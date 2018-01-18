# SciCat

A project to catalogue and provide access to metdatdata and raw experimental data.

## Building and Editing Locally

`npm i -g gitbook-cli`

`gitbook install`

`gitbook build . docs/`
The command above could be useful to put into a git hook to ensure that a build is made on each push.

## Summaries

The TOC for a Gitbook is read from the `Summary.md`, this can be handled by the python script: `summary_generator.py`
