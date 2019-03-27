#!/bin/bash
while [ 1 = 1 ]
do
echo "Scanned at " $(date)
echo "Scanned at " $(date) >> scan.txt
	iwlist wlan0 scan | grep -e ESSID -e Addres -e WPA -e WEP -e None >> scan.txt
	sleep 5
done
