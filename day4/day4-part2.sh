#!/bin/bash

function lineToArrays() {
    OLDIFS=$IFS
    IFS='|' read -ra my_array <<< "$1"
    left=${my_array[0]}
    
    IFS=':' read -ra left_arr <<< "$left"
    
    IFS=' ' read -ra id_arr <<< "${left_arr[0]}"


    id=$(sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'<<<"${id_arr[1]}")
    left=$(sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'<<<"${left_arr[1]}")
    right=$(sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'<<<"${my_array[1]}")

    IFS=$OLDIFS
}

function commonElements() {
    OLDIFS=$IFS
    IFS=' ' read -ra left_arr <<< "$1"
    IFS=' ' read -ra right_arr <<< "$2"

    intersectionStr=($(comm -12 <(printf '%s\n' "${left_arr[@]}" | LC_ALL=C sort) <(printf '%s\n' "${right_arr[@]}" | LC_ALL=C sort)))
    intersectionSize=$((${#intersectionStr[@]}))

    points=$intersectionSize
    
    IFS=$OLDIFS
}

input="./in-day4.txt"

# Get a value:
arrayGet() { 
    local array=$1 index=$2
    local i="${array}_$index"
    printf '%s' "${!i}"
}

cnt=0

while IFS= read -ra line
do
  lineToArrays "$line"
  commonElements "$left" "$right"
  declare "scores_$id=$points"
  declare "counts_$id=1"
  cnt=$(($cnt + 1))
done < "$input"

for i in $(seq 1 $cnt); 
do 
    score=$(arrayGet scores $i)
    currCount=$(arrayGet counts $i)

    if [[ $score -eq 0 ]]; then
        continue
    fi

    for j in $(seq 1 $score);
    do
        nextIdx=$((i+j))
        nextCount=$(arrayGet counts $nextIdx)
        nextCount=$((nextCount+currCount))
        declare "counts_$nextIdx=$nextCount"
    done
done

sum=0

for i in $(seq 1 $cnt); 
do
    val=$(arrayGet counts $i)
    sum=$((sum+val))
done

echo $sum