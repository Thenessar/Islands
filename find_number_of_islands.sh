#!/bin/bash

if [ $# -eq 0 ]; 
then
    echo "Parameters mismatch: expected 1 parameter but recieved $#."
    echo "To properly run the script, input path to a text file including matrix made of zeroes and ones. Do not put any separator between the numbers."
    exit 1
fi

python3 app.py $1