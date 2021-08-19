import json
from jsonschema import validate


s = open('schema.json','r')
schema = json.load(s)
print(schema)
f = open('./json_files/example.json','r')
example = json.load(f)


validate(instance = example, schema = schema)

