#!/bin/bash

while [ true ]; do
     rec -q -c 1 -r 16000 current.wav silence 1 0.3 3% 1 0.3 3%
     flac -f -s current.wav -o current.flac
     php textfromgoogle.php >voice.txt
done

