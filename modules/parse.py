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

# Replace all dangerous characters
tr_dict={"*":"%2a",">":"%3e","<":"%3c",":":"%3a",'/':''}

parser = argparse.ArgumentParser(description='Fetch all images from a website.')

commons = argparse.ArgumentParser(add_help=False)
commons.add_argument('--start','-s', type=int, help='the page to start with',default=0)
commons.add_argument('--find', type=int, help='the id of the picture to look for')
commons.add_argument('--name', help='custom name (you can use {tags}, {start} and {stop})',default='dl_{tags}{start}_{stop}.html')
commons.add_argument('--check-links', help='check for online existence',action='store_true')
commons.add_argument('--verbose','-v', help='degree of verbosity',action='count')
commons.add_argument('--website', help='website to fetch from',default=0)
commons.add_argument('--admin-tools', help='add the tools for administration',action='store_true')
#parser_fetch.add_argument('--pretty', help='custom css')
commons.add_argument('--fetch-pictures', help='fetch the picture and save them in a folder',action='store_true')
commons.add_argument('--fetch-thumbnails', help='fetch the thumbs and save them in a folder',action='store_true')

subparsers = parser.add_subparsers(dest='action',help="List of available actions")
parser_fetch = subparsers.add_parser('fetch', help='Fetch pictures',parents=[commons])
parser_fetch.add_argument('nb_pages', type=int,help='number of pages to process', nargs=1)
parser_fetch.add_argument('tags', help='the list of tags to append', nargs='*')

parser_hist = subparsers.add_parser('history', help='Show the history of the previous commands',parents=[commons])
parser_upda = subparsers.add_parser('update', help='Rerun an old command, with the possibility to change some options',parents=[commons])


def name(prs):
	name=''
	for tag in prs.tags:
		name+=make_site_compliant(tag)+'_'
	prs.save_name=prs.name.format(tags=name,start=prs.start,stop=prs.stop)
	prs.save_name=os.path.join("html",prs.save_name)
	
def update(prs):
	prs.nb_pages=prs.nb_pages[0]-1 # Index starts to 0
	prs.tags.sort()
	prs.stop=prs.start+prs.nb_pages
	name(prs)
	return prs

def make_site_compliant(txt):
	res=""
	for l in txt:
		try: res+=tr_dict[l]
		except: res+=l
	return res
