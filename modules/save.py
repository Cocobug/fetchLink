# -*- coding: utf-8 -*-
#
#  save.py
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

import logging

#fetch-pictures,fetch-thumbnails

save_file=".fl_history"
save_patern="{website}\t{start}\t{stop}\t{first_id}\t{find}\t{pretty}\t{admin_tools}\t{tags}\t{name}\n"

def save(parser,firstid):
	tags=""
	try:
		f=open(save_file,"a+")
		for tag in parser.tags:
			tags+=" "+tag
		f.write(save_patern.format(website=parser.website,start=parser.start,stop=parser.stop,find=parser.find,pretty=parser.pretty,admin_tools=parser.admin_tools,tags=tags,name=parser.name,first_id=firstid))
		f.close()
	except:
		logging.exception("Unknown")

def list(parser,website):
	try:
		f=open(save_file)
		for l in xrange(parser.nb_lines[0]):
			line=f.readline()
			if line=='' or line == "\n": return
			print l,line
	except IOError:
		print "No history file to load..."
	except:
		logging.exception("Unknown")

def load(number,website,parser): 
	pass
