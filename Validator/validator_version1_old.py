#########################################
#####Validator Dec/4th/2014 #############
#####Yongjie Xin ########################
### to compare the reco jets w.r.t ######
### gen jets and see their pt ratio #####
### distribution and will be implemented#
### with a fit function #################


import os
import glob
import math

#import ROOT
from ROOT import *
#ROOT.gROOT.Macro("rootlogon.C")

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle


from optparse import OptionParser
parser = OptionParser()

parser.add_option("-f", "--fileIn", dest="inputFile",
                  help="inputFile path")
parser.add_option("-o", "--output",dest="outputFileName",
                  help="output file name")


(options, args) = parser.parse_args()

files = glob.glob( options.inputFile + "PFL2_out_All10000Events_11*_*.root" )
#files = glob.glob( options.inputFile + "*.root" )
#files = glob.glob( options.inputFile )

print "input file path                  ", options.inputFile
print "output file name                 ", options.outputFileName


#this function is used to calculate deltaR
def deltaR( particle, jet ) : # could be used as deltaR(jet1, jet2) 
    """
        The existence of this code is because reco:candidate don't have 
        a deltaR function for them. deltaR will take two reco:candidate as
        input and calculate the dR between them, which is
        #sqrt{ dEta^2+dPhi^2 }.  
    """
    DeltaPhiHere = math.fabs( particle.phi() - jet.phi() )
    if DeltaPhiHere > math.pi :
        DeltaPhiHere = 2*math.pi - DeltaPhiHere

    deltaRHere = math.sqrt( (particle.eta() - jet.eta() )**2 + ( DeltaPhiHere )**2  )
    return deltaRHere


def Between( Num0, Low, High ) :

    if Low < Num0 < High :
	return True
    else :
	return False

def Response( Jet, EtaBin, PtBin ) # base on jet's pt and eta, return response value pair (a, b) 
   """
     Return response according to the EtaBin and PtBin
   """
    for i in range( len(EtaBin) - 1 ) :
	for j in range( len(PtBin) -1 ) :
	    if Between( Jet.eta(), EtaBin[i], EtaBin[i+1] ) and Between( Jet.pt(), PtBin[j], PtBin[j+1]) :
	 	return (i, j)
	    else :
		return "In response, no eta and pt found in the defined ranges"



def compare(ptList, etaList,  jets1, jets2, verbose) : #jets1 is a vector of jets
    """
       Compare two vectors of jets and matching them by each jet's dR 
       and return their pt1/pt_gen lists, we always put jets2 as gen jets
       which we call the reference jets
       ptList and etaList are lists, two float numbers
       ptList is the pt range for the reference jets
       etaList is the eta range for the reference jets
       This code is very not efficient.  better to have an array or something.  
    """
    if verbose == 0 :
	pass
    else :
	print "details of dR of those jets"	
    ratioVector = [] #store the output
    for jet2 in jets2 :
	if ( (ptList[0] <= jet2.pt() <= ptList[1]) and (etaList[0] <= jet2.eta() <= etaList[1])  ) :
	    pass #only study events in the desired pt and eta range
	else :
	    continue
    	for jet1 in jets1 :
	    dR = deltaR( jet1, jet2 )
	    if dR < 0.1  :
	    	ratioVector.append( jet1.pt()/jet2.pt() )
	    else :
		if (verbose == 0) :
		   pass
		else :
		   print dR
    return ratioVector

def compare( jets1, jets2, verbose ) 
    """
       new version of compare function
       ratioVector is a matrix of form 
       5 * 15 matrix 

       [         pt0to200, pt200to 400, ....                    
       eta0to1   [....  ]  [.....]      [.....]
       eta1to2   [.....]   [.....]      [.....]
       ...
       ....
       ]
       Not finished yet !!!!!!!!!!
    """
    if verbose == 0 :
	pass
    else :
	print "details of dR of those jets"

    ratioVector = []
     
    for jet1 in jets1 :
        for jet2 in jets2 :
	    dR = deltaR( jet1, jet2 )
	    
 	    #if 0 <= jet2.pt() <= 200 and 0 < jet2.eta() < 1.0 :

def compare( jets1, jets2, ListPlots, EtaBin, PtBin )
    """
       directly fill the plots, ListPlots are a list of TH1 plots, 
       ListPlots structure :
	Eta0to1Pt0to200, Eta0to1Pt200to400, .....
	Eta1to2Pt0to200, Eta1to2Pt200to400, .....
    """		
    for jet1 in jets1 :
	for jet2 in jets2 :
	    dR = deltaR( jet1, jet2 )
	    if dR < 0.1 :
	        (a, b) = Response( jet2, EtaBin, PtBin )
	        ListPlots[a][b].Fill( jet1.pt()/jet2.pt() )
    return 0


