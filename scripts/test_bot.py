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

import re
import os
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('ВАШ_ТОКЕН')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    

    while True:
        try:
            get_info()
            sleep(0.5)
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1



def echo(bot):
	
    """Echo the message the user sent."""
    
    
    global update_id

    
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            update.message.reply_text('My local IP is: ' + str(ip) + ' ' + str(wifi))

def get_info():
    global ip
    global wifi
    #global get_ip
    #global get_essid
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
            wifi = re.findall(r'\S+', wifi)
            wifi = wifi[3]
            print('My local IP is: ' + str(ip) + ' ' + str(wifi))
    except IndexError:
        sleep(3)
        get_info()

if __name__ == '__main__':
    main()
