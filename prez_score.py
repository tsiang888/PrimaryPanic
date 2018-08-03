#!/usr/bin/env python
#=====================================================================#
# Retrieve records from db and tabulate scores and insert them into db
# This file is executed whenever the master user (master email address
# as defined in prez.ini) updates the database (called by prez_ins_sql).
# Can also be run standalone from command line as a python program.
# $Id: prez_score.py,v 1.14 2017/12/07 19:26:45 tsiang Exp $
#=====================================================================#
from ConfigParser import SafeConfigParser
import MySQLdb
import sys
import datetime

def count_matches(master, contender,dont_care):
        # skip first two columns as they are email_addr and timestamp
	i=master[2:]
	j=contender[2:]
	count=sum(1 for a, b in zip(i, j) if (a == b) and (a!=dont_care))
	return(count)

def getvalues(cur,values,table, email_addr):
	if (email_addr!=""):
		# append to a single dimension list (if email_addr is specified)
		cur.execute("SELECT * FROM %s WHERE Email='%s' " % (table, email_addr))
                values.append(cur.fetchone())
	else:
		# append to a 2d list array indexed by the first value field which is the email address
                cur.execute("SELECT * FROM %s ORDER BY Email" % (table))
		for row in cur.fetchall():
			values.append(row)
	return()

def tabulate_scores():

        keys=[]
        parser = SafeConfigParser()
        parser.read('prez.ini')

        master_email=parser.get('prez', 'master_email')
        # temp make a different master email address for testing
        # master_email="tsiang@employees.org"
        db_host=parser.get('prez', 'db_host')
        db_username=parser.get('prez','db_username')
        db_password=parser.get('prez', 'db_password')
        db=parser.get('prez', 'db')

        con=MySQLdb.connect(db_host,db_username,db_password,db)


        with con:
	        cur = con.cursor()
                cur.execute("SELECT count(*) FROM State_Rep")
	        num_entries=cur.fetchone()
	        # Create list variables
	        state_dem_values,state_rep_values,state_win_values,pres_win_values=[],[],[],[]
	        state_dem_score,state_rep_score,state_win_score,pres_win_score=[],[],[],[]
	        master_state_dem_values,master_state_rep_values,master_state_win_values,master_pres_win_values=[],[],[],[]
	
	        getvalues(cur,state_dem_values,"State_Dem", "")
 	        getvalues(cur,state_rep_values,"State_Rep", "")
 	        getvalues(cur,state_win_values,"State_Win", "")
 	        getvalues(cur,pres_win_values,"Pres_Win", "")
                
 	        getvalues(cur,master_state_dem_values,"State_Dem", master_email)
 	        getvalues(cur,master_state_rep_values,"State_Rep", master_email)
 	        getvalues(cur,master_state_win_values,"State_Win", master_email)
 	        getvalues(cur,master_pres_win_values,"Pres_Win", master_email)
                
	        tick="'"
	        comma=", "
                # weights are: state_dem, state_rep, state_win, pres_win
	        score_weight=[1,1,3,5]
	        score_key_create = "Email CHAR(64) PRIMARY KEY, Timestamp Datetime, State_Dem_Score INT, State_Rep_Score INT, State_Win_Score INT, Pres_Win_Score INT, Total_Score INT"
	        # cur.execute("""CREATE TABLE if not exists Scores (%s)""" % score_key_create)

	        score_key = "Email, Timestamp, State_Dem_Score, State_Rep_Score, State_Win_Score, Pres_Win_Score, Total_Score" 
                # print "number of entries is", num_entries[0]
	        for i in range(num_entries[0]): #num_entries is a tuple with one entry so need [0]
		        user_email=state_dem_values[i][0] #email address of user
                        if (state_rep_values[i][0] != user_email) :
                                print "ERROR State_Rep Email does not match DEM Email"
                        if (state_win_values[i][0] != user_email) :
                                print "ERROR State_Win Email does not match DEM Email"
                        if (pres_win_values[i][0] != user_email) :
                                print "ERROR Pres_Win Email does not match DEM Email"
                        user_timestamp=state_dem_values[i][1]
                        new_timestamp=user_timestamp.strftime('%Y-%m-%d %H:%M:%S')
		        state_dem_matches=count_matches(master_state_dem_values[0], state_dem_values[i], 'NoSel')
		        state_rep_matches=count_matches(master_state_rep_values[0], state_rep_values[i], 'NoSel')
		        state_win_matches=count_matches(master_state_win_values[0], state_win_values[i], 'NoSel')
		        pres_win_matches=count_matches(master_pres_win_values[0], pres_win_values[i], 'NoSel')
		        score_weighted_sum= score_weight[0] * state_dem_matches
		        score_weighted_sum+= score_weight[1] * state_rep_matches
		        score_weighted_sum+= score_weight[2] * state_win_matches
		        score_weighted_sum+= score_weight[3] * pres_win_matches

                        score_set = ("Email=" + tick + user_email + tick + comma + "State_Dem_Score=" + str(state_dem_matches) + comma +
                        "State_Rep_Score=" + str(state_rep_matches) + comma + "State_Win_Score=" + str(state_win_matches) + comma +
                                     "Pres_Win_Score=" + str(pres_win_matches) + comma + "Total_Score=" + str(score_weighted_sum) + comma +
                                     "Timestamp=" + tick + new_timestamp + tick)

#                        print score_set
                        cur.execute("""INSERT INTO Scores SET %s ON DUPLICATE KEY UPDATE %s""" % (score_set, score_set))

if __name__=="__main__":
        tabulate_scores()

                

