from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
# write by botao

####################
# Set of producers used for select the smallest mass of di-lepton
####################

# dilepton mass > 12 GeV need SFOS
CalcSmallestDiMuonMass = Producer(
    name="CalcSmallestDiMuonMass",
    call='physicsobject::M_dileptonMass({df}, {output}, {input})',
    input=[nanoAOD.Muon_pt,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           nanoAOD.Muon_charge,
           q.good_muon_collection],
    output=[q.smallest_dimuon_mass],
    scopes=["m2m","e2m","eemm","eemm_cr","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
CalcSmallestBaseDiMuonMass = Producer(
    name="CalcSmallestBaseDiMuonMass",
    call='physicsobject::M_dileptonMass({df}, {output}, {input})',
    input=[nanoAOD.Muon_pt,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           nanoAOD.Muon_charge,
           q.base_muon_collection],
    output=[q.smallest_dimuon_mass],
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb","mmmm_cr"],
)
CalcSmallestDiElectronMass = Producer(
    name="CalcSmallestDiElectronMass",
    call='physicsobject::M_dileptonMass({df}, {output}, {input})',
    input=[nanoAOD.Electron_pt,
           nanoAOD.Electron_eta, 
           nanoAOD.Electron_phi, 
           nanoAOD.Electron_mass,
           nanoAOD.Electron_charge,
           q.dielectron_ZCand_collection],
    output=[q.smallest_dielectron_mass],
    scopes=["eemm","eemm_cr"],
)
LeptonChargeSumVeto = Producer(
    name="LeptonChargeSumVeto",
    call='physicsobject::LeptonChargeSum({df}, {output}, {input})',
    input=[nanoAOD.Muon_charge,  # only in m2m and 4m can input only muon charge
           q.good_muon_collection],
    output=[q.Flag_LeptonChargeSumVeto],   # 1 stands pm1, 2 stands 0, 0 stands others
    scopes=["m2m","mmmm","nnmm","fjmm","fjmm_cr","nnmm_dycontrol","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
BaseLeptonChargeSumVeto = Producer(
    name="BaseLeptonChargeSumVeto",
    call='physicsobject::LeptonChargeSum({df}, {output}, {input})',
    input=[nanoAOD.Muon_charge,  # only in m2m and 4m can input only muon charge
           q.base_muon_collection],
    output=[q.Flag_LeptonChargeSumVeto],   # 1 stands pm1, 2 stands 0, 0 stands others
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
)
LeptonChargeSumVeto_elemu = Producer(
    name="LeptonChargeSumVeto_elemu",
    call='physicsobject::LeptonChargeSumEleMu({df}, {output}, {input})',
    input=[nanoAOD.Muon_charge,  # only in e2m and 2e2m can input only muon charge
           nanoAOD.Electron_charge,
           q.good_muon_collection,
           q.good_electron_collection],
    output=[q.Flag_LeptonChargeSumVeto],   # 1 stands pm1, 2 stands 0, 0 stands others
    scopes=["e2m","eemm","nnmm_topcontrol","e2m_dyfakeinge_regionb"],
)
LeptonChargeSumVeto_mubaseele = Producer(
    name="LeptonChargeSumVeto_mubaseele",
    call='physicsobject::LeptonChargeSumEleMu({df}, {output}, {input})',
    input=[nanoAOD.Muon_charge,  # only in e2m and 2e2m can input only muon charge
           nanoAOD.Electron_charge,
           q.good_muon_collection,
           q.base_electron_collection],
    output=[q.Flag_LeptonChargeSumVeto],   # 1 stands pm1, 2 stands 0, 0 stands others
    scopes=["eemm_cr"],
)
LeptonChargeSumVeto_baseelegoodmu_regioncd = Producer(
    name="LeptonChargeSumVeto_baseelegoodmu_regioncd",
    call='physicsobject::LeptonChargeSumEleMu({df}, {output}, {input})',
    input=[nanoAOD.Muon_charge,  # only in e2m and 2e2m can input only muon charge
           nanoAOD.Electron_charge,
           q.good_muon_collection,
           q.base_electron_collection],
    output=[q.Flag_LeptonChargeSumVeto],   # 1 stands pm1, 2 stands 0, 0 stands others
    scopes=["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
### extra lepton (muon) in m2m channel
Mu1_W_m2m_index = Producer(
    name="Mu1_W_m2m_index",
    call="physicsobject::ExtraMuonIndexFromW({df}, {output}, {input})",
    input=[
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.good_muon_collection,
        q.dimuon_HiggsCand_collection,
    ],
    output=[q.extra_muon_index],
    scopes=["m2m"],
)
Mu1_W_m2m_index_regionb = Producer(
    name="Mu1_W_m2m_index_regionb",
    call="physicsobject::ExtraMuonIndexFromW({df}, {output}, {input})",
    input=[
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.good_muon_collection,
        q.dimuon_ZControl_collection,
    ],
    output=[q.extra_muon_index],
    scopes=["m2m_dyfakeingmu_regionb"],
)
Mu1_W_m2m_index_regionc = Producer(
    name="Mu1_W_m2m_index_regionc",
    call="physicsobject::ExtraMuonIndexFromW({df}, {output}, {input})",
    input=[
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.base_muon_collection,
        q.dimuon_HiggsCand_collection,
    ],
    output=[q.extra_muon_index],
    scopes=["m2m_dyfakeingmu_regionc"],
)
Mu1_W_m2m_index_regiond = Producer(
    name="Mu1_W_m2m_index_regiond",
    call="physicsobject::ExtraMuonIndexFromW({df}, {output}, {input})",
    input=[
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.base_muon_collection,
        q.dimuon_ZControl_collection,
    ],
    output=[q.extra_muon_index],
    scopes=["m2m_dyfakeingmu_regiond"],
)
Mu1_W_m2m = Producer(
    name="Mu1_W_m2m",
    call="physicsobject::ExtraMuonFromW({df}, {output}, {input})",
    input=[
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.extra_muon_index, # already the muon index, using index[0]
    ],
    output=[q.extra_lep_p4],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)

Mu1_W_m2m_noCorr = Producer(
    name="Mu1_W_m2m_noCorr",
    call="physicsobject::ExtraMuonFromW({df}, {output}, {input})",
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.extra_muon_index, # already the muon index, using index[0]
    ],
    output=[q.extra_lep_p4_noCorr],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
### extra lepton (electron) in e2m channel
Ele1_W_e2m = Producer(
    name="Ele1_W_e2m",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_electron_collection,
        q.Electron_pt_corrected,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.extra_lep_p4],
    scopes=["e2m","e2m_dyfakeinge_regionb"],
)
Ele1_W_e2m_noCorr = Producer(
    name="Ele1_W_e2m_noCorr",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_electron_collection,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.extra_lep_p4_noCorr],
    scopes=["e2m","e2m_dyfakeinge_regionb"],
)
Ele1_W_e2m_regioncd = Producer(
    name="Ele1_W_e2m_regioncd",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.base_electron_collection,
        q.Electron_pt_corrected,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.extra_lep_p4],
    scopes=["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
Ele1_W_e2m_regioncd_noCorr = Producer(
    name="Ele1_W_e2m_regioncd_noCorr",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.base_electron_collection,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.extra_lep_p4_noCorr],
    scopes=["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
### calc MT_W using lepton_p4 and met
Calc_MT_W = Producer(
    name="Calc_MT_W",
    call="quantities::mT_MHT({df}, {output}, {input})",
    input=[
        q.extra_lep_p4,
        q.met_p4_jetcorrected,
    ],
    output=[q.mt_W],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
### Z lep ID
RenameZlepID_eemm = Producer(
    name="RenameZlepID_eemm",
    call="physicsobject::RedirectZlepID({df}, 0, {output})", # ifMu == 0, return 11
    input=[],
    output=[q.Zlep_ID],
    scopes=["eemm","eemm_cr"],
)
RenameZlepID_mmmm = Producer(
    name="RenameZlepID_mmmm",
    call="physicsobject::RedirectZlepID({df}, 1, {output})", # ifMu == 1, return 13
    input=[],
    output=[q.Zlep_ID],
    scopes=["mmmm","mmmm_cr"],
)
##### extra_lep mvaTTH
### mu using extra_muon_index[0]
extra_muon_mvaTTH = Producer(
    name="extra_muon_mvaTTH",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the extra_muon_index[0]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.extra_muon_index,
    ],
    output=[q.extra_lep_mvaTTH],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)

### good ele using good_electron_collection[0]
extra_goodele_mvaTTH = Producer(
    name="extra_goodele_mvaTTH",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the good_electron_collection[0]
    input=[
        nanoAOD.Electron_mvaTTH,
        q.good_electron_collection,
    ],
    output=[q.extra_lep_mvaTTH],
    scopes=["e2m","e2m_dyfakeinge_regionb"],
)
### base ele using base_electron_collection[0]
extra_baseele_mvaTTH = Producer(
    name="extra_baseele_mvaTTH",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the base_electron_collection[0]
    input=[
        nanoAOD.Electron_mvaTTH,
        q.base_electron_collection,
    ],
    output=[q.extra_lep_mvaTTH],
    scopes=["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

### eemm good_electron_collection, collection[0],[1]
lep1_mvaTTH_eemm = Producer(
    name="lep1_mvaTTH_eemm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the good_electron_collection[0]
    input=[
        nanoAOD.Electron_mvaTTH,
        q.dielectron_ZCand_collection,
    ],
    output=[q.lep1_mvaTTH],
    scopes=["eemm","eemm_cr"],
)
lep2_mvaTTH_eemm = Producer(
    name="lep2_mvaTTH_eemm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 1)", # 0 stands the good_electron_collection[1]
    input=[
        nanoAOD.Electron_mvaTTH,
        q.dielectron_ZCand_collection,
    ],
    output=[q.lep2_mvaTTH],
    scopes=["eemm","eemm_cr"],
)
### mmmm quadmuon_HiggsZCand_collection, collection[2], collection[3]
lep1_mvaTTH_mmmm = Producer(
    name="lep1_mvaTTH_mmmm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 2)", # 2 stands the quadmuon_HiggsZCand_collection[2]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.quadmuon_HiggsZCand_collection,
    ],
    output=[q.lep1_mvaTTH],
    scopes=["mmmm","mmmm_cr"],
)
lep2_mvaTTH_mmmm = Producer(
    name="lep2_mvaTTH_mmmm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 3)", # 3 stands the quadmuon_HiggsZCand_collection[3]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.quadmuon_HiggsZCand_collection,
    ],
    output=[q.lep2_mvaTTH],
    scopes=["mmmm","mmmm_cr"],
)
