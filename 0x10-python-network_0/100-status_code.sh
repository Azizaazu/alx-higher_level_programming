#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument, and displays
curl -s -o /dev/null -w "%{http_code}" "$1"
