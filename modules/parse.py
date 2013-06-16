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

import sys,os

class parseR(object):
	"It's not an object, just a var container"
	def __init__(self):
		self.mx=0
		self.start_page=0
		self.max_page=3
		self.tags=[]
		self.check=0
	def name_me(self):
		self.save_name="dl"
		self.tags.sort()
		for tag in self.tags:
			self.save_name+='_'+tag
		self.save_name+='_{}_{}.html'.format(self.start_page+1,self.max_page)
		self.save_name=os.path.join("html",self.save_name)
def parse_vars(args,di):
	if len(args)<2: gtfo()
	prs=parseR()
	try:
		prs.max_page=int(args[1])
		for v in args[2:]:
			if v[0] == '?':
				prs.mx=v[1:]
				continue
			if v[0] == '%':
				prs.start_page=int(v[1:])
				continue
			if v[0]=='@':
				prs.check=1
				continue
			prs.tags.append(make_site_compliant(v,di))
	except:
		gtfo()
	prs.max_page+=prs.start_page
	prs.name_me()
	return prs

def make_site_compliant(txt,tr_dict):
	"Dict must assotiate no more than one symbol to a string"
	res=""
	for l in txt:
		try:
			res+=tr_dict[l]
		except:
			res+=l
	return res
	
def gtfo():
	print "Invalid number of arguments: Usage ./fetchLink <nbPagesToFetch> <listOfTags> [?imageMax] [%pageToStartWith] [@]"
	sys.exit()
