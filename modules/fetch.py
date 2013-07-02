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
import parse, html, save
from tools import *
import logging
import requests

# Verbosity 
try:
	from blessings import Terminal
	term = Terminal()
	if not term.is_a_tty: raise GTFOError
	empty="{:<"+str(min(term.width,80))+"}"
	def message(parsr,website,page_nb,nb,i,to_fetch,total_duration):
		global line
		if parsr.verbose>0:
			with term.location(0,term.height-4):
				if parsr.verbose==2 and nb!=0: print " "*80
				print empty.format("  > Processing page {} of {}".format(page_nb+1,parsr.stop+1)) # Index start at 0
				print empty.format("  > [NAME] "+website.get_page_number(to_fetch,page_nb))
				print ""
		if parsr.verbose>1:
			with term.location(0,term.height-5):
				if nb!=0: print empty.format("  > [ID] "+str(nb))
				print ""
		if term!=None:
			with term.location(0,term.height-2):
				print "Downloading pictures [{:<40}] {:.1%} ({}/{})".format("#"*(40*i/total_duration),i*1./total_duration,i,total_duration)
	def init_tty(parsr,website):
		lines=1
		if parsr.verbose>0: lines+=2
		#if parsr.verbose>1: lines+=website.post_per_page
		for i in xrange(lines): print ""
		return (parsr.stop-parsr.start+1)*website.post_per_page
except:
	def message(parsr,website,page_nb,nb,i,to_fetch,total_duration):
		if parsr.verbose>0:
			print "  > Processing page {} of {}".format(page_nb+1,parsr.stop+1) # Index start at 0
			print "  > [NAME] ",website.get_page_number(to_fetch,page_nb)
		if parsr.verbose>1:
			print "  > [ID]",nb
	def init_tty(parsr):
		return (parsr.stop-parsr.start+1)*website.post_per_page

def fetch_it(parsr,website):
	firstid,page_nb,i=None,0,0
	parsr=parse.update(parsr) # Update the values
	html.update(parsr,website) # Prettify according to arguments
	save_name=parsr.save_name
	print 'Results will be saved in "'+save_name+'"'
	to_fetch,listIdParsed=website.build_request(parsr.tags),[]
	ht=html.hCreate(save_name)
	html.hHeader(ht)
	def post_operations():
		parsr.stop=page_nb
		parse.name(parsr)
	
	total_duration=init_tty(parsr,website)
	
	if parsr.verbose>0: message(parsr,website,0,0,i,to_fetch,total_duration)
	try:
		for page_nb in xrange(parsr.start,parsr.stop+1):
			found,r=False,requests.get(website.get_page_number(to_fetch,page_nb))
			r.raise_for_status()
			soup=BeautifulSoup(r.text,"html5lib")
			if parsr.verbose>0: message(parsr,website,page_nb,0,i,to_fetch,total_duration)
			for nb,link,pict in website.find_next_picture(soup,parsr.find):
				found,i=True,i+1
				if parsr.verbose>1: message(parsr,website,page_nb,nb,i,to_fetch,total_duration)
				if firstid==None:
					save.save(parsr,nb)
					firstid=nb
				if parsr.check_links: # Find a better testing
					tst=requests.head(pict)
					if tst.status_code>=300: continue
				if nb not in listIdParsed: # Maybe it's getting useless...
					html.hAddline(ht,nb,link,pict,website,parsr)
					listIdParsed.append(nb)
				if nb==parsr.find:
					print "Found {}, exiting search".format(nb)
					raise GTFOError
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
	if parsr.verbose>0: message(parsr,website,page_nb,nb,i,to_fetch,total_duration)
	html.hFooter(ht)
	html.hClose(ht,save_name,parsr.save_name)
