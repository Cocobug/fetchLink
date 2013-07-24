# -*- coding: utf-8 -*-
#
#  verbose.py
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

def bck_message(parsr,website,page_nb,nb,i,to_fetch,total_duration,verbosity):
	if verbosity==1:
		print "  > Processing page {} of {}".format(page_nb+1,parsr.stop+1) # Index start at 0
		print "  > [NAME] ",website.get_page_number(to_fetch,page_nb)
	if parsr.verbose>1 and verbosity==2:
		print "  > [ID]",nb
def bck_init_tty(parsr,website):
	return (parsr.stop-parsr.start+1)*website.post_per_page


try:
	from blessings import Terminal
	term = Terminal()
	if not term.is_a_tty: raise GTFOError
	empty="{:<"+str(term.width)+"}"
	def message(parsr,website,page_nb,nb,i,to_fetch,total_duration,verbosity):
		global line
		if parsr.verbose>0:
			with term.location(0,term.height-4):
				if parsr.verbose==2 and nb!=0: print " "*80
				print empty.format("  > Processing page {} of {}".format(page_nb+1,parsr.stop+1)) # Index start at 0
				print empty.format("  > [NAME] "+website.get_page_number(to_fetch,page_nb))
				print ""
		if parsr.verbose>1:
			with term.location(0,term.height-5):
				if nb!=0: print empty.format("  > [ID] "+str(nb))
				print ""
		if term!=None:
			with term.location(0,term.height-2):
				print "Downloading pictures [{:<40}] {:.1%} ({}/{})".format("#"*(40*i/total_duration),i*1./total_duration,i,total_duration)
	def init_tty(parsr,website):
		lines=1
		if parsr.verbose>0: lines+=2
		for i in xrange(lines): print ""
		return (parsr.stop-parsr.start+1)*website.post_per_page
except:
	message=bck_message
	init_tty=bck_init_tty
