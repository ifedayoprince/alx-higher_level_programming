#!/usr/bin/python3
"""
Adds all program arguments to a Python list, and then save them to a JSON file.
"""


from os import path
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

if not path.exists(filename):
    open(filename, "a")
    json_obj = []
else:
    json_obj = load_from_json_file(filename)

if len(sys.argv) > 1:
    json_obj = json_obj + sys.argv[1:]

save_to_json_file(json_obj, filename)
