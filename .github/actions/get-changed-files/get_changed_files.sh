#!/usr/bin/env bash

# $1 - token
# $2 - head_branch
# $3 - target_branch
# $4 - files

format_py=.py
format_sql=.sql
format_txt=.txt
format_yml='.y*ml'

echo $2
echo $3


git fetch origin $2:$2
git fetch origin $3:$3

MODIFIED_FILES_python=$(git diff --name-only $2 $(git merge-base $2 $3) | grep -E "(${format_py})")
MODIFIED_FILES_sql=$(git diff --name-only $2 $(git merge-base $2 $3) | grep -E "(${format_sql})")
MODIFIED_FILES_txt=$(git diff --name-only $2 $(git merge-base $2 $3) | grep -E "(${format_txt})")
MODIFIED_FILES_yml=$(git diff --name-only $2 $(git merge-base $2 $3) | grep -E "(${format_yml})")
# head=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
# MODIFIED_FILES_python=$(git diff --name-only $head main | grep -E "(${format_py})")
# MODIFIED_FILES_sql=$(git diff --name-only $head main | grep -E "(${format_sql})")

echo "Modified python files1: "$MODIFIED_FILES_python
echo "Modified sql files: "$MODIFIED_FILES_sql
echo "Modified text files: "$MODIFIED_FILES_txt
echo "Modified yml files: "$MODIFIED_FILES_yml

echo "::set-output name=python_changed_files::$(echo $MODIFIED_FILES_python)"
echo "::set-output name=sql_changed_files::$(echo $MODIFIED_FILES_sql)"
echo "::set-output name=txt_changed_files::$(echo $MODIFIED_FILES_txt)"
echo "::set-output name=yml_changed_files::$(echo $MODIFIED_FILES_yml)"