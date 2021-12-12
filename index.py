import os
import sys
from PIL import Image

if len(sys.argv) >= 2:
    basepath = sys.argv[1]
    directories = os.listdir(basepath)
else:
    directories = os.listdir()

directories.sort()

def handle(path):
    response = input(f"Delete \"{path}\"?").lower()
    if response == "y":
        print("Deleting...")
        if basepath == None:
            os.remove(path)
        else:
            os.remove(f"{basepath}/{path}")
        print("Deleted \"{dir}\"")
    elif response == "v":
        print('Showing file...')
        name, extension = os.path.splitext(path)
        if extension.lower() == "png" or extension.lower() == "jpg" or extension.lower() == "jpeg":
            if basepath == None:
                with Image.open(path) as img:
                    img.show()
            else:
                with Image.open(f"{basepath}/{path}") as img:
                    img.show()
            handle(path)
    else:
        print("Skipped file.")

for path in directories:
    handle(path)
