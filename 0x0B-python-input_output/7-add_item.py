#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file"""

import json
from 6-load_from_json_file.py import load_from_json_file
from 5-save_to_json_file.py import save_to_json_file

json_filename = "add_item.json"

my_list = load_from_json_file(json_filename)
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, json_filename)
