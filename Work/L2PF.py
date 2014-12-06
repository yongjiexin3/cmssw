# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --conditions auto:run2_mc -s RAW2DIGI,L1Reco,RECO,EI,VALIDATION,DQM --datatier GEN-SIM-RECO,DQMIO -n 10 --magField 38T_PostLS1 --eventcontent RECOSIM,DQM --io RECOUP15.io --python RECOUP15.py --no_exec --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),                        
    fileNames = cms.untracked.vstring(
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/1A78B4DC-4376-E411-AD8A-FA163EB758D0.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/1AD05394-4476-E411-9881-02163E010F14.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/1EB6FED2-3E76-E411-8D3C-FA163EB058FA.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/283AE333-B676-E411-97F6-02163E00EB7E.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/32A26531-3D76-E411-9C7B-02163E00EAEA.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/3EFB1339-4076-E411-BB1D-02163E010EEA.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/7EC17A08-6277-E411-9543-02163E010DBE.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/C0C5A838-6476-E411-8781-002590494DA0.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/C2956D4A-3E76-E411-9FDF-0025904B5B28.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/DCB8B5EA-5476-E411-B915-02163E00EA4C.root',
'/store/relval/CMSSW_7_3_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-RECO/MCRUN2_73_V5-v1/00000/E0EE3345-3376-E411-AEF5-FA163E27E9EE.root',
     )
)


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('PFL2_out.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECO')
    )
)

process.RECOSIMoutput.outputCommands.append( "keep *_*_*_RECO2") 

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('DQMIO')
    )
)


##########################################################PF L2 Configuration########################################################
process.hltParticleFlowRecHitECAL = cms.EDProducer("PFRecHitProducer",
    producers = cms.VPSet(cms.PSet(
        src = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        name = cms.string('PFEBRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            threshold = cms.double(0.08),
            name = cms.string('PFRecHitQTestThreshold')
        ), 
            cms.PSet(
                skipTTRecoveredHits = cms.bool(True),
                cleaningThreshold = cms.double(2.0),
                timingCleaning = cms.bool(True),
                name = cms.string('PFRecHitQTestECAL'),
                topologicalCleaning = cms.bool(True)
            ))
    ), 
        cms.PSet(
            src = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                threshold = cms.double(0.3),
                name = cms.string('PFRecHitQTestThreshold')
            ), 
                cms.PSet(
                    skipTTRecoveredHits = cms.bool(True),
                    cleaningThreshold = cms.double(2.0),
                    timingCleaning = cms.bool(True),
                    name = cms.string('PFRecHitQTestECAL'),
                    topologicalCleaning = cms.bool(True)
                ))
        )),
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator'),
        endcap = cms.PSet(

        )
    )
)


process.hltParticleFlowRecHitHBHE = cms.EDProducer("PFRecHitProducer",
    producers = cms.VPSet(cms.PSet(
        src = cms.InputTag("hbhereco"),
        name = cms.string('PFHBHERecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            threshold = cms.double(0.8),
            name = cms.string('PFRecHitQTestThreshold')
        ), 
            cms.PSet(
                maxSeverities = cms.vint32(11),
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                name = cms.string('PFRecHitQTestHCALChannel')
            ))
    )),
    navigator = cms.PSet(
        sigmaCut = cms.double(4.0),
        timeResolutionCalc = cms.PSet(
            constantTermLowE = cms.double(6.0),
            noiseTermLowE = cms.double(0.0),
            constantTerm = cms.double(1.92),
            noiseTerm = cms.double(8.64),
            corrTermLowE = cms.double(0.0),
            threshLowE = cms.double(2.0),
            threshHighE = cms.double(8.0)
        ),
        name = cms.string('PFRecHitHCALNavigator')
    )
)


