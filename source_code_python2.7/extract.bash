#!bin/bash

FILE=$1
cd /home/tengmo/crawler_to_server_set_time/crawler/store/
if [ -f $FILE"filter.arc" ]; then
	echo "File $FILE"filter.arc" exists"
else
	echo "No_file"
	echo " cd /home/tengmo/Desktop/Project crawler/file"
	echo "gunzip $FILE .arc.gz"
	echo "iconv -f utf-8 -t utf-8 -c cascsac > filter_...
fi
