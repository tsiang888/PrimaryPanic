#!/usr/bin/env python
# ======================================================
# Retrieve previous prediction selections from db
# and build var strings to include with javascript
# which will then use the strings to select the 
# previous values
# 
# $Id: prez_ret_sql.py,v 1.14 2017/12/07 19:26:45 tsiang Exp $
# ======================================================

import MySQLdb
import sys
from ConfigParser import SafeConfigParser

# will get this from user page on submit - this is just for testing:
debug=0

def Get_Objects(email_address):

        def getkeys(keys,table):
                cur.execute("SHOW columns FROM %s" % table)
                for row in cur.fetchall():
                        v=row[0]
                        keys.append(v)
                return()
                        
        def getvalues(values,table, email_addr):
		cur.execute("SELECT * FROM %s WHERE Email='%s' " % (table, email_addr))
                for row in cur.fetchall():
			for i in row:
				values.append(i)
		return()

        def printlist(list):
                for i in list:
                        sys.stdout.write(i)
                        sys.stdout.write(' ')
                return()

        def js_obj_create(obj_name,key_list, value_list):
                # creates a string that does a javascript object definition
                tick="'"
                comma=","
                
                js_obj_string = "var %s = { " % obj_name
                # skip the first two items in list, it is email address and timestamp
                for i in range(2,len(key_list)):
                        # Protect against NULLs in database
                        if (value_list[i] == None):
                                value_list[i] = "NoSel"
                        js_obj_string = js_obj_string + key_list[i] + ":" + tick +  value_list[i] + tick + comma
                        
                        # Get rid of last comma and add closing brace
                js_obj_string = js_obj_string[:-1] + "};"
                return(js_obj_string)

        keys=[]

        parser = SafeConfigParser()
        parser.read('prez.ini')
        master_email=parser.get('prez', 'master_email')
        # Temporarily override for debug
        # master_email="tsiang@employees.org"
        db_host=parser.get('prez', 'db_host')
        db_username=parser.get('prez','db_username')
        db_password=parser.get('prez', 'db_password')
        db=parser.get('prez', 'db')

        con=MySQLdb.connect(db_host,db_username,db_password,db)

        with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM user WHERE email='%s' " % email_address)
                user_records=cur.fetchall()
                nickname=user_records[0][3]

                state_dem_key,state_rep_key,state_win_key,pres_win_key=[],[],[],[]
                state_dem_values,state_rep_values,state_win_values,pres_win_values=[],[],[],[]
                # variables for master picks
                m_state_dem_values,m_state_rep_values,m_state_win_values,m_pres_win_values=[],[],[],[]
                
                getkeys(state_dem_key,"State_Dem")
                getkeys(state_rep_key,"State_Rep")
                getkeys(state_win_key,"State_Win")
                getkeys(pres_win_key,"Pres_Win")
                
                getvalues(state_dem_values,"State_Dem", email_address)
                getvalues(state_rep_values,"State_Rep", email_address)
                getvalues(state_win_values,"State_Win", email_address)
                getvalues(pres_win_values,"Pres_Win", email_address)

                # get master values too so that we can calling routine can color code correct picks
                getvalues(m_state_dem_values,"State_Dem", master_email)
                getvalues(m_state_rep_values,"State_Rep", master_email)
                getvalues(m_state_win_values,"State_Win", master_email)
                getvalues(m_pres_win_values,"Pres_Win", master_email)

		if (debug==1):
			print email_address
			print state_dem_key
			print state_dem_values
			print state_rep_key
			print state_rep_values
			print state_win_key
			print state_win_values
			print pres_win_key
			print pres_win_values


		# Check to see if there was anything in the database attached to the email address
		# if not return null values except for nickname - this only happens if user is entering for the first time
		if (len(state_dem_values)!=0):
			state_rep_js_obj = js_obj_create("state_rep", state_rep_key, state_rep_values)
			state_dem_js_obj = js_obj_create("state_dem", state_dem_key, state_dem_values)
			state_win_js_obj = js_obj_create("state_win", state_win_key, state_win_values)
			pres_win_js_obj = js_obj_create("pres_win", pres_win_key, pres_win_values)

			m_state_rep_js_obj = js_obj_create("m_state_rep", state_rep_key, m_state_rep_values)
			m_state_dem_js_obj = js_obj_create("m_state_dem", state_dem_key, m_state_dem_values)
			m_state_win_js_obj = js_obj_create("m_state_win", state_win_key, m_state_win_values)
			m_pres_win_js_obj = js_obj_create("m_pres_win", pres_win_key, m_pres_win_values)

			return{'nickname_js_obj':'var nickname = "%s";' % nickname,
                               'state_rep_js_obj':state_rep_js_obj,
			       'state_dem_js_obj':state_dem_js_obj,
			       'state_win_js_obj':state_win_js_obj,
			       'pres_win_js_obj':pres_win_js_obj,
                               'm_state_rep_js_obj':m_state_rep_js_obj,
			       'm_state_dem_js_obj':m_state_dem_js_obj,
			       'm_state_win_js_obj':m_state_win_js_obj,
			       'm_pres_win_js_obj':m_pres_win_js_obj}
		else:
			return{'nickname_js_obj':'var nickname = "%s";' % nickname,
                               'state_rep_js_obj':"",
			       'state_dem_js_obj':"",
			       'state_win_js_obj':"",
                               'pres_win_js_obj':"",
                               'm_state_rep_js_obj':"",
			       'm_state_dem_js_obj':"",
			       'm_state_win_js_obj':"",
			       'm_pres_win_js_obj':""}
if __name__=="__main__":
        nl = "\n"
#        sql_objects=Get_Objects("tsiang@employees.org")
        sql_objects=Get_Objects("tripped888@gmail.com")
        print sql_objects['nickname_js_obj'],nl
        print sql_objects['state_rep_js_obj'], nl
        print sql_objects['state_dem_js_obj'], nl
        print sql_objects['state_win_js_obj'], nl
        print sql_objects['pres_win_js_obj'], nl
        print sql_objects['m_state_rep_js_obj'], nl
        print sql_objects['m_state_dem_js_obj'], nl
        print sql_objects['m_state_win_js_obj'], nl
        print sql_objects['m_pres_win_js_obj'], nl










