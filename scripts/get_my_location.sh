#!/bin/bash
echo "Getting my local ip "
	rm my_location.txt
	ifconfig wlan0 | grep -w "inet" >> my_location.txt
	iwconfig wlan0 | grep -e ESSID >> my_location.txt
	python3 parse_info.py
