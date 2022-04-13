#!/bin/bash
echo how many files
read var
for ((c=1;c < $var; c++))
do
    touch old/File$c
done