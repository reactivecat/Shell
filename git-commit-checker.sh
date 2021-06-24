#!/bin/bash
current_commit_message=`cat $1`
#commit_messages=`git log --oneline`
action=${current_commit_message:0:7}
moduleName=${current_commit_message:7:9}
echo "message:>>>>>$current_commit_message"
message=${current_commit_message:10:-1}
echo "action:$action"
echo 'message:'"$message"''
echo "module:"/bash/here/"$moduleName"
#echo "$commit_messages"