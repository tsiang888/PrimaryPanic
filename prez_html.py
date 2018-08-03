#!/usr/bin/env python

# ***************************************
# Main html page definition
# This is really just an html page
# defined as a function call that returns
# a string.  This allows one common html defintion
# of the bracket and monthly rankings to be used
#
# $Id: prez_html.py,v 1.45 2018/08/03 22:19:34 tsiang Exp $
# *********************************************

# this is the actual html main page shared by prez_ret_sql.cgi
# the string returned by get_html does not include </body> or </html> tags
# Any javascript that is to be executed after printing get_html()
# A typical python calling program that uses this file should do something like:

# ======================
# import prez_html
# print "Content-Type: text/html\n"
# print get_html()
# print <any addtional html code and/or any javascript you want to add can be added here>
# print </form>
# print </body> 
# print </html>
# ======================

# so these must be printed out by the calling program
# this seems to be required as the first line when generating html code from python
# The calling program should also do a print "Content-Type: text/html\n" as the very 
# first line before printing get_html()

def get_html(email_address):
    prez_html="""	
<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link href='http://fonts.googleapis.com/css?family=Droid+Serif|Candal' rel='stylesheet' type='text/css'>
    <LINK href="prez_main_style.css" rel="stylesheet" type="text/css">
    <title> Presidential Primaries Prediction </title>

<LINK href="prez_main_style.css" rel="stylesheet" type="text/css">
    <script src="http://code.jquery.com/jquery-1.7.1.min.js"></script>

<script>
$(document).ready(function()
                  {
                     $("#scoring_rules").hide(); 
                     $("#intro").hide();
                  });
</script>

</head>
<body>
<div id="contentframe" style="position:relative; left: 40px;">
<iframe id="CroppedCandidates" style="border:none" src="candidates.html" class="candidates" id="cand_links" name="cand_links" height=150 align="middle" width=1330px scrolling="no" ></iframe>
</div>
<noscript>This form requires that you have javascript enabled to work properly please enable javascript in your browser.</noscript>
<!-- Use the form with no target to get full dump of debug info to a new page -->
<!-- <form action="prez_ins_sql.py" > -->
<form action="prez_ins_sql.py" target="theiframe" method="POST">

<input type="hidden" name="email_address" value="%s" </input>

<p id="PrimaryPanic" style="text-align: center; font-family: 'Candal', sans-serif; font-size: 36px; width: 1340px;"><b><u>PRIMARY PANIC</u></b></p>
<p id="pNickname" style="text-align: center; font-family: 'Candal', sans-serif; font-size: 12px; width: 1340px;"></p>
<p style="clear:left"></p>


<input class="button_class" id="show_intro_button" type="button" value="Show Intro" onClick="$('#intro').show();$('#show_intro_button').hide();$('#up_intro_arrow').hide();">
<b id="up_intro_arrow" style="font-family: 'Wingdings3'">&#9660;</b><br>

<div id="intro">
<input class="button_class" id="hide_intro_button" type="button" value="Hide Intro" onClick="$('#intro').hide();$('#show_intro_button').show();$('#up_intro_arrow').show();">
<b style="font-family: 'Wingdings3'">&#9650;</b>

<p style="font-size:16px;">
What is a primary election? <br> Before the nationwide, general election, 
each state holds individual primary elections in order for parties to choose their presidential nominee.
These primary elections are held on varying dates from February to June. 
Learn about the candidates by clicking on their links at the top of the screen, then look at the bracket.
</p>
</div>


<input class="button_class" id="show_button" type="button" value="Show Scoring Rules" onClick="$('#scoring_rules').show();$('#show_button').hide();$('#up_arrow').hide();">
<b id="up_arrow" style="font-family: 'Wingdings3'">&#9660;</b>

<div id="scoring_rules">
<input class="button_class" id="hide_button" type="button" value="Hide Scoring Rules" onClick="$('#scoring_rules').hide();$('#show_button').show();$('#up_arrow').show();">
<b style="font-family: 'Wingdings3'">&#9650;</b>
<p style="font-size:16px;"><br>Scoring Rules:</p>

<ul style="font-size:16px;">
<li>You will win one point for every primary state you guess correctly.</li>
<li>You will earn three points for guessing the GOP and Democrat nomination winners correctly.</li>
<li>You will earn five points for guessing the President correctly.</li>
<li>Prizes will be awarded after each month to the player who has accumulated the most points.</li>
<li>There will first and second place prizes awarded for April/May.</li>
<li>There will be one grand prize, and second and third place prizes after the general election in November for the person who with most points overall.</li>
<li>In case of a tie, the earliest submitted entry will be deemed the winner.</li>
</ul>

<p style="font-size:16px;"> PRIZES (Amazon Gift Cards):
Feb $15
Mar $30, 
April/May: First: $40, Second $20
June: First:$80 Second: $40
Final: First: $160 second place $80 third place $40
<br>
</div>
<p style="clear:left"></p>

<div id="instructions" class="row">                                                                                                                                                                                       
  <div class="dy1">                                                                                                                                                                                     
    <div class="dt">1</div>                                                                                                                                                                             
    <div class="di">The states are organized in columns by the month when their primary occurs. Most states have links to polls to help you decide.</div>                                                              </div>                                                                                                                                                                                                
  <div class="dy2">                                                                                                                                                                                     
    <div class="dt">2</div>                                                                                                                                                                             
    <div class="di">On the left-hand side, choose which GOP candidate will win each state and party nomination.</div>                                                                        
  </div>                                                                                                                                                                                                
  <div class="dy3">                                                                                                                                                                                     
    <div class="dt">3</div>                                                                                                                                                                             
    <div class="di">On the right-hand side, choose which democratic candidate will win each state and party nomination.</div>                                                                                          </div>                                                                                                                                                                                                
  <div class="dy4">                                                                                                                                                                                     
    <div class="dt">4</div>                                                                                                                                                                             
    <div style="color: white; display: float:left; padding: 4px;">There is also a "Preload" feature on the left and right corners, 
    where you can initially set one candidate to win every state.</div> 
  </div>                                                                                                                                                                                                
  <div class="dy5">                                                                                                                                                                                     
    <div class="dt">5</div>                                                                                                                                                                             
    <div class="di">Finally, pick the candidate you think will be the new president. Double-check your answers and then click SAVE! </div>                                                                             </div>                                                                                                                                                                                                
  <div class="dy6">                                                                                                                                                                                     
    <div class="dt">6</div>                                                                                                                                                                             
    <div class="di">You may make changes for the February primaries until February 1st.  
      You may make changes to the rest of the months until March 1st.</div>                           
</div>                                                                                                                                                                                               </div>
<p style="clear:left"></p>

<br>

<div class="row">
  <label class="parties"></label>
  <!-- <SPAN STYLE="color: #5B0F00; font-family: 'Droid Serif', serif; font-size: 24px; font-style: normal; font-variant: normal; font-weight: 500;">REPUBLICANS</SPAN> -->
  <SPAN STYLE="color: #5B0F00; font-family: 'Candal', sans-serif; font-size: 24px; font-style: normal; font-variant: normal; font-weight: 500;">REPUBLICANS</SPAN>
  <label class="parties"></label>
  <SPAN STYLE="color: black; font-family: 'Candal', sans-serif; font-size: 36px;">BRACKET</SPAN>
  <label class="parties"></label>
  <!-- <SPAN STYLE="color: #0b6291; font-family: 'Droid Serif', serif; font-size: 24px; font-style: normal; font-variant: normal; font-weight: 500;">DEMOCRATS</SPAN> -->
  <SPAN STYLE="color: #0b6291; font-family: 'Candal', sans-serif; font-size: 24px; font-style: normal; font-variant: normal; font-weight: 500;">DEMOCRATS</SPAN>
  <label class="parties"></label>
</div>
<div class="row">
  <div class="dm1">
    <label class="months1">FEBRUARY</label>
    <label id="preload1" class="nullstate" style="color:white">Preload<select class="SelRep" name="none" onchange="Rep_preload(this.value)" ></select></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="state1"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/iowa-caucus")'>Iowa</a><select class="SelRep" name="IA_Rep"></select></label>
    <label class="nullstate1"></label>
    <label class="state1"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/New-Hampshire-primary")'>New Hampshire</a><select class="SelRep" name="NH_Rep"></select></label>
    <label class="nullstate1"></label>
    <label class="state1"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/South-Carolina-primary")'>South Carolina</a><select class="SelRep" name="SC_Rep"></select></label>
    <label class="nullstate1"></label>
    <label class="state1"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Nevada-caucus")'>Nevada</a><select class="SelRep" name="NV_Rep"></select></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
  </div>
  <div class="dm2">
    <label class="months2">MARCH</label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Alabama-primary")'>Alabama</a><select class="SelRep" name="AL_Rep"></select></label>
    <label class="state2b"><a class="nourl">Alaska</a><select class="SelRep" name="AK_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Arkansas-primary")'>Arkansas</a><select class="SelRep" name="AR_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Georgia-primary")'>Georgia</a> <select class="SelRep" name="GA_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Massachusetts-primary")'>Massachusetts </a> <select class="SelRep" name="MA_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Minnesota-caucus")'>Minnesota</a><select class="SelRep" name="MN_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Oklahoma-primary")'>Oklahoma</a><select class="SelRep" name="OK_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Tennessee-primary")'>Tennessee</a><select class="SelRep" name="TN_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Texas-primary")'>Texas</a><select class="SelRep" name="TX_Rep"></select></label>
    <label class="state2b"><a class="nourl">Vermont</a><select class="SelRep" name="VT_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Virginia-primary")'>Virginia</a><select class="SelRep" name="VI_Rep"></select></label>
    <label class="state2"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333316")'>Kansas</a><select class="SelRep" name="KS_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Louisiana-primary")'>Louisiana</a><select class="SelRep" name="LA_Rep"></select></label>
    <label class="state2"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333319")'>Maine</a><select class="SelRep" name="ME_Rep"></select></label>
    <label class="state2b"><a class="nourl">Puerto Rico</a><select class="SelRep" name="PR_Rep"></select></label>
    <label class="state2"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333311")'>Hawaii</a><select class="SelRep" name="HI_Rep"></select></label>
    <label class="state2"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333312")'>Idaho</a><select class="SelRep" name="ID_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Mississippi-primary")'>Mississippi</a><select class="SelRep" name="MS_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Michigan-primary")'>Michigan</a><select class="SelRep" name="MI_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.realclearpolitics.com/epolls/2016/president/wy/wyoming_republican_presidential_caucus-4023.html")'>Wyoming</a><select class="SelRep" name="WY_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/North-Carolina-primary")'>North Carolina</a><select class="SelRep" name="NC_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Ohio-primary")'>Ohio</a><select class="SelRep" name="OH_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Florida-primary")'>Florida</a><select class="SelRep" name="FL_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Illinois-primary")'>Illinois</a><select class="SelRep" name="IL_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Missouri-primary")'>Missouri</a><select class="SelRep" name="MO_Rep"></select></label>
    <label class="state2"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Arizona-primary")'>Arizona</a><select class="SelRep" name="AZ_Rep"></select></label>
    <label class="state2"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333344")'>Utah</a><select class="SelRep" name="UT_Rep"></select></label>
    <label class="nullstate"></label>
  </div>
  <div class="dm3">
    <label class="months3">APRIL/MAY</label>
    <label class="nullstate"></label>
    <label class="nullstate"></label>
    <label class="nullstate"></label>
    <label class="nullstate"></label>
    <label class="state3b"><a class="nourl" >North Dakota </a><select class="SelRep" name="ND_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Wisconsin-primary")'>Wisconsin</a><select class="SelRep" name="WI_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/New-York-primary")'>New York </a><select class="SelRep" name="NY_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Connecticut-primary")'>Connecticut</a><select class="SelRep" name="CT_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333306")'>Delaware</a><select class="SelRep" name="DE_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Maryland-primary")'>Maryland</a><select class="SelRep" name="MD_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Pennsylvania-primary")'>Pennsylvania</a><select class="SelRep" name="PA_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333339")'>Rhode Island</a><select class="SelRep" name="RI_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("https://www.isidewith.com\/2016-republican-primary-poll\/801555698\/9333314")'>Indiana</a><select class="SelRep" name="IN_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333327")'>Nebraska</a><select class="SelRep" name="NB_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.realclearpolitics.com/epolls/2016/president/wv/west_virginia_republican_presidential_primary-5423.html")'>West Virginia </a><select class="SelRep" name="WV_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Kentucky-caucus")'>Kentucky</a><select class="SelRep" name="KT_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333337")'>Oregon</a><select class="SelRep" name="OR_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="state3"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Washington-primary")'>Washington</a><select class="SelRep" name="WA_Rep"></select></label>
    <label class="nullstate"></label>
    <label class="nullstate"></label>
    <label class="nullstate"></label>
    <label class="nullstate"></label>
  </div>
  <div class="dm4">
    <label class="months4">JUNE</label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="state4"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/California-primary")'>California</a><select class="SelRep" name="CA_Rep"></select></label>
    <label class="state4"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/Montana-primary")'>Montana</a><select class="SelRep" name="MT_Rep"></select></label>
    <label class="state4"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/New-Jersey-primary")'>New Jersey</a><select class="SelRep" name="NJ_Rep"></select></label>
    <label class="state4"><a onclick='newwin("https://www.isidewith.com/2016-republican-primary-poll/801555698/9333331")'>New Mexico</a><select class="SelRep" name="NM_Rep"></select></label>
    <label class="state4"><a onclick='newwin("http://www.270towin.com\/2016-republican-nomination\/South-Dakota-primary")'>South Dakota </a><select class="SelRep" name="SD_Rep"></select></label>
    <label class="state4b"><a class="nourl" >DC</a><br><select class="SelRep" name="DC_Rep"></select></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
  </div>
  <div class="dm">
    <label class="months">FINALS</label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label style="border-style: solid; border-width: 1px; border-color: #cfd2d3; border-radius: 5px; text-align: center; background: #FCBFBF;padding: 8px;">
      GOP Winner<select class="SelRepWin" name="GOP_Winner"></select></label>
    <label class="nullstate1"></label>
    <label style="border-style: solid; border-width: 1px; border-color: #cfd2d3; border-radius: 5px; text-align: center; background: #BBBBBB; padding: 8px;">
      President<select class="SelPres" name="President"></select></label>
    <label class="nullstate1"></label>
    <label style="border-style: solid; border-width: 1px; border-color: #cfd2d3; border-radius: 5px; text-align: center; background: #c2dbe8; padding: 4px;">
      Democrat Winner<select class="SelDemWin" name="Dem_Winner"></select></label>
    <label class="nullstate1"></label>

    <div style="float:left; width: 140px; padding: 2px margin:20px;">
    <input id=SubmitSave type="submit" style="display:block; margin:0 auto; cursor:pointer; background:#777777; width:120px;height:180px;border-style:solid;border-radius:3px;
				border-width: 6px; border-color: #555555; font-family: 'Droid Serif', serif; font-size: 25px; color: white;" value="SAVE">
    <iframe class="rank" display:block id="theiframe" name="theiframe" height=130px width=100px scrolling="no" ></iframe>
    <a id="url_home_page" style="margin:auto; text-align:center; display:block;" target="_parent" href="../" title="Back to the Home page"><b>HOME PAGE</b></a>
    <label id="url_leaderboard" class="status"><a onclick='newwin("prez_ret_score.py?Email=lookmeup")' title="Display Leaderboard"><b>Leaderboard</b)></a></label>
    <label id="url_election_results" class="status" <a  onclick='newwin("prez_master_user_display.py")'>Election Results</a> </label>
    </div>

    <br>
  </div>
  <div class="dm5">
    <label class="months5">JUNE</label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="state5b"><a class="nourl">Puerto Rico</a><select class="SelDem" name="PR_Dem"></select></label>
    <label class="state5"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/California-primary")'>California</a><select class="SelDem" name="CA_Dem"></select></label>
    <label class="state5"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Montana-primary")'>Montana</a><select class="SelDem" name="MT_Dem"></select></label>
    <label class="state5"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/New-Jersey-primary")'>New Jersey</a><select class="SelDem" name="NJ_Dem"></select></label>
    <label class="state5b"><a class="nourl">New Mexico</a><select class="SelDem" name="NM_Dem"></select></label>
    <label class="state5b"><a class="nourl" >North Dakota </a><select class="SelDem" name="ND_Dem"></select></label>
    <label class="state5b"><a class="nourl">South Dakota </a><select class="SelDem" name="SD_Dem"></select></label>
    <label class="state5b"><a class="nourl" >DC</a><br><select class="SelDem" name="DC_Dem"></select></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
  </div>
  <div class="dm6">
    <label class="months6">APRIL/MAY</label>
    <label class="nullstate1"></label>
    <label class="nullstate"></label>
    <label class="state6"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Wisconsin-primary")'>Wisconsin</a><select class="SelDem" name="WI_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6b"><a class="nourl">Wyoming</a><select class="SelDem" name="WY_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/New-York-primary")'>New York </a><select class="SelDem" name="NY_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Connecticut-primary")'>Connecticut</a><select class="SelDem" name="CT_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Maryland-primary")'>Maryland</a><select class="SelDem" name="MD_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6b"><a class="nourl">Delaware</a><select class="SelDem" name="DE_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Pennsylvania-primary")'>Pennsylvania</a><select class="SelDem" name="PA_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6b"><a class="nourl">Rhode Island</a><select class="SelDem" name="RI_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6b"><a class="nourl">Indiana</a><select class="SelDem" name="IN_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6b"><a class="nourl">Nebraska</a><select class="SelDem" name="NB_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6"><a onclick='newwin("https://www.isidewith.com/2016-democratic-primary-poll/801555698/9333348")'>West Virginia </a><select class="SelDem" name="WV_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Kentucky-primary")'>Kentucky</a><select class="SelDem" name="KT_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6b"><a class="nourl">Oregon</a><select class="SelDem" name="OR_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="state6b"><a class="nourl">Washington</a><select class="SelDem" name="WA_Dem"></select></label>
    <label class="nullstate"></label>
    <label class="nullstate"></label>
  </div>
  <div class="dm7">
    <label class="months7">MARCH</label>
    <label class="state7b"><a class="nourl">Alabama</a><select class="SelDem" name="AL_Dem"></select></label>
    <label class="state7b"><a class="nourl">Arkansas</a><select class="SelDem" name="AR_Dem"></select></label>
    <label class="state7b"><a class="nourl">Colorado</a><select class="SelDem" name="CO_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Georgia-primary")'>Georgia</a> <select class="SelDem" name="GA_Dem"></select></label>
    <label class="state7b"><a class="nourl">Massachusetts</a> <select class="SelDem" name="MA_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Minnesota-caucus")'>Minnesota</a><select class="SelDem" name="MN_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Oklahoma-primary")'>Oklahoma</a><select class="SelDem" name="OK_Dem"></select></label>
    <label class="state7b"><a class="nourl">Tennessee</a><select class="SelDem" name="TN_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Texas-primary")'>Texas</a><select class="SelDem" name="TX_Dem"></select></label>
    <label class="state7b"><a class="nourl">Vermont</a><select class="SelDem" name="VT_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Virginia-primary")'>Virginia</a><select class="SelDem" name="VI_Dem"></select></label>
    <label class="state7b"><a class="nourl">Kansas</a><select class="SelDem" name="KS_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Louisiana-primary")'>Louisiana</a><select class="SelDem" name="LA_Dem"></select></label>
    <label class="state7b"><a class="nourl">Maine</a><select class="SelDem" name="ME_Dem"></select></label>
    <label class="state7b"><a class="nourl">Mississippi</a><select class="SelDem" name="MS_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Michigan-primary")'>Michigan</a><select class="SelDem" name="MI_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/North-Carolina-primary")'>North Carolina</a><select class="SelDem" name="NC_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Ohio-primary")'>Ohio</a><select class="SelDem" name="OH_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Florida-primary")'>Florida</a><select class="SelDem" name="FL_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Illinois-primary")'>Illinois</a><select class="SelDem" name="IL_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Missouri-primary")'>Missouri</a><select class="SelDem" name="MO_Dem"></select></label>
    <label class="state7"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Arizona-primary")'>Arizona</a><select class="SelDem" name="AZ_Dem"></select></label>
    <label class="state7b"><a class="nourl">Idaho</a><select class="SelDem" name="ID_Dem"></select></label>
    <label class="state7b"><a class="nourl">Hawaii</a><select class="SelDem" name="HI_Dem"></select></label>
    <label class="state7"><a onclick='newwin("https://www.isidewith.com/2016-democratic-primary-poll/801555698/9333344")'>Utah</a><select class="SelDem" name="UT_Dem"></select></label>
    <label class="state7b"><a class="nourl">Alaska</a><select class="SelDem" name="AK_Dem"></select></label>
    <label class="nullstate"></label>
  </div>
  <div class="dm8">
    <label class="months8">FEBRUARY</label>
    <label id="preload2" class="nullstate" style="color:white">Preload<select class="SelDem" name="none" onchange="Dem_preload(this.value)"></select></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
    <label class="state8"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Iowa-caucus")'>Iowa</a><select class="SelDem" name="IA_Dem"></select></label>
    <label class="nullstate1"></label>
    <label class="state8"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/New-Hampshire-primary")'>New Hampshire</a><select class="SelDem" name="NH_Dem"></select></label>
    <label class="nullstate1"></label>
    <label class="state8"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/South-Carolina-primary")'>South Carolina</a><select class="SelDem" name="SC_Dem"></select></label>
    <label class="nullstate1"></label>
    <label class="state8"><a onclick='newwin("http://www.270towin.com\/2016-democrat-nomination\/Nevada-caucus")'>Nevada</a><select class="SelDem" name="NV_Dem"></select></label>
    <label class="nullstate1"></label>
    <label class="nullstate1"></label>
  </div>
</div>


<script>
function newwin(URL) {
   myWindow=window.open(URL, 'mywin','toolbar=0,menubar=0,scrollbars=1,height=600,width=1360');
}
</script>

</body>
""" % email_address
    return(prez_html)

