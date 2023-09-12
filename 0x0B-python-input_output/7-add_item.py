#!/usr/bin/python3
'''
Module that adds args to JSON file
'''

import sys
import os

# Get the command-line arguments (excluding the script name)
arg_list = sys.argv[1:]

# Import the save_to_json_file and load_from_json_file functions from external modules
save_JSON = __import__('5-save_to_json_file').save_to_json_file
load_JSON = __import__('6-load_from_json_file').load_from_json_file

# Initialize an empty list
lisst = []

# Check if the "add_item.json" file exists, and if it does, load its contents
if os.path.exists('add_item.json'):
    lisst = load_JSON('add_item.json')

# Append the command-line arguments to the loaded list
save_JSON(lisst + arg_list, "add_item.json")
