# -*- coding: utf-8 -*-
#
#  danbooru.py
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


t_base_website="http://danbooru.donmai.us"
t_website=t_base_website+"/posts"
message="Have fun"

import safebooru as model
model.t_base_website=t_base_website
model.t_website=t_website

t_tag=model.t_tag
t_npage="&page="
post_per_page=20

#delete_link=model.delete_link
def build_request(tags):
	adress=t_website
	if len(tags)==0: return adress
	adress+=t_tag+tags[0]
	for t in tags[1:]:	adress+='+'+t
	return adress

make_link=model.make_link

def get_page_number(page,nb):
	if nb==0: return page
	return page+t_npage+str(nb)

find_next_picture=model.find_next_picture
