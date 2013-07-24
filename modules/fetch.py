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

import os,sys,logging,requests,random
from bs4 import BeautifulSoup
import parse, html, save,verbose
from tools import *

#############################
# Fetching of results
############
def fetch_it(parsr,website):
	firstid,page_nb,i,nb,find_id=None,parsr.start,0,0,False
	parsr=parse.update(parsr) # Update the values
	html.update(parsr,website) # Prettify according to arguments
	if parsr.no_blessings: init_tty,message=verbose.bck_init_tty,verbose.bck_message
	else: init_tty,message=verbose.init_tty,verbose.message
	save_name=parsr.save_name
	to_fetch,listIdParsed=website.build_request(parsr.tags),[]
	
	print 'Results will be saved in "'+save_name+'.html"'
	ht=html.hCreate(save_name)
	html.hHeader(ht)
	
	def post_operations():
		parsr.stop=page_nb
		parse.name(parsr)
	
	def new_page(ht):
		end=parsr.stop
		post_operations()
		html.hFooter(ht)
		html.hClose(ht,save_name,parsr.save_name)
		parsr.stop=end
		parsr.start=page_nb
		parse.name(parsr)
		ht=html.hCreate(parsr.save_name)
		html.hHeader(ht)
		return ht
	
	total_duration=init_tty(parsr,website)
	try:
		for page_nb in xrange(parsr.start,parsr.stop+1):
			parsr.wait_fn(parsr)
			found,r=False,requests.get(website.get_page_number(to_fetch,page_nb))
			r.raise_for_status()
			soup=BeautifulSoup(r.text,"html5lib")
			message(parsr,website,page_nb,0,i,to_fetch,total_duration,1)
			for nb,link,pict in website.find_next_picture(soup,parsr.find):
				found,i=True,i+1
				message(parsr,website,page_nb,nb,i,to_fetch,total_duration,2)
				if firstid==None:
					save.save(parsr,nb)
					firstid=nb
				if parsr.check_links: # Find a better testing
					tst=requests.head(pict)
					if tst.status_code>=300: continue
				if nb not in listIdParsed: # Maybe it's getting useless...
					html.hAddline(ht,nb,link,pict,website,parsr)
					listIdParsed.append(nb)
				else:
					print "Error on pict",i,nb
				if nb==parsr.find:
					print "Found {}, exiting search".format(nb)
					find_id=True
					raise GTFOError
				if parsr.split!=0:
					if i%parsr.split==0:
						parsr.img_nb=i
						ht=new_page(ht)
						save_name=parsr.save_name
			if not found: 
				page_nb-=1
				print "  > [PAGE {}] No pictures were fetch".format(page_nb+1)
				raise GTFOError	
	except GTFOError:
		post_operations()
	except KeyboardInterrupt:
		print "Not cool... you killed me dude, NOT cool..."
		post_operations()
	except:
		logging.exception("Unknown error")
	
	# Finishing
	if parsr.verbose>0:
		message(parsr,website,page_nb,nb,i,to_fetch,total_duration,1)
		if parsr.find>0 and not find_id: print "  > [FIND] Couldn't find id",parsr.find
	html.hFooter(ht)
	html.hClose(ht,save_name,parsr.save_name)
