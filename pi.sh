#!/bin/bash

START=1
# MAX=224399
MAX=314159
STEP=500

if ! [[ -z "$1" ]]; then
    START=$1
fi
if ! [[ -z "$2" ]]; then
    MAX=$2
fi
if ! [[ -z "$3" ]]; then
    STEP=$3
fi

for i in $(seq $START $STEP $MAX); do
    printf "$i:$((i*14))\n"
    ./pi.py $i > pi.txt
    git add -A
    git commit -m"$(($i * 14))"
    git push
done
