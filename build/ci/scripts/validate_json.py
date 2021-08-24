import argparse
import json
import os
from jsonschema.exceptions import ValidationError
from json.decoder import JSONDecodeError
from jsonschema import validate
import fastjsonschema

my_parser = argparse.ArgumentParser(description='List the json files of a folder')
my_parser.add_argument('--path', type=str, nargs = '+', help='Input files Path', required = True)
my_parser.add_argument('--schema_path', type=str, nargs = '+', help='Schema File path', required = True)
my_parser.add_argument('--method',type=str,nargs = '+', help='jsonschema or fastjsonschema')
my_parser.add_argument('--filter',type=str,nargs='+',help='filter files', required = True)

args = my_parser.parse_args()


def filter_paths(input_paths, filter_on):
    filter_input_paths = []
    for input_path in input_paths:
        if (input_path.startswith(filter_on)):
            filter_input_paths.append(input_path)

    print("Files to work on are ",filter_input_paths)

    return filter_input_paths


def validate_json_files(filter_input_paths, schema_file_path, repo_path, method = 'jsonschema'):
    error = 0
    try:
        s = open(schema_file_path,'r')
        schema = json.load(s)
    except JSONDecodeError as jsonerror:
        print("---------------------------------------------------------------------------")
        print("JSONDecodeError in SCHEMA FILE ", schema_file_path)
        print(jsonerror)
        raise

    if method == 'jsonschema':
        for input_file in filter_input_paths:
            try: 
                f = open(os.path.join(repo_path, input_file),'r')
                example = json.load(f)
                validate(instance = example, schema = schema)
            except JSONDecodeError as jsonerror:
                print("---------------------------------------------------------------------------")
                print("JSONDecodeError in ", input_file)
                print(jsonerror)
                error = 1
                
            except ValidationError as valerror:
                print("---------------------------------------------------------------------------")
                print("Schema ValidationError in ", input_file)
                print(valerror)
                error = 1
            f.close()
        
        if error == 1:
            raise Exception('Errors Occured while validating input json files...')

    elif method == 'fastjsonschema':
        for input_file in filter_input_paths:
            try:
                f = open(os.path.join(repo_path, input_file),'r')
                example = json.load(f)
                fastjsonschema.validate(schema, example)
            except Exception:
                print("Exception in File: ", input_file)
                raise
            f.close()


if __name__== "__main__":
    input_paths = args.path
    print(input_paths)
    schema_file_path = args.schema_path[0]
    method = args.method[0]
    filter_on = args.filter[0]
    print("filter = ",filter_on)
    repo_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    # schema_file_path = "it_engineering/etl/great_expectations/staging/app/cloud_engg/schema/schema.json"
    # filter_on = f'it_engineering/etl/great_expectations/staging/app/cloud_engg/input_jsons'
    filter_input_paths = filter_paths(input_paths, filter_on = filter_on)
    validate_json_files(filter_input_paths = filter_input_paths, 
                        schema_file_path = schema_file_path, 
                        repo_path = repo_path,
                        method = 'jsonschema')


    # Example use case 
    # python build/ci/scripts/validate_json_cloud_engg.py 
    # --path it_engineering/etl/great_expectations/staging/app/cloud_engg/input_jsons/example.json 
    # --schema it_engineering/etl/great_expectations/staging/app/cloud_engg/schema/schema.json 
    # --method jsonschema 
    # --filter it_engineering/etl/great_expectations/staging/app/cloud_engg/input_jsons 
