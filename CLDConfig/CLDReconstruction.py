from Gaudi.Configuration import *

from Configurables import LcioEvent, k4DataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []

evtsvc = k4DataSvc("EventDataSvc")


CONFIG = {
             "CalorimeterIntegrationTimeWindow": "10",
             "Overlay": ["False"],
             "OverlayChoices": ["False", "91GeV", "365GeV"],
             "Tracking": ["Conformal"],
             "TrackingChoices": ["Truth", "Conformal"],
             "VertexUnconstrained": ["OFF"],
             "VertexUnconstrainedChoices": ["ON", "OFF"]
}


read = LcioEvent()
read.OutputLevel = WARNING
read.Files = ["/run/simulation/with/ddsim/to/create/a/file.slcio"]
algList.append(read)

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = WARNING
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["histograms"],
                              "FileType": ["root"]
                              }

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = WARNING
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = WARNING
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": [os.environ["K4GEO"]+"/FCCee/CLD/compact/FCCee_o1_v04/FCCee_o1_v04.xml"],
                         "EncodingStringParameter": ["GlobalTrackerReadoutID"]
                         }

OverlayParameters = {
    "MCParticleCollectionName": ["MCParticle"],
    "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
    "Delta_t": ["20"],
    "NBunchtrain": ["20"],
    "Collection_IntegrationTimes": [
        "VertexBarrelCollection", "380",
        "VertexEndcapCollection", "380",
        "InnerTrackerBarrelCollection", "380",
        "InnerTrackerEndcapCollection", "380",
        "OuterTrackerBarrelCollection", "380",
        "OuterTrackerEndcapCollection", "380",
        "ECalBarrelCollection", "380",
        "ECalEndcapCollection", "380",
        "HCalBarrelCollection", "380",
        "HCalEndcapCollection", "380",
        "HCalRingCollection", "380",
        "YokeBarrelCollection", "380",
        "YokeEndcapCollection", "380",
        "LumiCalCollection", "380"
     ],
    "PhysicsBX": ["1"],
    "Poisson_random_NOverlay": ["false"],
    "RandomBx": ["false"],
    "TPCDriftvelocity": ["0.05"],
    "BackgroundFileNames": ["pairs_Z_sim.slcio"],
}
Overlay = {}

Overlay["False"] = MarlinProcessorWrapper("OverlayFalse")
Overlay["False"].OutputLevel = WARNING
Overlay["False"].ProcessorType = "OverlayTimingGeneric"
Overlay["False"].Parameters = OverlayParameters.copy()
Overlay["False"].Parameters |= {
                           "BackgroundFileNames": [],
                           "NBunchtrain": ["0"],
                           "NumberBackground": ["0."],
                           }

# XXX: Caution, this probably needs an update
Overlay["91GeV"] = MarlinProcessorWrapper("Overlay91GeV")
Overlay["91GeV"].OutputLevel = WARNING
Overlay["91GeV"].ProcessorType = "OverlayTimingGeneric"
Overlay["91GeV"].Parameters = OverlayParameters.copy()
Overlay["91GeV"].Parameters |= {
                           "NumberBackground": ["1."],
                           }

# XXX: Caution, this probably needs an update
Overlay["365GeV"] = MarlinProcessorWrapper("Overlay365GeV")
Overlay["365GeV"].OutputLevel = WARNING
Overlay["365GeV"].ProcessorType = "OverlayTimingGeneric"
Overlay["365GeV"].Parameters = OverlayParameters.copy()
Overlay["365GeV"].Parameters |= {
                            "Delta_t": ["3396"],
                            "NBunchtrain": ["3"],
                            "NumberBackground": ["1."],
                            }

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = WARNING
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
                                 "IsStrip": ["false"],
                                 "ResolutionU": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
                                 "ResolutionV": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
                                 "SimTrackHitCollectionName": ["VertexBarrelCollection"],
                                 "SimTrkHitRelCollection": ["VXDTrackerHitRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TrackerHitCollectionName": ["VXDTrackerHits"]
                                 }

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = WARNING
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
                                 "IsStrip": ["false"],
                                 "ResolutionU": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
                                 "ResolutionV": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
                                 "SimTrackHitCollectionName": ["VertexEndcapCollection"],
                                 "SimTrkHitRelCollection": ["VXDEndcapTrackerHitRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TrackerHitCollectionName": ["VXDEndcapTrackerHits"]
                                 }

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = WARNING
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
                                       "IsStrip": ["false"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.09"],
                                       "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["InnerTrackerBarrelHitsRelations"],
                                       "SubDetectorName": ["InnerTrackers"],
                                       "TrackerHitCollectionName": ["ITrackerHits"]
                                       }

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper("InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = WARNING
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
                                             "IsStrip": ["false"],
                                             "ResolutionU": ["0.005", "0.007", "0.007", "0.007", "0.007", "0.007", "0.007"],
                                             "ResolutionV": ["0.005", "0.09", "0.09", "0.09", "0.09", "0.09", "0.09"],
                                             "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["InnerTrackerEndcapHitsRelations"],
                                             "SubDetectorName": ["InnerTrackers"],
                                             "TrackerHitCollectionName": ["ITrackerEndcapHits"]
                                             }

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = WARNING
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
                                       "IsStrip": ["false"],
                                       "ResolutionU": ["0.007", "0.007", "0.007"],
                                       "ResolutionV": ["0.09", "0.09", "0.09"],
                                       "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["OuterTrackerBarrelHitsRelations"],
                                       "SubDetectorName": ["OuterTrackers"],
                                       "TrackerHitCollectionName": ["OTrackerHits"]
                                       }

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper("OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = WARNING
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
                                             "IsStrip": ["false"],
                                             "ResolutionU": ["0.007", "0.007", "0.007", "0.007", "0.007"],
                                             "ResolutionV": ["0.09", "0.09", "0.09", "0.09", "0.09"],
                                             "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["OuterTrackerEndcapHitsRelations"],
                                             "SubDetectorName": ["OuterTrackers"],
                                             "TrackerHitCollectionName": ["OTrackerEndcapHits"]
                                             }