def FillPlot( Plot1, List1 ) :
    """
        loop ove the List1, and fill the Plot1
    """
    for listNum in List1 :
	Plot1.Fill( listNum )	
    return 0
#    return Plot1   # I don't think we need the return 


f =  TFile(options.outputFileName, 'recreate')

f.cd()

ak4GenJetsHandle = Handle( "vector<reco::GenJet>" )
ak4GenJetsLabel  = ( "ak4GenJets",                 "" )

ak4PFClusterJetsHandle = Handle( "vector<reco::PFClusterJet>"  )
ak4PFClusterJetsLabel  = (  "ak4PFClusterJets",          "" )

ak4PFJetsHandle = Handle( "vector<reco::PFJet>"  )  #the Ak4 PF jets
ak4PFJetsLabel  = (  "hltL2PFJets",          "" )

ak4CaloJetsHandle = Handle( "vector<reco::CaloJet>" )
ak4CaloJetsLabel  = (  "ak4CaloJets",               "")

ak4PFJetsRealLabel = (  "ak4PFJets" ,              "")

#binning = [0, 200, 400, 600, 800, 1000, 1200, 1400, 2000, 2500, 3000] # this is list of range points
binning = range(0, 3000, 200)
#etaBinning = [0, 0.5, 1.0, 2.5, 2.7]
etaBinning = range(0, 5, 1) # will deal with this later


LastNames = []
MiddleNames = []
for i in range( len(binning) -1 ) :
    LastNames.append( str(binning[i]) + "to" + str(binning[i+1]) ) 
for i in range( len(etaBinning) -1 ) :
    MiddleNames.append( str(etaBinning[i]) + "to" + str(etaBinning[i+1]) )

# List to store plots
PFClusterPlotsList = []
PFRealPlotsList    = []
CaloPlotsList 	   = []
PFNoTrackPlotsList = []

for m in range( len(etaBinning) ) :
    PFClusterPlotsList.append( [] )
    PFRealPlotsList.append( [] )
    CaloPlotsList.append( [] )
    PFClusterPlotsList.append( [] )
  
FirstNames = [ "rPFClusterGen", "rPFNoTrackGen", "rCaloGen", "PFReal"]