process.hltParticleFlowRecHitHF = cms.EDProducer("PFRecHitProducer",
    producers = cms.VPSet(cms.PSet(
        HADDepthCorrection = cms.double(25.0),
        src = cms.InputTag("hfreco"),
        LongFibre_Cut = cms.double(120.0),
        ShortFibre_Cut = cms.double(60.0),
        qualityTests = cms.VPSet(cms.PSet(
            maxSeverities = cms.vint32(11, 9, 9),
            cleaningThresholds = cms.vdouble(0.0, 120.0, 60.0),
            flags = cms.vstring('Standard', 
                'HFLong', 
                'HFShort'),
            name = cms.string('PFRecHitQTestHCALChannel')
        ), 
            cms.PSet(
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth'),
                cuts = cms.VPSet(cms.PSet(
                    threshold = cms.double(1.2),
                    depth = cms.int32(1)
                ), 
                    cms.PSet(
                        threshold = cms.double(1.8),
                        depth = cms.int32(2)
                    ))
            )),
        LongFibre_Fraction = cms.double(0.1),
        EMDepthCorrection = cms.double(22.0),
        thresh_HF = cms.double(0.4),
        ShortFibre_Fraction = cms.double(0.01),
        HFCalib29 = cms.double(1.07),
        name = cms.string('PFHFRecHitCreator')
    )),
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        name = cms.string('PFRecHitHCALNavigator'),
        endcap = cms.PSet(

        )
    )
)


process.hltParticleFlowRecHitHO = cms.EDProducer("PFRecHitProducer",
    producers = cms.VPSet(cms.PSet(
        src = cms.InputTag("horeco"),
        name = cms.string('PFHORecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            threshold = cms.double(0.05),
            name = cms.string('PFRecHitQTestThreshold')
        ), 
            cms.PSet(
                maxSeverities = cms.vint32(11),
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                name = cms.string('PFRecHitQTestHCALChannel')
            ))
    )),
    navigator = cms.PSet(
        name = cms.string('PFRecHitHCALNavigator')
    )
)


process.hltParticleFlowClusterECAL = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.08),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTermLowE = cms.double(0.0),
                noiseTermLowE = cms.double(1.31883),
                constantTerm = cms.double(0.428192),
                noiseTerm = cms.double(1.10889),
                corrTermLowE = cms.double(0.0510871),
                threshLowE = cms.double(0.5),
                threshHighE = cms.double(5.0)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTermLowE = cms.double(0.0),
                noiseTermLowE = cms.double(6.92683000001),
                constantTerm = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                corrTermLowE = cms.double(0.0),
                threshLowE = cms.double(1.0),
                threshHighE = cms.double(10.0)
            ),
            minAllowedNormalization = cms.double(1e-09)
        ),
        showerSigma = cms.double(1.5),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.08),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTermLowE = cms.double(0.0),
                noiseTermLowE = cms.double(1.31883),
                constantTerm = cms.double(0.428192),
                noiseTerm = cms.double(1.10889),
                corrTermLowE = cms.double(0.0510871),
                threshLowE = cms.double(0.5),
                threshHighE = cms.double(5.0)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTermLowE = cms.double(0.0),
                noiseTermLowE = cms.double(6.92683000001),
                constantTerm = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                corrTermLowE = cms.double(0.0),
                threshLowE = cms.double(1.0),
                threshHighE = cms.double(10.0)
            ),
            minAllowedNormalization = cms.double(1e-09)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            recHitEnergyNorm = cms.double(0.08)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )),
        stoppingTolerance = cms.double(1e-08),
        positionCalcForConvergence = cms.PSet(
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minFractionInCalc = cms.double(0.0),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            minAllowedNormalization = cms.double(0.0),
            X0 = cms.double(0.89),
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1)
        ),
        minFractionToKeep = cms.double(1e-07),
        excludeOtherSeeds = cms.bool(True)
    ),
    positionReCalc = cms.PSet(
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minFractionInCalc = cms.double(0.0),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        minAllowedNormalization = cms.double(0.0),
        X0 = cms.double(0.89),
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1)
    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.08)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThresholdPt = cms.double(0.0),
                gatheringThreshold = cms.double(0.3)
            )),
        useCornerCells = cms.bool(True)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            minS4S1_a = cms.double(0.04),
            minS4S1_b = cms.double(-0.024),
            fractionThresholdModifier = cms.double(3.0),
            energyThresholdModifier = cms.double(2.0),
            doubleSpikeThresh = cms.double(10.0),
            singleSpikeThresh = cms.double(4.0),
            doubleSpikeS6S2 = cms.double(0.04),
            detector = cms.string('ECAL_BARREL')
        ), 
            cms.PSet(
                minS4S1_a = cms.double(0.02),
                minS4S1_b = cms.double(-0.0125),
                fractionThresholdModifier = cms.double(3.0),
                energyThresholdModifier = cms.double(2.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                singleSpikeThresh = cms.double(15.0),
                doubleSpikeS6S2 = cms.double(-1.0),
                detector = cms.string('ECAL_ENDCAP')
            ))
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            seedingThreshold = cms.double(0.6),
            seedingThresholdPt = cms.double(0.15),
            detector = cms.string('ECAL_ENDCAP')
        ), 
            cms.PSet(
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0),
                detector = cms.string('ECAL_BARREL')
            )),
        nNeighbours = cms.int32(8)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECAL")
)