MyTruthTrackFinder = MarlinProcessorWrapper("MyTruthTrackFinder")
MyTruthTrackFinder.OutputLevel = WARNING
MyTruthTrackFinder.ProcessorType = "TruthTrackFinder"
MyTruthTrackFinder.Parameters = {
                                 "FitForward": ["true"],
                                 "MCParticleCollectionName": ["MCParticle"],
                                 "SiTrackCollectionName": ["SiTracks"],
                                 "SiTrackRelationCollectionName": ["SiTrackRelations"],
                                 "SimTrackerHitRelCollectionNames": ["VXDTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations"],
                                 "TrackerHitCollectionNames": ["VXDTrackerHits", "ITrackerHits", "OTrackerHits", "VXDEndcapTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
                                 "UseTruthInPrefit": ["false"]
                                 }

MyConformalTracking = MarlinProcessorWrapper("MyConformalTracking")
MyConformalTracking.OutputLevel = WARNING
MyConformalTracking.ProcessorType = "ConformalTrackingV2"
MyConformalTracking.Parameters = {
                                  "DebugHits": ["DebugHits"],
                                  "DebugPlots": ["false"],
                                  "DebugTiming": ["false"],
                                  "MCParticleCollectionName": ["MCParticle"],
                                  "MaxHitInvertedFit": ["0"],
                                  "MinClustersOnTrackAfterFit": ["3"],
                                  "RelationsNames": ["VXDTrackerHitRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations"],
                                  "RetryTooManyTracks": ["false"],
                                  "SiTrackCollectionName": ["SiTracksCT"],
                                  "SortTreeResults": ["true"],
                                  "Steps": ["[VXDBarrel]", "@Collections", ":", "VXDTrackerHits", "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.03;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker", "@Functions", ":", "CombineCollections,", "BuildNewTracks", "[VXDEncap]", "@Collections", ":", "VXDEndcapTrackerHits", "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.03;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker", "@Functions", ":", "CombineCollections,", "ExtendTracks", "[LowerCellAngle1]", "@Collections", ":", "VXDTrackerHits,", "VXDEndcapTrackerHits", "@Parameters", ":", "MaxCellAngle", ":", "0.05;", "MaxCellAngleRZ", ":", "0.05;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.03;", "SlopeZRange:", "10.0;HighPTCut:", "10.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch", "@Functions", ":", "CombineCollections,", "BuildNewTracks", "[LowerCellAngle2]", "@Collections", ":", "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "2000;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.03;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch", "@Functions", ":", "BuildNewTracks,", "SortTracks", "[Tracker]", "@Collections", ":", "ITrackerHits,", "OTrackerHits,", "ITrackerEndcapHits,", "OTrackerEndcapHits", "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "2000;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.03;", "SlopeZRange:", "10.0;", "HighPTCut:", "1.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch", "@Functions", ":", "CombineCollections,", "ExtendTracks", "[Displaced]", "@Collections", ":", "VXDTrackerHits,", "VXDEndcapTrackerHits,", "ITrackerHits,", "OTrackerHits,", "ITrackerEndcapHits,", "OTrackerEndcapHits", "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "1000;", "MinClustersOnTrack", ":", "5;", "MaxDistance", ":", "0.015;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "OnlyZSchi2cut,", "RadialSearch", "@Functions", ":", "CombineCollections,", "BuildNewTracks"],
                                  "ThetaRange": ["0.05"],
                                  "TooManyTracks": ["100000"],
                                  "TrackerHitCollectionNames": ["VXDTrackerHits", "VXDEndcapTrackerHits", "ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
                                  "trackPurity": ["0.7"]
                                  }

ClonesAndSplitTracksFinder = MarlinProcessorWrapper("ClonesAndSplitTracksFinder")
ClonesAndSplitTracksFinder.OutputLevel = WARNING
ClonesAndSplitTracksFinder.ProcessorType = "ClonesAndSplitTracksFinder"
ClonesAndSplitTracksFinder.Parameters = {
                                         "EnergyLossOn": ["true"],
                                         "InputTrackCollectionName": ["SiTracksCT"],
                                         "MultipleScatteringOn": ["true"],
                                         "OutputTrackCollectionName": ["SiTracks"],
                                         "SmoothOn": ["false"],
                                         "extrapolateForward": ["true"],
                                         "maxSignificancePhi": ["3"],
                                         "maxSignificancePt": ["2"],
                                         "maxSignificanceTheta": ["3"],
                                         "mergeSplitTracks": ["false"],
                                         "minTrackPt": ["1"]
                                         }

Refit = MarlinProcessorWrapper("Refit")
Refit.OutputLevel = WARNING
Refit.ProcessorType = "RefitFinal"
Refit.Parameters = {
                    "EnergyLossOn": ["true"],
                    "InputRelationCollectionName": ["SiTrackRelations"],
                    "InputTrackCollectionName": ["SiTracks"],
                    "Max_Chi2_Incr": ["1.79769e+30"],
                    "MinClustersOnTrackAfterFit": ["3"],
                    "MultipleScatteringOn": ["true"],
                    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
                    "OutputTrackCollectionName": ["SiTracks_Refitted"],
                    "ReferencePoint": ["-1"],
                    "SmoothOn": ["false"],
                    "extrapolateForward": ["true"]
                    }

MyClicEfficiencyCalculator = MarlinProcessorWrapper("MyClicEfficiencyCalculator")
MyClicEfficiencyCalculator.OutputLevel = WARNING
MyClicEfficiencyCalculator.ProcessorType = "ClicEfficiencyCalculator"
MyClicEfficiencyCalculator.Parameters = {
                                         "MCParticleCollectionName": ["MCParticle"],
                                         "MCParticleNotReco": ["MCParticleNotReco"],
                                         "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
                                         "TrackCollectionName": ["SiTracks_Refitted"],
                                         "TrackerHitCollectionNames": ["VXDTrackerHits", "VXDEndcapTrackerHits", "ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
                                         "TrackerHitRelCollectionNames": ["VXDTrackerHitRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations"],
                                         "efficiencyTreeName": ["trktree"],
                                         "mcTreeName": ["mctree"],
                                         "morePlots": ["false"],
                                         "purityTreeName": ["puritytree"],
                                         "reconstructableDefinition": ["ILDLike"],
                                         "vertexBarrelID": ["1"]
                                         }

MyTrackChecker = MarlinProcessorWrapper("MyTrackChecker")
MyTrackChecker.OutputLevel = WARNING
MyTrackChecker.ProcessorType = "TrackChecker"
MyTrackChecker.Parameters = {
                             "MCParticleCollectionName": ["MCParticle"],
                             "TrackCollectionName": ["SiTracks_Refitted"],
                             "TrackRelationCollectionName": ["SiTracksMCTruthLink"],
                             "TreeName": ["checktree"],
                             "UseOnlyTree": ["true"]
                             }

MyDDSimpleMuonDigi = MarlinProcessorWrapper("MyDDSimpleMuonDigi")
MyDDSimpleMuonDigi.OutputLevel = WARNING
MyDDSimpleMuonDigi.ProcessorType = "DDSimpleMuonDigi"
MyDDSimpleMuonDigi.Parameters = {
                                 "CalibrMUON": ["70.1"],
                                 "MUONCollections": ["YokeBarrelCollection", "YokeEndcapCollection"],
                                 "MUONOutputCollection": ["MUON"],
                                 "MaxHitEnergyMUON": ["2.0"],
                                 "MuonThreshold": ["1e-06"],
                                 "RelationOutputCollection": ["RelationMuonHit"]
                                 }

MyStatusmonitor = MarlinProcessorWrapper("MyStatusmonitor")
MyStatusmonitor.OutputLevel = WARNING
MyStatusmonitor.ProcessorType = "Statusmonitor"
MyStatusmonitor.Parameters = {
                              "HowOften": ["100"]
                              }

MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
MyRecoMCTruthLinker.OutputLevel = WARNING
MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
MyRecoMCTruthLinker.Parameters = {
                                  "BremsstrahlungEnergyCut": ["1"],
                                  "CalohitMCTruthLinkName": ["CalohitMCTruthLink"],
                                  "ClusterCollection": ["PandoraClusters"],
                                  "ClusterMCTruthLinkName": ["ClusterMCTruthLink"],
                                  "FullRecoRelation": ["false"],
                                  "InvertedNonDestructiveInteractionLogic": ["false"],
                                  "KeepDaughtersPDG": ["22", "111", "310", "13", "211", "321", "3120"],
                                  "MCParticleCollection": ["MCPhysicsParticles"],
                                  "MCParticlesSkimmedName": ["MCParticlesSkimmed"],
                                  "MCTruthClusterLinkName": [],
                                  "MCTruthRecoLinkName": [],
                                  "MCTruthTrackLinkName": [],
                                  "RecoMCTruthLinkName": ["RecoMCTruthLink"],
                                  "RecoParticleCollection": ["PandoraPFOs"],
                                  "SaveBremsstrahlungPhotons": ["false"],
                                  "SimCaloHitCollections": ["ECalBarrelCollection", "ECalEndcapCollection", "ECalPlugCollection", "HCalBarrelCollection", "HCalEndcapCollection", "HCalRingCollection", "YokeBarrelCollection", "YokeEndcapCollection", "LumiCalCollection", "BeamCalCollection"],
                                  "SimCalorimeterHitRelationNames": ["RelationCaloHit", "RelationMuonHit"],
                                  "SimTrackerHitCollections": ["VertexBarrelCollection", "VertexEndcapCollection", "InnerTrackerBarrelCollection", "OuterTrackerBarrelCollection", "InnerTrackerEndcapCollection", "OuterTrackerEndcapCollection"],
                                  "TrackCollection": ["SiTracks_Refitted"],
                                  "TrackMCTruthLinkName": ["SiTracksMCTruthLink"],
                                  "TrackerHitsRelInputCollections": ["VXDTrackerHitRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations"],
                                  "UseTrackerHitRelations": ["true"],
                                  "UsingParticleGun": ["false"],
                                  "daughtersECutMeV": ["10"]
                                  }

MyHitResiduals = MarlinProcessorWrapper("MyHitResiduals")
MyHitResiduals.OutputLevel = WARNING
MyHitResiduals.ProcessorType = "HitResiduals"
MyHitResiduals.Parameters = {
                             "EnergyLossOn": ["true"],
                             "MaxChi2Increment": ["1000"],
                             "MultipleScatteringOn": ["true"],
                             "SmoothOn": ["false"],
                             "TrackCollectionName": ["SiTracks_Refitted"],
                             "outFileName": ["residuals.root"],
                             "treeName": ["restree"]
                             }

LumiCalReco = MarlinProcessorWrapper("LumiCalReco")
LumiCalReco.OutputLevel = WARNING
LumiCalReco.ProcessorType = "MarlinLumiCalClusterer"
LumiCalReco.Parameters = {
                          "ClusterMinNumHits": ["15"],
                          "ElementsPercentInShowerPeakLayer": ["0.03"],
                          "EnergyCalibConst": ["0.01213"],
                          "LogWeigthConstant": ["6.5"],
                          "LumiCal_Clusters": ["LumiCalClusters"],
                          "LumiCal_Collection": ["LumiCalCollection"],
                          "LumiCal_RecoParticles": ["LumiCalRecoParticles"],
                          "MaxRecordNumber": ["10"],
                          "MemoryResidentTree": ["0"],
                          "MiddleEnergyHitBoundFrac": ["0.01"],
                          "MinClusterEngy": ["2.0"],
                          "MinHitEnergy": ["20e-06"],
                          "MoliereRadius": ["20"],
                          "NumEventsTree": ["500"],
                          "NumOfNearNeighbor": ["6"],
                          "OutDirName": ["rootOut"],
                          "OutRootFileName": [],
                          "SkipNEvents": ["0"],
                          "WeightingMethod": ["LogMethod"],
                          "ZLayerPhiOffset": ["0.0"]
                          }

RenameCollection = MarlinProcessorWrapper("RenameCollection")
RenameCollection.OutputLevel = WARNING
RenameCollection.ProcessorType = "MergeCollections"
RenameCollection.Parameters = {
                               "CollectionParameterIndex": ["0"],
                               "InputCollectionIDs": [],
                               "InputCollections": ["PandoraPFOs"],
                               "OutputCollection": ["PFOsFromJets"]
                               }

MyFastJetProcessor = MarlinProcessorWrapper("MyFastJetProcessor")
MyFastJetProcessor.OutputLevel = WARNING
MyFastJetProcessor.ProcessorType = "FastJetProcessor"
MyFastJetProcessor.Parameters = {
                                 "algorithm": ["ValenciaPlugin", "1.2", "1.0", "0.7"],
                                 "clusteringMode": ["ExclusiveNJets", "2"],
                                 "jetOut": ["JetsAfterGamGamRemoval"],
                                 "recParticleIn": ["TightSelectedPandoraPFOs"],
                                 "recParticleOut": ["PFOsFromJets"],
                                 "recombinationScheme": ["E_scheme"],
                                 "storeParticlesInJets": ["true"]
                                 }

JetClusteringAndRefiner = MarlinProcessorWrapper("JetClusteringAndRefiner")
JetClusteringAndRefiner.OutputLevel = WARNING
JetClusteringAndRefiner.ProcessorType = "LcfiplusProcessor"
JetClusteringAndRefiner.Parameters = {
                                      "Algorithms": ["JetClustering", "JetVertexRefiner"],
                                      "JetClustering.AlphaParameter": ["1.0"],
                                      "JetClustering.BetaParameter": ["1.0"],
                                      "JetClustering.GammaParameter": ["1.0"],
                                      "JetClustering.InputVertexCollectionName": ["BuildUpVertices"],
                                      "JetClustering.JetAlgorithm": ["ValenciaVertex"],
                                      "JetClustering.MaxNumberOfJetsForYThreshold": ["10"],
                                      "JetClustering.MuonIDExternal": ["0"],
                                      "JetClustering.MuonIDMaximum3DImpactParameter": ["5.0"],
                                      "JetClustering.MuonIDMinimumD0Significance": ["5.0"],
                                      "JetClustering.MuonIDMinimumEnergy": ["0"],
                                      "JetClustering.MuonIDMinimumProbability": ["0.5"],
                                      "JetClustering.MuonIDMinimumZ0Significance": ["5.0"],
                                      "JetClustering.NJetsRequested": ["2"],
                                      "JetClustering.OutputJetCollectionName": ["VertexJets"],
                                      "JetClustering.OutputJetStoresVertex": ["0"],
                                      "JetClustering.PrimaryVertexCollectionName": ["PrimaryVertices"],
                                      "JetClustering.RParameter": ["1.0"],
                                      "JetClustering.UseBeamJets": ["1"],
                                      "JetClustering.UseMuonID": ["1"],
                                      "JetClustering.VertexSelectionK0MassWidth": ["0.02"],
                                      "JetClustering.VertexSelectionMaximumDistance": ["30."],
                                      "JetClustering.VertexSelectionMinimumDistance": ["0.3"],
                                      "JetClustering.YAddedForJetLeptonLepton": ["100"],
                                      "JetClustering.YAddedForJetLeptonVertex": ["100"],
                                      "JetClustering.YAddedForJetVertexLepton": ["0"],
                                      "JetClustering.YAddedForJetVertexVertex": ["100"],
                                      "JetClustering.YCut": ["0."],
                                      "JetVertexRefiner.BNessCut": ["-0.80"],
                                      "JetVertexRefiner.BNessCutE1": ["-0.15"],
                                      "JetVertexRefiner.InputJetCollectionName": ["VertexJets"],
                                      "JetVertexRefiner.InputVertexCollectionName": ["BuildUpVertices"],
                                      "JetVertexRefiner.MaxAngleSingle": ["0.5"],
                                      "JetVertexRefiner.MaxCharmFlightLengthPerJetEnergy": ["0.1"],
                                      "JetVertexRefiner.MaxPosSingle": ["30."],
                                      "JetVertexRefiner.MaxSeparationPerPosSingle": ["0.1"],
                                      "JetVertexRefiner.MinEnergySingle": ["1."],
                                      "JetVertexRefiner.MinPosSingle": ["0.3"],
                                      "JetVertexRefiner.OneVertexProbThreshold": ["0.001"],
                                      "JetVertexRefiner.OutputJetCollectionName": ["RefinedVertexJets"],
                                      "JetVertexRefiner.OutputVertexCollectionName": ["RefinedVertices"],
                                      "JetVertexRefiner.PrimaryVertexCollectionName": ["PrimaryVertices"],
                                      "JetVertexRefiner.V0VertexCollectionName": ["BuildUpVertices_V0"],
                                      "JetVertexRefiner.mind0sigSingle": ["5."],
                                      "JetVertexRefiner.minz0sigSingle": ["5."],
                                      "JetVertexRefiner.useBNess": ["0"],
                                      "MCPCollection": ["MCParticle"],
                                      "MCPFORelation": ["RecoMCTruthLink"],
                                      "MagneticField": ["2.0"],
                                      "PFOCollection": ["PFOsFromJets"],
                                      "PrintEventNumber": ["1"],
                                      "ReadSubdetectorEnergies": ["0"],
                                      "TrackHitOrdering": ["2"],
                                      "UpdateVertexRPDaughters": ["0"],
                                      "UseMCP": ["0"]
                                      }

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = WARNING
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
                         "DropCollectionNames": [],
                         "DropCollectionTypes": [],
                         "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles"],
                         "KeepCollectionNames": [],
                         "LCIOOutputFile": ["Output_REC.slcio"],
                         "LCIOWriteMode": ["WRITE_NEW"]
                         }

Output_DST = MarlinProcessorWrapper("Output_DST")
Output_DST.OutputLevel = WARNING
Output_DST.ProcessorType = "LCIOOutputProcessor"
Output_DST.Parameters = {
                         "DropCollectionNames": [],
                         "DropCollectionTypes": ["MCParticle", "LCRelation", "SimCalorimeterHit", "CalorimeterHit", "SimTrackerHit", "TrackerHit", "TrackerHitPlane", "Track", "ReconstructedParticle", "LCFloatVec"],
                         "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles", "MCPhysicsParticles"],
                         "KeepCollectionNames": ["MCParticlesSkimmed", "MCPhysicsParticles", "RecoMCTruthLink", "SiTracks", "SiTracks_Refitted", "PandoraClusters", "PandoraPFOs", "SelectedPandoraPFOs", "LooseSelectedPandoraPFOs", "TightSelectedPandoraPFOs", "RefinedVertexJets", "RefinedVertexJets_rel", "RefinedVertexJets_vtx", "RefinedVertexJets_vtx_RP", "BuildUpVertices", "BuildUpVertices_res", "BuildUpVertices_RP", "BuildUpVertices_res_RP", "BuildUpVertices_V0", "BuildUpVertices_V0_res", "BuildUpVertices_V0_RP", "BuildUpVertices_V0_res_RP", "PrimaryVertices", "PrimaryVertices_res", "PrimaryVertices_RP", "PrimaryVertices_res_RP", "RefinedVertices", "RefinedVertices_RP"],
                         "LCIOOutputFile": ["Output_DST.slcio"],
                         "LCIOWriteMode": ["WRITE_NEW"]
                         }

