#!/bin/sh

# change to the directory of the script
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

# execute test script 
./env/bin/pytest runTest.py 