#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  htcreate.py
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


def hCreate(name):
	return open(name,"w+")

def hClose(name):
	name.close()

def hHeader(f):
	f.write("<!DOCTYPE html><html><body> ")

def hAddline(f,text,pict):
	f.write("\n<a href='{}'> <img src='{}'></a>".format(text,pict))

def hFooter(f):
	f.write("</body></html>")