MyDDCaloDigiParameters = {
                                "Histograms": ["0"],
                                "RootFile": ["Digi_SiW.root"],
                                "RelationOutputCollection": ["RelationCaloHit"],
                                "energyPerEHpair": ["3.6"],
                                # ECAL
                                "ECALCollections": ["ECalBarrelCollection", "ECalEndcapCollection", "ECalPlugCollection"],
                                "ECALOutputCollection0": ["ECALBarrel"],
                                "ECALOutputCollection1": ["ECALEndcap"],
                                "ECALOutputCollection2": ["ECALOther"],
                                "IfDigitalEcal": ["0"],
                                "ECALLayers": ["41", "100"],
                                "ECAL_default_layerConfig": ["000000000000000"],
                                "StripEcal_default_nVirtualCells": ["9"],
                                "CalibECALMIP": ["0.0001"],
                                "ECALThreshold": ["5e-05"],
                                "ECALThresholdUnit": ["GeV"],
                                "ECALGapCorrection": ["1"],
                                "ECALGapCorrectionFactor": ["1"],
                                "ECALModuleGapCorrectionFactor": ["0.0"],
                                "MapsEcalCorrection": ["0"],
                                "ECAL_PPD_N_Pixels": ["10000"],
                                "ECAL_PPD_N_Pixels_uncertainty": ["0.05"],
                                "ECAL_PPD_PE_per_MIP": ["7"],
                                "ECAL_apply_realistic_digi": ["0"],
                                "ECAL_deadCellRate": ["0"],
                                "ECAL_deadCell_memorise": ["false"],
                                "ECAL_elec_noise_mips": ["0"],
                                "ECAL_maxDynamicRange_MIP": ["2500"],
                                "ECAL_miscalibration_correl": ["0"],
                                "ECAL_miscalibration_uncorrel": ["0"],
                                "ECAL_miscalibration_uncorrel_memorise": ["false"],
                                "ECAL_pixel_spread": ["0.05"],
                                "ECAL_strip_absorbtionLength": ["1e+06"],
                                "UseEcalTiming": ["1"],
                                "ECALCorrectTimesForPropagation": ["1"],
                                "ECALTimeWindowMin": ["-1"],
                                "ECALSimpleTimingCut": ["true"],
                                "ECALDeltaTimeHitResolution": ["10"],
                                "ECALTimeResolution": ["10"],
                                # HCAL
                                "HCALCollections": ["HCalBarrelCollection", "HCalEndcapCollection", "HCalRingCollection"],
                                "HCALOutputCollection0": ["HCALBarrel"],
                                "HCALOutputCollection1": ["HCALEndcap"],
                                "HCALOutputCollection2": ["HCALOther"],
                                "IfDigitalHcal": ["0"],
                                "HCALLayers": ["100"],
                                "CalibHCALMIP": ["0.0001"],
                                "HCALThreshold": ["0.00025"],
                                "HCALThresholdUnit": ["GeV"],
                                "HCALEndcapCorrectionFactor": ["1.000"],
                                "HCALGapCorrection": ["1"],
                                "HCALModuleGapCorrectionFactor": ["0.5"],
                                "HCAL_PPD_N_Pixels": ["400"],
                                "HCAL_PPD_N_Pixels_uncertainty": ["0.05"],
                                "HCAL_PPD_PE_per_MIP": ["10"],
                                "HCAL_apply_realistic_digi": ["0"],
                                "HCAL_deadCellRate": ["0"],
                                "HCAL_deadCell_memorise": ["false"],
                                "HCAL_elec_noise_mips": ["0"],
                                "HCAL_maxDynamicRange_MIP": ["200"],
                                "HCAL_miscalibration_correl": ["0"],
                                "HCAL_miscalibration_uncorrel": ["0"],
                                "HCAL_miscalibration_uncorrel_memorise": ["false"],
                                "HCAL_pixel_spread": ["0"],
                                "UseHcalTiming": ["1"],
                                "HCALCorrectTimesForPropagation": ["1"],
                                "HCALTimeWindowMin": ["-1"],
                                "HCALSimpleTimingCut": ["true"],
                                "HCALDeltaTimeHitResolution": ["10"],
                                "HCALTimeResolution": ["10"],
}

