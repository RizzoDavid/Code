#!/bin/bash

#Find INCORRECT_PASSWORD and change to ACCESS_DENIED  from what ever file is named
#Send Results to file of your choosing

sed s/INCORRECT_PASSWORD/ACCESS_DENIED/ $1 > $2 

#Only keep date and username from specified output from argument 2
#Send that information to a file of your choosing

awk '{print $4 $6}' $2 > $3

#list files in directory to verify that all files are there

ls

#cat last file to verify correct contents

cat $3 |less