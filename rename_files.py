import os, shutil

base_original = '/home/project'
filenames_original = [x for x in os.listdir(base_original) if '_17,' in x]
print(filenames_original)

for filename in filenames_original:
    path_old = os.path.join(base_original, filename)
    path_new = os.path.join(base_original, filename.replace('_17,', '_16,'))
    os.rename(path_old, path_new)
    print(path_old, path_new)
