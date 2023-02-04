#!/bin/bash
# This feels like sliding down a warm fudge mountain; I dearly hope the github action
# we write if this works can maintain this simplicity
find codegen/specs/stytch -name "*.yml" -delete

find ../protobuf/api -name "*.yml.python" |                                       
while read line
do
  cp $line `echo $line | sed 's|.*/\([^.]*\).yml.python$|codegen/specs/stytch/\1.yml|'`
done