process.hltParticleFlowClusterHBHE = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        clusterTimeResFromSeed = cms.bool(False),
        timeSigmaEE = cms.double(10.0),
        minFracTot = cms.double(1e-20),
        maxIterations = cms.uint32(50),
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        timeSigmaEB = cms.double(10.0),
        timeResolutionCalcBarrel = cms.PSet(
            constantTermLowE = cms.double(4.24),
            noiseTermLowE = cms.double(8),
            constantTerm = cms.double(2.82),
            noiseTerm = cms.double(21.86),
            corrTermLowE = cms.double(0.0),
            threshLowE = cms.double(6.0),
            threshHighE = cms.double(15.0)
        ),
        showerSigma = cms.double(10.0),
        positionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(5),
            algoName = cms.string('Basic2DGenericPFlowPositionCalc')
        ),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        allCellsPositionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(-1),
            algoName = cms.string('Basic2DGenericPFlowPositionCalc')
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcEndcap = cms.PSet(
            constantTermLowE = cms.double(4.24),
            noiseTermLowE = cms.double(8),
            constantTerm = cms.double(2.82),
            noiseTerm = cms.double(21.86),
            corrTermLowE = cms.double(0.0),
            threshLowE = cms.double(6.0),
            threshHighE = cms.double(15.0)
        ),
        minFractionToKeep = cms.double(1e-07),
        excludeOtherSeeds = cms.bool(True)
    ),
    positionReCalc = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThresholdPt = cms.double(0.0),
                gatheringThreshold = cms.double(0.8)
            )),
        useCornerCells = cms.bool(True)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            seedingThreshold = cms.double(1.0),
            seedingThresholdPt = cms.double(0.0),
            detector = cms.string('HCAL_BARREL1')
        ), 
            cms.PSet(
                seedingThreshold = cms.double(1.1),
                seedingThresholdPt = cms.double(0.0),
                detector = cms.string('HCAL_ENDCAP')
            )),
        nNeighbours = cms.int32(4)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHBHE")
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    pfClusterBuilder = cms.PSet(
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0),
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(-1),
            algoName = cms.string('Basic2DGenericPFlowPositionCalc')
        ),
        minFractionToKeep = cms.double(1e-07)
    ),
    energyCorrector = cms.PSet(

    ),
    positionReCalc = cms.PSet(

    ),
    clustersSource = cms.InputTag("hltParticleFlowClusterHBHE")
)

process.hltParticleFlowClusterHO = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        allCellsPositionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.5),
            posCalcNCrystals = cms.int32(-1),
            algoName = cms.string('Basic2DGenericPFlowPositionCalc')
        ),
        showerSigma = cms.double(10.0),
        positionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.5),
            posCalcNCrystals = cms.int32(5),
            algoName = cms.string('Basic2DGenericPFlowPositionCalc')
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL2_RING0'),
            recHitEnergyNorm = cms.double(0.5)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                recHitEnergyNorm = cms.double(1.0)
            )),
        stoppingTolerance = cms.double(1e-08),
        minFractionToKeep = cms.double(1e-07),
        excludeOtherSeeds = cms.bool(True)
    ),
    positionReCalc = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL2_RING0'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.5)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                gatheringThresholdPt = cms.double(0.0),
                gatheringThreshold = cms.double(1.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            seedingThreshold = cms.double(1.0),
            seedingThresholdPt = cms.double(0.0),
            detector = cms.string('HCAL_BARREL2_RING0')
        ), 
            cms.PSet(
                seedingThreshold = cms.double(3.1),
                seedingThresholdPt = cms.double(0.0),
                detector = cms.string('HCAL_BARREL2_RING1')
            )),
        nNeighbours = cms.int32(4)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHO")
)



