from code_generation.quantity import NanoAODQuantity
from code_generation.modifiers import EraModifier

run = NanoAODQuantity("run")
luminosityBlock = NanoAODQuantity("luminosityBlock")
event = NanoAODQuantity("event")
LHE_Njets = NanoAODQuantity("LHE_Njets")
# prefireWeight = NanoAODQuantity("L1PreFiringWeight_Nom")

Tau_pt = NanoAODQuantity("Tau_pt")
Tau_eta = NanoAODQuantity("Tau_eta")
Tau_phi = NanoAODQuantity("Tau_phi")
Tau_mass = NanoAODQuantity("Tau_mass")
Tau_dz = NanoAODQuantity("Tau_dz")
Tau_dxy = NanoAODQuantity("Tau_dxy")
Tau_charge = NanoAODQuantity("Tau_charge")
Tau_decayMode = NanoAODQuantity("Tau_decayMode")
Tau_genMatch = NanoAODQuantity("Tau_genPartFlav")
### 24
Tau_IDraw = NanoAODQuantity("Tau_rawDeepTau2018v2p5VSjet")
######
Tau_indexToGen = NanoAODQuantity("Tau_genPartIdx")
Tau_associatedJet = NanoAODQuantity("Tau_jetIdx")
### 24
Tau_ID_vsJet = NanoAODQuantity("Tau_idDeepTau2018v2p5VSjet")
Tau_ID_vsEle = NanoAODQuantity("Tau_idDeepTau2018v2p5VSe")
Tau_ID_vsMu = NanoAODQuantity("Tau_idDeepTau2018v2p5VSmu")
######

Muon_pt = NanoAODQuantity("Muon_pt")
Muon_bsConstrainedPt = NanoAODQuantity("Muon_bsConstrainedPt")
Muon_bsConstrainedPtErr = NanoAODQuantity("Muon_bsConstrainedPtErr")
Muon_tunepRelPt = NanoAODQuantity("Muon_tunepRelPt")
Muon_eta = NanoAODQuantity("Muon_eta")
Muon_phi = NanoAODQuantity("Muon_phi")
Muon_mass = NanoAODQuantity("Muon_mass")
Muon_dz = NanoAODQuantity("Muon_dz")
Muon_dxy = NanoAODQuantity("Muon_dxy")
Muon_charge = NanoAODQuantity("Muon_charge")
Muon_genMatch = NanoAODQuantity("Muon_genPartFlav")
Muon_indexToGen = NanoAODQuantity("Muon_genPartIdx")
Muon_sip3d = NanoAODQuantity("Muon_sip3d") # vh
Muon_pfRelIso04_all = NanoAODQuantity("Muon_pfRelIso04_all") # vh
### 24
Muon_mvaTTH = NanoAODQuantity("Muon_promptMVA")
######
Muon_nTrackerLayers = NanoAODQuantity("Muon_nTrackerLayers")

Electron_pt = NanoAODQuantity("Electron_pt")
Electron_r9 = NanoAODQuantity("Electron_r9")
Electron_seedGain = NanoAODQuantity("Electron_seedGain")
Electron_eta = NanoAODQuantity("Electron_eta")
Electron_dxy = NanoAODQuantity("Electron_dxy")
Electron_dz = NanoAODQuantity("Electron_dz")
Electron_phi = NanoAODQuantity("Electron_phi")
Electron_mass = NanoAODQuantity("Electron_mass")
Electron_iso = NanoAODQuantity("Electron_pfRelIso03_all")
Electron_charge = NanoAODQuantity("Electron_charge")
Electron_indexToGen = NanoAODQuantity("Electron_genPartIdx")
# write by botao
Electron_deltaEtaSC = NanoAODQuantity("Electron_deltaEtaSC")
Electron_sip3d = NanoAODQuantity("Electron_sip3d")
# Electron_mvaFall17V2noIso_WP90 = NanoAODQuantity("Electron_mvaFall17V2noIso_WP90")
Electron_convVeto = NanoAODQuantity("Electron_convVeto")
Electron_lostHits = NanoAODQuantity("Electron_lostHits")
### 24
Electron_mvaTTH = NanoAODQuantity("Electron_promptMVA")
######
Electron_pdgId = NanoAODQuantity("Electron_pdgId")
Muon_pdgId = NanoAODQuantity("Muon_pdgId")
# end write

GenJet_pt = NanoAODQuantity("GenJet_pt")
GenJet_eta = NanoAODQuantity("GenJet_eta")
GenJet_phi = NanoAODQuantity("GenJet_phi")

