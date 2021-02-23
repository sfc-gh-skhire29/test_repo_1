#!/usr/bin/env bash

head=main
test_branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
echo $head
echo $test_branch
git diff --name-only $test_branch $head