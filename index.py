import os
import sys
from PIL import Image
import subprocess
import signal

if len(sys.argv) >= 2:
    basepath = sys.argv[1]
    directories = os.listdir(basepath)
else:
    basepath = None
    directories = os.listdir()

directories.sort()

def handle(path, completion=None):
    try:
        response = input(f"Delete \"{path}\"?\n").lower()
        if response == "y":
            print("Deleting...\n")
            os.chmod(path, 0o777)
            os.remove(path)
            print(f"Deleted \"{path}\"\n")
            if completion != None:
                completion()
        elif response == "v":
            print('Showing file...\n')
            name, extension = os.path.splitext(path)
            if extension.lower() == ".png" or extension.lower() == ".jpg" or extension.lower() == ".jpeg":
                with Image.open(path) as img:
                    img.show()
                    def c():
                        if completion != None:
                            completion()
                        # img.hide()
                    handle(path, c)
            elif extension.lower() == ".pdf":
                os.chmod(path, 0o777)
                os.system(path)
                # subprocess.Popen([path], shell=True)
                # plot = subprocess.Popen("evince '%s'" % path, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
                handle(path)
            else:
                print("Can't show this file.\n")
                # with open(path) as infile:
                #     for line in infile:
                #         outfile.write(line)
                handle(path)
        else:
            print("Skipped file.\n")
            if completion != None:
                completion()
    except PermissionError:
        print(f"A PermissionError occured.\n")
        handle(path)

for path in directories:
    if basepath == None:
        handle(path)
    else:
        handle(f"{basepath}/{path}")