Jet_eta = NanoAODQuantity("Jet_eta")
Jet_phi = NanoAODQuantity("Jet_phi")
Jet_pt = NanoAODQuantity("Jet_pt")
Jet_mass = NanoAODQuantity("Jet_mass")
Jet_area = NanoAODQuantity("Jet_area")
Jet_flavor = NanoAODQuantity("Jet_hadronFlavour")
Jet_rawFactor = NanoAODQuantity("Jet_rawFactor")
#### Method for 2024: Calculating jetid by hand Details at: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13p6TeV#nanoAOD_Flags
Jet_ID = NanoAODQuantity("Jet_jetId")
Jet_PUID = NanoAODQuantity("Jet_puId")
'''
PUId for CHS jet subtracts pileup at jet level
For v12 and v15, jets are puppi jets, and pileup is subtracted at particle level, so the PUId is aborted
What about the Jet_puIdDisc in v15??? Details at: https://github.com/cms-sw/cmssw/pull/46137
Most of the analysis can ignore this Id. PileUp Jet Id is a mess and nobody follow this any more.
'''
Jet_chEmEF = NanoAODQuantity("Jet_chEmEF") # charged Electromagnetic Energy Fraction
Jet_neEmEF = NanoAODQuantity("Jet_neEmEF") # neutral Electromagnetic Energy Fraction
Jet_neHEF = NanoAODQuantity("Jet_neHEF") # neutral Hadron Energy Fraction
Jet_chHEF = NanoAODQuantity("Jet_chHEF")
Jet_muEF = NanoAODQuantity("Jet_muEF")
Jet_chMultiplicity = NanoAODQuantity("Jet_chMultiplicity")
Jet_neMultiplicity = NanoAODQuantity("Jet_neMultiplicity")



Jet_associatedGenJet = NanoAODQuantity("Jet_genJetIdx")
# BJet_discriminator = NanoAODQuantity("Jet_btagDeepFlavB") # DeepFlavour
BJet_discriminator = NanoAODQuantity("Jet_btagDeepB") # vh DeepCSV it seems previous work using Jet_btagDeepB
# BJet_discriminator_PNet = NanoAODQuantity("Jet_btagPNetB") # PNet
### synchronize with GloParT
BJet_discriminator_PNet = NanoAODQuantity("Jet_btagUParTAK4B")

Pileup_nTrueInt = NanoAODQuantity("Pileup_nTrueInt")
rho = NanoAODQuantity("Pileup_pudensity")

GenParticle_eta = NanoAODQuantity("GenPart_eta")
GenParticle_phi = NanoAODQuantity("GenPart_phi")
GenParticle_pt = NanoAODQuantity("GenPart_pt")
GenParticle_mass = NanoAODQuantity("GenPart_mass")
GenParticle_pdgId = NanoAODQuantity("GenPart_pdgId")
GenParticle_status = NanoAODQuantity("GenPart_status")
GenParticle_statusFlags = NanoAODQuantity("GenPart_statusFlags")
GenParticle_motherid = NanoAODQuantity("GenPart_genPartIdxMother")

## Trigger Objects
TriggerObject_bit = NanoAODQuantity("TrigObj_filterBits") ###24: ULong64_t, 22-23: Int_t
TriggerObject_pt = NanoAODQuantity("TrigObj_pt")
TriggerObject_eta = NanoAODQuantity("TrigObj_eta")
TriggerObject_phi = NanoAODQuantity("TrigObj_phi")
TriggerObject_id = NanoAODQuantity("TrigObj_id")

## HTXS quantities
HTXS_Higgs_pt = NanoAODQuantity("HTXS_Higgs_pt")
HTXS_Higgs_y = NanoAODQuantity("HTXS_Higgs_y")
HTXS_njets30 = NanoAODQuantity("HTXS_njets30")
HTXS_stage_0 = NanoAODQuantity("HTXS_stage_0")
HTXS_stage_1_pTjet30 = NanoAODQuantity("HTXS_stage_1_pTjet30")
HTXS_stage1_1_fine_cat_pTjet30GeV = NanoAODQuantity("HTXS_stage1_1_fine_cat_pTjet30GeV")
HTXS_stage1_2_cat_pTjet30GeV = NanoAODQuantity("HTXS_stage1_2_cat_pTjet30GeV")
HTXS_stage1_2_fine_cat_pTjet30GeV = NanoAODQuantity("HTXS_stage1_2_fine_cat_pTjet30GeV")

