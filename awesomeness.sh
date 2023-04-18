#!/bin/bash
# This feels like sliding down a warm fudge mountain; I dearly hope the github action
# we write if this works can maintain this simplicity
find codegen/specs/stytch -name "*.yml" -delete
find codegen/specs/stytch_b2b -name "*.yml" -delete

find ../protobuf/api -name "*.yml.python" |                                       
while read line
do

  consumerFile=`echo $line | sed 's|.*/\([^.]*\).yml.python$|codegen/specs/stytch/\1.yml|'`
  b2bFile=`echo $line | sed 's|.*/\([^.]*\).yml.python$|codegen/specs/stytch_b2b/\1.yml|'`

  # filter for the appropriate methods then put them in the appropriate spec folder
  cat $line | yq -y '.methods=[.methods[] | 
    select(.vertical == "CONSUMER") | 
    select(.include_in_backend_sdk_codegen == true) | 
    del(.vertical) | 
    del(.include_in_backend_sdk_codegen)]' |
    sed 's/methods: \[\]/methods: /' > $consumerFile

  cat $line | yq -y '.methods=[.methods[] | 
    select(.vertical == "B2B") | 
    select(.include_in_backend_sdk_codegen == true) | 
    del(.vertical) | 
    del(.include_in_backend_sdk_codegen)]' |
    sed 's/methods: \[\]/methods: /'  > $b2bFile

  # then we have to tack the ALL vertical methods onto both files
  cat $line | yq -y '[.methods[] | 
    select(.vertical == "ALL") | 
    select(.include_in_backend_sdk_codegen == true) | 
    del(.vertical) | 
    del(.include_in_backend_sdk_codegen)]' |
    sed 's/^/  /' |
    grep -v "^ *\[\] *$"  >> $consumerFile

  cat $line | yq -y '[.methods[] | 
    select(.vertical == "ALL") | 
    select(.include_in_backend_sdk_codegen == true) | 
    del(.vertical) | 
    del(.include_in_backend_sdk_codegen)]' |
    sed 's/^/  /' |
    grep -v "^ *\[\] *$"  >> $b2bFile


done

# delete any files that are only 2 lines because they're just a classname and
# a null methods entry
find . -name "*.yml" | xargs wc -l | awk '/^ *2 / {print $2}' | xargs rm

./bin/generate-api.sh
