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
lines=[]
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

def loadlines():
	try:
		f=open(save_file)
		line,ln=f.readline(),0
		while line!='':
			lines.append(line[:-1])
			line,ln=f.readline(),ln+1
		return lines,ln
	except IOError:
		print "No history file to load..."
	except:
		logging.exception("Unknown")

def list(parser,website):
		lines,ln=loadlines()
		if parser.nb_lines[0]>0: mi,ma=0,parser.nb_lines[0]
		else: mi,ma=ln+parser.nb_lines[0],ln
		for i in xrange(max(mi,0),min(ma,ln)):
			print i,lines[-i]
		f.close()

def load(parser,website):
	# Initializing
	number=parser.number[0]
	lines,nb=loadlines()
	# Checking
	if number<0: number=nb-number
	if number>nb or number<0: print "This history line doesn't exist"
	# Loading variables
	line=lines[number].split('\t')
	model=save_patern[1:-2].split('}\t{')
	# Processing
	for i in xrange(len(line)):
		print model[i],line[i]
		parser.__setattr__(model[i],line[i])
	parser.nb_pages=[parser.stop-parser.start+1]
	return parser,website