## MET quantities
## TODO Swich to Puppi versions for METCOV and Signifiance as soon as they are in the nanoAOD
### 24
MET_covXX = NanoAODQuantity("PFMET_covXX")
MET_covXY = NanoAODQuantity("PFMET_covXY")
MET_covYY = NanoAODQuantity("PFMET_covYY")
MET_significance = NanoAODQuantity("PFMET_significance")
#############################

MET_phi = NanoAODQuantity("PuppiMET_phi")
MET_pt = NanoAODQuantity("PuppiMET_pt")
MET_sumEt = NanoAODQuantity("PuppiMET_sumEt")
### 24
PFMET_phi = NanoAODQuantity("PFMET_phi")
PFMET_pt = NanoAODQuantity("PFMET_pt")
PFMET_sumEt = NanoAODQuantity("PFMET_sumEt")
#############################

GenMET_pt = NanoAODQuantity("GenMET_pt")
GenMET_phi = NanoAODQuantity("GenMET_phi")

## Embedding Quantities
genWeight = NanoAODQuantity("genWeight")
# TauEmbedding_initialMETEt = NanoAODQuantity("TauEmbedding_initialMETEt")
# TauEmbedding_initialMETphi = NanoAODQuantity("TauEmbedding_initialMETphi")
# TauEmbedding_initialPuppiMETEt = NanoAODQuantity("TauEmbedding_initialPuppiMETEt")
# TauEmbedding_initialPuppiMETphi = NanoAODQuantity("TauEmbedding_initialPuppiMETphi")
# TauEmbedding_isMediumLeadingMuon = NanoAODQuantity("TauEmbedding_isMediumLeadingMuon")
# TauEmbedding_isMediumTrailingMuon = NanoAODQuantity("TauEmbedding_isMediumTrailingMuon")
# TauEmbedding_isTightLeadingMuon = NanoAODQuantity("TauEmbedding_isTightLeadingMuon")
# TauEmbedding_isTightTrailingMuon = NanoAODQuantity("TauEmbedding_isTightTrailingMuon")
# TauEmbedding_InitialPairCandidates = NanoAODQuantity(
#     "TauEmbedding_nInitialPairCandidates"
# )
# TauEmbedding_SelectionOldMass = NanoAODQuantity("TauEmbedding_SelectionOldMass")
# TauEmbedding_SelectionNewMass = NanoAODQuantity("TauEmbedding_SelectionNewMass")

## Fat Jet Quantities
GenJetAK8_pt = NanoAODQuantity("GenJetAK8_pt")
GenJetAK8_eta = NanoAODQuantity("GenJetAK8_eta")
GenJetAK8_phi = NanoAODQuantity("GenJetAK8_phi")

FatJet_eta = NanoAODQuantity("FatJet_eta")
FatJet_phi = NanoAODQuantity("FatJet_phi")
FatJet_pt = NanoAODQuantity("FatJet_pt")
FatJet_mass = NanoAODQuantity("FatJet_mass")
FatJet_area = NanoAODQuantity("FatJet_area")
FatJet_rawFactor = NanoAODQuantity("FatJet_rawFactor")
### Method for 2024: Fatjet_jetId should be calculated by hand, same method for jetId, Details at: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13p6TeV#nanoAOD_Flags
FatJet_ID = NanoAODQuantity("FatJet_jetId")
FatJet_chEmEF = NanoAODQuantity("FatJet_chEmEF") # charged Electromagnetic Energy Fraction
FatJet_neEmEF = NanoAODQuantity("FatJet_neEmEF") # neutral Electromagnetic Energy Fraction
FatJet_neHEF = NanoAODQuantity("FatJet_neHEF") # neutral Hadron Energy Fraction
FatJet_chHEF = NanoAODQuantity("FatJet_chHEF")
FatJet_muEF = NanoAODQuantity("FatJet_muEF")
FatJet_chMultiplicity = NanoAODQuantity("FatJet_chMultiplicity")
FatJet_neMultiplicity = NanoAODQuantity("FatJet_neMultiplicity")
FatJet_msoftdrop = NanoAODQuantity("FatJet_msoftdrop")
FatJet_particleNet_massCorr = NanoAODQuantity("FatJet_globalParT3_massCorrX2p")
'''
GlobalParT-3 mass regression corrector with respect to the original jet mass, 
optimised for resonance 2-prong (bb/cc/cs/ss/qq) jets. 
Use (massCorrX2p * mass * (1 - rawFactor)) to get the regressed mass
'''
# FatJet_particleNet_massCorr = NanoAODQuantity("FatJet_globalParT3_massCorrGeneric")
'''
GlobalParT-3 mass regression corrector with respect to the original jet mass, 
optimised for generic jet cases. 
Use (massCorrGeneric * mass * (1 - rawFactor)) to get the regressed mass
'''
# FatJet_PUID = NanoAODQuantity("FatJet_puId")
# Jet_associatedGenJet = NanoAODQuantity("Jet_genJetIdx")
#BJet_discriminator = NanoAODQuantity("Jet_btagDeepFlavB") # DeepFlavour
# BFatJet_discriminator = NanoAODQuantity("FatJet_btagDeepB") # vh DeepCSV

