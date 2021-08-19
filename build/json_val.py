import argparse
import json
import os
from jsonschema.exceptions import ValidationError
from json.decoder import JSONDecodeError
from jsonschema import validate

my_parser = argparse.ArgumentParser(description='List the json files of a folder')
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       nargs = '+',
                       help='the path')

args = my_parser.parse_args()
input_paths = args.Path
print("Files Passed are ",input_paths)

dirpath = os.path.dirname(os.path.abspath(__file__))
repo_path  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
schema_file_path = os.path.join(dirpath,'complete_schema_crowdstrike.json')
try:
    s = open(schema_file_path,'r')
    schema = json.load(s)
except JSONDecodeError as jsonerror:
    print("---------------------------------------------------------------------------")
    print("JSONDecodeError in SCHEMA FILE ", schema_file_path)
    print(jsonerror)

for input_file in input_paths:
    try: 
        f = open(os.path.join(repo_path, input_file),'r')
        example = json.load(f)
        validate(instance = example, schema = schema)
    except JSONDecodeError as jsonerror:
        print("---------------------------------------------------------------------------")
        print("JSONDecodeError in ", input_file)
        # print(jsonerror)
        
    except ValidationError as valerrr:
        print("---------------------------------------------------------------------------")
        print("Schema ValidationError in ", input_file)
        # print(valerrr)
        raise
    f.close()
