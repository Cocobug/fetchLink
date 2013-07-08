# -*- coding: utf-8 -*-
#
#  gelbooru.py
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
message="Have fun"

import safebooru as model
model.t_base_website=t_base_website
model.t_website=t_website

t_tag=model.t_tag
t_npage=model.t_npage
post_per_page=model.post_per_page

delete_link=model.delete_link
build_request=model.build_request
make_link=model.make_link
get_page_number=model.get_page_number
find_next_picture=model.find_next_picture
