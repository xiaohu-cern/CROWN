from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, Filter

####################
# Set of producers used for selection possible good fatjets
####################

### energy corrections
# vh these pT corrections are copied from Htautau
# TODO check if L1FastJet L2L3 and residual corrections are consistent with hmm
Create_FatJetTightID_v15 = Producer( ############# This producer is used to create FatJetTightID for NANOAODv15 ###############################
    name="Create_FatJetTightID_v15",
    call="physicsobject::jet::Cal_JetTightID_v15({df}, {output}, {input})",
    input=[
        nanoAOD.FatJet_eta,
        nanoAOD.FatJet_neEmEF,
        nanoAOD.FatJet_neHEF,
        nanoAOD.FatJet_chEmEF,
        nanoAOD.FatJet_chHEF,
        nanoAOD.FatJet_chMultiplicity,
        nanoAOD.FatJet_neMultiplicity,
    ],
    output=[q.fatjetTightID],
    scopes=["global"],
)
# Create_FatJetTightID_v12 = Producer( ############# This producer is used to create FatJetTightID for NANOAODv15 ###############################
#     name="Create_FatJetTightID_v12",
#     call="physicsobject::jet::Cal_JetTightID_v12({df}, {output}, {input})",
#     input=[
#         nanoAOD.FatJet_eta,
#         nanoAOD.FatJet_neEmEF,
#         nanoAOD.FatJet_neHEF,
#         nanoAOD.FatJet_ID,
#     ],
#     output=[q.fatjetTightID],
#     scopes=["global"],
# )
# Create_FatJetTightLepVetoID = Producer( ############# This producer is used to create FatJetTightLepVetoID for NANOAODv15 ###############################
#     name="Create_FatJetTightLepVetoID",
#     call="physicsobject::jet::Cal_JetTightLepVetoID({df}, {output}, {input})",
#     input=[
#         nanoAOD.FatJet_eta,
#         q.fatjetTightID,
#         nanoAOD.FatJet_muEF,
#         nanoAOD.FatJet_chEmEF,
#     ],
#     output=[q.fatjetTightLepVetoID],
#     scopes=["global"],
# )

