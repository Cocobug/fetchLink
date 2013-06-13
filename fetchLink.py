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
from html import *
from tools import *
from parse import *

from bs4 import BeautifulSoup

############
# Website skeleton

# Constructing url
t_website="http://safebooru.org/index.php?page=post&s=list"
t_tag="&tags="

# Fetching new page

t_npage="&pid="
post_per_page=20

############
# Fetching vars
parsr=parse_vars(sys.argv)
l_tags=parsr.tags
pages_to_process=parsr.max_page
start_page=parsr.start_page

# Saving results
save_name=parsr.save_name

to_fetch=build_request(t_website,t_tag,l_tags)

#########
# Html creation

# Initialisation
ht=hCreate(save_name)
hHeader(ht)

# Parsing
for nb in xrange(start_page,pages_to_process):
	print "Processing page {} of {}".format(nb+1,pages_to_process)
	active=0
	#print get_page_number(to_fetch,t_npage,nb,post_per_page)
	r=requests.get(get_page_number(to_fetch,t_npage,nb,post_per_page))
	r.raise_for_status()
	text=r.text
	
	#with open(save_name) as r: text=unicode(r.read())
	
	soup=BeautifulSoup(text,"html5lib")
	for nb,link,pict in find_next_picture(soup):
		hAddline(ht,nb,make_link(t_website,link),pict,make_delete_link(t_website,nb))
		
# Finishing
hFooter(ht)
hClose(ht)