for j in range( len(etaBinning) ) :
    for i in range( len(binning) ) :
        # will be 5 * 15 plots in each Lists, takes a lot memory. Careful.  
	PFClusterPlotsList[j].append( TH1F(FirstNames[0] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )
        PFNoTrackPlotsList[j].append( TH1F(FirstNames[1] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )
        CaloPlotsList[j].append(      TH1F(FirstNames[2] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )
        PFRealPlotsList[j].append(    TH1F(FirstNames[3] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )

print len( PFClusterPlotsList )
print PFClusterPlotsList
#rPFClusterGenPlot0 = TH1F( FirstNames[0] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )
#rPFGenPlot0 = TH1F( FirstNames[1] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )
#
#rCaloGenPlot0 = TH1F( FirstNames[2] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )
#rCaloGenPlot1 = TH1F( FirstNames[2] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[1], "", 200, 0, 2  )
#
#rPFRealGenPlot0 = TH1F( FirstNames[3] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )





print files
events = Events(files)

count = 0
print "Start looping"
for event in events :
    count = count + 1
    if count % 100 == 0 :
        print "processing events", count
    #if count > 10 :
#	break

    event.getByLabel (ak4GenJetsLabel, ak4GenJetsHandle)
    ak4GenJets = ak4GenJetsHandle.product()

    event.getByLabel (ak4PFClusterJetsLabel, ak4PFClusterJetsHandle)
    ak4PFClusterJets = ak4PFClusterJetsHandle.product()

    event.getByLabel (ak4PFJetsLabel, ak4PFJetsHandle)
    ak4PFJets = ak4PFJetsHandle.product()

    event.getByLabel (ak4CaloJetsLabel, ak4CaloJetsHandle)
    ak4CaloJets = ak4CaloJetsHandle.product()

    event.getByLabel (ak4PFJetsRealLabel, ak4PFJetsHandle )
    ak4PFReal = ak4PFJetsHandle.product()

    #Find the dR < 0.1 jet to Ak4 Gen jets    
    #print len(ak4GenJets), len(ak4PFClusterJets) , len(ak4PFJets), len(ak4CaloJets)
    #print dir(ak4GenJets[0])
    #print dir(ak4PFClusterJets[0])
    for i in range( len(binning) -1 ) :
	ptRange = [ binning[i], binning[i+1] ] 
	#print len(etaBinning)
	for j in range( len(etaBinning) -1 ) :
            #print j
	    etaRange = [ etaBinning[j], etaBinning[j+1] ] 

	    #use pt and eta Range of reference jets,get the ratio values
	    rPFClusterJetsGen = compare( ptRange, etaRange, ak4PFClusterJets, ak4GenJets, 0 ) #this return the list
	    rPFJetsGen = compare( ptRange, etaRange, ak4PFJets, ak4GenJets, 0 ) #this return the list
	    rCaloJetsGen = compare( ptRange, etaRange, ak4CaloJets, ak4GenJets, 0 ) #this return the list
	    rPFReal  = compare( ptRange, etaRange, ak4PFReal, ak4GenJets, 0 )
	 
	    if ( ptRange[0] == 0 and etaRange[0] == 0) :
            	FillPlot( rPFClusterGenPlot0, rPFClusterJetsGen )
	    	FillPlot( rPFGenPlot0, rPFJetsGen )
		FillPlot( rCaloGenPlot0, rCaloJetsGen )
		FillPlot( rPFRealGenPlot0, rPFReal )

	    if ( ptRange[0] == 200 and etaRange[0] == 0) :
            	FillPlot( rPFClusterGenPlot1, rPFClusterJetsGen )
	    	FillPlot( rPFGenPlot1, rPFJetsGen )
		FillPlot( rCaloGenPlot1, rCaloJetsGen )
		FillPlot( rPFRealGenPlot1, rPFReal )

	    if ( ptRange[0] == 400 and etaRange[0] == 0) :
            	FillPlot( rPFClusterGenPlot2, rPFClusterJetsGen )
	    	FillPlot( rPFGenPlot2, rPFJetsGen )
		FillPlot( rCaloGenPlot2, rCaloJetsGen )
		FillPlot( rPFRealGenPlot2, rPFReal )

	    if ( ptRange[0] == 600 and etaRange[0] == 0) :
            	FillPlot( rPFClusterGenPlot3, rPFClusterJetsGen )
	    	FillPlot( rPFGenPlot3, rPFJetsGen )
		FillPlot( rCaloGenPlot3, rCaloJetsGen )
		FillPlot( rPFRealGenPlot3, rPFReal )
	
	    if ( ptRange[0] == 800 and etaRange[0] == 0) :
            	FillPlot( rPFClusterGenPlot4, rPFClusterJetsGen )
	    	FillPlot( rPFGenPlot4, rPFJetsGen )
		FillPlot( rCaloGenPlot4, rCaloJetsGen )
		FillPlot( rPFRealGenPlot4, rPFReal )

	    if ( ptRange[0] == 1000 and etaRange[0] == 0) :
            	FillPlot( rPFClusterGenPlot5, rPFClusterJetsGen )
	    	FillPlot( rPFGenPlot5, rPFJetsGen )
		FillPlot( rCaloGenPlot5, rCaloJetsGen )
		FillPlot( rPFRealGenPlot5, rPFReal )

	    if ( ptRange[0] == 1200 and etaRange[0] == 0) :
            	FillPlot( rPFClusterGenPlot6, rPFClusterJetsGen )
	    	FillPlot( rPFGenPlot6, rPFJetsGen )
		FillPlot( rCaloGenPlot6, rCaloJetsGen )
		FillPlot( rPFRealGenPlot6, rPFReal )



print "OK"

f.cd()
f.Write()
f.Close()






 
	
"""
	    Switch( ptRange[0] ) {
		case 0 :
		    Switch ( etaRange[0] ) :
		        case 0 :
		            PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )
                            PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )
                            PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )

	    }  
 
	    

    #return the ratio values
    rPFClusterJetsGen = compare([0, 100], [0, 0.5], ak4PFClusterJets, ak4GenJets, 0 ) #this return the list
    rPFJetsGen = compare([0, 100], [0, 0.5], ak4PFJets, ak4GenJets, 0 ) #this return the list
    rCaloJetsGen = compare([0, 100], [0, 0.5], ak4CaloJets, ak4GenJets, 0 ) #this return the list
    # make the plots
    PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )  
    PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )  
    PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )  
#    print rPFClusterJetsGen
#    if len(rPFClusterJetsGen)  == 0:
#	compare( ak4PFClusterJets, ak4GenJets, 1 )

    #return the ratio values
    rPFClusterJetsGen = compare([100, 200], [0, 0.5], ak4PFClusterJets, ak4GenJets, 0 ) #this return the list
    rPFJetsGen = compare([100, 200], [0, 0.5], ak4PFJets, ak4GenJets, 0 ) #this return the list
    rCaloJetsGen = compare([100,200], [0, 0.5], ak4CaloJets, ak4GenJets, 0 ) #this return the list
    # make the plots
    PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )  
    PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )  
    PlotFill( rPFClusterGen0to100Plot, rPFClusterJetsGen )  

"""

