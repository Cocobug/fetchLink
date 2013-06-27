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


t_base_website="http://gelbooru.com"
t_website=t_base_website+"/index.php?page=post&s=list"

import safebooru
safebooru.t_base_website=t_base_website
safebooru.t_website=t_website

t_tag=safebooru.t_tag
t_npage=safebooru.t_npage
post_per_page=safebooru.post_per_page

# To delete
t_dlt="<a href='{}/public/remove.php?id={}&amp;removepost=1&amp;delete=no&amp;reason={}' target='_blank'>Delete</a>"
def make_delete_link(pict):
	return t_dlt.format(t_base_website,pict,("Questionnable - SAD (Script Assisted Deletion)"))

build_request=safebooru.build_request
make_link=safebooru.make_link
get_page_number=safebooru.get_page_number
find_next_picture=safebooru.find_next_picture
