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
if [ -$action != "CHANGED" ];
  then
    echo "action is not listed in [CHNAGED,ADD,REMOVE,REFACTOR,OPTIMIZE,VERSION]"
else
  echo "yeah ,you did it!!!222333"
fi
#echo "$commit_messages"