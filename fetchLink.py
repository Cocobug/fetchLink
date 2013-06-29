#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from modules import parse,fetch,save
from websites import default as Website

############
# Modules to be implemented
	
def update(p,w):
	save.load(p,w)
	parser.find=parser.first_id
	website=Website.load_website(parser)
	actions["fetch"](parser,website)
	#print "Not implemented yet"

actions={'fetch':fetch.fetch_it,'history':save.list,'update':update}
parser=parse.parser.parse_args()
website=Website.load_website(parser)
actions[parser.action](parser,website)
