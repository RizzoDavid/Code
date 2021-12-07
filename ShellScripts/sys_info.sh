#! /bin/bash

echo "May The Odds Ever Be In Your Favor"
date | awk '{print $1" "$2" "$3" "$6}' 
echo "Machine Type: $MACHTYPE"
hostname -I | awk '{print $1}'
hostname 