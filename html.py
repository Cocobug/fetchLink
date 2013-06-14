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
	
	<table border="0" cellpadding="20" style="text-align:center;">
			<th> # </th>
		<th>Thumbnail</th>
		<th> Delete link </th>
			""")

def hAddline(f,num,text,pict,delete_link):
	f.write("""\n<tr>
		<td> {} </td>
		<td><a href='{}' target="_blank"> <img src='{}' onerror="imgError(this);"></a></td>
		<td> {} </td>
	</tr>
""".format(num,text,pict,delete_link))

def hFooter(f):
	f.write("</center></table></body></html>")
