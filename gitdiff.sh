#!/usr/bin/env bash

format_py=.py
format_sql=.sql
target=main
head=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
echo "target branch: "$target
echo "test/current branch: "$head
MODIFIED_FILES_python=$(git diff --name-only $head $target | grep -E "(${format_py})")
MODIFIED_FILES_sql=$(git diff --name-only $head $target | grep -E "(${format_sql})")
echo "Modified python files: "$MODIFIED_FILES_python
echo "Modified sql files: "$MODIFIED_FILES_sql