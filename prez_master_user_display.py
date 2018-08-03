#!/usr/bin/env python
# ***************************************
# Returning user screen
# Displays an retriieved bracket for a user to inspect/modify
# 
# $Id: prez_master_user_display.py,v 1.9 2017/12/08 17:05:08 tsiang Exp $
# *********************************************

import os
import cgi
import prez_html
import prez_ret_sql
import logging
import Cookie
import urllib
import MySQLdb
import logging
from ConfigParser import SafeConfigParser

FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(filename="log/prez_master_user_display.log", format=FORMAT, level=logging.DEBUG)

nl = "\n"

debug=0
print "Content-Type: text/html\n"
parser = SafeConfigParser()
parser.read('prez.ini')

email_address=parser.get('prez', 'master_email')
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
print """<p style="text-align: center; font-family: 'Droid Serif', serif; font-size: 36px; width: 1300px;"><b><u>ELECTION RESULTS</u></b></p>"""
print prez_html.get_html(email_address)
print "</form>"

# override select and <a> styling for master results display
print "<style>"
print "select {"
print "-webkit-appearance:none;"
print "text-align: center;"
print "border-color: transparent;"
print "color: black"
print "}"
print "a {"
print "text-decoration:none;"
print "}"
print "label[class^='state'] {"
print "cursor:default;"
print "}"
print "</style>"

print '<script src="prez_js.js"></script>'
print "<script>"
print 'Set_Select_Options();'

sql_objects=prez_ret_sql.Get_Objects(email_address)

if (sql_objects['state_rep_js_obj']==""):
    print "Init_Predictions();"
    if (debug==1):
        # already within a <script> so don't need to print it 
        print "alert('first_time_user!!');"
else:
    if (debug==1):
        # already within a <script> so don't need to print it 
        print "alert('returning_user!!');"
    print sql_objects['state_rep_js_obj'], nl
    print sql_objects['state_dem_js_obj'], nl
    print sql_objects['state_win_js_obj'], nl
    print sql_objects['pres_win_js_obj'], nl
    print sql_objects['m_state_rep_js_obj'], nl
    print sql_objects['m_state_dem_js_obj'], nl
    print sql_objects['m_state_win_js_obj'], nl
    print sql_objects['m_pres_win_js_obj'], nl

    print "Set_Predictions();"

print 'Disable_select();'
print 'hide_master_display();'
print 'hide_master_display_links();'
print 'Remove_onclick();'            
print "</script>"
# print """<p style="clear:left"></p>"""
print "</body>"
print "</html>"
