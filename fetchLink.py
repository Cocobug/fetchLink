#!/usr/bin/env python
# -*- coding: utf-8 --
#
#  main.py
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

import os,sys
import logging
from bs4 import BeautifulSoup

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR,'modules'))

import parse
import fetch



############
# Modules to be implemented
def history(p,w):
	print "Not implemented yet"
	
def repeat(p,w):
	print "Not implemented yet"

###################
# Website skeleton
class Website(object):
	pass

actions={'fetch':fetch.fetch_it,'history':history,'repeat':repeat}
parser=parse.parser.parse_args()
website=Website()
actions[parser.action](parser,website)
