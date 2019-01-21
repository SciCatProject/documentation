#!/usr/bin/env bash
git init cat
cd cat
git remote add origin https://github.com/ScicatProject/catanie
git config core.sparsecheckout true
echo "documentation/*" >> .git/info/sparse-checkout
git pull --depth=1 origin develop
ls 
