import shutil, os

cwd = os.getcwd()
print(cwd)
for folder, sub, filenames in os.walk(cwd):
    if filenames:
        if not folder == cwd:
            for file in filenames:
                print(file, folder)
                shutil.copy(folder+'\\'+file,cwd+'\\'+'all_files')