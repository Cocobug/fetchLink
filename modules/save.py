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

import logging,argparse

def tags(tag):
	return tag.split(' ')
	
save_file=".fl_history"
save_patern="{website}\t{start}\t{stop}\t{first_id}\t{find}\t{pretty}\t{admin_tools}\t{tags}\t{name}\n"
save_type=[str,int,int,int,int,str,bool,tags,str]
lines=[]

def save(parser,firstid):
	tags=""
	try:
		f=open(save_file,"a+")
		for tag in parser.tags:
			tags+=tag+' '
		tags=tags[:-1]
		f.write(save_patern.format(website=parser.website,start=parser.start+1,stop=parser.stop,find=parser.find,pretty=parser.pretty,admin_tools=parser.admin_tools,tags=tags,name=parser.name,first_id=firstid))
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
		f.close()
		return lines,ln
	except IOError:
		print "No history file to load..."
		return None,None
	except:
		logging.exception("Unknown")

def list(parser,website):
		lines,ln=loadlines()
		if lines==None: return
		text="# "
		if parser.lines>0: mi,ma=0,parser.lines
		else: mi,ma=ln+parser.lines,ln
		for tag in save_patern[1:-2].split("}\t{"):
			text+=tag[:5]+".\t"
		print text
		for i in xrange(max(mi,0),min(ma,ln)):
			print i,lines[i]

def load(parsr,website,args):
	from parse import parser
	deflt={key:None for key in vars(parsr)}
	parser.set_defaults(**deflt)
	par=parser.parse_args(args[1:])
	number=parsr.number[0]
	lines,nb=loadlines()
	if lines==0: return
	if number<0: number=nb-number
	if number>nb or number<0: print "This history line doesn't exist"
	line=lines[number].split('\t')
	model=save_patern[1:-2].split('}\t{')
	for i in xrange(len(line)):
		try:val=save_type[i](line[i])
		except: pass
		if getattr(par,model[i],None)==None: setattr(par,model[i],val)
	par.nb_pages=[par.stop-par.start+1]
	print par
	return par
