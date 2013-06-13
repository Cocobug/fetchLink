#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tools.py
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

def build_request(adress,t_tags,tags):
	if len(tags)==0: return adress
	adress+=t_tags+tags.pop()
	for t in tags:	adress+='+'+t
	return adress

def make_link(webs,link):
	return webs+link

def get_page_number(page,txt,nb,post_per_page):
	if nb==0: return page
	return page+txt+str(nb*post_per_page)

def find_next_picture(page,img_max):
	for link in page.find_all("a"):
		try:
			lk=link.img#find_next('img',attrs={'class':'preview'})
			if lk:
				
				pict=lk.get('src')
				lk=link.get("href")
				nb=lk[lk.rfind("&")+4:]
				yield nb,lk,pict
				if nb in img_max:
					break
		except:
			continue
