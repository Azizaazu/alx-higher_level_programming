#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response=$(curl -sI "$url" | grep -i content-length)
size=$(echo "$response" | awk '{print $2}')

echo "${size}"
