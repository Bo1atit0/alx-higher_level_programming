#!/bin/bash
# Write a Bash script that takes in a URL,
# sends a request to that URL,
# and displays the size of the body of the response

if [ -z "$1" ];
then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$UR"L)

echo "$SIZE"
