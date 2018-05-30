#!/usr/bin/env python3
import os, glob

ROOT_DIR = '.'

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
    global summary
    all_files = list(glob.iglob(startpath + '**/*.md', recursive=True))
    all_file2 = [x for x in all_files  if not 'node_modules' in x]
    all_file2 = [x for x in all_files  if not '_book' in x]
    all_file2 = [x for x in all_files  if not 'docs' in x]
    #all_files = sorted(all_files2)
    for f in all_files:
        if not 'node_modules' in f.lower():
            split_path = f.split('/')
            print(split_path, f)
            title = split_path[-1]
            level = 0
            if len(split_path) > 2:
                title = split_path[-1] if 'readme' not in split_path[-1].lower() else split_path[-2]
                formatted = f.lower().replace('/readme.md', '').split('/')
                level = len(formatted) if not 'readme' in f.lower() else len(formatted) - 2
            title = title.replace('.md', '').title()
            title = title.replace('_', ' ').title()
            summary += "{0}* [{1}]({2}) \n".format(' ' * (level * 2), title, f)
    print(summary)
    return summary


def save_output(contents):
    """Save contents of md files found to summmary md file"""
    with open('SUMMARY.md', 'w') as out:
        out.write(contents)

print("Generating SUMMARY")
txt = list_files('./')
save_output(txt)