# FatJetPtCorrection = Producer(
#     name="FatJetPtCorrection",
#     call="physicsobject::jet::FatJetPtCorrection({df}, {output}, {input}, {fatjet_reapplyJES}, {fatjet_jes_sources}, {fatjet_jes_shift}, {fatjet_jer_shift}, {fatjet_jec_file}, {fatjet_jer_tag}, {fatjet_jes_tag}, {fatjet_jec_algo}, {fatjet_veto_map}, {fatjet_veto_tag})",
#     input=[
#         nanoAOD.FatJet_pt,
#         nanoAOD.FatJet_eta,
#         nanoAOD.FatJet_phi,
#         nanoAOD.FatJet_area,
#         nanoAOD.FatJet_rawFactor,
#         nanoAOD.FatJet_ID,
#         nanoAOD.GenJetAK8_pt,
#         nanoAOD.GenJetAK8_eta,
#         nanoAOD.GenJetAK8_phi,
#         nanoAOD.rho,
#     ],
#     output=[q.FatJet_pt_corrected],
#     scopes=["global"],
# )
FatJetPtCorrection_v15 = Producer(
    name="FatJetPtCorrection_v15",
    call="physicsobject::jet::FatJetPtCorrection_v15({df}, {output}, {input}, {fatjet_reapplyJES}, {fatjet_jes_sources}, {fatjet_jes_shift}, {fatjet_jer_shift}, {fatjet_jec_file}, {fatjet_jer_tag}, {fatjet_jes_tag}, {fatjet_jec_algo}, {fatjet_veto_map}, {fatjet_veto_tag}, {year_id}, {Phi_in_L2Relative})",
    input=[
        nanoAOD.FatJet_pt,
        nanoAOD.FatJet_eta,
        nanoAOD.FatJet_phi,
        nanoAOD.FatJet_area,
        nanoAOD.FatJet_rawFactor,
        nanoAOD.GenJetAK8_pt,
        nanoAOD.GenJetAK8_eta,
        nanoAOD.GenJetAK8_phi,
        nanoAOD.rho,
    ],
    output=[q.FatJet_pt_corrected],
    scopes=["global"],
)
FatJetPtCorrection_v15_data = Producer(
    name="FatJetPtCorrection_v15_data",
    call="physicsobject::jet::FatJetPtCorrection_v15_data({df}, {output}, {input}, {fatjet_reapplyJES}, {fatjet_jec_file}, {fatjet_jes_tag_data}, {fatjet_jec_algo}, {fatjet_veto_map}, {fatjet_veto_tag}, {year_id}, {Phi_in_L2Relative})",
    input=[
        nanoAOD.FatJet_pt,
        nanoAOD.FatJet_eta,
        nanoAOD.FatJet_phi,
        nanoAOD.FatJet_area,
        nanoAOD.FatJet_rawFactor,
        nanoAOD.rho,
        nanoAOD.run,
    ],
    output=[q.FatJet_pt_corrected],
    scopes=["global"],
)
FatJetPtCorrection_run2 = Producer(
    name="FatJetPtCorrection_run2",
    call="physicsobject::jet::JetPtCorrection_run2({df}, {output}, {input}, {fatjet_reapplyJES}, {fatjet_jes_sources}, {fatjet_jes_shift}, {fatjet_jer_shift}, {fatjet_jec_file}, {fatjet_jer_tag}, {fatjet_jes_tag}, {fatjet_jec_algo}, {fatjet_veto_map}, {fatjet_veto_tag})",
    input=[
        nanoAOD.FatJet_pt,
        nanoAOD.FatJet_eta,
        nanoAOD.FatJet_phi,
        nanoAOD.FatJet_area,
        nanoAOD.FatJet_rawFactor,
        nanoAOD.FatJet_ID,
        nanoAOD.GenJetAK8_pt,
        nanoAOD.GenJetAK8_eta,
        nanoAOD.GenJetAK8_phi,
        nanoAOD.rho,
    ],
    output=[q.FatJet_pt_corrected],
    scopes=["global"],
)
FatJetMassCorrection = Producer(
    name="FatJetMassCorrection",
    call="physicsobject::ObjectMassCorrectionWithPt({df}, {output}, {input})",
    input=[
        nanoAOD.FatJet_mass,
        nanoAOD.FatJet_pt,
        q.FatJet_pt_corrected,
    ],
    output=[q.FatJet_mass_corrected],
    scopes=["global"],
)
# FatJetEnergyCorrection = ProducerGroup(
#     name="FatJetEnergyCorrection",
#     call=None,
#     input=None,
#     output=None,
#     scopes=["global"],
#     subproducers=[FatJetPtCorrection, FatJetMassCorrection],
# )
FatJetEnergyCorrection = ProducerGroup(
    name="FatJetEnergyCorrection",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[FatJetPtCorrection_v15, FatJetMassCorrection],
)
FatJetEnergyCorrection_data = ProducerGroup(
    name="FatJetEnergyCorrection_data",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[FatJetPtCorrection_v15_data, FatJetMassCorrection],
)
FatJetEnergyCorrection_run2 = ProducerGroup(
    name="FatJetEnergyCorrection_run2",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[FatJetPtCorrection_run2, FatJetMassCorrection],
)
# in data and embdedded sample, we simply rename the nanoAOD jets to the jet_pt_corrected column
# RenameFatJetPt = Producer(
#     name="RenameFatJetPt",
#     call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
#     input=[nanoAOD.FatJet_pt],
#     output=[q.FatJet_pt_corrected],
#     scopes=["global"],
# )
RenameFatJetPt = Producer(
    name="RenameFatJetPt",
    call="physicsobject::jet::FatJetVetoMap({df}, {output}, {input}, {fatjet_veto_map}, {fatjet_veto_tag})",
    input=[
        nanoAOD.FatJet_pt,
        nanoAOD.FatJet_eta,
        nanoAOD.FatJet_phi,
    ],
    output=[q.FatJet_pt_corrected],
    scopes=["global"],
)
RenameFatJetMass = Producer(
    name="RenameFatJetMass",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.FatJet_mass],
    output=[q.FatJet_mass_corrected],
    scopes=["global"],
)
FatJetEnergyCorrection_2017_noPtCorr = ProducerGroup(
    name="FatJetEnergyCorrection_2017_noPtCorr",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[RenameFatJetPt, FatJetMassCorrection],
)
# RenameFatJetsData = ProducerGroup(
#     name="RenameFatJetsData",
#     call=None,
#     input=None,
#     output=None,
#     scopes=["global"],
#     subproducers=[RenameFatJetPt, RenameFatJetMass],
# )
### discard the event if any Jet_pt_corrected == -999
FlagFatJetVetoMap = Producer(
    name="FlagFatJetVetoMap",
    call='physicsobject::PassJetVetoFlag({df}, {input}, {output})',
    input=[q.FatJet_pt_corrected],
    output=[q.FatJetFlag_pass_veto_map],
    scopes=["global"],
)
FatJetPtCut = Producer(
    name="FatJetPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_fatjet_pt})",
    input=[q.FatJet_pt_corrected],
    output=[],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
FatJetEtaCut = Producer(
    name="FatJetEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_fatjet_eta})",
    input=[nanoAOD.FatJet_eta],
    output=[],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
FatJetSDMassCut = Producer(
    name="FatJetSDMassCut",
    call="physicsobject::CutVarMin({df}, {input}, {output}, {min_fatjet_MSD})",
    input=[nanoAOD.FatJet_msoftdrop],
    output=[],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
FatJetIDCut = Producer(
    name="FatJetIDCut",
    call="physicsobject::jet::CutID({df}, {output}, {input}, {fatjet_id})",
    input=[nanoAOD.FatJet_ID],
    output=[q.fatjet_id_mask],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
FatJetIDCut_Bool = Producer( ######## for v15 and v12
    name="FatJetIDCut_Bool",
    call="physicsobject::jet::CutBoolID({df}, {output}, {input})",
    input=[q.fatjetTightID],
    output=[q.fatjet_id_mask],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
## 2022preEE fatjet id UChar_t 
FatJetIDCut_UChar = Producer(
    name="FatJetIDCut_UChar",
    call="physicsobject::jet::CutUCharID({df}, {output}, {input}, {fatjet_id})",
    input=[nanoAOD.FatJet_ID],
    output=[q.fatjet_id_mask],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
# in fjmm, 2 good muons and 0 good electron, no need to do dR with ele
VetoOverlappingFatJetsWithMuons = Producer(
    name="VetoOverlappingFatJetsWithMuons",
    call="jet::VetoOverlappingJets({df}, {output}, {input}, {deltaR_fatjet_veto})",
    input=[nanoAOD.FatJet_eta, nanoAOD.FatJet_phi, nanoAOD.Muon_eta, nanoAOD.Muon_phi, q.good_muon_collection], # vh base or good muon?
    output=[q.fatjet_overlap_veto_mask],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
GoodFatJets = ProducerGroup(
    name="GoodFatJets",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_fatjets_mask],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
    subproducers=[FatJetPtCut, FatJetEtaCut, FatJetSDMassCut, FatJetIDCut_UChar, VetoOverlappingFatJetsWithMuons],
)
GoodFatJets_v15 = ProducerGroup(
    name="GoodFatJets_v15",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_fatjets_mask],
    scopes=["fjmm","fjmm_cr","nnmm", "e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
    subproducers=[FatJetPtCut, FatJetEtaCut, FatJetSDMassCut, FatJetIDCut_Bool, VetoOverlappingFatJetsWithMuons],
)
GoodFatJets_run2 = ProducerGroup(
    name="GoodFatJets_run2",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_fatjets_mask],
    scopes=["fjmm","fjmm_cr"],
    subproducers=[FatJetPtCut, FatJetEtaCut, FatJetSDMassCut, FatJetIDCut, VetoOverlappingFatJetsWithMuons],
)
NumberOfGoodFatJets = Producer(
    name="NumberOfGoodFatJets",
    call="quantities::NumberOfGoodObjects({df}, {output}, {input})",
    input=[q.good_fatjets_mask],
    output=[q.nfatjets],
    scopes=["fjmm","fjmm_cr","nnmm","e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
NFatjetFlag = Producer(
    name="NFatjetFlag",
    call='physicsobject::flagNumObject({df}, {output}, {input}, {vh_good_nfatjets}, ">=")',
    input=[q.nfatjets],
    output=[],
    scopes=["fjmm","fjmm_cr"],
)
VetoNFatjetFlag = Producer(
    name="VetoNFatjetFlag",
    call='physicsobject::flagNumObject({df}, {output}, {input}, {vh_good_nfatjets}, "<")',
    input=[q.nfatjets],
    output=[],
    scopes=["e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
)
# call='basefunctions::FilterThreshold({df}, {input}, {vh_good_nfatjets}, ">=", "Number of fatjets >= 1")',
FilterNFatjets_fjmm = Filter(
    name="FilterNFatjets_fjmm",
    call='basefunctions::FilterFlagsAny({df}, "Number of fatjets >= 1", {input})',
    input=[],
    scopes=["fjmm","fjmm_cr"],
    subproducers=[NFatjetFlag]
)
FilterVetoNFatjets_fjmm = Filter(
    name="FilterVetoNFatjets_fjmm",
    call='basefunctions::FilterFlagsAny({df}, "Number of fatjets < 1", {input})',
    input=[],
    scopes=["e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
    subproducers=[VetoNFatjetFlag]
)

# fatjet collection
FatJetCollection = Producer(
    name="FatJetCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    input=[q.FatJet_pt_corrected, q.good_fatjets_mask],
    output=[q.good_fatjet_collection],
    scopes=["fjmm","fjmm_cr"],
)
LVFatJet1 = Producer(
    name="LVFatJet1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_fatjet_collection,
        q.FatJet_pt_corrected,
        nanoAOD.FatJet_eta,
        nanoAOD.FatJet_phi,
        q.FatJet_mass_corrected,
    ],
    output=[q.fatjet_p4_1],
    scopes=["fjmm","fjmm_cr"],
)
Pnet_Fatjet_Mass_Corr = Producer(
    name="Pnet_Fatjet_Mass_Corr",
    call="lorentzvectors::buildVar({df}, {input_vec}, {output}, 0)",
    input=[
        q.good_fatjet_collection,
        nanoAOD.FatJet_particleNet_massCorr,
    ],
    output=[q.good_FatJet_particleNet_massCorr],
    scopes=["fjmm", "fjmm_cr"],
)
GoodFatjet_RawFactor = Producer(
    name="GoodFatjet_RawFactor",
    call="lorentzvectors::buildVar({df}, {input_vec}, {output}, 0)",
    input=[
        q.good_fatjet_collection,
        nanoAOD.FatJet_rawFactor,
    ],
    output=[q.good_FatJet_rawfactor],
    scopes=["fjmm", "fjmm_cr"],
)

BuildSubJet1 = Producer(
    name="BuildSubJet1",
    call="quantities::jet::buildSubJet({df}, {input}, 0, {output})",
    input=[
        nanoAOD.SubJet_pt,
        nanoAOD.SubJet_eta,
        nanoAOD.SubJet_phi,
        nanoAOD.SubJet_mass,
        q.good_fatjet_collection,
        nanoAOD.FatJet_subJetIdx1,
    ],
    output=[q.subjet_p4_1],
    scopes=["fjmm", "fjmm_cr"]
)
BuildSubJet2 = Producer(
    name="BuildSubJet2",
    call="quantities::jet::buildSubJet({df}, {input}, 0, {output})",
    input=[
        nanoAOD.SubJet_pt,
        nanoAOD.SubJet_eta,
        nanoAOD.SubJet_phi,
        nanoAOD.SubJet_mass,
        q.good_fatjet_collection,
        nanoAOD.FatJet_subJetIdx2,
    ],
    output=[q.subjet_p4_2],
    scopes=["fjmm", "fjmm_cr"]
)