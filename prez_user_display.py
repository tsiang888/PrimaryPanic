#!/usr/bin/env python
# ***************************************
# Returning user screen
# Displays a retrieved bracket
# 
# $Id: prez_user_display.py,v 1.3 2017/12/07 19:26:45 tsiang Exp $
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
import cgitb

cgitb.enable()

# set up logging
FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(filename="log/prez_user_display.log", format=FORMAT, level=logging.DEBUG)

form = cgi.FieldStorage()

for key in form.keys():
        variable = str(key)
        value=str(form.getvalue(variable))
        logging.warning("values are %s %s ", variable,value)

nickName=value

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
    cur.execute("select email from user where nickName=%s", nickName);
    r=cur.fetchall()


for i in r:
    email_address=i[0]
    logging.warning("email:%s",email_address)
print """<p style="text-align: center;  font-size: 36px; width: 1300px;"><b>Bracket for contestant: %s """ % nickName
print """<button onclick="goBack()">Go Back to Leaderboard</button>"""
print """
<script>
function goBack() {
            window.history.back();
        }
</script>
"""

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
