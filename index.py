import os
import sys
from PIL import Image

if len(sys.argv) >= 2:
    basepath = sys.argv[1]
    directories = os.listdir(basepath)
else:
    basepath = None
    directories = os.listdir()

directories.sort()

def handle(path):
    response = input(f"Delete \"{path}\"?").lower()
    if response == "y":
        print("Deleting...")
        os.remove(path)
        print("Deleted \"{dir}\"")
    elif response == "v":
        print('Showing file...')
        name, extension = os.path.splitext(path)
        if extension.lower() == ".png" or extension.lower() == ".jpg" or extension.lower() == ".jpeg":
            with Image.open(path) as img:
                img.show()
        else:
            print("Can't show this file.")
            # with open(path) as infile:
            #     for line in infile:
            #         outfile.write(line)
        handle(path)
    else:
        print("Skipped file.")

for path in directories:
    if basepath == None:
        handle(path)
    else:
        handle(f"{basepath}/{path}")
