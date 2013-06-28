# -*- coding: utf-8 -*-
#
#  fetch.py
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
import parse, html
from tools import *
import logging
import requests

# Constructing url
#t_website="http://safebooru.org/index.php?page=post&s=list"
#t_base_website=t_website[:t_website[7:].find('/')+7]
t_tag="&tags="
	
def fetch_it(parsr,website):
	parsr=parse.update(parsr) # Update the values
	html.update(parsr,website) # Prettify according to arguments
	save_name=parsr.save_name
	print 'Results will be saved in "'+save_name+'"'
	to_fetch=website.build_request(parsr.tags)
	listIdParsed=[]
	ht=html.hCreate(save_name)
	html.hHeader(ht)
	
	try:
		for page_nb in xrange(parsr.start,parsr.stop+1):
			found=False
			if parsr.verbose>0:
				print "  > Processing page {} of {}".format(page_nb+1,parsr.stop+1) # Index start at 0
				print "  > [NAME] ",website.get_page_number(to_fetch,page_nb)
			r=requests.get(website.get_page_number(to_fetch,page_nb))
			r.raise_for_status()
					
			soup=BeautifulSoup(r.text,"html5lib")
			for nb,link,pict in website.find_next_picture(soup,parsr.find):
				if parsr.verbose>1: print "  > [ID]",nb
				found=True
				if parsr.check_links: # Find a better testing
					tst=requests.head(pict)
					if tst.status_code>=300: continue
				if nb not in listIdParsed: # Maybe it's getting useless...
					html.hAddline(ht,nb,link,pict,website,parsr)
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
	html.hFooter(ht)
	html.hClose(ht,save_name,parsr.save_name)

def post_operations():
		parsr.stop=page_nb+1
		parse.name(parsr)
