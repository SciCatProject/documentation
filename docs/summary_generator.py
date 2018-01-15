import os

ROOT_DIR = './'

ignore = ['node_modules', '_book', '.git', 'img', 'docs']

summary = "# Summary \n\n"

# def scan(dir, name):
#     print(dir, name)
#     for entry in os.scandir(dir):
#         if entry.is_dir() and entry.name not in ignore:
#             folders.append(entry.path)
#             scan(entry.path, entry.name)
#             summary.append({'name':entry.name, 'path': entry.path + '/README.md'})
#         elif entry.is_file():
#             if 'README.md' is entry.name:
#                 summary = "* [{0}]({2}) \n"
#             files.append(entry.path)

def list_files(startpath):
    """Scan all dirs for md files and generate contents."""
    global summary
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [x for x in dirs if x not in ignore]
        split_path = root.split('/')
        level = len(split_path)
        title = split_path[-1]
        title = title if title else "Home"
        summary += "{0}* [{1}]({2}) \n".format(' ' * (level), title, root + '/README.md')
        md_files  = [x for x  in files if 'md' in x.lower() and not 'readme' in x.lower() and not 'summary' in x.lower()]
        for f in md_files:
            f_name = f.lower().replace('_', ' ').replace('.md', '').title()
            summary += "{0}* [{1}]({2}) \n".format(' ' * (level*2), f_name, os.path.join(root, f))
    return summary


def save_output(contents):
    """Save contents of md files found to summmary md file"""
    with open('SUMMARY.md', 'w') as out:
        out.write(contents)

print("Generating SUMMARY")
txt = list_files('./')
save_output(txt)
