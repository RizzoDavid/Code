#! /bin/bash

#Using If Statements

if [ -d ~/research]
    then
        echo "found"
    else
        mkdir ~/research
fi

if [ -f ~/research/sys_info.txt]
    then   
        sudo rm ~/research/sys_info.txt
    end
fi

#Bonus Variables

var1=$(ip addr | grep inet | tail -2 | head -1)
var2=$(find /home -type f -perm 777)

