// ***************************************************
// Javascript functions
//
// $Id: prez_js.js,v 1.22 2016/03/03 23:31:39 rollingm Exp $
// ***************************************************

// Global variables (constants in this case)

    var DemIndex = {
	NoSel : 0,
	Clinton : 1,
	Sanders : 2,
	OMalley : 3 
    };
    
    var RepIndex = {
	NoSel : 0,
	Paul : 1,
	Trump : 2,
	Bush : 3,
	Fiorina : 4,
	Christie : 5,
	Cruz : 6,
	Gilmore : 7,
	Huckabee : 8,
	Kasich : 9,
	Rubio : 10,
	Santorum : 11,
	Carson : 12
    };

    var PresIndex = {
	NoSel : 0,
	Clinton : 1,
	Sanders : 2,
	OMalley : 3,
	NoSel : 4,
	Paul : 5,
	Trump : 6,
	Bush : 7,
	Fiorina : 8,
	Christie : 9,
	Cruz : 10,
	Gilmore : 11,
	Huckabee : 12,
	Kasich : 13,
	Rubio : 14,
	Santorum :15,
        Carson : 16
    };

    var DemObject = {
        NoSel : 'None',
        Clinton : 'Hillary Clinton',
        Sanders : 'Bernie Sanders',
        OMalley : "Martin O\'Malley"
    };
    
    var RepObject = {
        NoSel : 'None',
        Paul : 'Rand Paul',
        Trump : 'Donald Trump',
        Bush : 'Jeb Bush',
        Fiorina : 'Carly Fiorina',
        Christie : 'Chris Christie',
        Cruz : 'Ted Cruz',
        Gilmore : 'Jim Gilmore',
        Huckabee : 'Mike Huckabee',
        Kasich : 'John Kasich',
        Rubio : 'Marco Rubio',
        Santorum : 'Rick Santorum',
        Carson : 'Ben Carson'
    };
    
function Set_Select_Options() {
// Add selector options to all the select statements in labels

    var i;
    var x;
    var select;

    x = document.getElementsByClassName("SelDem");
    for (i = 0; i < x.length; i++) {
	select = x[i];
	for(index in DemObject) {
	    select.options[select.options.length] = new Option(DemObject[index], index);
	}
    }
    x = document.getElementsByClassName("SelRep");
    for (i = 0; i < x.length; i++) {
	select = x[i];
	for(index in RepObject) {
	    select.options[select.options.length] = new Option(RepObject[index], index);
	}
    }

    x = document.getElementsByClassName("SelPres");
    for (i = 0; i < x.length; i++) {
	select = x[i];
	for(index in DemObject) {
	    select.options[select.options.length] = new Option(DemObject[index], index);
	}
	for(index in RepObject) {
	    select.options[select.options.length] = new Option(RepObject[index], index);
	}
    }

    x = document.getElementsByClassName("SelDemWin");
    for (i = 0; i < x.length; i++) {
	select = x[i];
	for(index in DemObject) {
	    select.options[select.options.length] = new Option(DemObject[index], index);
	}
    }

    x = document.getElementsByClassName("SelRepWin");
    for (i = 0; i < x.length; i++) {
	select = x[i];
	for(index in RepObject) {
	    select.options[select.options.length] = new Option(RepObject[index], index);
	}
    }

}


function Init_Predictions() {
// initialize predictions and set <a> links to open in a new tab

    var x;
    var i;
    
    // Init select fields to select NoSel

    x = document.getElementsByClassName("SelPres");
    // Presidential select has only 1 element (element 0), select NoSel
    x[0].options[0].selected="selected";


    x = document.getElementsByClassName("SelDem");
    for (i = 0; i < x.length; i++) {
	x[i].options[0].selected="selected";
    }

    x = document.getElementsByClassName("SelRep");
    for (i = 0; i < x.length; i++) {
	x[i].options[0].selected="selected";
    }

    x = document.getElementsByClassName("SelWin");
    for (i = 0; i < x.length; i++) {
	x[i].options[0].selected="selected";
    }

    // Enter default values of 0 for primary state rankings
    x = document.getElementsByTagName("input");
    for (i = 0; i < x.length; i++) {
	if (x[i].type=="text") {
	    x[i].value="0";
	}
    }

    // // set target attribute on <a>
    // x = document.getElementsByTagName("a");
    // i;
    // for (i=0; i < x.length; i++) {
    // 	select = x[i];
    // 	select.target = "_blank";
    // 	//	      select.target = "theiframe";
    // }

}

