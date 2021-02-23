#!/usr/bin/env bash

path=test_codes
head=main
test_branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
echo $head
echo $test_branch
MODIFIED_FILES=$(git diff --name-only $test_branch $head | grep -E "(${path})")
echo $MODIFIED_FILES