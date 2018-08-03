#!/usr/bin/env python
# ***************************************
# Returning user screen
# Displays an retriieved bracket for a user to inspect/modify
# 
# $Id: prez_sample_bracket.py,v 1.6 2017/12/08 16:59:39 tsiang Exp $
# *********************************************

import os
import cgi
import prez_html
import prez_ret_sql
import Cookie
import urllib
import MySQLdb
import sys
import logging
from ConfigParser import SafeConfigParser

FORMAT = '%(asctime)s  %(message)s'
logging.basicConfig(filename="log/prez_returning_user.log", format=FORMAT, level=logging.DEBUG)

nl = "\n"

debug=0
if (debug==0):
    print "Content-Type: text/html\n"

# if script is failing set debug=1 to see traceback in browser window
if (debug==1):
    sys.stderr = sys.stdout
    print "Content-Type: text/plain"
    print



parser = SafeConfigParser()
parser.read('prez.ini')

email_address=parser.get('prez', 'master_email')
db_host=parser.get('prez', 'db_host')
db_username=parser.get('prez','db_username')
db_password=parser.get('prez', 'db_password')
db=parser.get('prez', 'db')


#Example of a debug alert box - change to if(debug==0) to test
if (debug==2):
    print "<script> alert('Got here something ",db_host,"'); </script>"

con=MySQLdb.connect(db_host,db_username,db_password,db)

with con:
    cur=con.cursor()
    cur.execute("select nickName from user where email=%s", (email_address,))
    r=cur.fetchall()

for i in r:
    username=i[0]
    logging.warning("Displaying sample bracket of username:%s",username)

print """<br><p style="text-align: center; font-family: 'Droid Serif', serif; font-size: 40px; width: 1300px;"><b><u>SAMPLE BRACKET (CANNOT SAVE)</u></b></p>"""
print prez_html.get_html(email_address)
print "</form>"

print '<script src="prez_js.js"></script>'
print '<script src="disable_primary.js"></script>'
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


print "disable_primary();"

#print 'Disable_select();'
print 'hide_master_display_links();'
#print 'Remove_onclick();'            
print "Set_Predictions();"

print "</script>"

print "<H1> PREVIEW ONLY - LOGIN/REGISTER TO ENTER AND SAVE A BRACKET </H1>"
# print """<p style="clear:left"></p>"""
print "</body>"
print "</html>"
