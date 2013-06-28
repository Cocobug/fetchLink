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

import os,random

liste_messages=["Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","I believe in you.","I have faith in you.","Carry on, you're on the good way.","Carry on, you're on the good way.","Never give up.","Moderators are Safebooru's defensors.","Slayerduck and me are relying on you.","We, the moderation team, are Safebooru's only hope to be totally safe one day.","You're not paid for what you're doing with money, but with all our love.","Moderator One Kennoby you are our only hope.",]
message=random.choice(liste_messages)


header="""<!DOCTYPE html><html><body style="font-family:helvetica;"><center>
<script type="text/javascript">
function imgError(image) {
	image.parentNode.parentNode.innerHTML="<strike>Picture deleted</strike>";
	return true;
}
</script>
<div style="font-size:42px; padding-top:30px; color:#0000EE;"><b>fetchLink.py</b></div>
<div style="font-size:14.2px; padding-bottom:30px;">"""+message+"""</div>
"""
table="""<table border="0" cellpadding="20" style="text-align:center;">
<th> # </th>
<th>Thumbnail</th>
"""

picture="<a href='{link}' target='_blank'><img src='{pict}' onerror='imgError(this);'></a>"
footer="<p/><img src='python-powered.png'></center></body></html>"

def update(parser,website):
	global header,picture, footer,table
	if parser.pretty=="none":
		return
	if parser.pretty=="table":
		if parser.admin_tools and hasattr(website,'make_delete_link'):
			table+="<th> Delete link </th>"
		header+=table
		picture="<tr><td>{num}</td><td>"+picture+"</td>{delete}</tr>"
		website.delete_link="<td>"+website.delete_link+"</td>"
		footer="</table>"+footer
		return
	if parser.pretty=="css":
		raise NotImplemented

def hCreate(name):
	if not os.path.exists("html"):
		os.mkdir("html")
	return open(name,"w+")

def hClose(name,oldname,rename):
	name.close()
	if rename!=oldname:
		os.rename(oldname,rename)
		print 'Renamed to "'+rename+'"'

def hHeader(f):
	f.write(header)

def hAddline(f,num,link,pict,website,parser):
	if parser.admin_tools and hasattr(website,'make_delete_link'):
		delete=website.make_delete_link(pict)
	else: delete=""
	f.write(picture.format(num=num,link=website.make_link(link),pict=pict,delete=delete))

def hFooter(f):
	f.write(footer)
