#!/usr/bin/env bash

# Check if an argument (N) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

N="$1"  # The number of </page> tags to capture
COUNT=0 # Counter for </page> occurrences

awk -v n="$N" '
    /<\/revision>/ { count++; if (count >= n) { print; exit } }
    { print }
'

echo "</mediawiki>"
