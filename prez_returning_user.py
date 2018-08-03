#!/usr/bin/env python
# ***************************************
# Returning user screen
# Displays an retriieved bracket for a user to inspect/modify
# 
# $Id: prez_returning_user.py,v 1.26 2018/08/03 21:51:43 tsiang Exp $
# *********************************************

import os
import sys
import cgi
import prez_html
import prez_ret_sql
import logging
import Cookie
import urllib
import MySQLdb
from ConfigParser import SafeConfigParser

FORMAT = '%(asctime)s  %(message)s'
logging.basicConfig(filename="log/prez_returning_user.log", format=FORMAT, level=logging.DEBUG)

nl = "\n"

#email_address="tripped888@employees.org"
#email_address="tsiang888@employees.org"
email_address="master@master.com"
#email_address="tsiang888@gmail.com"

# Get cookie sent by client and extract the session ID that is set on login
# Note that we only trust the session ID, even though email address is in the HTTP cookie
# It could have been forged by the user.
http_cookies_1= os.environ["HTTP_COOKIE"]
C=Cookie.SimpleCookie(http_cookies_1)
session_id=C['PHPSESSID'].value

#print "Content-Type: text/html\n"
f=open('/home/tsiang/WWW/tmp/sess_%s' % session_id, 'r')
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

logging.warning(email_address)

debug=0
print "Content-Type: text/html\n"
parser = SafeConfigParser()
parser.read('prez.ini')

master_email=parser.get('prez', 'master_email')
db_host=parser.get('prez', 'db_host')
db_username=parser.get('prez','db_username')
db_password=parser.get('prez', 'db_password')
db=parser.get('prez', 'db')


con=MySQLdb.connect(db_host,db_username,db_password,db)

with con:
    cur=con.cursor()
    cur.execute("select nickName from user where email=%s", (email_address,))
    r=cur.fetchall()


for i in r:
    username=i[0]
    logging.warning("username:%s",username)


print prez_html.get_html(email_address)
print "</form>"


print '<script src="prez_js.js"></script>'
print '<script src="disable_primary.js"></script>'
print "<script>"
print 'Set_Select_Options();'

sql_objects=prez_ret_sql.Get_Objects(email_address)


# Note: already within a <script> 
if (sql_objects['state_rep_js_obj']==""):
    print "Init_Predictions();"
    print sql_objects['nickname_js_obj'], nl
    if (debug==1):
        print "alert('first_time_user!!');"
else:
    if (debug==1):
        print "alert('returning_user!!');"
    # print out to html javascript variables retrieved from prez_ret_sql.Get_Objects
    # from user as well as from master (so we can do color coding in Set_Predictions
    # for those races that have already concluded
    print sql_objects['state_rep_js_obj'], nl
    print sql_objects['state_dem_js_obj'], nl
    print sql_objects['state_win_js_obj'], nl
    print sql_objects['pres_win_js_obj'], nl
    print sql_objects['m_state_rep_js_obj'], nl
    print sql_objects['m_state_dem_js_obj'], nl
    print sql_objects['m_state_win_js_obj'], nl
    print sql_objects['m_pres_win_js_obj'], nl
    print sql_objects['nickname_js_obj'], nl

print 'display_text_n="Welcome back " + nickname; $("#pNickname").text(display_text_n);'

# disable modifying primary picks if past lock date
if (email_address != master_email):
    print "disable_primary();"

# set selectors to initial predictions
print "Set_Predictions();"

print "</script>"
# print """<p style="clear:left"></p>"""
print "</body>"
print "</html>"
