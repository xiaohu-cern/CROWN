from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
# write by botao

####################
# Set of producers used for nnmm DY control region and Top control region
####################

DY_DiMuonPair_CR = Producer(
    name="DY_DiMuonPair_CR",
    call='physicsobject::DY_DiMuonPair_CR({df}, {output}, {input})',
    input=[q.Muon_pt_corrected,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           nanoAOD.Muon_charge,
           q.good_muon_collection],
    output=[q.dimuon_ZControl_collection], # index about the two selected muons may from Z boson
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)

DY_DiMuonPair_CR_HighMass = Producer(
    name="DY_DiMuonPair_CR_HighMass",
    call='physicsobject::DY_DiMuonPair_CR_HighMass({df}, {output}, {input})',
    input=[q.Muon_pt_corrected,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           nanoAOD.Muon_charge,
           q.good_muon_collection],
    output=[q.dimuon_ZControl_collection], # index about the two selected muons may from Z boson
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)


Flag_DiMuonFromCR = Producer(
    name="Flag_DiMuonFromCR",
    call='physicsobject::DiMuonFromCR({df}, {output}, {input})',
    input=[q.dimuon_ZControl_collection],
    output=[q.Flag_DiMuonFromCR],
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
###
DiMuonPairCR_p4 = Producer(
    name="DiMuonPairCR_p4",
    call='physicsobject::ZControlDiMuonPairP4({df}, {output}, {input})',
    input=[q.Muon_pt_corrected,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           q.dimuon_ZControl_collection],
    output=[q.dimuon_p4_CR],
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
DiMuonPairCR_p4_PureTunepPT = Producer(
    name="DiMuonPairCR_p4_PureTunepPT",
    call='physicsobject::ZControlDiMuonPairP4({df}, {output}, {input})',
    input=[q.Muon_pt_corrected_PureTunepPT,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           q.dimuon_ZControl_collection],
    output=[q.dimuon_p4_CR_PureTunepPT],
    scopes=["fjmm_cr"],
)
DiMuonPairCR_p4_BSCTunepPT = Producer(
    name="DiMuonPairCR_p4_BSCTunepPT",
    call='physicsobject::ZControlDiMuonPairP4({df}, {output}, {input})',
    input=[q.Muon_pt_corrected_BSCTunepPT,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           q.dimuon_ZControl_collection],
    output=[q.dimuon_p4_CR_BSCTunepPT],
    scopes=["fjmm_cr"],
)
DiMuonPairCR_p4_BSCTunepPTCorr = Producer(
    name="DiMuonPairCR_p4_BSCTunepPTCorr",
    call='physicsobject::ZControlDiMuonPairP4({df}, {output}, {input})',
    input=[q.Muon_pt_corrected_BSCTunepPTCorr,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           q.dimuon_ZControl_collection],
    output=[q.dimuon_p4_CR_BSCTunepPTCorr],
    scopes=["fjmm_cr"],
)
### cut flag
FilterFlag_DiMuonFromCR = Producer(
    name="FilterFlag_DiMuonFromCR",
    call='basefunctions::FilterThreshold({df}, {input}, {flag_DiMuonFromCR}, "==", "DiMuon From DY CR")',
    input=[q.Flag_DiMuonFromCR],
    output=None,
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
#####
dimuonCR_pt = Producer(
    name="dimuonCR_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.dimuon_p4_CR,
    ],
    output=[q.dimuonCR_pt],
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)

dimuonCR_eta = Producer(
    name="dimuonCR_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.dimuon_p4_CR,
    ],
    output=[q.dimuonCR_eta],
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
dimuonCR_phi = Producer(
    name="dimuonCR_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.dimuon_p4_CR,
    ],
    output=[q.dimuonCR_phi],
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
dimuonCR_mass = Producer(
    name="dimuonCR_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.dimuon_p4_CR,
    ],
    output=[q.dimuonCR_mass],
    scopes=["nnmm_dycontrol","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
dimuonCR_mass_PureTunepPT = Producer(
    name="dimuonCR_mass_PureTunepPT",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.dimuon_p4_CR_PureTunepPT,
    ],
    output=[q.dimuonCR_mass_PureTunepPT],
    scopes=["fjmm_cr"],
)
dimuonCR_mass_BSCTunepPT = Producer(
    name="dimuonCR_mass_BSCTunepPT",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.dimuon_p4_CR_BSCTunepPT,
    ],
    output=[q.dimuonCR_mass_BSCTunepPT],
    scopes=["fjmm_cr"],
)
dimuonCR_mass_BSCTunepPTCorr = Producer(
    name="dimuonCR_mass_BSCTunepPTCorr",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.dimuon_p4_CR_BSCTunepPTCorr,
    ],
    output=[q.dimuonCR_mass_BSCTunepPTCorr],
    scopes=["fjmm_cr"],
)

