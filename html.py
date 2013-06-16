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

import random
liste_messages=["Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","Have fun.","Good luck.","Courage.","You can do it.","I believe in you.","I have faith in you.","Carry on, you're on the good way.","Carry on, you're on the good way.","Never give up.","Moderators are Safebooru's defensors.","Slayerduck and me are relying on you.","We, the moderation team, are Safebooru's only hope to be totally safe one day.","You're not paid for what you're doing with money, but with all our love.","Carry on privates, you wanna live forever ?","Moderator One Kennoby you are our only hope."]
message=random.choice(liste_messages)

version='0.2a'
t_dlt="<a href='{}/public/remove.php?id={}&amp;removepost=1&amp;delete=no&amp;reason={}' target='_blank'>Delete</a>"
def make_delete_link(web,pict):
	return t_dlt.format(web,pict,("Questionnable - SAD (Script Assisted Deletion)"))

def hCreate(name):
	return open(name,"w+")

def hClose(name):
	name.close()

def hHeader(f):
	f.write("""<!DOCTYPE html><html><body style="font-family:helvetica;"><center>
	<script type="text/javascript">
    function imgError(image) {
        image.parentNode.parentNode.innerHTML="<strike>Picture deleted</strike>";
        return true;
    }
    </script>
	<div style="font-size:42px; padding-top:30px; color:#0000EE;"><b>fetchLink.py</b></div>
	<div style="font-size:14.2px; padding-bottom:30px;">{message}</div>
	
	<table border="0" cellpadding="20" style="text-align:center;">
			<th> # </th>
		<th>Thumbnail</th>
		<th> Delete link </th>
	""".format(message=message))

def hAddline(f,num,text,pict,delete_link):
	f.write("""\n<tr>
		<td> {} </td>
		<td><a href='{}' target="_blank"> <img src='{}' onerror="imgError(this);"></a></td>
		<td> {} </td>
	</tr>
	""".format(num,text,pict,delete_link))

def hFooter(f):
	f.write("</center></table></body></html>")
