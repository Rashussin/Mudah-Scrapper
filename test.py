#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2019 Wan Rashdan <Wan Rashdan@DESKTOP-GIM6MP2>
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
import json
import requests
#import bs4
from bs4 import BeautifulSoup
import smtplib
import array

def main(args):
	
	user="YourEmail@gmail.com"
	pwd ="Password"
	recepient_email = "recepient_email@gmail.com"
	
	res = requests.get('https://www.mudah.my/malaysia/cars-for-sale?lst=0&fs=1&q=kelisa&so=1&trm=1&pe=2')
	soup = BeautifulSoup(res.text, 'lxml')
	#type(res)
	#print(soup.find_all('title'))
	#print(soup.prettify())
	link_script = soup.find_all("script", type="application/ld+json")
	#link_container =  soup.find_all('div', class_ = 'footerline.listing_right.list_ads.list_big_thumbnail')
	
	#-----------------------------process response for div
	#print(type(link_container))
	#print(len(link_container))
	#for link in link_container:
		#print(link.get('id'))
		#print(link)
		
	#------------------------------process response script
	#print(len(link_script))
	#for data_text in link_script:
		#print(data_text.get_text()[27:])
	#link_script_data = json.loads()
	link_script_data = json.loads(link_script[2].get_text())
	i = 0
	msg = []
	
	for data in link_script_data['itemListElement']:
	#	print("Name :", data['name'])
	#	print("--- Price :","Price :",data['offers']['price'])
	#	print("--- URL   :", data['url'])
	#	print(" ")
		data_str = "Name :" + data['name'] + '\n' + "--- Price :RM" + data['offers']['price']+'\n' + "--- URL   :" + data['url']+'\n\n'
		msg.append(data_str)
		#print(msg[i])
		i = i + 1
	
	#print(msg)
	msg.append('Contact Me: \n https://github.com/syirasky \n https://www.facebook.com/ras.rizal.1')
	appended_msg = ''.join(msg)
	print(appended_msg)
	try:
		s = smtplib.SMTP('smtp.gmail.com',587)
		s.starttls()
		s.login(user,pwd)
		s.sendmail(user,recepient_email,'Subject: Mudah Scrapper (Syirasky)\n'+appended_msg)
		print("Email Sent")
	except smtplib.SMTPException:
		print("Error Occured")
	
	
	return 0
	
	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
