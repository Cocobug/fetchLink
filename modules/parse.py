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

import sys,os
import argparse


parser = argparse.ArgumentParser(description='Fetch all images from a website.')
subparsers = parser.add_subparsers(help='Modules')

parser_fetch = subparsers.add_parser('fetch', help='Fetch the pictures')
parser_fetch.add_argument('nb_pages', type=int,help='number of pages to process', nargs=1)
parser_fetch.add_argument('tags', help='the list of tags to append', nargs='*')
parser_fetch.add_argument('--start', type=int, help='the page to start with',default=0)
parser_fetch.add_argument('--find', type=int, help='the id of the picture to look for')
parser_fetch.add_argument('--name', help='custom name (you can use <tags>, <start>, <stop> and <id>)',default=0)
parser_fetch.add_argument('--check-links', help='check for online existence',action='store_true')
parser_fetch.add_argument('--website', help='website to fetch from',default=0) #choices=['rock', 'paper', 'scissors']
parser_fetch.add_argument('--admin-tools', help='add the tools for administration',action='store_true')
#parser_fetch.add_argument('--pretty', help='custom css')
parser_fetch.add_argument('--fetch-pictures', help='fetch the picture and save them in a folder',action='store_true')
parser_fetch.add_argument('--fetch-thumbnails', help='fetch the thumbs and save them in a folder',action='store_true')


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

if __name__=='__main__':
	print parser.parse_args()
