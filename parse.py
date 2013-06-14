#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parse.py
#  
#  Copyright 2013 Maximilien Rigaut <max[dot]rigaut[at]orange.fr>
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

import sys

class parseR(object):
	"It's not an object, just a var container"
	def __init__(self):
		self.mx=0
		self.start_page=0
		self.max_page=3
		self.tags=[]
		self.save_name="dl"
		self.check=0
		
def parse_vars(args):
	if len(args)<3: gtfo()
	prs=parseR()
	try:
		prs.max_page=int(args[1])
		for v in args[2:]:
			if v[0] == '?':
				prs.mx=v[1:]
			else:
				if v[0] == '%':
					prs.start_page=int(v[1:])
				else: 
					if v[0]=='@':
						prs.check=1
					else: prs.tags.append(v)
	except:
		gtfo()
	prs.tags.sort()
	for tag in prs.tags:
		prs.save_name+='_'+tag
	prs.save_name+='_{}_{}.html'.format(prs.start_page+1,prs.max_page)
	return prs

def gtfo():
	print "Invalid number of args: Usage ./fetchLink <nbPagesToFetch> <listOfTags> [?imageMax] [%pageToStartWith] [@]"
	sys.exit()
