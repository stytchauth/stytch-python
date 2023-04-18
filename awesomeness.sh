#!/bin/bash
# This feels like sliding down a warm fudge mountain; I dearly hope the github action
# we write if this works can maintain this simplicity
find codegen/specs/stytch -name "*.yml" -delete
find codegen/specs/stytch_b2b -name "*.yml" -delete

find ../protobuf/api -name "*.yml.python" |                                       
while read line
do
  vertical=`tail -n 1 $line`

  echo "vertical for $line is $vertical"

  # once we have the vertical we go ahead and remove it from the file so it won't
  # break anything
  cat $line | awk 'BEGIN {buffer=""} // {if (buffer != "") {print buffer};  buffer=$0}' > ${line}.tmp
  rm $line
  mv ${line}.tmp $line

  consumerFile=`echo $line | sed 's|.*/\([^.]*\).yml.python$|codegen/specs/stytch/\1.yml|'`
  b2bFile=`echo $line | sed 's|.*/\([^.]*\).yml.python$|codegen/specs/stytch_b2b/\1.yml|'`

  # I know the single `=` is scary, but I promise it's not an assignment in bash
  # and is in fact what we want to do here. What we want is to copy consumer files
  # into the regular dir, copy the b2b files into the b2b dir, and "ALL" vertical
  # files into both
  if [[ "$vertical" = "CONSUMER" ]]
  then
    echo "hit consumer branch, copying $line to $consumerFile"
    cp $line $consumerFile
  elif [[ "$vertical" = "B2B" ]]
  then
    echo "hit b2b branch, copying $line to $b2bFile"
    cp $line $b2bFile
  else
    echo "hit all branch, copying $line to $b2bFile and $consumerFile"
    cp $line $consumerFile
    cp $line $b2bFile
  fi
done
