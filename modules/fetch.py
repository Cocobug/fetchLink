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

import os,sys
from bs4 import BeautifulSoup
import parse
from html import *
from tools import *
import logging
import requests

# Constructing url
t_website="http://safebooru.org/index.php?page=post&s=list"
t_base_website=t_website[:t_website[7:].find('/')+7]
t_tag="&tags="
# Fetching new page
t_npage="&pid="
post_per_page=40
	
def fetch_it(parsr,website):
	parsr=parse.update(parsr) # Update the values
	save_name=parsr.save_name
	print 'Results will be saved in "'+save_name+'"'
	to_fetch=build_request(t_website,t_tag,parsr.tags)
	#########
	# Html creation
	listIdParsed=[]
	# Initialisation
	ht=hCreate(save_name)
	hHeader(ht)

	def post_operations():
		parsr.stop=page_nb+1
		parse.name(parsr)
		
	# Parsing
	try:
		for page_nb in xrange(parsr.start,parsr.stop):
			found=False
			if parsr.verbose>0:
				print "  > Processing page {} of {}".format(page_nb+1,parsr.stop)
				print "  > [NAME] ",get_page_number(to_fetch,t_npage,page_nb,post_per_page)
			r=requests.get(get_page_number(to_fetch,t_npage,page_nb,post_per_page))
			r.raise_for_status()
			text=r.text
					
			soup=BeautifulSoup(text,"html5lib")
			for nb,link,pict in find_next_picture(soup,parsr.find):
				if parsr.verbose>1: print "  > [ID]",nb
				found=True
				if parsr.check_links: # Find a better testing
					tst=requests.head(pict)
					if tst.status_code>=300: continue
				if nb not in listIdParsed:
					hAddline(ht,nb,make_link(t_website,link),pict,make_delete_link(t_base_website,nb))
					listIdParsed.append(nb)
				if nb==parsr.find: 
					if parsr.verbose>0: print "Found {}, exiting search".format(nb)
					raise GTFOError
			if not found: 
				if parsr.verbose>0: print "I'm afraid you've seen everyting there is to see"
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
