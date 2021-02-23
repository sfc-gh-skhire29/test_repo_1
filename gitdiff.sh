#!/usr/bin/env bash

format_py=.py
format_sql=.sql
head=main
test_branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
echo "head branch: " $head
echo "test/current branch: " $test_branch
MODIFIED_FILES_python=$(git diff --name-only $test_branch $head | grep -E "(${format_py})")
MODIFIED_FILES_sql=$(git diff --name-only $test_branch $head | grep -E "(${format_sql})")
echo "Modified python files: "$MODIFIED_FILES_python
echo "Modified sql files: "$MODIFIED_FILES_sql