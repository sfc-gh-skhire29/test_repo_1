import argparse
import json
import os
import fastjsonschema

my_parser = argparse.ArgumentParser(description='List the json files of a folder')
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       nargs = '+',
                       help='the path')

args = my_parser.parse_args()
input_paths = args.Path
print("Files Passed are ",input_paths)

filter_input_paths = []
for input_path in input_paths:
    if (input_path.startswith('it_engineering/etl/great_expectations')):
        # dirname = os.path.dirname(input_path)
        # dirbasename = os.path.basename(dirname)
        # filename = os.path.basename(input_path)
        # print(dirname)
        # print(dirbasename)
        # print(filename)
        # filter_input_paths.append(os.path.join(dirbasename,filename))
        filter_input_paths.append(input_path)

print("Files to work on are ",filter_input_paths)


dirpath = os.path.dirname(os.path.abspath(__file__))
repo_path  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
schema_file_path = os.path.join(dirpath,'complete_schema_crowdstrike.json')

s = open(schema_file_path,'r')
schema = json.load(s)

for input_file in filter_input_paths:
    f = open(os.path.join(repo_path, input_file),'r')
    example = json.load(f)
    fastjsonschema.validate(schema, example)
    # print(valerrr)
    f.close()
