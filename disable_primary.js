
function disable_primary_select(name) {
    var x = document.getElementsByName(name);
    x[0].disabled="true";
}

function disable_primary() {
    
    var Date_Current = new Date();
    var Date_Feb = new Date("Feb 1, 2016");
    var Date_March = new Date("March 1, 2016");
    var Date_AprMay = new Date("March 1, 2016");
    var Date_June = new Date("March 1, 2016");
    var Date_Aug = new Date("March 1, 2016");

    if (Date_Current >= Date_Feb) {
	disable_primary_select("IA_Rep");
	disable_primary_select("NH_Rep");
	disable_primary_select("SC_Rep");
	disable_primary_select("NV_Rep");
    }

    if (Date_Current >= Date_March) {
    	disable_primary_select("AL_Rep");
    	disable_primary_select("AK_Rep");
    	disable_primary_select("AR_Rep");
    	disable_primary_select("GA_Rep");
    	disable_primary_select("MA_Rep");
    	disable_primary_select("MN_Rep");
    	disable_primary_select("OK_Rep");
    	disable_primary_select("TN_Rep");
    	disable_primary_select("TX_Rep");
    	disable_primary_select("VT_Rep");
    	disable_primary_select("VI_Rep");
    	disable_primary_select("KS_Rep");
    	disable_primary_select("LA_Rep");
    	disable_primary_select("ME_Rep");
    	disable_primary_select("PR_Rep");
    	disable_primary_select("HI_Rep");
    	disable_primary_select("ID_Rep");
    	disable_primary_select("MS_Rep");
    	disable_primary_select("MI_Rep");
    	disable_primary_select("WY_Rep");
    	disable_primary_select("NC_Rep");
    	disable_primary_select("OH_Rep");
    	disable_primary_select("FL_Rep");
    	disable_primary_select("IL_Rep");
    	disable_primary_select("MO_Rep");
    	disable_primary_select("AZ_Rep");
    	disable_primary_select("UT_Rep");
    	disable_primary_select("ND_Rep");
    }

    if (Date_Current >= Date_AprMay) {
    	disable_primary_select("WI_Rep");
    	disable_primary_select("NY_Rep");
    	disable_primary_select("CT_Rep");
    	disable_primary_select("DE_Rep");
    	disable_primary_select("MD_Rep");
    	disable_primary_select("PA_Rep");
    	disable_primary_select("RI_Rep");
    	disable_primary_select("IN_Rep");
    	disable_primary_select("NB_Rep");
    	disable_primary_select("WV_Rep");
    	disable_primary_select("KT_Rep");
    	disable_primary_select("OR_Rep");
    	disable_primary_select("WA_Rep");
    }

    if (Date_Current >= Date_June) {
    	disable_primary_select("CA_Rep");
    	disable_primary_select("MT_Rep");
    	disable_primary_select("NJ_Rep");
    	disable_primary_select("NM_Rep");
    	disable_primary_select("SD_Rep");
    	disable_primary_select("DC_Rep");
    }

    if (Date_Current >= Date_Aug) {
    	disable_primary_select("GOP_Winner");
    	disable_primary_select("President");
    	disable_primary_select("Dem_Winner");
    }

    if (Date_Current >= Date_June) {
    	disable_primary_select("PR_Dem");
    	disable_primary_select("CA_Dem");
    	disable_primary_select("MT_Dem");
    	disable_primary_select("NJ_Dem");
    	disable_primary_select("NM_Dem");
    	disable_primary_select("ND_Dem");
    	disable_primary_select("SD_Dem");
    	disable_primary_select("DC_Dem");
    }

    if (Date_Current >= Date_AprMay) {
    	disable_primary_select("WI_Dem");
    	disable_primary_select("WY_Dem");
    	disable_primary_select("NY_Dem");
    	disable_primary_select("CT_Dem");
    	disable_primary_select("MD_Dem");
    	disable_primary_select("DE_Dem");
    	disable_primary_select("PA_Dem");
    	disable_primary_select("RI_Dem");
    	disable_primary_select("IN_Dem");
    	disable_primary_select("NB_Dem");
    	disable_primary_select("WV_Dem");
    	disable_primary_select("KT_Dem");
    	disable_primary_select("OR_Dem");
    	disable_primary_select("WA_Dem");
    }

    if (Date_Current >= Date_March) {
    	disable_primary_select("AL_Dem");
    	disable_primary_select("AR_Dem");
    	disable_primary_select("CO_Dem");
    	disable_primary_select("GA_Dem");
    	disable_primary_select("MA_Dem");
    	disable_primary_select("MN_Dem");
    	disable_primary_select("OK_Dem");
    	disable_primary_select("TN_Dem");
    	disable_primary_select("TX_Dem");
    	disable_primary_select("VT_Dem");
    	disable_primary_select("VI_Dem");
    	disable_primary_select("KS_Dem");
    	disable_primary_select("LA_Dem");
    	disable_primary_select("ME_Dem");
    	disable_primary_select("MS_Dem");
    	disable_primary_select("MI_Dem");
    	disable_primary_select("NC_Dem");
    	disable_primary_select("OH_Dem");
    	disable_primary_select("FL_Dem");
    	disable_primary_select("IL_Dem");
    	disable_primary_select("MO_Dem");
    	disable_primary_select("AZ_Dem");
    	disable_primary_select("ID_Dem");
    	disable_primary_select("HI_Dem");
    	disable_primary_select("UT_Dem");
    	disable_primary_select("AK_Dem");
    }

    if (Date_Current >= Date_Feb) {
    	disable_primary_select("IA_Dem");
    	disable_primary_select("NH_Dem");
    	disable_primary_select("SC_Dem");
    	disable_primary_select("NV_Dem");
    }
}
