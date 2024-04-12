#!/bin/bash

# define file paths
in_file="logs"
out_file="out_bash.txt"

# search folder with pattern and output it
grep -Eo 'CMPN\{[^\}]+\}|picoCTF\{[^\}]+\}|fastctf\{[^\}]+\}|[A-Z]+_[A-Z]+' "$in_file" > "$out_file"
