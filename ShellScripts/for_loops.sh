#! /bin/bash

my_states=(
    'Hawaii'
    'NewYork'
    'NorthCarolina'
    'Maine'
    'Colorado'
)

for state in ${my_states[@]}
    do 
        if [ $state == Hawaii]
            then 
                echo "Hawaii is the best"
            else  
                echo "I am not fonf of Hawaii"
        fi
    done