#TODO: make this nice with a dictionary
MyDDCaloDigi_10ns = MarlinProcessorWrapper("MyDDCaloDigi_10ns")
MyDDCaloDigi_10ns.OutputLevel = WARNING
MyDDCaloDigi_10ns.ProcessorType = "DDCaloDigi"
MyDDCaloDigi_10ns.Parameters = MyDDCaloDigiParameters.copy()
MyDDCaloDigi_10ns.Parameters |= {
                                "CalibrECAL": ["37.5227197175", "37.5227197175"],
                                "ECALEndcapCorrectionFactor": ["1.03245503522"],
                                "ECALBarrelTimeWindowMax": ["10"],
                                "ECALEndcapTimeWindowMax": ["10"],
                                "CalibrHCALBarrel": ["45.9956826061"],
                                "CalibrHCALEndcap": ["46.9252540291"],
                                "CalibrHCALOther": ["57.4588011802"],
                                "HCALBarrelTimeWindowMax": ["10"],
                                "HCALEndcapTimeWindowMax": ["10"],
                                }

MyDDCaloDigi_400ns = MarlinProcessorWrapper("MyDDCaloDigi_400ns")
MyDDCaloDigi_400ns.OutputLevel = WARNING
MyDDCaloDigi_400ns.ProcessorType = "DDCaloDigi"
MyDDCaloDigi_400ns.Parameters = MyDDCaloDigiParameters.copy()
MyDDCaloDigi_400ns.Parameters |= {
                                 "CalibrECAL": ["37.4591745147", "37.4591745147"],
                                 "ECALEndcapCorrectionFactor": ["1.01463983425"],
                                 "ECALBarrelTimeWindowMax": ["400"],
                                 "ECALEndcapTimeWindowMax": ["400"],
                                 "CalibrHCALBarrel": ["42.544403752"],
                                 "CalibrHCALEndcap": ["42.9667604345"],
                                 "CalibrHCALOther": ["51.3503963688"],
                                 "HCALBarrelTimeWindowMax": ["400"],
                                 "HCALEndcapTimeWindowMax": ["400"],
                                 }

