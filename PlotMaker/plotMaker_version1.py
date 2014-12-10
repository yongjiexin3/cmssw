### very naitive one #####
### just as a starter ####
### to make these plot ###
### left open to write ###
### a more compact one ###
### to draw all plots#####

### Plot maker ###########
### Yongjie Xin ##########
### Dec/5th/2014 #########
##########################

import math
from ROOT import *
import numpy as n

TGaxis.SetMaxDigits(3)

gROOT.Reset()
gROOT.ForceStyle();
gROOT.SetStyle("Plain")
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)
gStyle.SetTitleOffset(1.2,"Y")
gStyle.SetPadLeftMargin(0.18)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadTopMargin(0.06)
gStyle.SetPadRightMargin(0.05)
gStyle.SetMarkerSize(0.5)
gStyle.SetHistLineWidth(1)
gStyle.SetStatFontSize(0.020)
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetNdivisions(510, "XYZ")
gStyle.SetLegendBorderSize(0)
gStyle.SetTitleFont(62)


f = TFile( "PlotsGenRecoAll.root" )

#some constants, globally
ptMin = 0
ptMax = 200
ptStep = 20
etaMin = 0
etaMax = 5
etaStep = 1


binning = range( ptMin, ptMax, ptStep )
etaBinning = range( etaMin, etaMax, etaStep)

LastNames = []
MiddleNames = []
#Note : +200 and +1 is not quite efficient
for i in range( len(binning) ) :
    LastNames.append( str(binning[i]) + "to" + str(binning[i] + ptStep) )
for i in range( len(etaBinning) ) :
    MiddleNames.append( str(etaBinning[i]) + "to" + str(etaBinning[i]+etaStep) )

FirstNames = [ "rPFClusterGen", "rPFNoTrackGen", "rCaloGen", "PFReal"]

def plotBeautify( plot1, lineColor, lineStyle) :
    plot1.SetLineColor( lineColor )
    plot1.SetLineStyle( lineStyle )
    plot1.Rebin( 2 )
    plot1.SetLineWidth(2)
    if plot1.Integral() != 0 :
        plot1.Scale( 1.0/plot1.Integral() )

def FitDistr( Histogram1, lineColor ) :
    """
	Gaussian fit twice, the second fit 
        is bounded in range[mean-sigma, mean+sigma]
	return second fit results,  (mean, sigma)
    """
    Histogram1.Fit( "gaus" )
    if Histogram1.GetFunction( "gaus" ) == None :
	print "HHAHHHHAHHHHHHHHHHHHHHHHHHHH"
	return ( "None", "None")
    else :
        mean = Histogram1.GetFunction( "gaus" ).GetParameter(1)
        sigma = Histogram1.GetFunction( "gaus" ).GetParameter(2)
        Histogram1.Fit( "gaus", "R", "", mean-sigma, mean+sigma )
        Histogram1.GetFunction( "gaus" ).SetLineColor( lineColor )
        return ( "%.2f" % Histogram1.GetFunction( "gaus" ).GetParameter(1), "%.2f" % Histogram1.GetFunction( "gaus" ).GetParameter(2)  )


for j in range( len(etaBinning) ) :
    for i in range( len(binning) ) :
        # will be 5 * 15 plots in each Lists, takes a lot memory. Careful. 
        #print j, i 
        
	g1 = f.Get( FirstNames[0] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i] )
	p1 = f.Get( FirstNames[1] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i] )
	h1 = f.Get( FirstNames[2] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i] )
	d1 = f.Get( FirstNames[3] +"Eta" +  MiddleNames[j] +"Pt"+LastNames[i] )


	plotBeautify( g1, 2, 1 )
	plotBeautify( p1, 4, 1 )
	plotBeautify( h1, 6, 1 )
	plotBeautify( d1, 12, 1 )

	g1AB = FitDistr( g1, 2 )
	p1AB = FitDistr( p1, 4 )
	h1AB = FitDistr( h1, 6 )
	d1AB = FitDistr( d1, 12)

	leg = TLegend( 0.6, 0.68, 0.8, 0.85 )
	leg.SetTextSize(0.03)
	leg.SetFillStyle(0)
	leg.AddEntry( g1, "PFCluster_#mu"+g1AB[0] + "_#sigma"+g1AB[1], "l")
	leg.AddEntry( p1, "PFNoTrack_#mu"+p1AB[0] + "_#sigma"+p1AB[1], "l")
	leg.AddEntry( h1, "CaloJets__#mu"+h1AB[0] + "_#sigma"+h1AB[1], "l")
	leg.AddEntry( d1, "PFJets____#mu"+d1AB[0] + "_#sigma"+d1AB[1], "l")

	#g1.SetTitle( "Eta in [0, 1], Pt in [0, 200] GeV" )
	d1.SetTitle( "Eta in "+ str(etaBinning[j]) + "to" + str(etaBinning[j] + etaStep) + \
		"  Pt in" + str(binning[i]) + "to" + str(binning[i]+ptStep)  )
	d1.SetXTitle( "P_{T}/P_{T}^{Gen}" )
	#d1.GetXaxis().SetRangeUser( 0.4, 1.6)

	c = TCanvas( "c", "c", 400, 400 )
	#c.SetLogy()
	d1.Draw(  ) 
	g1.Draw( "same" )
	h1.Draw( "same" )
	p1.Draw( "same" )
	leg.Draw()
	c.SaveAs( "Eta" +  MiddleNames[j] +"Pt"+LastNames[i]  + ".pdf" )




  	#break



