#!/bin/sh

# Argument: <package_name> <duration> <interval>
PACKAGE_NAME=$1
DURATION=$2
INTERVAL=$3

if [ -z "$PACKAGE_NAME" ] || [ -z "$DURATION" ] || [ -z "$INTERVAL" ]; then
  echo "Failed to execute"
  echo "Usage: $0 <package_name> <duration> <interval>"
  exit 1
fi

echo "Package name: $PACKAGE_NAME" 
echo "Duration: $DURATION" 
echo "Interval: $INTERVAL" 
echo "" 

ITERATIONS=$((DURATION / INTERVAL))

top -b -d "$INTERVAL" -n "$ITERATIONS" -p $(pgrep -d',' -f "$PACKAGE_NAME") | grep -v -e 'top' -e "$0"
