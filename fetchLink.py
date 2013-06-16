#!/usr/bin/env python
# -*- coding: utf-8 --
#
#  main.py
#  
#  Copyright 2012 Maximilien Rigaut <max[dot]rigaut[at]orange.fr>
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

import requests
import os,sys
import logging

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR,'modules'))

from html import *
from tools import *
from parse import *

from bs4 import BeautifulSoup

############
# Website skeleton
# Constructing url
t_website="http://safebooru.org/index.php?page=post&s=list"
t_base_website=t_website[:t_website[7:].find('/')+7]
t_tag="&tags="
tr_dict={"*":"%2a",">":"%3e","<":"%3c",":":"%3a"}
# Fetching new page
t_npage="&pid="
post_per_page=20

############
# Fetching vars
parsr=parse_vars(sys.argv,tr_dict)
l_tags=parsr.tags
pages_to_process=parsr.max_page
start_page=parsr.start_page
check=parsr.check

# Saving results
save_name=parsr.save_name
print 'Results will be saved in "'+save_name+'"'
to_fetch=build_request(t_website,t_tag,l_tags)

#########
# Html creation
listIdParsed=[]
# Initialisation
ht=hCreate(save_name)
hHeader(ht)

def post_operations():
	parsr.max_page=page_nb+1
	parsr.name_me()

# Parsing
try:
	for page_nb in xrange(start_page,pages_to_process):
		found=False
		print "  > Processing page {} of {}".format(page_nb+1,pages_to_process)
		#print get_page_number(to_fetch,t_npage,nb,post_per_page)
		r=requests.get(get_page_number(to_fetch,t_npage,page_nb,post_per_page))
		r.raise_for_status()
		text=r.text
		
		#with open(save_name) as r: text=unicode(r.read())
		
		soup=BeautifulSoup(text,"html5lib")
		for nb,link,pict in find_next_picture(soup,parsr.mx):
			found=True
			if check:
				tst=requests.head(pict)
				if tst.status_code>=300:
					continue
			if nb not in listIdParsed:
				hAddline(ht,nb,make_link(t_website,link),pict,make_delete_link(t_base_website,nb))
				listIdParsed.append(nb)
			if nb==parsr.mx: 
				print "Found {}, exiting search".format(nb)
				raise GTFOError
		if not found: 
			print "I'm afraid you've seen everyting there is to see"
			raise GTFOError
except GTFOError:
	post_operations()
except KeyboardInterrupt:
	print "Not cool... you killed me dude, NOT cool..."
	post_operations()
except:
	logging.exception("Unknown error")

# Finishing
hFooter(ht)
hClose(ht,save_name,parsr.save_name)

