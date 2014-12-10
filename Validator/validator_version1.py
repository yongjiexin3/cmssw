#########################################
#####Validator Dec/4th/2014 #############
#####Yongjie Xin ########################
### to compare the reco jets w.r.t ######
### gen jets and see their pt ratio #####
### distribution and will be implemented#
### with a fit function #################
### some of the lines are not optimal####
#########################################

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

#files = glob.glob( options.inputFile + "PFL2_out_All10000Events_11*_*.root" )
files = glob.glob( options.inputFile + "*.root" )
#files = glob.glob( options.inputFile )

print "input file path                  ", options.inputFile
print "output file name                 ", options.outputFileName


#some constants, globally
ptMin = 0
#ptMax = 3000
ptMax = 200
ptStep = 20
#ptStep = 200

etaMin = 0
etaMax = 5
etaStep = 1




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

    if Low < math.fabs(Num0) < High :
	return True
    else :
	return False

def Response( Jet, EtaBin, PtBin ) : # base on jet's pt and eta, return response value pair (a, b) 
    """
     Return response according to the EtaBin and PtBin
    """
    #print EtaBin
    #print PtBin
    for i in range( len(EtaBin)  ) :
	for j in range( len(PtBin) ) :
	    if Between( Jet.eta(), EtaBin[i], EtaBin[i]+etaStep ) and Between( Jet.pt(), PtBin[j], PtBin[j]+ptStep ) :
		#print Jet.eta(), Jet.pt(), "success"
	 	return (i, j)
	    else :
		continue
		#print Jet.eta(), Jet.pt()
		#print "In response, no eta and pt found in the defined ranges"
	        #break 
    print Jet.eta(), Jet.pt()    


def compare( jets1, jets2, ListPlots, EtaBin, PtBin ) :
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
		if jet2.pt() > ptMax or math.fabs(jet2.eta()) > etaMax : #skip these events
		    continue
		else :
	            (a, b) = Response( jet2, EtaBin, PtBin )
	            ListPlots[a][b].Fill( jet1.pt()/jet2.pt() )
    return 0




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


# Note: range function only works when the step is integer
# one needs to reimplement it when the stop is float 
binning = range( ptMin, ptMax, ptStep )
etaBinning = range( etaMin, etaMax, etaStep) 

LastNames = []
MiddleNames = []
#Note : +200 and +1 is not quite efficient
for i in range( len(binning) ) :
    LastNames.append( str(binning[i]) + "to" + str(binning[i] + ptStep) )
for i in range( len(etaBinning) ) :
    MiddleNames.append( str(etaBinning[i]) + "to" + str(etaBinning[i]+etaStep) )

# List to store plots
PFClusterPlotsList = []
PFRealPlotsList    = []
CaloPlotsList 	   = []
PFNoTrackPlotsList = []

for m in range( len(etaBinning) ) :
    PFClusterPlotsList.append( [] )
    PFRealPlotsList.append( [] )
    CaloPlotsList.append( [] )
    PFNoTrackPlotsList.append( [] )
  
FirstNames = [ "rPFClusterGen", "rPFNoTrackGen", "rCaloGen", "PFReal"]

print  PFClusterPlotsList, len(binning)