MyDDMarlinPandora_10ns = MarlinProcessorWrapper("MyDDMarlinPandora_10ns")
MyDDMarlinPandora_10ns.OutputLevel = WARNING
MyDDMarlinPandora_10ns.ProcessorType = "DDPandoraPFANewProcessor"
MyDDMarlinPandora_10ns.Parameters = {
                                     "ClusterCollectionName": ["PandoraClusters"],
                                     "CreateGaps": ["false"],
                                     "CurvatureToMomentumFactor": ["0.00015"],
                                     "D0TrackCut": ["200"],
                                     "D0UnmatchedVertexTrackCut": ["5"],
                                     "DigitalMuonHits": ["0"],
                                     "ECalBarrelNormalVector": ["0", "0", "1"],
                                     "ECalCaloHitCollections": ["ECALBarrel", "ECALEndcap", "ECALOther"],
                                     "ECalMipThreshold": ["0.5"],
                                     "ECalScMipThreshold": ["0"],
                                     "ECalScToEMGeVCalibration": ["1"],
                                     "ECalScToHadGeVCalibrationBarrel": ["1"],
                                     "ECalScToHadGeVCalibrationEndCap": ["1"],
                                     "ECalScToMipCalibration": ["1"],
                                     "ECalSiMipThreshold": ["0"],
                                     "ECalSiToEMGeVCalibration": ["1"],
                                     "ECalSiToHadGeVCalibrationBarrel": ["1"],
                                     "ECalSiToHadGeVCalibrationEndCap": ["1"],
                                     "ECalSiToMipCalibration": ["1"],
                                     "ECalToEMGeVCalibration": ["1.01776966108"],
                                     "ECalToHadGeVCalibrationBarrel": ["1.11490774181"],
                                     "ECalToHadGeVCalibrationEndCap": ["1.11490774181"],
                                     "ECalToMipCalibration": ["175.439"],
                                     "EMConstantTerm": ["0.01"],
                                     "EMStochasticTerm": ["0.17"],
                                     "FinalEnergyDensityBin": ["110."],
                                     "HCalBarrelNormalVector": ["0", "0", "1"],
                                     "HCalCaloHitCollections": ["HCALBarrel", "HCALEndcap", "HCALOther"],
                                     "HCalMipThreshold": ["0.3"],
                                     "HCalToEMGeVCalibration": ["1.01776966108"],
                                     "HCalToHadGeVCalibration": ["1.00565042407"],
                                     "HCalToMipCalibration": ["45.6621"],
                                     "HadConstantTerm": ["0.03"],
                                     "HadStochasticTerm": ["0.6"],
                                     "InputEnergyCorrectionPoints": [],
                                     "KinkVertexCollections": ["KinkVertices"],
                                     "LCalCaloHitCollections": [],
                                     "LHCalCaloHitCollections": [],
                                     "LayersFromEdgeMaxRearDistance": ["250"],
                                     "MCParticleCollections": ["MCParticle"],
                                     "MaxBarrelTrackerInnerRDistance": ["200"],
                                     "MaxClusterEnergyToApplySoftComp": ["200."],
                                     "MaxHCalHitHadronicEnergy": ["10000000."],
                                     "MaxTrackHits": ["5000"],
                                     "MaxTrackSigmaPOverP": ["0.15"],
                                     "MinBarrelTrackerHitFractionOfExpected": ["0"],
                                     "MinCleanCorrectedHitEnergy": ["0.1"],
                                     "MinCleanHitEnergy": ["0.5"],
                                     "MinCleanHitEnergyFraction": ["0.01"],
                                     "MinFtdHitsForBarrelTrackerHitFraction": ["0"],
                                     "MinFtdTrackHits": ["0"],
                                     "MinMomentumForTrackHitChecks": ["0"],
                                     "MinTpcHitFractionOfExpected": ["0"],
                                     "MinTrackECalDistanceFromIp": ["0"],
                                     "MinTrackHits": ["0"],
                                     "MuonBarrelBField": ["-1.0"],
                                     "MuonCaloHitCollections": ["MUON"],
                                     "MuonEndCapBField": ["0.01"],
                                     "MuonHitEnergy": ["0.5"],
                                     "MuonToMipCalibration": ["20703.9"],
                                     "NEventsToSkip": ["0"],
                                     "NOuterSamplingLayers": ["3"],
                                     "OutputEnergyCorrectionPoints": [],
                                     "PFOCollectionName": ["PandoraPFOs"],
                                     "PandoraSettingsXmlFile": ["PandoraSettingsFCCee/PandoraSettingsDefault.xml"],
                                     "ProngVertexCollections": ["ProngVertices"],
                                     "ReachesECalBarrelTrackerOuterDistance": ["-100"],
                                     "ReachesECalBarrelTrackerZMaxDistance": ["-50"],
                                     "ReachesECalFtdZMaxDistance": ["1"],
                                     "ReachesECalMinFtdLayer": ["0"],
                                     "ReachesECalNBarrelTrackerHits": ["0"],
                                     "ReachesECalNFtdHits": ["0"],
                                     "RelCaloHitCollections": ["RelationCaloHit", "RelationMuonHit"],
                                     "RelTrackCollections": ["SiTracks_Refitted_Relation"],
                                     "ShouldFormTrackRelationships": ["1"],
                                     "SoftwareCompensationWeights": ["2.40821", "-0.0515852", "0.000711414", "-0.0254891", "-0.0121505", "-1.63084e-05", "0.062149", "0.0690735", "-0.223064"],
                                     "SplitVertexCollections": ["SplitVertices"],
                                     "StartVertexAlgorithmName": ["PandoraPFANew"],
                                     "StartVertexCollectionName": ["PandoraStartVertices"],
                                     "StripSplittingOn": ["0"],
                                     "TrackCollections": ["SiTracks_Refitted"],
                                     "TrackCreatorName": ["DDTrackCreatorCLIC"],
                                     "TrackStateTolerance": ["0"],
                                     "TrackSystemName": ["DDKalTest"],
                                     "UnmatchedVertexTrackMaxEnergy": ["5"],
                                     "UseEcalScLayers": ["0"],
                                     "UseNonVertexTracks": ["1"],
                                     "UseOldTrackStateCalculation": ["0"],
                                     "UseUnmatchedNonVertexTracks": ["0"],
                                     "UseUnmatchedVertexTracks": ["1"],
                                     "V0VertexCollections": ["V0Vertices"],
                                     "YokeBarrelNormalVector": ["0", "0", "1"],
                                     "Z0TrackCut": ["200"],
                                     "Z0UnmatchedVertexTrackCut": ["5"],
                                     "ZCutForNonVertexTracks": ["250"]
                                     }

