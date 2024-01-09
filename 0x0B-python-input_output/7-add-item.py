#!/usr/bin/python3
"""Load,add,save"""


import json
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
def add_item(*args):
    """ A function to Load, add, save"""
    filename = "add_item.json"
    if not exists(filename):
        with open(filename, "w+") as f:
            json.dump([],f)

    list_ele = load_from_json_file(filename)

    list_ele.extend(args)

    save_to_json_file(list_ele, filename)

if __name__ == "__main__":
    import sys
    add_item(*sys.argv[1:])

