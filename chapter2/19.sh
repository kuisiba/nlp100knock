#! /bin/sh

cut -f 1 chapter2/hightemp.txt | sort | uniq -c | sort -r