process.hltParticleFlowClusterHF = cms.EDProducer("PFClusterProducer",
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        allCellsPositionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(-1),
            algoName = cms.string('Basic2DGenericPFlowPositionCalc')
        ),
        showerSigma = cms.double(10.0),
        positionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            logWeightDenominator = cms.double(0.8),
            posCalcNCrystals = cms.int32(5),
            algoName = cms.string('Basic2DGenericPFlowPositionCalc')
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        stoppingTolerance = cms.double(1e-08),
        minFractionToKeep = cms.double(1e-07),
        excludeOtherSeeds = cms.bool(True)
    ),
    positionReCalc = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            gatheringThresholdPt = cms.double(0.0),
            gatheringThreshold = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                gatheringThresholdPt = cms.double(0.0),
                gatheringThreshold = cms.double(0.8)
            )),
        useCornerCells = cms.bool(False)
    ),
    energyCorrector = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            minS4S1_a = cms.double(0.11),
            minS4S1_b = cms.double(-0.19),
            fractionThresholdModifier = cms.double(1.0),
            energyThresholdModifier = cms.double(1.0),
            doubleSpikeThresh = cms.double(1000000000.0),
            singleSpikeThresh = cms.double(80.0),
            doubleSpikeS6S2 = cms.double(-1.0),
            detector = cms.string('HF_EM')
        ), 
            cms.PSet(
                minS4S1_a = cms.double(0.045),
                minS4S1_b = cms.double(-0.08),
                fractionThresholdModifier = cms.double(1.0),
                energyThresholdModifier = cms.double(1.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                singleSpikeThresh = cms.double(120.0),
                doubleSpikeS6S2 = cms.double(-1.0),
                detector = cms.string('HF_HAD')
            ))
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            seedingThreshold = cms.double(1.4),
            seedingThresholdPt = cms.double(0.0),
            detector = cms.string('HF_EM')
        ), 
            cms.PSet(
                seedingThreshold = cms.double(1.4),
                seedingThresholdPt = cms.double(0.0),
                detector = cms.string('HF_HAD')
            )),
        nNeighbours = cms.int32(0)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHF")
)


process.hltParticleFlowBlockL2 = cms.EDProducer("PFBlockProducer",
    debug = cms.untracked.bool(False),
    elementImporters = cms.VPSet(
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterECAL"),
            importerName = cms.string('GenericClusterImporter')
        ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterHCAL"),
            importerName = cms.string('GenericClusterImporter')
        ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterHO"),
            importerName = cms.string('GenericClusterImporter')
        ), 
        cms.PSet(
            source = cms.InputTag("hltParticleFlowClusterHF"),
            importerName = cms.string('GenericClusterImporter')
        ) 
    ),
    verbose = cms.untracked.bool(False),
    linkDefinitions = cms.VPSet(
        cms.PSet(
            linkType = cms.string('ECAL:HCAL'),
            useKDTree = cms.bool(False),
            linkerName = cms.string('ECALAndHCALLinker')
        ), 
        cms.PSet(
            linkType = cms.string('HCAL:HO'),
            useKDTree = cms.bool(False),
            linkerName = cms.string('HCALAndHOLinker')
        ), 
        cms.PSet(
            linkType = cms.string('HFEM:HFHAD'),
            useKDTree = cms.bool(False),
            linkerName = cms.string('HFEMAndHFHADLinker')
        ), 
        cms.PSet(
            linkType = cms.string('ECAL:ECAL'),
            useKDTree = cms.bool(False),
            linkerName = cms.string('ECALAndECALLinker')
        ) 
   )
)


