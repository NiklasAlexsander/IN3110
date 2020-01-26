#!/bin/bash

climb(){
dirjumps=0

if [ $# -eq 0 ]; then
dirjumps=1
else
dirjumps=$1
fi

stringTest=""

for ((i=1; i<=${dirjumps};i++))
do
cd ../
done
}

climb $1
