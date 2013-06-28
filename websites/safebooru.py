# -*- coding: utf-8 -*-
#
#  safebooru.py
#  
#  Copyright 2012 Maximilien Rigaut <max[dot]rigaut[at]orange.fr>
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

t_base_website="http://safebooru.org"
t_website=t_base_website+"/index.php?page=post&s=list"

t_tag="&tags="
t_npage="&pid="
post_per_page=40
delete_link="<a href='{}/public/remove.php?id={}&amp;removepost=1&amp;delete=no&amp;reason={}' target='_blank'>Delete</a>"

def make_delete_link(pict):
	return delete_link.format(t_base_website,pict,("Questionnable - SAD (Script Assisted Deletion)"))

def build_request(tags):
	adress=t_website
	if len(tags)==0: return adress
	adress+=t_tag+tags[0]
	for t in tags[1:]:	adress+='+'+t
	return adress

def make_link(link):
	return t_website+link

def get_page_number(page,nb):
	if nb==0: return page
	return page+t_npage+str(nb*post_per_page)

def find_next_picture(page,max_image):
	for link in page.find_all("a"):
		try:
			lk=link.img#find_next('img',attrs={'class':'preview'})
			if lk:
				pict=lk.get('src')
				lk=link.get("href")
				nb=lk[lk.rfind("&")+4:]
				yield nb,lk,pict
		except GeneratorExit:
			return
		except:
			pass
