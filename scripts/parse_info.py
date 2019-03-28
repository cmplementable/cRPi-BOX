import re

with open("my_location.txt") as f:
	ip = f.readline()
	ip = re.findall(r'\S+', ip)
	ip = ip[1]
	print("My local IP is:", ip)
	wifi = f.readline()
	wifi = re.findall(r'\S+', wifi)
	wifi = wifi[3]
	print(wifi)
