from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers used for selection possible good jets
####################

### energy corrections
# vh these pT corrections are copied from Htautau
# TODO check if L1FastJet L2L3 and residual corrections are consistent with hmm
JetPtCorrection = Producer(
    name="JetPtCorrection",
    call="physicsobject::jet::JetPtCorrection({df}, {output}, {input}, {jet_reapplyJES}, {jet_jes_sources}, {jet_jes_shift}, {jet_jer_shift}, {jet_jec_file}, {jet_jer_tag}, {jet_jes_tag}, {jet_jec_algo})",
    input=[
        nanoAOD.Jet_pt,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        nanoAOD.Jet_area,
        nanoAOD.Jet_rawFactor,
        nanoAOD.Jet_ID,
        nanoAOD.GenJet_pt,
        nanoAOD.GenJet_eta,
        nanoAOD.GenJet_phi,
        nanoAOD.rho,
    ],
    output=[q.Jet_pt_corrected],
    scopes=["global"],
)
JetPtCorrection_run2 = Producer(
    name="JetPtCorrection_run2",
    call="physicsobject::jet::JetPtCorrection_run2({df}, {output}, {input}, {jet_reapplyJES}, {jet_jes_sources}, {jet_jes_shift}, {jet_jer_shift}, {jet_jec_file}, {jet_jer_tag}, {jet_jes_tag}, {jet_jec_algo})",
    input=[
        nanoAOD.Jet_pt,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        nanoAOD.Jet_area,
        nanoAOD.Jet_rawFactor,
        nanoAOD.Jet_ID,
        nanoAOD.GenJet_pt,
        nanoAOD.GenJet_eta,
        nanoAOD.GenJet_phi,
        nanoAOD.rho,
    ],
    output=[q.Jet_pt_corrected],
    scopes=["global"],
)
JetMassCorrection = Producer(
    name="JetMassCorrection",
    call="physicsobject::ObjectMassCorrectionWithPt({df}, {output}, {input})",
    input=[
        nanoAOD.Jet_mass,
        nanoAOD.Jet_pt,
        q.Jet_pt_corrected,
    ],
    output=[q.Jet_mass_corrected],
    scopes=["global"],
)
JetEnergyCorrection = ProducerGroup(
    name="JetEnergyCorrection",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[JetPtCorrection, JetMassCorrection],
)
JetEnergyCorrection_run2 = ProducerGroup(
    name="JetEnergyCorrection_run2",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[JetPtCorrection_run2, JetMassCorrection],
)
# in data and embdedded sample, we simply rename the nanoAOD jets to the jet_pt_corrected column
RenameJetPt = Producer(
    name="RenameJetPt",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_pt],
    output=[q.Jet_pt_corrected],
    scopes=["global"],
)
RenameJetMass = Producer(
    name="RenameJetMass",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_mass],
    output=[q.Jet_mass_corrected],
    scopes=["global"],
)
RenameJetsData = ProducerGroup(
    name="RenameJetsData",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[RenameJetPt, RenameJetMass],
)
### selecting jets