MyDDMarlinPandora_400ns = MarlinProcessorWrapper("MyDDMarlinPandora_400ns")
MyDDMarlinPandora_400ns.OutputLevel = WARNING
MyDDMarlinPandora_400ns.ProcessorType = "DDPandoraPFANewProcessor"
MyDDMarlinPandora_400ns.Parameters = {
                                      "ClusterCollectionName": ["PandoraClusters"],
                                      "CreateGaps": ["false"],
                                      "CurvatureToMomentumFactor": ["0.00015"],
                                      "D0TrackCut": ["200"],
                                      "D0UnmatchedVertexTrackCut": ["5"],
                                      "DigitalMuonHits": ["0"],
                                      "ECalBarrelNormalVector": ["0", "0", "1"],
                                      "ECalCaloHitCollections": ["ECALBarrel", "ECALEndcap", "ECALOther"],
                                      "ECalMipThreshold": ["0.5"],
                                      "ECalScMipThreshold": ["0"],
                                      "ECalScToEMGeVCalibration": ["1"],
                                      "ECalScToHadGeVCalibrationBarrel": ["1"],
                                      "ECalScToHadGeVCalibrationEndCap": ["1"],
                                      "ECalScToMipCalibration": ["1"],
                                      "ECalSiMipThreshold": ["0"],
                                      "ECalSiToEMGeVCalibration": ["1"],
                                      "ECalSiToHadGeVCalibrationBarrel": ["1"],
                                      "ECalSiToHadGeVCalibrationEndCap": ["1"],
                                      "ECalSiToMipCalibration": ["1"],
                                      "ECalToEMGeVCalibration": ["1.02513816926"],
                                      "ECalToHadGeVCalibrationBarrel": ["1.07276660331"],
                                      "ECalToHadGeVCalibrationEndCap": ["1.07276660331"],
                                      "ECalToMipCalibration": ["175.439"],
                                      "EMConstantTerm": ["0.01"],
                                      "EMStochasticTerm": ["0.17"],
                                      "FinalEnergyDensityBin": ["110."],
                                      "HCalBarrelNormalVector": ["0", "0", "1"],
                                      "HCalCaloHitCollections": ["HCALBarrel", "HCALEndcap", "HCALOther"],
                                      "HCalMipThreshold": ["0.3"],
                                      "HCalToEMGeVCalibration": ["1.02513816926"],
                                      "HCalToHadGeVCalibration": ["1.01147686143"],
                                      "HCalToMipCalibration": ["49.7512"],
                                      "HadConstantTerm": ["0.03"],
                                      "HadStochasticTerm": ["0.6"],
                                      "InputEnergyCorrectionPoints": [],
                                      "KinkVertexCollections": ["KinkVertices"],
                                      "LCalCaloHitCollections": [],
                                      "LHCalCaloHitCollections": [],
                                      "LayersFromEdgeMaxRearDistance": ["250"],
                                      "MCParticleCollections": ["MCParticle"],
                                      "MaxBarrelTrackerInnerRDistance": ["200"],
                                      "MaxClusterEnergyToApplySoftComp": ["200."],
                                      "MaxHCalHitHadronicEnergy": ["10000000."],
                                      "MaxTrackHits": ["5000"],
                                      "MaxTrackSigmaPOverP": ["0.15"],
                                      "MinBarrelTrackerHitFractionOfExpected": ["0"],
                                      "MinCleanCorrectedHitEnergy": ["0.1"],
                                      "MinCleanHitEnergy": ["0.5"],
                                      "MinCleanHitEnergyFraction": ["0.01"],
                                      "MinFtdHitsForBarrelTrackerHitFraction": ["0"],
                                      "MinFtdTrackHits": ["0"],
                                      "MinMomentumForTrackHitChecks": ["0"],
                                      "MinTpcHitFractionOfExpected": ["0"],
                                      "MinTrackECalDistanceFromIp": ["0"],
                                      "MinTrackHits": ["0"],
                                      "MuonBarrelBField": ["-1.0"],
                                      "MuonCaloHitCollections": ["MUON"],
                                      "MuonEndCapBField": ["0.01"],
                                      "MuonHitEnergy": ["0.5"],
                                      "MuonToMipCalibration": ["20703.9"],
                                      "NEventsToSkip": ["0"],
                                      "NOuterSamplingLayers": ["3"],
                                      "OutputEnergyCorrectionPoints": [],
                                      "PFOCollectionName": ["PandoraPFOs"],
                                      "PandoraSettingsXmlFile": ["PandoraSettingsFCCee/PandoraSettingsDefault_400nsCalTimeWindow.xml"],
                                      "ProngVertexCollections": ["ProngVertices"],
                                      "ReachesECalBarrelTrackerOuterDistance": ["-100"],
                                      "ReachesECalBarrelTrackerZMaxDistance": ["-50"],
                                      "ReachesECalFtdZMaxDistance": ["1"],
                                      "ReachesECalMinFtdLayer": ["0"],
                                      "ReachesECalNBarrelTrackerHits": ["0"],
                                      "ReachesECalNFtdHits": ["0"],
                                      "RelCaloHitCollections": ["RelationCaloHit", "RelationMuonHit"],
                                      "RelTrackCollections": ["SiTracks_Refitted_Relation"],
                                      "ShouldFormTrackRelationships": ["1"],
                                      "SoftwareCompensationWeights": ["2.43375", "-0.0430951", "0.000244914", "-0.145478", "-0.00044577", "-8.37222e-05", "0.237484", "0.243491", "-0.0713701"],
                                      "SplitVertexCollections": ["SplitVertices"],
                                      "StartVertexAlgorithmName": ["PandoraPFANew"],
                                      "StartVertexCollectionName": ["PandoraStartVertices"],
                                      "StripSplittingOn": ["0"],
                                      "TrackCollections": ["SiTracks_Refitted"],
                                      "TrackCreatorName": ["DDTrackCreatorCLIC"],
                                      "TrackStateTolerance": ["0"],
                                      "TrackSystemName": ["DDKalTest"],
                                      "UnmatchedVertexTrackMaxEnergy": ["5"],
                                      "UseEcalScLayers": ["0"],
                                      "UseNonVertexTracks": ["1"],
                                      "UseOldTrackStateCalculation": ["0"],
                                      "UseUnmatchedNonVertexTracks": ["0"],
                                      "UseUnmatchedVertexTracks": ["1"],
                                      "V0VertexCollections": ["V0Vertices"],
                                      "YokeBarrelNormalVector": ["0", "0", "1"],
                                      "Z0TrackCut": ["200"],
                                      "Z0UnmatchedVertexTrackCut": ["5"],
                                      "ZCutForNonVertexTracks": ["250"]
                                      }

MyCLICPfoSelectorDefault = MarlinProcessorWrapper("MyCLICPfoSelectorDefault")
MyCLICPfoSelectorDefault.OutputLevel = WARNING
MyCLICPfoSelectorDefault.ProcessorType = "CLICPfoSelector"
MyCLICPfoSelectorDefault.Parameters = {
                                       "ChargedPfoLooseTimingCut": ["3"],
                                       "ChargedPfoNegativeLooseTimingCut": ["-1"],
                                       "ChargedPfoNegativeTightTimingCut": ["-0.5"],
                                       "ChargedPfoPtCut": ["0"],
                                       "ChargedPfoPtCutForLooseTiming": ["4"],
                                       "ChargedPfoTightTimingCut": ["1.5"],
                                       "CheckKaonCorrection": ["0"],
                                       "CheckProtonCorrection": ["0"],
                                       "ClusterLessPfoTrackTimeCut": ["10"],
                                       "CorrectHitTimesForTimeOfFlight": ["0"],
                                       "DisplayRejectedPfos": ["1"],
                                       "DisplaySelectedPfos": ["1"],
                                       "FarForwardCosTheta": ["0.975"],
                                       "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                       "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                       "HCalBarrelLooseTimingCut": ["20"],
                                       "HCalBarrelTightTimingCut": ["10"],
                                       "HCalEndCapTimingFactor": ["1"],
                                       "InputPfoCollection": ["PandoraPFOs"],
                                       "KeepKShorts": ["1"],
                                       "MaxMomentumForClusterLessPfos": ["2"],
                                       "MinECalHitsForTiming": ["5"],
                                       "MinHCalEndCapHitsForTiming": ["5"],
                                       "MinMomentumForClusterLessPfos": ["0.5"],
                                       "MinPtForClusterLessPfos": ["0.5"],
                                       "MinimumEnergyForNeutronTiming": ["1"],
                                       "Monitoring": ["0"],
                                       "MonitoringPfoEnergyToDisplay": ["1"],
                                       "NeutralFarForwardLooseTimingCut": ["2"],
                                       "NeutralFarForwardTightTimingCut": ["1"],
                                       "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                       "NeutralHadronLooseTimingCut": ["2.5"],
                                       "NeutralHadronPtCut": ["0"],
                                       "NeutralHadronPtCutForLooseTiming": ["8"],
                                       "NeutralHadronTightTimingCut": ["1.5"],
                                       "PhotonFarForwardLooseTimingCut": ["2"],
                                       "PhotonFarForwardTightTimingCut": ["1"],
                                       "PhotonLooseTimingCut": ["2"],
                                       "PhotonPtCut": ["0"],
                                       "PhotonPtCutForLooseTiming": ["4"],
                                       "PhotonTightTimingCut": ["1"],
                                       "PtCutForTightTiming": ["0.75"],
                                       "SelectedPfoCollection": ["SelectedPandoraPFOs"],
                                       "UseClusterLessPfos": ["1"],
                                       "UseNeutronTiming": ["0"]
                                       }

