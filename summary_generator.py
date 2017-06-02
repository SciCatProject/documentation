import os

ROOT_DIR = './'

ignore = ['node_modules', '_book', '.git']
folders = []
files = []

summary = ""

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
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [x for x in dirs if x not in ignore]
        # print(root)
        # print(files)
        split_path = root.split('/')
        level = len(split_path)
        title = split_path[-1]
        print(level)
        title = title if title else "Home"
        print(title)
        # print(dirs)
        # for k,d in enumerate(dirs):
        #     print(k, d) 
        # print(dirs)
        # print(files)
        # for entry in root:
        #     if entry in ignore:
        #         del entry
        # level = root.replace(startpath, '').count(os.sep)
        # indent = ' ' * 4 * (level)
        # print('{}{}/'.format(indent, os.path.basename(root)))
        # subindent = ' ' * 4 * (level + 1)
        # for f in files:
        #     print('{}{}'.format(subindent, f))



print("Generating")
list_files('./')
print('Folders:')
print(summary)