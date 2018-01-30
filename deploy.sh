#!/bin/bash 

git init
git config user.name "Chris Gwilliams"
git config user.email "encima@gmail.com"

git remote add upstream "https://$GH_TOKEN@github.com/SciCatProject/docs.git"
git fetch upstream

git add -A .
git commit -m "rebuild pages at ${rev}"
git push upstream master
