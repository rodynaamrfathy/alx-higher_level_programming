#!/usr/bin/python3
"""a function that writes an Object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """an Object to a text file using a JSON representation"""

    with open(filename, "w") as f:
        content = json.dumps(my_obj)
        f.write(content)
    #or use json.dump(my_obj, f)
