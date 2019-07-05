var fs = require('fs');

const IGNORED = ['node_modules', 'docs', '.git', 'img']

function getFiles (dir, level, text, files_){
    files_ = files_ || [];
    level = level || 0;
    text = text || "# Summary \n\n";
    dir = dir.replace('./', '');
    if (IGNORED.indexOf(dir) === -1) {
      var files = fs.readdirSync(dir);
      console.log(dir, level);
      for (var i in files){
          var name = dir + '/' + files[i];
          if (fs.statSync(name).isDirectory()){
              const f = name.split('/');
              getFiles(name, f.length, text, files_);
          } else if (name.indexOf('.md') !== -1) {
              files_.push(name);
          }
      }
    }
    return text;
}

const f = getFiles('.');
// console.log(f);
