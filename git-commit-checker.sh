#!/bin/bash
hi=`cat $1`
commit_messages=`git log --oneline`
echo $commit_messages