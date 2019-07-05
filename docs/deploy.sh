#!/bin/bash

git init
git config user.name "Chris Gwilliams"
git config user.email "encima@gmail.com"

git remote add upstream "https://encima:$GH_TOKEN@github.com/SciCatProject/docs.git"
git pull origin upstream
git checkout gh-pages
git merge master
./node_modules/gitbook-cli/bin/gitbook.js build . docs
exec `rm -rf '("docs")`
mv docs/* .
rm -rf docs

git add -a .
git commit -m "rebuild pages at ${rev}"
git push upstream gh-pages