for j in range( len(etaBinning) ) :
    for i in range( len(binning) ) :
        # will be 5 * 15 plots in each Lists, takes a lot memory. Careful. 
        #print j, i 
	PFClusterPlotsList[j].append( TH1F(FirstNames[0] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )
        PFNoTrackPlotsList[j].append( TH1F(FirstNames[1] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )
        CaloPlotsList[j].append(      TH1F(FirstNames[2] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )
        PFRealPlotsList[j].append(    TH1F(FirstNames[3] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i], "",  200, 0, 2) )

#print len( PFClusterPlotsList )
#print PFClusterPlotsList
#rPFClusterGenPlot0 = TH1F( FirstNames[0] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )
#rPFGenPlot0 = TH1F( FirstNames[1] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )
#
#rCaloGenPlot0 = TH1F( FirstNames[2] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )
#rCaloGenPlot1 = TH1F( FirstNames[2] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[1], "", 200, 0, 2  )
#
#rPFRealGenPlot0 = TH1F( FirstNames[3] +"Eta" +  MiddleNames[0] +"Pt"+LastNames[0], "", 200, 0, 2  )

## Plot the PF energy fraction plots for AK4 without tracks jets
EtaRange = [0, 1.3, 3.0]
ListFractionNames = ['chargedEmEnergyFractionPlot', 'chargedHadronEnergyFractionPlot', 'chargedMuEnergyFractionPlot', \
                     'electronEnergyFractionPlot', 'HFEMEnergyFractionPlot', 'HFHadronEnergyFractionPlot', \
			'muonEnergyFractionPlot', 'neutralEmEnergyFractionPlot', 'neutralHadronEnergyFractionPlot', \
 			'photonEnergyFractionPlot']

FractionPlotLists = []
for i in range( len(EtaRange) ) :
    for jName in ListFractionNames :
	if EtaRange[i] != 3.0 :
	    FractionPlotLists.append( TH1F( jName+"Eta"+str(EtaRange[i])+"to"+str(EtaRange[i+1]), '', 100, 0, 1) )
	else :
	    FractionPlotLists.append( TH1F( jName+"Eta"+str(EtaRange[i])+"Up", '', 100, 0, 1) )

#the Plot matrix is like this :
# eta = 0,  chargedEmEnergyFractionPlot, chargedHadronEnergyFractionPlot, .........
# eta = 1.3, chargedEmEnergyFractionPlot, chargedHadronEnergyFractionPlot, ........

#chargedEmEnergyFractionPlot = TH1F( 'chargedEmEnergyFractionPlot', 'chargedEmEnergyFractionPlot', 200, 0, 2 )
#chargedHadronEnergyFractionPlot = TH1F( 'chargedHadronEnergyFractionPlot', 'chargedHadronEnergyFractionPlot', 200, 0, 2 ) 
#chargedMuEnergyFractionPlot     = TH1F( 'chargedMuEnergyFractionPlot', 'chargedMuEnergyFractionPlot', 200, 0, 2 )
#electronEnergyFractionPlot	= TH1F( 'electronEnergyFractionPlot', '', 200, 0, 2 )   
#HFEMEnergyFractionPlot		= TH1F( 'HFEMEnergyFractionPlot', '', 200, 0, 2 ) 
#HFHadronEnergyFractionPlot	= TH1F( 'HFHadronEnergyFractionPlot', '', 200, 0, 2 )
#muonEnergyFractionPlot		= TH1F( 'muonEnergyFractionPlot', '', 200, 0, 2 )
#neutralEmEnergyFractionPlot	= TH1F( 'neutralEmEnergyFractionPlot', '', 200, 0, 2 )
#neutralHadronEnergyFractionPlot	= TH1F( 'neutralHadronEnergyFractionPlot', '', 200, 0, 2 )
#photonEnergyFractionPlot	= TH1F( 'photonEnergyFractionPlot', '', 200, 0, 2 )

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
    ak4PFNoTrackJets = ak4PFJetsHandle.product()

    event.getByLabel (ak4CaloJetsLabel, ak4CaloJetsHandle)
    ak4CaloJets = ak4CaloJetsHandle.product()

    event.getByLabel (ak4PFJetsRealLabel, ak4PFJetsHandle )
    ak4PFRealJets = ak4PFJetsHandle.product()

    for iJet in ak4PFNoTrackJets :
        ListFraction = []
	ListFraction.append( iJet.chargedEmEnergyFraction() )
	ListFraction.append( iJet.chargedHadronEnergyFraction() )
	ListFraction.append( iJet.chargedMuEnergyFraction() )
	ListFraction.append( iJet.electronEnergyFraction() ) 
	ListFraction.append( iJet.HFEMEnergyFraction() ) 
	ListFraction.append( iJet.HFHadronEnergyFraction() ) 
	ListFraction.append( iJet.muonEnergyFraction() ) 
	ListFraction.append( iJet.neutralEmEnergyFraction() ) 
	ListFraction.append( iJet.neutralHadronEnergyFraction() ) 
	ListFraction.append( iJet.photonEnergyFraction() ) 
	if Between( iJet.eta(), 0,  1.3) :
	    for i in range( len(ListFraction) ) :
		FractionPlotLists[i].Fill( ListFraction[i] )			
	elif Between( iJet.eta(), 1.3, 3.0 ) :
	    for i in range( len(ListFraction) ) :
		FractionPlotLists[ len(ListFraction) + i ].Fill( ListFraction[i] )
	else :
            for i in range( len(ListFraction) ) :
                FractionPlotLists[ 2*len(ListFraction) + i ].Fill( ListFraction[i] )

    ###plot the CHF and neutral hadron fraction for pF without tracks jets
#    print dir(ak4PFNoTrackJets[0])
#    break
    compare( ak4PFClusterJets, ak4GenJets, PFClusterPlotsList, etaBinning, binning )
    compare( ak4PFNoTrackJets, ak4GenJets, PFNoTrackPlotsList, etaBinning, binning )
    compare( ak4CaloJets,      ak4GenJets, CaloPlotsList,      etaBinning, binning )
    compare( ak4PFRealJets,    ak4GenJets, PFRealPlotsList,    etaBinning, binning )




print "OK"

f.cd()
f.Write()
f.Close()






