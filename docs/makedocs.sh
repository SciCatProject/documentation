rm -rf SUMMARY.md  docs


yarn

python3 summary_generator.py
   ./node_modules/gitbook-cli/bin/gitbook.js install
   ./node_modules/gitbook-cli/bin/gitbook.js build . docs