JetPtCut = Producer(
    name="JetPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_jet_pt})",
    input=[q.Jet_pt_corrected],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BJetPtCut = Producer(
    name="BJetPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_bjet_pt})",
    input=[q.Jet_pt_corrected],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
JetEtaCut = Producer(
    name="JetEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_jet_eta})",
    input=[nanoAOD.Jet_eta],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BJetEtaCut = Producer(
    name="BJetEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_bjet_eta})",
    input=[nanoAOD.Jet_eta],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
JetIDCut = Producer(
    name="JetIDCut",
    call="physicsobject::jet::CutID({df}, {output}, {input}, {jet_id})",
    input=[nanoAOD.Jet_ID],
    output=[q.jet_id_mask],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
JetIDCut_UChar = Producer(
    name="JetIDCut_UChar",
    call="physicsobject::jet::CutUCharID({df}, {output}, {input}, {jet_id})",
    input=[nanoAOD.Jet_ID],
    output=[q.jet_id_mask],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
JetPUIDCut = Producer(
    name="JetPUIDCut",
    call="physicsobject::jet::CutPUID({df}, {output}, {input}, {jet_puid}, {jet_puid_max_pt})",
    input=[nanoAOD.Jet_PUID, q.Jet_pt_corrected],
    output=[q.jet_puid_mask],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BTagCutLoose = Producer(
    name="BTagCutLoose",
    call="physicsobject::jet::CutRawID({df}, {input}, {output}, {btag_cut_loose})",
    input=[nanoAOD.BJet_discriminator],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BTagCutLoose_PNet = Producer(
    name="BTagCutLoose_PNet",
    call="physicsobject::jet::CutRawID({df}, {input}, {output}, {btag_cut_loose})",
    input=[nanoAOD.BJet_discriminator_PNet],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BTagCutMedium = Producer(
    name="BTagCutMedium",
    call="physicsobject::jet::CutRawID({df}, {input}, {output}, {btag_cut_medium})",
    input=[nanoAOD.BJet_discriminator],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BTagCutMedium_PNet = Producer(
    name="BTagCutMedium_PNet",
    call="physicsobject::jet::CutRawID({df}, {input}, {output}, {btag_cut_medium})",
    input=[nanoAOD.BJet_discriminator_PNet],
    output=[],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb",
            "m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb",
            "e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

# vh veto overlapping jets against muons
# TODO this runs over all jets, not efficient!!!
# need to run over only good jets

# overlap with good muon and good ele for m2m,e2m,regionb*2,nnmm,fjmm 
VetoOverlappingJets_GoodMuon = Producer(
    name="VetoOverlappingJets_GoodMuon",
    call="jet::VetoOverlappingJets({df}, {output}, {input}, {deltaR_jet_veto})",
    input=[nanoAOD.Jet_eta, nanoAOD.Jet_phi, nanoAOD.Muon_eta, nanoAOD.Muon_phi, q.good_muon_collection],
    output=[q.jet_overlap_veto_mask],
    scopes=["m2m","e2m","mmmm","eemm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
VetoOverlappingJets_GoodEle = Producer(
    name="VetoOverlappingJets_GoodEle",
    call="jet::VetoOverlappingJets({df}, {output}, {input}, {deltaR_jet_veto})",
    input=[nanoAOD.Jet_eta, nanoAOD.Jet_phi, nanoAOD.Electron_eta, nanoAOD.Electron_phi, q.good_electron_collection],
    output=[q.jet_overlap_veto_ele_mask],
    scopes=["m2m","e2m","mmmm","eemm","nnmm","fjmm","fjmm_cr","nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb"],
)
# overlap with base muon for m2m regionc and regiond, they require 3 base muon
VetoOverlappingJets_BaseMuon = Producer(
    name="VetoOverlappingJets_BaseMuon",
    call="jet::VetoOverlappingJets({df}, {output}, {input}, {deltaR_jet_veto})",
    input=[nanoAOD.Jet_eta, nanoAOD.Jet_phi, nanoAOD.Muon_eta, nanoAOD.Muon_phi, q.base_muon_collection],
    output=[q.jet_overlap_veto_mask],
    scopes=["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
# overlap with base ele, good mu for e2m regionc and regiond
VetoOverlappingJets_BaseEle = Producer(
    name="VetoOverlappingJets_BaseEle",
    call="jet::VetoOverlappingJets({df}, {output}, {input}, {deltaR_jet_veto})",
    input=[nanoAOD.Jet_eta, nanoAOD.Jet_phi, nanoAOD.Electron_eta, nanoAOD.Electron_phi, q.base_electron_collection],
    output=[q.jet_overlap_veto_ele_mask],
    scopes=["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
########################
########################
########################
GoodJets_2022_GoodMu_GoodEle = ProducerGroup(
    name="GoodJets_2022_GoodMu_GoodEle",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_jets_mask],
    scopes=["m2m","e2m","mmmm","eemm","nnmm","fjmm","nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb","fjmm_cr"],
    subproducers=[JetPtCut, JetEtaCut, JetIDCut_UChar,VetoOverlappingJets_GoodMuon, VetoOverlappingJets_GoodEle],
)
GoodJets_2022_BaseMu = ProducerGroup(
    name="GoodJets_2022_BaseMu",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_jets_mask],
    scopes=["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
    subproducers=[JetPtCut, JetEtaCut, JetIDCut_UChar,VetoOverlappingJets_BaseMuon],
)
GoodJets_2022_BaseEle_GoodMu = ProducerGroup(
    name="GoodJets_2022_BaseEle_GoodMu",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_jets_mask],
    scopes=["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[JetPtCut, JetEtaCut, JetIDCut_UChar,VetoOverlappingJets_BaseEle, VetoOverlappingJets_GoodMuon],
)
########################
# Jet_jetid -> jet_id UChar_t in v12, Int_t in v9
########################
########################
GoodJets_run2_GoodMu_GoodEle = ProducerGroup(
    name="GoodJets_run2_GoodMu_GoodEle",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_jets_mask],
    scopes=["m2m","e2m","mmmm","eemm","nnmm","fjmm","nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb","fjmm_cr"],
    subproducers=[JetPtCut, JetEtaCut, JetIDCut, JetPUIDCut, VetoOverlappingJets_GoodMuon, VetoOverlappingJets_GoodEle],
)
GoodJets_run2_BaseMu = ProducerGroup(
    name="GoodJets_run2_BaseMu",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_jets_mask],
    scopes=["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
    subproducers=[JetPtCut, JetEtaCut, JetIDCut,VetoOverlappingJets_BaseMuon],
)
GoodJets_run2_BaseEle_GoodMu = ProducerGroup(
    name="GoodJets_run2_BaseEle_GoodMu",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_jets_mask],
    scopes=["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[JetPtCut, JetEtaCut, JetIDCut,VetoOverlappingJets_BaseEle, VetoOverlappingJets_GoodMuon],
)
########################
########################
########################

GoodBJetsLoose = ProducerGroup(
    name="GoodBJetsLoose",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_jets_mask],
    output=[q.good_bjets_mask_loose],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[BJetPtCut, BJetEtaCut, BTagCutLoose],
)
GoodBJetsMedium = ProducerGroup(
    name="GoodBJetsMedium",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_bjets_mask_loose],
    output=[q.good_bjets_mask_medium],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[BTagCutMedium],
)
#############################
#############################
#############################
GoodBJetsLoose_PNet = ProducerGroup(
    name="GoodBJetsLoose_PNet",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_jets_mask],
    output=[q.good_bjets_mask_loose],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[BJetPtCut, BJetEtaCut, BTagCutLoose_PNet],
)
#############################
#############################
#############################
GoodBJetsMedium_PNet = ProducerGroup(
    name="GoodBJetsMedium_PNet",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_bjets_mask_loose],
    output=[q.good_bjets_mask_medium],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[BTagCutMedium_PNet],
)
NumberOfLooseB = Producer(
    name="NumberOfLooseB",
    call="quantities::NumberOfGoodObjects({df}, {output}, {input})",
    input=[q.good_bjets_mask_loose],
    output=[q.nbjets_loose],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
NumberOfMediumB = Producer(
    name="NumberOfMediumB",
    call="quantities::NumberOfGoodObjects({df}, {output}, {input})",
    input=[q.good_bjets_mask_medium],
    output=[q.nbjets_medium],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
# define MHT from good_jet_collection
Calc_MHT = Producer(
    name="Calc_MHT",
    call="physicsobject::MHT_Calculation({df}, {output}, {input})",
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
        q.good_jet_collection,
    ],
    output=[q.MHT_p4],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
# n jets ouput
NumberOfGoodJets = Producer(
    name="NumberOfGoodJets",
    call="quantities::NumberOfGoodObjects({df}, {output}, {input})",
    input=[q.good_jets_mask],
    output=[q.njets],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
# jet collection
JetCollection = Producer(
    name="JetCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    input=[q.Jet_pt_corrected, q.good_jets_mask],
    output=[q.good_jet_collection],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
LVJet1 = Producer(
    name="LVJet1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_jet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.jet_p4_1],
    scopes=["global"],
)
LVJet2 = Producer(
    name="LVJet2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.good_jet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.jet_p4_2],
    scopes=["global"],
)
LVJet3 = Producer(
    name="LVJet3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.good_jet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.jet_p4_3],
    scopes=["global"],
)
LVJet4 = Producer(
    name="LVJet4",
    call="lorentzvectors::build({df}, {input_vec}, 3, {output})",
    input=[
        q.good_jet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.jet_p4_4],
    scopes=["global"],
)
FilterNJets = Producer(
    name="FilterNJets",
    call='basefunctions::FilterThreshold({df}, {input}, {vh_njets}, ">=", "Number of jets >= 3")',
    input=[q.njets],
    output=None,
    scopes=["global"],
)
Calc_MHT_all = Producer(
    name="Calc_MHT_all",
    call="physicsobject::MHT_CalculationALL({df}, {output}, {input})",
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.good_muon_collection,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        q.good_electron_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
        q.good_jet_collection,
    ],
    output=[q.MHTALL_p4],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)