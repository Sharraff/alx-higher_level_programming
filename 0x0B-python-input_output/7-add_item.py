#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Authored: Musharraff Ibrahim
"""

import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    jsonList = load_from_json_file("add_item.json")
except:
    jsonList = []

for i in sys.argv[1:]:
    jsonList.append(i)
save_to_json_file(jsonList, "add_item.json")
