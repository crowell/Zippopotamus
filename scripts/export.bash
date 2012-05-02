#!/bin/bash

# Check that we have at least n arguments

if [  $# -ne 4 ] 
then
	echo "Please enter <append> <raw-dump-dir> <user> <pass>"
	exit -1
fi


# Get directory and name
appendix=$1
raw=$2
user=$3
pass=$4

echo "Dumping $appendix into $raw.txt"

while read line
do
	echo -e "$line \n"
	name=${line:0:2}
	mongoexport --db zip  --collection global -u $user -p $pass -q "{'country abbreviation':'$name'}" -f 'country','country abbreviation','post code','place name','state','state abbreviation','latitude','longitude' --csv -o $raw$name.txt
done < $appendix

