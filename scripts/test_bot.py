#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_bot.py
#  
#  Copyright 2019 Piter Pentester
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#


import logging
import re
import os

from telegram.ext import Updater
from telegram.ext import  CallbackQueryHandler
from telegram.ext import  CommandHandler
from telegram import  ReplyKeyboardRemove


#import telegramcalendar


TOKEN = ""


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def get_ip_and_wifi():
    global ip
    global wifi
    #get info about ip and essid
    
    rm_my_location = 'rm my_location.txt'
    get_ip = 'ifconfig wlan0 | grep -w "inet" >> my_location.txt'
    get_essid = 'iwconfig wlan0 | grep -e ESSID >> my_location.txt'

    os.system(rm_my_location)
    os.system(get_ip)
    os.system(get_essid)
    
    try:
        with open("my_location.txt") as f:
            #ip
            ip = f.readline()
            ip = re.findall(r'\S+', ip)
            ip = ip[1]
            #wifi
            wifi = f.readline()
            wifi = re.split('"', wifi)
            wifi = wifi[1]
            print('My local IP is: ' + str(ip) + ' WIFI:' + str(wifi))
    except IndexError:
        sleep(3)
        get_ip_and_wifi()

def nmap_scan(target):
	nmap_simple = "nmap -vv " + target
	print(os.system(nmap_simple))


def location_handler(bot,update):
    get_ip_and_wifi()
    update.message.reply_text("Getting location: ")
    update.message.reply_text('My local IP is: ' + str(ip) + ' WIFI:' + str(wifi))

def start_handler(bot, update):
	update.message.reply_text("Now I can get my location, scan target with nmap. Type /my_location - to get location, /scan <ip> to scan target")
	
def help_handler(bot, update):
	update.message.reply_text("Use /my_location to get IP-address and Wi-Fi ESSID, /scan <target> to scan specific target!")
	
def scan_handler(bot, update):
	try:
		command = update['message']['text']
		command = command.split(" ")
		target = command[1]
		nmap_scan(target)
	except IndexError:
		print("Target not set!!!")
		update.message.reply_text("Target not set!!! Use /scan <ip>")

"""
def inline_handler(bot,update):
    selected,date = telegramcalendar.process_calendar_selection(bot, update)
    if selected:
        bot.send_message(chat_id=update.callback_query.from_user.id,
                        text="You selected %s" % (date.strftime("%d/%m/%Y")),
                        reply_markup=ReplyKeyboardRemove())
"""

if TOKEN == "":
    print("Please write TOKEN into file")
else:
    up = Updater(TOKEN)

    up.dispatcher.add_handler(CommandHandler("my_location",location_handler))
    up.dispatcher.add_handler(CommandHandler("start", start_handler))
    up.dispatcher.add_handler(CommandHandler("help", help_handler))
    up.dispatcher.add_handler(CommandHandler("scan", scan_handler))
    #up.dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    up.start_polling()
    up.idle()

