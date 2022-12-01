#!/bin/bash

set -e
set -x

mkdir original_solutions/day_$1
cp boilerplate.py original_solutions/day_$1/day_$1.py
echo " " > original_solutions/day_$1/test.txt 