#!/bin/bash
echo "Getting my local ip "
	ifconfig wlan0 | grep -w "inet" >> my_ip.txt