process.hltParticleFlowL2 = cms.EDProducer("PFProducer",
    photon_SigmaiEtaiEta_endcap = cms.double(0.034),
    minPtForPostCleaning = cms.double(20.0),
    pf_nsigma_ECAL = cms.double(0.0),
    GedPhotonValueMap = cms.InputTag(""),
    sumPtTrackIsoForPhoton = cms.double(2.0),
    metFactorForFakes = cms.double(4.0),
    muon_HO = cms.vdouble(0.9, 0.9),
    electron_missinghits = cms.uint32(1),
    metSignificanceForCleaning = cms.double(3.0),
    usePFPhotons = cms.bool(False),
    dptRel_DispVtx = cms.double(10.0),
    nTrackIsoForEgammaSC = cms.uint32(2),
    pf_nsigma_HCAL = cms.double(1.0),
    cosmicRejectionDistance = cms.double(1.0),
    useEGammaFilters = cms.bool(False),
    useEGammaElectrons = cms.bool(False),
    nsigma_TRACK = cms.double(1.0),
    useEGammaSupercluster = cms.bool(False),
    eventFractionForCleaning = cms.double(0.5),
    usePFDecays = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    eventFractionForRejection = cms.double(0.8),
    pf_locC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterLCorr_14Dec2011.root'),
    photon_MinEt = cms.double(10.0),
    usePFNuclearInteractions = cms.bool(False),
    maxSignificance = cms.double(2.5),
    electron_iso_mva_endcap = cms.double(-0.1075),
    electron_noniso_mvaCut = cms.double(-0.1),
    pf_convID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt'),
    calibHF_eta_step = cms.vdouble(0.0, 2.9, 3.0, 3.2, 4.2, 
        4.4, 4.6, 4.8, 5.2, 5.4),
    ptErrorScale = cms.double(8.0),
    minSignificance = cms.double(2.5),
    minMomentumForPunchThrough = cms.double(100.0),
    pf_conv_mvaCut = cms.double(0.0),
    useCalibrationsFromDB = cms.bool(True),
    usePFElectrons = cms.bool(False),
    blocks = cms.InputTag("hltParticleFlowBlockL2"),
    photon_combIso = cms.double(10.0),
    electron_iso_mva_barrel = cms.double(-0.1875),
    postHFCleaning = cms.bool(False),
    factors_45 = cms.vdouble(10.0, 100.0),
    cleanedHF = cms.VInputTag(cms.InputTag("particleFlowRecHitHF","Cleaned"), cms.InputTag("particleFlowClusterHF","Cleaned")),
    coneEcalIsoForEgammaSC = cms.double(0.3),
    egammaElectrons = cms.InputTag(""),
    photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
    calibHF_b_HADonly = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    minPixelHits = cms.int32(1),
    maxDPtOPt = cms.double(1.0),
    useHO = cms.bool(True),
    pf_electron_output_col = cms.string('electrons'),
    debug = cms.untracked.bool(False),
    GedElectronValueMap = cms.InputTag("gedGsfElectronsTmp"),
    useVerticesForNeutral = cms.bool(False),
    trackQuality = cms.string('highPurity'),
    PFEGammaCandidates = cms.InputTag(""),
    sumPtTrackIsoSlopeForPhoton = cms.double(0.001),
    coneTrackIsoForEgammaSC = cms.double(0.3),
    minDeltaMet = cms.double(0.4),
    pt_Error = cms.double(1.0),
    useProtectionsForJetMET = cms.bool(False),
    metFactorForRejection = cms.double(4.0),
    sumPtTrackIsoForEgammaSC_endcap = cms.double(4.0),
    calibHF_use = cms.bool(False),
    verbose = cms.untracked.bool(False),
    usePFConversions = cms.bool(False),
    calibPFSCEle_endcap = cms.vdouble(1.153, -16.5975, 5.668, -0.1772, 16.22, 
        7.326, 0.0483, -4.068, 9.406),
    metFactorForCleaning = cms.double(4.0),
    eventFactorForCosmics = cms.double(10.0),
    minSignificanceReduction = cms.double(1.4),
    minEnergyForPunchThrough = cms.double(100.0),
    minTrackerHits = cms.int32(8),
    iCfgCandConnector = cms.PSet(
        nuclCalibFactors = cms.vdouble(0.8, 0.15, 0.5, 0.5, 0.05),
        ptErrorSecondary = cms.double(1.0),
        bCalibPrimary = cms.bool(True),
        bCorrect = cms.bool(True),
        dptRel_MergedTrack = cms.double(5.0),
        dptRel_PrimaryTrack = cms.double(10.0)
    ),
    rejectTracks_Bad = cms.bool(False),
    pf_electronID_crackCorrection = cms.bool(False),
    sumPtTrackIsoForEgammaSC_barrel = cms.double(4.0),
    calibHF_a_EMonly = cms.vdouble(0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 
        0.89718, 0.98674, 1.4681, 1.458, 1.458),
    pf_Res_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes_14Dec2011.root'),
    metFactorForHighEta = cms.double(25.0),
    minHFCleaningPt = cms.double(5.0),
    muon_HCAL = cms.vdouble(3.0, 3.0),
    pf_electron_mvaCut = cms.double(-0.1),
    ptFactorForHighEta = cms.double(2.0),
    sumEtEcalIsoForEgammaSC_endcap = cms.double(2.0),
    maxDeltaPhiPt = cms.double(7.0),
    pf_electronID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt'),
    muons = cms.InputTag(""),
    calibHF_b_EMHAD = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    pf_GlobC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr_14Dec2011.root'),
    photon_HoE = cms.double(0.05),
    sumEtEcalIsoForEgammaSC_barrel = cms.double(1.0),
    calibPFSCEle_Fbrem_endcap = cms.vdouble(0.9, 6.5, -0.0692932, 0.101776, 0.995338, 
        -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 
        0.923165, 0.000474665, 1.10782),
    punchThroughFactor = cms.double(3.0),
    algoType = cms.uint32(0),
    electron_iso_combIso_barrel = cms.double(10.0),
    postMuonCleaning = cms.bool(False),
    calibPFSCEle_barrel = cms.vdouble(1.004, -1.536, 22.88, -1.467, 0.3555, 
        0.6227, 14.65, 2051, 25, 0.9932, 
        -0.5444, 0, 0.5438, 0.7109, 7.645, 
        0.2904, 0),
    electron_protectionsForJetMET = cms.PSet(
        maxTrackPOverEele = cms.double(1.0),
        maxEcalEOverP_2 = cms.double(0.2),
        maxHcalEOverEcalE = cms.double(0.1),
        maxEcalEOverP_1 = cms.double(0.5),
        maxHcalEOverP = cms.double(1.0),
        maxEeleOverPoutRes = cms.double(0.5),
        maxEcalEOverPRes = cms.double(0.2),
        maxHcalE = cms.double(10.0),
        maxEeleOverPout = cms.double(0.2),
        maxNtracks = cms.double(3.0),
        maxEleHcalEOverEcalE = cms.double(0.1),
        maxDPhiIN = cms.double(0.1),
        maxE = cms.double(50.0)
    ),
    electron_iso_pt = cms.double(10.0),
    isolatedElectronID_mvaWeightFile = cms.string('RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml'),
    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
    X0_Map = cms.string('RecoParticleFlow/PFProducer/data/allX0histos.root'),
    calibPFSCEle_Fbrem_barrel = cms.vdouble(0.6, 6, -0.0255975, 0.0576727, 0.975442, 
        -0.000546394, 1.26147, 25, -0.02025, 0.04537, 
        0.9728, -0.0008962, 1.172),
    electron_iso_combIso_endcap = cms.double(10.0),
    punchThroughMETFactor = cms.double(4.0),
    metSignificanceForRejection = cms.double(4.0),
    photon_protectionsForJetMET = cms.PSet(
        sumPtTrackIsoSlope = cms.double(0.001),
        sumPtTrackIso = cms.double(4.0)
    ),
    usePhotonReg = cms.bool(False),
    dzPV = cms.double(0.2),
    calibHF_a_EMHAD = cms.vdouble(1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 
        0.98504, 1.00802, 1.0593, 1.4576, 1.4576),
    useRegressionFromDB = cms.bool(True),
    muon_ECAL = cms.vdouble(0.5, 0.5),
    usePFSCEleCalib = cms.bool(False)
)



process.hltL2PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doOutputJets = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    voronoiRfact = cms.double(-0.9),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(True),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('PFJet'),
    src = cms.InputTag("hltParticleFlowL2"),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    doAreaDiskApprox = cms.bool(False),
    inputEMin = cms.double(0.0),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.5)
)



process.PFL2 = cms.Path(
process.hltParticleFlowRecHitECAL*
process.hltParticleFlowRecHitHBHE*
process.hltParticleFlowRecHitHF*
process.hltParticleFlowRecHitHO*
process.hltParticleFlowClusterECAL*
process.hltParticleFlowClusterHBHE*
process.hltParticleFlowClusterHCAL*
process.hltParticleFlowClusterHF*
process.hltParticleFlowClusterHO*
process.hltParticleFlowBlockL2*
process.hltParticleFlowL2*
process.hltL2PFJets
)

##########################################################PF L2 Configuration########################################################




# Additional output definition

# Other statements
#process.mix.playback = True
#process.mix.digitizers = cms.PSet()
#for a in process.aliases: delattr(process, a)
#process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

# Path and EndPath definitions
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)


# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.RECOSIMoutput_step)
process.schedule = cms.Schedule(process.PFL2,process.RECOSIMoutput_step)

# customisation of the proces
# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)
