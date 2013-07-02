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

parser = argparse.ArgumentParser(description='Fetch all, or some, images from a website.',usage="./%(prog)s fetch|history|update [options]")

commons = argparse.ArgumentParser(add_help=False)
commons.add_argument('--start','-s',metavar="#", type=int, help='the page to start with',default=0)
commons.add_argument('--find',metavar="ID", type=int, help='the id of the picture to look for (will abort upon finding)')
commons.add_argument('--name', help='custom name (you can use {tags}, {start}, {stop} and {site}, default is {site}_{tags}{start}_{stop}.html)',default='{site}_{tags}{start}_{stop}.html')
commons.add_argument('--check-links', help='check for online existence (longify)',action='store_true')
commons.add_argument('-v', help='degree of verbosity (none (default) displays almost nothing, -v displays useful infos, -v -v or -vv is debug mode)',action='count')
commons.add_argument('--website', help='website to fetch from (requires appropriate file in website/)',default="")
admin_tools = commons.add_mutually_exclusive_group()
admin_tools.add_argument('--admin-tools', help='add administration tools (you need to be already logged in via web browser)',action='store_true',default=True)
admin_tools.add_argument('--no-admin-tools',dest='admin_tools', help='forbid the tools for administration',action='store_false')
commons.add_argument('--pretty', help='customizing the output result',metavar="table|none",choices=["table","none"],default="table")
commons.add_argument('--fetch-pictures', help='fetch the picture and save them in a folder',action='store_true')
commons.add_argument('--fetch-thumbnails', help='fetch the thumbnails and save them in a folder',action='store_true')

subparsers = parser.add_subparsers(dest='action',help="List of available actions")
parser_fetch = subparsers.add_parser('fetch', help='Fetch pictures following arguments.',parents=[commons],usage="./fetchLink.py fetch nb_pages tags [options]")
parser_fetch.add_argument('nb_pages', type=int,help='number of pages to process', nargs=1)
parser_fetch.add_argument('tags', help='the list of tags to append', nargs='*')

parser_hist = subparsers.add_parser('history', help='Show the history of previous commands.',usage="./fetchLink.py history nb_lines")
parser_hist.add_argument('nb_lines', type=int,help='number of lines to load (negative values display lastest first)', nargs=1)

parser_upda = subparsers.add_parser('update', help='Rerun an old command, with or without changes.',
parents=[commons],usage="./fetchLink.py update nb_pages tags [options]")
parser_upda.add_argument('number', type=int,help='number of the line to show', nargs=1)

def name(prs):
	name=''
	for tag in prs.tags:
		name+=make_site_compliant(tag)+'_'
	prs.save_name=prs.name.format(tags=name,start=prs.start+1,stop=prs.stop+1,site=prs.website)
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
