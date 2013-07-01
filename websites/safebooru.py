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

import random
t_base_website="http://safebooru.org"
t_website=t_base_website+"/index.php?page=post&s=list"

t_tag="&tags="
t_npage="&pid="
post_per_page=40
delete_link="<a href='{}/public/remove.php?id={}&amp;removepost=1&amp;delete=no&amp;reason={}' target='_blank'>Delete</a>"

list_messages=["Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","I believe in you.","I have faith in you.","Carry on, you're on the good way.","Carry on, you're on the good way.","Never give up.","Moderators are Safebooru's defensors.","Slayerduck and me are relying on you.","We, the moderation team, are Safebooru's only hope to be totally safe one day.","You're not paid for what you're doing with money, but with all our love.","Moderator One Kennoby you are our only hope.",]
message='<div style="font-size:14.2px; padding-bottom:30px;">'+random.choice(list_messages)+'</div>'

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
				nb=int(lk[lk.rfind("&")+4:])
				yield nb,lk,pict
		except GeneratorExit:
			return
		except:
			pass
