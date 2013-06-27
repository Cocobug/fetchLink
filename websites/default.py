# -*- coding: utf-8 -*-
#
#  default.py
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

from importlib import import_module
import safebooru as website
import logging

default_name="safebooru"

def load_website(parser):
	if parser.website=="": parser.website=default_name
	try:
		return import_module('.'+parser.website,'websites')
	except:
		logging.exception("Website {} was not loaded".format(parser.website))
	
