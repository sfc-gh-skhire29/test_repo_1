#!/usr/bin/env bash

format=.{py,sql}
head=main
test_branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
echo "head branch: " $head
echo "test/current branch: " $test_branch
MODIFIED_FILES=$(git diff --name-only $test_branch $head | grep -E "(${format})")
echo $MODIFIED_FILES