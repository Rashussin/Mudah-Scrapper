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

def main(args):
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
	print(len(link_script))
	#for data_text in link_script:
		#print(data_text.get_text()[27:])
	#link_script_data = json.loads()
	link_script_data = json.loads(link_script[2].get_text())
	print(link_script_data)
	
	
	
	return 0
	
	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
