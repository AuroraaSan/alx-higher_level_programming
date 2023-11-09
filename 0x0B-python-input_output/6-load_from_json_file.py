#!/usr/bin/python3
""" defining json """

import json

def load_from_json_file(filename):
    """ return json representation """
    with open(filename, 'r', encoding= 'utf-8') as f:
        return json.load(f)