MyCLICPfoSelectorLoose = MarlinProcessorWrapper("MyCLICPfoSelectorLoose")
MyCLICPfoSelectorLoose.OutputLevel = WARNING
MyCLICPfoSelectorLoose.ProcessorType = "CLICPfoSelector"
MyCLICPfoSelectorLoose.Parameters = {
                                     "ChargedPfoLooseTimingCut": ["3"],
                                     "ChargedPfoNegativeLooseTimingCut": ["-2.0"],
                                     "ChargedPfoNegativeTightTimingCut": ["-2.0"],
                                     "ChargedPfoPtCut": ["0"],
                                     "ChargedPfoPtCutForLooseTiming": ["4"],
                                     "ChargedPfoTightTimingCut": ["1.5"],
                                     "CheckKaonCorrection": ["0"],
                                     "CheckProtonCorrection": ["0"],
                                     "ClusterLessPfoTrackTimeCut": ["1000."],
                                     "CorrectHitTimesForTimeOfFlight": ["0"],
                                     "DisplayRejectedPfos": ["1"],
                                     "DisplaySelectedPfos": ["1"],
                                     "FarForwardCosTheta": ["0.975"],
                                     "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                     "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                     "HCalBarrelLooseTimingCut": ["20"],
                                     "HCalBarrelTightTimingCut": ["10"],
                                     "HCalEndCapTimingFactor": ["1"],
                                     "InputPfoCollection": ["PandoraPFOs"],
                                     "KeepKShorts": ["1"],
                                     "MaxMomentumForClusterLessPfos": ["2"],
                                     "MinECalHitsForTiming": ["5"],
                                     "MinHCalEndCapHitsForTiming": ["5"],
                                     "MinMomentumForClusterLessPfos": ["0.0"],
                                     "MinPtForClusterLessPfos": ["0.25"],
                                     "MinimumEnergyForNeutronTiming": ["1"],
                                     "Monitoring": ["0"],
                                     "MonitoringPfoEnergyToDisplay": ["1"],
                                     "NeutralFarForwardLooseTimingCut": ["2.5"],
                                     "NeutralFarForwardTightTimingCut": ["1.5"],
                                     "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                     "NeutralHadronLooseTimingCut": ["2.5"],
                                     "NeutralHadronPtCut": ["0"],
                                     "NeutralHadronPtCutForLooseTiming": ["8"],
                                     "NeutralHadronTightTimingCut": ["1.5"],
                                     "PhotonFarForwardLooseTimingCut": ["2"],
                                     "PhotonFarForwardTightTimingCut": ["1"],
                                     "PhotonLooseTimingCut": ["2."],
                                     "PhotonPtCut": ["0"],
                                     "PhotonPtCutForLooseTiming": ["4"],
                                     "PhotonTightTimingCut": ["2."],
                                     "PtCutForTightTiming": ["0.75"],
                                     "SelectedPfoCollection": ["LooseSelectedPandoraPFOs"],
                                     "UseClusterLessPfos": ["1"],
                                     "UseNeutronTiming": ["0"]
                                     }

MyCLICPfoSelectorTight = MarlinProcessorWrapper("MyCLICPfoSelectorTight")
MyCLICPfoSelectorTight.OutputLevel = WARNING
MyCLICPfoSelectorTight.ProcessorType = "CLICPfoSelector"
MyCLICPfoSelectorTight.Parameters = {
                                     "ChargedPfoLooseTimingCut": ["2.0"],
                                     "ChargedPfoNegativeLooseTimingCut": ["-0.5"],
                                     "ChargedPfoNegativeTightTimingCut": ["-0.25"],
                                     "ChargedPfoPtCut": ["0"],
                                     "ChargedPfoPtCutForLooseTiming": ["4"],
                                     "ChargedPfoTightTimingCut": ["1.0"],
                                     "CheckKaonCorrection": ["0"],
                                     "CheckProtonCorrection": ["0"],
                                     "ClusterLessPfoTrackTimeCut": ["10"],
                                     "CorrectHitTimesForTimeOfFlight": ["0"],
                                     "DisplayRejectedPfos": ["1"],
                                     "DisplaySelectedPfos": ["1"],
                                     "FarForwardCosTheta": ["0.95"],
                                     "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                     "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                     "HCalBarrelLooseTimingCut": ["20"],
                                     "HCalBarrelTightTimingCut": ["10"],
                                     "HCalEndCapTimingFactor": ["1"],
                                     "InputPfoCollection": ["PandoraPFOs"],
                                     "KeepKShorts": ["1"],
                                     "MaxMomentumForClusterLessPfos": ["1.5"],
                                     "MinECalHitsForTiming": ["5"],
                                     "MinHCalEndCapHitsForTiming": ["5"],
                                     "MinMomentumForClusterLessPfos": ["0.5"],
                                     "MinPtForClusterLessPfos": ["1.0"],
                                     "MinimumEnergyForNeutronTiming": ["1"],
                                     "Monitoring": ["0"],
                                     "MonitoringPfoEnergyToDisplay": ["1"],
                                     "NeutralFarForwardLooseTimingCut": ["1.5"],
                                     "NeutralFarForwardTightTimingCut": ["1"],
                                     "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                     "NeutralHadronLooseTimingCut": ["2.5"],
                                     "NeutralHadronPtCut": ["0.5"],
                                     "NeutralHadronPtCutForLooseTiming": ["8"],
                                     "NeutralHadronTightTimingCut": ["1.5"],
                                     "PhotonFarForwardLooseTimingCut": ["2"],
                                     "PhotonFarForwardTightTimingCut": ["1"],
                                     "PhotonLooseTimingCut": ["2"],
                                     "PhotonPtCut": ["0.2"],
                                     "PhotonPtCutForLooseTiming": ["4"],
                                     "PhotonTightTimingCut": ["1"],
                                     "PtCutForTightTiming": ["1.0"],
                                     "SelectedPfoCollection": ["TightSelectedPandoraPFOs"],
                                     "UseClusterLessPfos": ["0"],
                                     "UseNeutronTiming": ["0"]
                                     }

