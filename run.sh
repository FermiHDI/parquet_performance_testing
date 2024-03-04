#!/bin/bash
pip install -r requirements.txt

if [ $# -ne 2 ]; than
    echo "Usage: $0 <python script>"
    exit 1
fi

python3 $@