#!/bin/bash

#java LongLexTo [input text file] [output csv file]

max=11
javac LongLexTo.java
for i in `seq 1 $max`
do
	java LongLexTo "sample/sample$i.txt" "wordcut/wordcut$i.csv"
    echo "LongLexTo sample/sample$i.txt wordcut/wordcut$i.csv"
done
