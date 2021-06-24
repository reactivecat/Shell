#!/usr/bin/env bash
commit_revision_numbers=$(git log --pretty=format:"%h")
#echo "$commit_revision_numbers"
echo "edcd2fa\n7ad4381\n46cb19d\n00a6447"
#revision_arr=()
#while read -r line ; do
#    echo "---$line"
#    revision_arr+=("$line")
#done
#echo "hah"
#echo "len:${#revision_arr}"