########
### for nnmm top control region
########
TOP_EleMuPair_CR_corrected = Producer(
    name="TOP_EleMuPair_CR_corrected",
    call='physicsobject::TOP_EleMuPair_CR({df}, {output}, {input})',
    input=[q.Muon_pt_corrected,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           nanoAOD.Muon_charge,
           q.good_muon_collection,
           q.Electron_pt_corrected,
           nanoAOD.Electron_eta, 
           nanoAOD.Electron_phi, 
           nanoAOD.Electron_mass,
           nanoAOD.Electron_charge,
           q.good_electron_collection],
    output=[q.elemu_TopControl_collection], # index about the two selected ele and mu, index[0] stands mu
    scopes=["nnmm_topcontrol"],
)
Flag_EleMuFromCR = Producer(
    name="Flag_EleMuFromCR",
    call='physicsobject::EleMuFromCR({df}, {output}, {input})',
    input=[q.elemu_TopControl_collection],
    output=[q.Flag_EleMuFromCR],
    scopes=["nnmm_topcontrol"],
)
EleMuPairCR_p4_corrected = Producer(
    name="EleMuPairCR_p4_corrected",
    call='physicsobject::TopControlEleMuPairP4({df}, {output}, {input})',
    input=[q.Muon_pt_corrected,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           q.Electron_pt_corrected,
           nanoAOD.Electron_eta, 
           nanoAOD.Electron_phi, 
           nanoAOD.Electron_mass,
           q.elemu_TopControl_collection],
    output=[q.elemu_p4_CR_corrected],
    scopes=["nnmm_topcontrol"],
)
EleMuPairCR_p4 = Producer(
    name="EleMuPairCR_p4",
    call='physicsobject::TopControlEleMuPairP4({df}, {output}, {input})',
    input=[q.Muon_pt_corrected,
           nanoAOD.Muon_eta, 
           nanoAOD.Muon_phi, 
           nanoAOD.Muon_mass,
           q.Electron_pt_corrected,
           nanoAOD.Electron_eta, 
           nanoAOD.Electron_phi, 
           nanoAOD.Electron_mass,
           q.elemu_TopControl_collection],
    output=[q.elemu_p4_CR],
    scopes=["nnmm_topcontrol"],
)
### cut flag
FilterFlag_EleMuFromCR = Producer(
    name="FilterFlag_EleMuFromCR",
    call='basefunctions::FilterThreshold({df}, {input}, {flag_EleMuFromTopCR}, "==", "EleMu From Top CR")',
    input=[q.Flag_EleMuFromCR],
    output=None,
    scopes=["nnmm_topcontrol"],
)
#####
elemuCR_pt_corrected = Producer(
    name="elemuCR_pt_corrected",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.elemu_p4_CR_corrected,
    ],
    output=[q.elemuCR_pt_corrected],
    scopes=["nnmm_topcontrol"],
)
elemuCR_pt = Producer(
    name="elemuCR_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.elemu_p4_CR,
    ],
    output=[q.elemuCR_pt],
    scopes=["nnmm_topcontrol"],
)
elemuCR_eta = Producer(
    name="elemuCR_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.elemu_p4_CR,
    ],
    output=[q.elemuCR_eta],
    scopes=["nnmm_topcontrol"],
)
elemuCR_phi = Producer(
    name="elemuCR_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.elemu_p4_CR,
    ],
    output=[q.elemuCR_phi],
    scopes=["nnmm_topcontrol"],
)
elemuCR_mass = Producer(
    name="elemuCR_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.elemu_p4_CR,
    ],
    output=[q.elemuCR_mass],
    scopes=["nnmm_topcontrol"],
)
Mu_Top_CR = Producer(
    name="Mu_Top_CR",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.elemu_TopControl_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_1],
    scopes=["nnmm_topcontrol"],
)
Mu_Top_CR_uncorrected = Producer(
    name="Mu_Top_CR_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.elemu_TopControl_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_1_uncorrected],
    scopes=["nnmm_topcontrol"],
)
Ele_Top_CR = Producer(
    name="Ele_Top_CR",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.elemu_TopControl_collection,
        q.Electron_pt_corrected,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.ele_Top_CR],
    scopes=["nnmm_topcontrol"],
)
Ele_Top_CR_uncorrected = Producer(
    name="Ele_Top_CR_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.elemu_TopControl_collection,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.ele_Top_CR_uncorrected],
    scopes=["nnmm_topcontrol"],
)
