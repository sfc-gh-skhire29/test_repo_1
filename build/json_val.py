import json
import os
from jsonschema import validate

dirpath = os.path.dirname(os.path.abspath(__file__))
repo_path  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(dirpath,'complete_schema.json'),'r')
schema = json.load(s)

f = open(os.path.join(repo_path, 'json_files/example.json'),'r')
example = json.load(f)


validate(instance = example, schema = schema)

