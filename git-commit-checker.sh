#!/bin/bash
commit_msg=$(cat "${$1:?Missing commit message file}")
echo "commit_msg ------>"