function Set_Predictions() {


    var n;
    var idx;

    // Pre-select based on previous values in database - uses object
    // Presidential select has only 1 element (element 0)
    x = document.getElementsByClassName("SelPres");
    n=pres_win[x[0].name];
    idx=PresIndex[n];
    x[0].options[idx].selected="selected";
    if (m_pres_win[x[0].name] != "NoSel") {
	if (pres_win[x[0].name] != m_pres_win[x[0].name]) {
	    x[0].style.opacity="0.6";
	    x[0].style.textDecoration="line-through";
	}
	else {
	    x[0].style.opacity="0.6";
//	    x[0].style.textDecoration="underline";
	}
    }
    // Retrieve previous values from database - uses object 
    x = document.getElementsByClassName("SelDem");
    for (i = 0; i < x.length; i++) {
	if(x[i].name != "none"){ // exclude preload selectors
            n=state_dem[x[i].name];
            idx=DemIndex[n];
            x[i].options[idx].selected="selected";
	    if (m_state_dem[x[i].name] != "NoSel") {
		if (state_dem[x[i].name] != m_state_dem[x[i].name]) {
		    x[i].style.opacity="0.6";
		    x[i].style.textDecoration="line-through";
		}
		else {
		    x[i].style.opacity="0.6";
//		    x[i].style.textDecoration="underline";
		}
	    }
	}
    }

    // Retrieve previous values from database - uses object 
    x = document.getElementsByClassName("SelRep");
    for (i = 0; i < x.length; i++) {
	if(x[i].name != "none"){ // exclude preload selectors
            n=state_rep[x[i].name];
            idx=RepIndex[n];
            x[i].options[idx].selected="selected";
	    // Compare predictions to master and line-through incorrect predictions
	    if (m_state_rep[x[i].name] != "NoSel") {
		if (state_rep[x[i].name] != m_state_rep[x[i].name]) {
		    x[i].style.textDecoration="line-through";
		    x[i].style.opacity="0.6";
		    }
		else {
//		    x[i].style.textDecoration="underline";
		    x[i].style.opacity="0.6";
		}
	    }

	}
    }

    // Retrieve previous values from database - uses object - only one object in each Win class
    x = document.getElementsByClassName("SelRepWin");
    n=state_win[x[0].name];
    idx=RepIndex[n];
    x[0].options[idx].selected="selected";
    if (m_state_win[x[0].name] != "NoSel") {
	if (state_win[x[0].name] != m_state_win[x[0].name]) {
	    x[0].style.opacity="0.6";
	    x[0].style.textDecoration="line-through";
	}
		else {
//		    x[0].style.textDecoration="underline";
		    x[0].style.opacity="0.6";
		}
    }

    x = document.getElementsByClassName("SelDemWin");
    n=state_win[x[0].name];
    idx=DemIndex[n];
    x[0].options[idx].selected="selected";
    if (m_state_win[x[0].name] != "NoSel") {
	if (state_win[x[0].name] != m_state_win[x[0].name]) {
	    x[0].style.opacity="0.6";
	    x[0].style.textDecoration="line-through";
	}
	else {
//	    x[0].style.textDecoration="underline";
	    x[0].style.opacity="0.6";
	}
    }

    // // set target attribute on <a> so links go to a new tab or window
    // x = document.getElementsByTagName("a");
    // i;
    // for (i=0; i < x.length; i++) {
    // 	select = x[i];
    // 	select.target = "_blank";
    // 	//	      select.target = "theiframe";
    // }
}

function Master_Init_Predictions() {
// initialize predictions and set <a> links to open in a new tab

    // Init select fields to select NoSel

    x = document.getElementsByClassName("SelPres");
    // Presidential select has only 1 element (element 0), select NoSel
    x[0].options[0].selected="selected";


    x = document.getElementsByClassName("SelDem");
    for (i = 0; i < x.length; i++) {
	x[i].options[0].selected="selected";
    }

    x = document.getElementsByClassName("SelRep");
    for (i = 0; i < x.length; i++) {
	x[i].options[0].selected="selected";
    }

    x = document.getElementsByClassName("SelWin");
    for (i = 0; i < x.length; i++) {
	x[i].options[0].selected="selected";
    }

}

function Rep_preload(value) {
    var x;
    var i;
    var idx;
    if (value=="") return;
    x = document.getElementsByClassName("SelRep");
    for (i = 0; i < x.length; i++) {
	if (x[i].disabled==false) {
	    idx=RepIndex[value];
	    x[i].options[idx].selected="selected";
	}
    }
}

function Dem_preload(value) {
    var x;
    var i;
    var idx;
    if (value=="") return;
    x = document.getElementsByClassName("SelDem");
    for (i = 0; i < x.length; i++) {
	if (x[i].disabled==false) {
	    idx=DemIndex[value];
	    x[i].options[idx].selected="selected";
	}
    }

}

function Disable_select() {
    // set disabled attribute on <select>
    var x = document.getElementsByTagName("select");
    for (i=0; i < x.length; i++) {
	x[i].disabled="true";
    }
}

function Remove_onclick() {
    // Disable onclick links (use this when displaying master / election results)
    var x = document.getElementsByTagName("a");
    for (i=0; i < x.length; i++) {
	x[i].removeAttribute("onclick");
    }
}


function hide_master_display() {
    // hide some elements when displaying the master (i.e. election results)
    var x;    //http://www.w3schools.com/js/js_htmldom_nodes.asp
    // x.disabled="true";
    // x.style.visibility="hidden";
    x=document.getElementById("CroppedCandidates");
    x.parentNode.removeChild(x);
    x=document.getElementById("instructions");
    x.parentNode.removeChild(x);
    x=document.getElementById("PrimaryPanic");
    x.parentNode.removeChild(x);
    x=document.getElementById("preload1");
    x.parentNode.removeChild(x);
    x=document.getElementById("preload2");
    x.parentNode.removeChild(x);
    $('#show_button').hide();
    $('#up_arrow').hide();
    $('#show_intro_button').hide();
    $('#up_intro_arrow').hide();
}

function hide_master_display_links() {
    // hide some elements when displaying the master (i.e. election results)
    var x = document.getElementById("SubmitSave");
    x.parentNode.removeChild(x);
    x=document.getElementById("url_home_page");
    x.parentNode.removeChild(x);
    x=document.getElementById("url_leaderboard");
    x.parentNode.removeChild(x);
    x=document.getElementById("url_election_results");
    x.parentNode.removeChild(x);
 }
