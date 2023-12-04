#!/bin/bash

function lineToArrays() {
    OLDIFS=$IFS
    IFS='|' read -ra my_array <<< "$1"
    left=${my_array[0]}
    
    IFS=':' read -ra left_arr <<< "$left"
    
    left=$(sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'<<<"${left_arr[1]}")
    right=$(sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'<<<"${my_array[1]}")

    IFS=$OLDIFS
}

function commonElements() {
    OLDIFS=$IFS
    IFS=' ' read -ra left_arr <<< "$1"
    IFS=' ' read -ra right_arr <<< "$2"

    intersectionStr=($(comm -12 <(printf '%s\n' "${left_arr[@]}" | LC_ALL=C sort) <(printf '%s\n' "${right_arr[@]}" | LC_ALL=C sort)))
    intersectionSize=$((${#intersectionStr[@]}-1))

    if [ $intersectionSize -lt 0 ]; then
        points=0
    else
        points=$((2**$intersectionSize))
    fi
    
    IFS=$OLDIFS
}

input="./in-day4.txt"

sum=0

while IFS= read -ra line
do
  lineToArrays "$line"
  commonElements "$left" "$right"
  sum=$((sum+points))
done < "$input"

echo $sum