# FatJet DeepBoostedJet tagger
# FatJet_deepTag_WvsQCD = NanoAODQuantity("FatJet_deepTag_WvsQCD") # DeepBoostedJet tagger W vs QCD discriminator
# FatJet_deepTag_ZvsQCD = NanoAODQuantity("FatJet_deepTag_ZvsQCD") # DeepBoostedJet tagger Z vs QCD discriminator
# FatJet_deepTag_QCD = NanoAODQuantity("FatJet_deepTag_QCD") # DeepBoostedJet tagger QCD(bb,cc,b,c,others) sum
# FatJet_deepTagMD_WvsQCD = NanoAODQuantity("FatJet_deepTagMD_WvsQCD") # Mass-decorrelated DeepBoostedJet tagger W vs QCD discriminator
# FatJet_deepTagMD_ZvsQCD = NanoAODQuantity("FatJet_deepTagMD_ZvsQCD") # Mass-decorrelated DeepBoostedJet tagger Z vs QCD discriminator

# in NanoAOD v9
# FatJet_particleNet_QCD_Nanov9 = NanoAODQuantity("FatJet_particleNet_QCD") # ParticleNet tagger QCD(bb,cc,b,c,others) sum
# FatJet_particleNet_WvsQCD_Nanov9 = NanoAODQuantity("FatJet_particleNet_WvsQCD") # ParticleNet tagger W vs QCD discriminator
# FatJet_particleNet_ZvsQCD_Nanov9 = NanoAODQuantity("FatJet_particleNet_ZvsQCD") # ParticleNet tagger Z vs QCD discriminator
# FatJet_particleNet_TvsQCD_Nanov9 = NanoAODQuantity("FatJet_particleNet_TvsQCD") # ParticleNet tagger top vs QCD discriminator

# in NanoAOD v15 24
FatJet_particleNet_QCD = NanoAODQuantity("FatJet_globalParT3_QCD") # ParticleNet tagger QCD(0+1+2HF) sum
FatJet_particleNetWithMass_QCD = NanoAODQuantity("FatJet_particleNetWithMass_QCD") # ParticleNet tagger (w/ mass) QCD(bb,cc,b,c,others) sum
FatJet_particleNetWithMass_WvsQCD = NanoAODQuantity("FatJet_globalParT3_withMassWvsQCD") # ParticleNet tagger (w/ mass) W vs QCD discriminator
FatJet_particleNetWithMass_ZvsQCD = NanoAODQuantity("FatJet_globalParT3_withMassZvsQCD") # ParticleNet tagger (w/ mass) Z vs QCD discriminator
FatJet_particleNetWithMass_TvsQCD = NanoAODQuantity("FatJet_globalParT3_withMassTopvsQCD") # ParticleNet tagger (w/ mass) top vs QCD discriminator
#####################

Electron_cutBased = NanoAODQuantity("Electron_cutBased")
Muon_ptErr = NanoAODQuantity("Muon_ptErr")

# FatJet_tau1 = NanoAODQuantity("FatJet_tau1")
# FatJet_tau2 = NanoAODQuantity("FatJet_tau2")
# FatJet_tau3 = NanoAODQuantity("FatJet_tau3")
# FatJet_tau4 = NanoAODQuantity("FatJet_tau4")

##### Muon FSR recovery #####
Muon_fsrPhotonIdx = NanoAODQuantity("Muon_fsrPhotonIdx")
FsrPhoton_pt = NanoAODQuantity("FsrPhoton_pt")
FsrPhoton_eta = NanoAODQuantity("FsrPhoton_eta")
FsrPhoton_phi = NanoAODQuantity("FsrPhoton_phi")
FsrPhoton_dROverEt2 = NanoAODQuantity("FsrPhoton_dROverEt2")
FsrPhoton_relIso03 = NanoAODQuantity("FsrPhoton_relIso03")
