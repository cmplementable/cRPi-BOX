#!/bin/bash
echo "Getting my local ip "
echo "Getting my local ip " >> my_ip.txt
	ifconfig wlan0 | grep -w "inet"
