#!/bin/bash

#python nounphrase [input wordcut csv file] [output csv file]

max=9
for i in `seq 1 $max`
do
	python nounphrase.py wordcut/wordcut$i.csv output/output$i.csv
    echo "python nounphrase.py wordcut/wordcut$i.csv output/output$i.csv"
done
