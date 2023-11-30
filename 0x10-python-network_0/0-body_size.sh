#!/bin/bash
# Write a Bash script that takes in a URL,send and display size
curl -s "$1" | wc -c
