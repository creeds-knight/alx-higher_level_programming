#!/bin/bash
# sends Json POST to url and displays response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
