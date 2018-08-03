#!/usr/bin/env python

# ************************************************************
# Processes FORM from prez_html.cgi
# Inserts into database
# Prints a bunch of debug stuff temporarily
# Into an iframe at the bottom of the prez_html.cgi web page
#
# $Id: prez_ins_sql.py,v 1.18 2018/08/03 22:16:24 tsiang Exp $
# ************************************************************

import prez_score
import cgi
import re
import MySQLdb
import sys
import cgitb
from ConfigParser import SafeConfigParser

cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html\n"
print '<html><body>'

stop=1500
variable = ""
value = ""
i=0


state_rep_key = state_rep_val =""
state_dem_key = state_dem_val =""
state_win_key = state_win_val =""
pres_win_key = pres_win_val =""

state_rep_set=""
state_dem_set=""
state_win_set=""
pres_win_set=""

comma=","
tick="'"
equals="="
email_address=""

# CREATE INSERT VALUES INTO A STRING
for key in form.keys():
        i=i+1
        if(i<stop):
                variable = str(key)
                value = str(form.getvalue(variable))
                # Look for State predictors
                if (re.match("(^.._Dem)",variable)):
                        state_dem_set = state_dem_set + variable + equals + tick + value + tick + comma
                elif (re.match("(^.._Rep)",variable)):
                        state_rep_set = state_rep_set + variable + equals + tick + value + tick + comma
                elif (re.match("(^..._Winner)",variable)): 
                        state_win_set = state_win_set + variable + equals + tick + value + tick + comma
                elif (re.match("(^President)",variable)): 
                        pres_win_set = pres_win_set + variable + equals + tick + value + tick + comma
		elif (variable=="email_address"):
			email_address=value
                elif (variable != "none"):
                        print "THERE SEEMS TO BE AN ERROR HERE"
                        print key,"=", value, " <br>"
                        print 

# set email address to default of tsiang888 in case we want to run this without going
# through login (e.g. for debug)
if (email_address==""):
	email_address="tsiang888@gmail.com"

if len(email_address) > 64 :
        email_address=email_address[0:63]
        
# This keys are used only when creating a table for the first time
                                                               
state_rep_key_create= "Email CHAR(64)," + state_rep_key[:-1].replace(",", " TEXT,") + " TEXT," + " PRIMARY KEY(Email)"
state_dem_key_create= "Email CHAR(64)," + state_dem_key[:-1].replace(",", " TEXT,") + " TEXT," + " PRIMARY KEY(Email)"
state_win_key_create= "Email CHAR(64)," + state_win_key[:-1].replace(",", " TEXT,") + " TEXT," + " PRIMARY KEY(Email)"
pres_win_key_create= "Email CHAR(64)," + pres_win_key[:-1].replace(",", " TEXT,") + " TEXT," + " PRIMARY KEY(Email)"

# Add email address and trim off extra comma at the end

state_dem_set = "Email" + equals + tick + email_address + tick + comma + state_dem_set[:-1];
state_rep_set = "Email" + equals + tick + email_address + tick + comma + state_rep_set[:-1];
state_win_set = "Email" + equals + tick + email_address + tick + comma + state_win_set[:-1];
pres_win_set = "Email" + equals + tick + email_address + tick + comma + pres_win_set[:-1];


parser = SafeConfigParser()
parser.read('prez.ini')

master_email=parser.get('prez', 'master_email')
db_host=parser.get('prez', 'db_host')
db_username=parser.get('prez','db_username')
db_password=parser.get('prez', 'db_password')
db=parser.get('prez', 'db')

# disable insert for all other than master email
if (email_address == master_email) :
        con=MySQLdb.connect(db_host,db_username,db_password,db)
        # uncomment to skip the rest of execution (for debug)
        # raise SystemExit
        # insert values
        with con:
                cur = con.cursor()

                #        cur.execute("""CREATE TABLE if not exists State_Dem (%s)""" % (state_dem_key_create))
                cur.execute("""INSERT INTO State_Dem SET %s ON DUPLICATE KEY UPDATE %s""" % (state_dem_set, state_dem_set))
                
                #        cur.execute("""CREATE TABLE if not exists State_Rep (%s)""" % (state_rep_key_create))
                cur.execute("""INSERT INTO State_Rep SET %s ON DUPLICATE KEY UPDATE %s""" % (state_rep_set, state_rep_set))
                
                #        cur.execute("""CREATE TABLE if not exists State_Win (%s)""" % (state_win_key_create))
                cur.execute("""INSERT INTO State_Win SET %s ON DUPLICATE KEY UPDATE %s""" % (state_win_set, state_win_set))
                
                #        cur.execute("""CREATE TABLE if not exists Pres_Win (%s)""" % (pres_win_key_create))
                cur.execute("""INSERT INTO Pres_Win SET %s ON DUPLICATE KEY UPDATE %s""" % (pres_win_set, pres_win_set))
                
                # if the current update is from the master email address, then retabulate scores
                print """<p style="margin-left:18" "id=submit_status">
                Saved!!  Continue selecting or click on Home
                </p>"""
else:
        print """<p style="margin-left:18" "id=submit_status">
        Sorry! Prediction entry has ended - no changes can be made.
        </p>"""

if email_address == master_email:
        # go to manual recalc of scores from cli to control timestamp update
        prez_score.tabulate_scores() # function imported from prez_score
        print """<p style="margin-left:18"> Scores Updated </p>"""

print '</body></html>'
