import os
import sys
from pathlib import Path


def get_extensions(dir_full_path):
    list_current_dir = os.listdir(dir_full_path)
    extensions = list()

    for entry in list_current_dir:

        full_path = os.path.join(dir_full_path, entry)

        if os.path.isdir(full_path):
            extensions = extensions + get_extensions(full_path)
        else:
            ext = Path(entry).suffix.lower()
            if ext:
                extensions.append(ext)
    
    return extensions


dir_full_path = sys.argv[1]

extensions = get_extensions(dir_full_path)
extensions = list(dict.fromkeys(extensions))

textfile = open("extensions.txt", "w")
for ext in extensions:
    textfile.write(ext + "\n")

textfile.close()