VertexFinder = MarlinProcessorWrapper("VertexFinder")
VertexFinder.OutputLevel = WARNING
VertexFinder.ProcessorType = "LcfiplusProcessor"
VertexFinder.Parameters = {
                           "Algorithms": ["PrimaryVertexFinder", "BuildUpVertex"],
                           "BeamSizeX": ["38.2E-3"],
                           "BeamSizeY": ["68E-6"],
                           "BeamSizeZ": ["1.97"],
                           "BuildUpVertex.AVFTemperature": ["5.0"],
                           "BuildUpVertex.AssocIPTracks": ["1"],
                           "BuildUpVertex.AssocIPTracksChi2RatioSecToPri": ["2.0"],
                           "BuildUpVertex.AssocIPTracksMinDist": ["0."],
                           "BuildUpVertex.MassThreshold": ["10."],
                           "BuildUpVertex.MaxChi2ForDistOrder": ["1.0"],
                           "BuildUpVertex.MinDistFromIP": ["0.3"],
                           "BuildUpVertex.PrimaryChi2Threshold": ["25."],
                           "BuildUpVertex.SecondaryChi2Threshold": ["9."],
                           "BuildUpVertex.TrackMaxD0": ["10."],
                           "BuildUpVertex.TrackMaxD0Err": ["0.1"],
                           "BuildUpVertex.TrackMaxZ0": ["20."],
                           "BuildUpVertex.TrackMaxZ0Err": ["0.1"],
                           "BuildUpVertex.TrackMinFtdHits": ["1"],
                           "BuildUpVertex.TrackMinPt": ["0.1"],
                           "BuildUpVertex.TrackMinTpcHits": ["1"],
                           "BuildUpVertex.TrackMinTpcHitsMinPt": ["999999"],
                           "BuildUpVertex.TrackMinVxdFtdHits": ["1"],
                           "BuildUpVertex.TrackMinVxdHits": ["1"],
                           "BuildUpVertex.UseAVF": ["false"],
                           "BuildUpVertex.UseV0Selection": ["1"],
                           "BuildUpVertex.V0VertexCollectionName": ["BuildUpVertices_V0"],
                           "BuildUpVertexCollectionName": ["BuildUpVertices"],
                           "MCPCollection": ["MCParticle"],
                           "MCPFORelation": ["RecoMCTruthLink"],
                           "MagneticField": ["2.0"],
                           "PFOCollection": ["PFOsFromJets"],
                           "PrimaryVertexCollectionName": ["PrimaryVertices"],
                           "PrimaryVertexFinder.BeamspotConstraint": ["1"],
                           "PrimaryVertexFinder.BeamspotSmearing": ["false"],
                           "PrimaryVertexFinder.Chi2Threshold": ["25."],
                           "PrimaryVertexFinder.TrackMaxD0": ["20."],
                           "PrimaryVertexFinder.TrackMaxInnermostHitRadius": ["61"],
                           "PrimaryVertexFinder.TrackMaxZ0": ["20."],
                           "PrimaryVertexFinder.TrackMinFtdHits": ["999999"],
                           "PrimaryVertexFinder.TrackMinTpcHits": ["999999"],
                           "PrimaryVertexFinder.TrackMinTpcHitsMinPt": ["999999"],
                           "PrimaryVertexFinder.TrackMinVtxFtdHits": ["1"],
                           "PrimaryVertexFinder.TrackMinVxdHits": ["999999"],
                           "PrintEventNumber": ["1"],
                           "ReadSubdetectorEnergies": ["0"],
                           "TrackHitOrdering": ["2"],
                           "UpdateVertexRPDaughters": ["0"],
                           "UseMCP": ["0"]
                           }

VertexFinderUnconstrained = MarlinProcessorWrapper("VertexFinderUnconstrained")
VertexFinderUnconstrained.OutputLevel = WARNING
VertexFinderUnconstrained.ProcessorType = "LcfiplusProcessor"
VertexFinderUnconstrained.Parameters = {
                                        "Algorithms": ["PrimaryVertexFinder", "BuildUpVertex"],
                                        "BeamSizeX": ["38.2E-3"],
                                        "BeamSizeY": ["68E-6"],
                                        "BeamSizeZ": ["1.97"],
                                        "BuildUpVertex.AVFTemperature": ["5.0"],
                                        "BuildUpVertex.AssocIPTracks": ["1"],
                                        "BuildUpVertex.AssocIPTracksChi2RatioSecToPri": ["2.0"],
                                        "BuildUpVertex.AssocIPTracksMinDist": ["0."],
                                        "BuildUpVertex.MassThreshold": ["10."],
                                        "BuildUpVertex.MaxChi2ForDistOrder": ["1.0"],
                                        "BuildUpVertex.MinDistFromIP": ["0.3"],
                                        "BuildUpVertex.PrimaryChi2Threshold": ["25."],
                                        "BuildUpVertex.SecondaryChi2Threshold": ["9."],
                                        "BuildUpVertex.TrackMaxD0": ["10."],
                                        "BuildUpVertex.TrackMaxD0Err": ["0.1"],
                                        "BuildUpVertex.TrackMaxZ0": ["20."],
                                        "BuildUpVertex.TrackMaxZ0Err": ["0.1"],
                                        "BuildUpVertex.TrackMinFtdHits": ["1"],
                                        "BuildUpVertex.TrackMinPt": ["0.1"],
                                        "BuildUpVertex.TrackMinTpcHits": ["1"],
                                        "BuildUpVertex.TrackMinTpcHitsMinPt": ["999999"],
                                        "BuildUpVertex.TrackMinVxdFtdHits": ["1"],
                                        "BuildUpVertex.TrackMinVxdHits": ["1"],
                                        "BuildUpVertex.UseAVF": ["false"],
                                        "BuildUpVertex.UseV0Selection": ["1"],
                                        "BuildUpVertex.V0VertexCollectionName": ["BuildUpVertices_V0_res"],
                                        "BuildUpVertexCollectionName": ["BuildUpVertices_res"],
                                        "MCPCollection": ["MCParticle"],
                                        "MCPFORelation": ["RecoMCTruthLink"],
                                        "MagneticField": ["2.0"],
                                        "PFOCollection": ["TightSelectedPandoraPFOs"],
                                        "PrimaryVertexCollectionName": ["PrimaryVertices_res"],
                                        "PrimaryVertexFinder.BeamspotConstraint": ["0"],
                                        "PrimaryVertexFinder.BeamspotSmearing": ["false"],
                                        "PrimaryVertexFinder.Chi2Threshold": ["25."],
                                        "PrimaryVertexFinder.TrackMaxD0": ["20."],
                                        "PrimaryVertexFinder.TrackMaxInnermostHitRadius": ["61"],
                                        "PrimaryVertexFinder.TrackMaxZ0": ["20."],
                                        "PrimaryVertexFinder.TrackMinFtdHits": ["999999"],
                                        "PrimaryVertexFinder.TrackMinTpcHits": ["999999"],
                                        "PrimaryVertexFinder.TrackMinTpcHitsMinPt": ["999999"],
                                        "PrimaryVertexFinder.TrackMinVtxFtdHits": ["1"],
                                        "PrimaryVertexFinder.TrackMinVxdHits": ["999999"],
                                        "PrintEventNumber": ["1"],
                                        "ReadSubdetectorEnergies": ["0"],
                                        "TrackHitOrdering": ["2"],
                                        "UpdateVertexRPDaughters": ["0"],
                                        "UseMCP": ["0"]
                                        }

algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(InitDD4hep)
algList.append(Overlay[CONFIG["Overlay"]])
algList.append(VXDBarrelDigitiser)
algList.append(VXDEndcapDigitiser)
algList.append(InnerPlanarDigiProcessor)
algList.append(InnerEndcapPlanarDigiProcessor)
algList.append(OuterPlanarDigiProcessor)
algList.append(OuterEndcapPlanarDigiProcessor)
# algList.append(MyTruthTrackFinder)  # Config.TrackingTruth
# algList.append(MyConformalTracking)  # Config.TrackingConformal
# algList.append(ClonesAndSplitTracksFinder)  # Config.TrackingConformal
algList.append(Refit)
algList.append(MyDDCaloDigi_${CalorimeterIntegrationTimeWindow}ns)
algList.append(MyDDSimpleMuonDigi)
algList.append(MyDDMarlinPandora_${CalorimeterIntegrationTimeWindow}ns)
algList.append(LumiCalReco)
algList.append(MyClicEfficiencyCalculator)
algList.append(MyRecoMCTruthLinker)
algList.append(MyTrackChecker)
algList.append(MyCLICPfoSelectorDefault)
algList.append(MyCLICPfoSelectorLoose)
algList.append(MyCLICPfoSelectorTight)

if CONFIG["Overlay"] == "False":
    algList.append(RenameCollection)
else:
    algList.append(MyFastJetProcessor)

algList.append(VertexFinder)
algList.append(JetClusteringAndRefiner)
# algList.append(VertexFinderUnconstrained)  # Config.VertexUnconstrainedON
algList.append(Output_REC)
algList.append(Output_DST)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=WARNING
              )
