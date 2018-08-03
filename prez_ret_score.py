#!/usr/bin/env python

# ************************************************************
# Retrieves score from database and prints it out as a table
# $Id: prez_ret_score.py,v 1.17 2017/12/07 19:26:45 tsiang Exp $
# ************************************************************

import os
import os.path
import cgi
import MySQLdb
import sys
import subprocess
import logging
import Cookie
from ConfigParser import SafeConfigParser

# Recover email address either from cgi (if calling page is index.html)
# Else get it from session_id lookup (if calling page is prez_html which means we are logged in)

FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(filename="log/prez_ret_score.log", format=FORMAT, level=logging.DEBUG)

form = cgi.FieldStorage()

for key in form.keys():
        variable = str(key)
        value=str(form.getvalue(variable))
        if variable == "Email" :
                if value != "lookmeup":
                        email_address=value
                else:
                        # Get cookie sent by client and extract the session ID that is set on login
                        # Note that we only trust the session ID, even though email address is in the HTTP cookie
                        # It could have been forged by the user.
                        http_cookies_1= os.environ["HTTP_COOKIE"]
                        C=Cookie.SimpleCookie(http_cookies_1)
                        session_id=C['PHPSESSID'].value
                        
                        f=open('/home/tsiang/WWW/tmp/sess_%s' % session_id)
                        s=f.readline()
                        # session record is of form:
                        #loginEmail|s:19:"tsiang888@gmail.com";uid|s:4:"8206";
                        
                        # find 'loginEmail|s and cursor past it by adding in length of 'loginEmail|s'
                        lcursor=s.find('loginEmail|s:')+12 
                        # find first " after that, and add 1 to cursor past the "
                        lcursor+= s[lcursor:].find('"')+1
                        # find next " after that as the right cursor
                        rcursor=s[lcursor:].find('"')
                        #email address is now the substring (slice) between the right and left cursors
                        email_address= s[lcursor:rcursor+lcursor]
        else:
                email_address="Error in email_address"
                
#subprocess.call("./prez_score.py", shell=True)

logging.warning(email_address)

print "Content-Type: text/html\n"

hdr="""
<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <LINK href="prez_main_style.css" rel="stylesheet" type="text/css">
    <title> Presidential Primaries Prediction </title>

<LINK href="prez_main_style.css" rel="stylesheet" type="text/css">
</head>
<body>
"""

# retrieve score values

parser = SafeConfigParser()
parser.read('prez.ini')

master_email=parser.get('prez', 'master_email')
db_host=parser.get('prez', 'db_host')
db_username=parser.get('prez','db_username')
db_password=parser.get('prez', 'db_password')
db=parser.get('prez', 'db')

con=MySQLdb.connect(db_host,db_username,db_password,db)

rows=[]
scores=[]
user_records=[]

with con:
        cur = con.cursor()
	cur.execute("SELECT * FROM Scores ORDER BY Total_Score DESC, Timestamp")
        scores=cur.fetchall()

print hdr
print "<br>"

#print "<H1> OVERALL LEADERBOARD </H1>"

print """<table style="margin-left:50px" summary="Leaderboard" class="sofT" cellspacing="0">"""
print """<tr><td colspan="8" class="helpHed">LEADERBOARD</td></tr>"""
print """<tr><td class="helpHed">Rank<td class="helpHed">Nickname<br>(Click to<br>see bracket)</td><td class="helpHed"> # of correct <br> Democratic <br>primary  winners<br></td>"""
print """<td class="helpHed"># of correct  <br> Republican <br>primary winners</td>"""
print """<td class="helpHed"># of correct  <br> nomination and <br>election winners</td><td class="helpHed">President</td>"""
print """<td class="helpHed">Points</td><td class="helpHed">Date / Time submitted</td></tr>"""

rank=1
for i in scores:
        if i[0] != master_email :
	        print "<tr>"
                cur.execute("SELECT * FROM user WHERE email='%s' " % i[0])
                user_records=cur.fetchall()
                nickname=user_records[0][3]
                # style row that contains the user in red
                if i[0] == email_address :
                        td_style_name="sup2"
                        td_style_bod="helpBod2"
                else :
                        td_style_name="sup"
                        td_style_bod="helpBod"
	        print '<td class="%s">' % td_style_bod,rank,'</td>'
                print '<td class="%s">' % td_style_name,'<a href="prez_user_display.py?nickName=%s">' % nickname,nickname,'</td>'               
                print '<td class="%s">' % td_style_bod, str(i[2]), "</td>"
                print '<td class="%s"> ' % td_style_bod, str(i[3]), "</td>"
                print '<td class="%s">' % td_style_bod, str(i[4]), "</td>"
                print '<td class="%s">' % td_style_bod, str(i[5]), "</td>"
                print '<td class="%s">' % td_style_bod, str(i[6]), "</td>"
                print '<td class="%s">' % td_style_bod, str(i[1]), "</td>"
	        print "</tr>"
                rank=rank+1

print "</table>"
print '</body></html>'
