#!/bin/bash

prev=/
curr=$(inotifywait -r -e 'modify,move,create,delete' -q --format %f .) 

#DEBUG
echo "il file preso in considerazione è $curr"

if [ curr != prev ];
then
    prev=$curr
    $curr>>cache.txt
fi
