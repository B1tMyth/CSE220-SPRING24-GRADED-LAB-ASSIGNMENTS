from collections import namedtuple
from pathlib import Path 
import re

cwd = Path.cwd()
id_regex = re.compile(r'\d{8}')
file_info = namedtuple("File_Name_Info", ["name", "suffix"])
file_dct = {}

for file in cwd.iterdir(): 
    file_path = cwd / file
    match = id_regex.search(file.name)

    if match: 
        file_dct[file_path] = file_info(name=match.group(), suffix=file.suffix)
    else: 
        file_path.unlink(missing_ok=True) if not file.name == "script.py" else None 

file_dct = dict(sorted(file_dct.items(), key=lambda item:item[1].name))

for idx, (old_file_name, file_name_data) in enumerate(file_dct.items(), start=1):
    new_file_name = cwd / f"{idx}. {file_name_data.name}{file_name_data.suffix}"
    old_file_name.rename(new_file_name)
    

