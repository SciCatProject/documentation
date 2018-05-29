rm -rf node_modules SUMMARY.md  docs

   npm install

python3 summary_generator.py
   ./node_modules/gitbook-cli/bin/gitbook.js install
   ./node_modules/gitbook-cli/bin/gitbook.js build . docs
