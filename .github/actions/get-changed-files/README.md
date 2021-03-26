# Get Changed Files


**get-changed-files**  is a Github Action which returns the absolute path of the changed files in current branch from the target branch (on Pull Requests)

Currently supporting:
 - SQL files (.sql)
 - Python files (.py)
 - Text files (.txt)
 - Yaml files (.yaml, .yml)

#### Inputs:
 - No inputs is required

#### Outputs:
 -   Changed .sql files		(outputs.sql_changed) 
 -   Changed .py files		(outputs.python_changed)
 -  Changed .txt files		(outputs.txt_changed)
 -  Changed .yml/.yaml files (outputs.yml_changed) 

Place the action in the ```./.github/actions``` folder and refer below to use the action

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:  
      - uses: actions/checkout@v2
   
      - uses: ./.github/actions/get-changed-files
        id: changed_files

      - name: Print python changed files
        run: echo "${{ steps.changed_files.outputs.python_changed }}"
        
      - name: Print sql changed files
        run: echo "${{ steps.changed_files.outputs.sql_changed }}"  
      
      - name: Print text changed files
        run: echo "${{ steps.changed_files.outputs.txt_changed }}"
        
      - name: Print yml/yaml changed files
        run: echo "${{ steps.changed_files.outputs.yml_changed }}" 
``` 
