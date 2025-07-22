from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
# write by botao

BuildMetVector = Producer(
    name="BuildMetVector",
    call="lorentzvectors::buildMet({df}, {input}, {output})",
    input=[
        nanoAOD.MET_pt,
        nanoAOD.MET_phi,
    ],
    output=[q.met_p4_uncorrected],
    scopes=["global"],
)
BuildPFMetVector = Producer(
    name="BuildPFMetVector",
    call="lorentzvectors::buildMet({df}, {input}, {output})",
    input=[
        nanoAOD.PFMET_pt,
        nanoAOD.PFMET_phi,
    ],
    output=[q.pfmet_p4],
    scopes=["global"],
)
BuildGenMetVector = Producer(
    name="BuildGenMetVector",
    call="lorentzvectors::buildMet({df}, {input}, {output})",
    input=[
        nanoAOD.GenMET_pt,
        nanoAOD.GenMET_phi,
    ],
    output=[q.genmet_p4],
    scopes=["global"],
)

MetSumEt = Producer(
    name="MetSumEt",
    call="basefunctions::rename<float>({df}, {input}, {output})",
    input=[
        nanoAOD.MET_sumEt,
    ],
    output=[q.metSumEt],
    scopes=["global"],
)

MetPt_uncorrected = Producer(
    name="MetPt_uncorrected",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.met_p4_uncorrected],
    output=[q.met_uncorrected],
    scopes=["global"],
)
MetPhi_uncorrected = Producer(
    name="MetPhi_uncorrected",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.met_p4_uncorrected],
    output=[q.metphi_uncorrected],
    scopes=["global"],
)
CalculateGenBosonVector = Producer(
    name="calculateGenBosonVector",
    call="met::calculateGenBosonVector({df}, {input}, {output}, {is_data})",
    input=[
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_statusFlags,
    ],
    output=[q.recoil_genboson_p4_vec],
    scopes=["global"],
)

MetBasics = ProducerGroup(
    name="MetBasics",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[
        BuildPFMetVector,
        BuildMetVector,
        # MetPt_uncorrected,
        # MetPhi_uncorrected,
        MetSumEt,
        CalculateGenBosonVector,
        # BuildGenMetVector,
    ],
)

### after apply the highPt muon's correction, need to change the corrected p4
# PropagateLeptonsToMet = Producer(
#     name="PropagateLeptonsToMet",
#     call="met::propagateLeptonsToMet({df}, {input}, {output}, {propagateLeptons})",
#     input=[q.met_p4_uncorrected, q.muon_p4_1, q.muon_p4_2, q.extra_lep_p4, q.muon_p4_1, q.muon_p4_2, q.extra_lep_p4],
#     output=[q.met_p4_leptoncorrected],
#     scopes=["e2m","m2m",
#             "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
#             "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
# )

PropagateFourLeptonsToMet = Producer(
    name="PropagateFourLeptonsToMet",
    call="met::propagateLeptonsToMet({df}, {input}, {output}, {propagateLeptons})",
    input=[q.met_p4_uncorrected, 
           q.muon_leadingp4_H, q.muon_subleadingp4_H, q.lepton_leadingp4_Z, q.lepton_subleadingp4_Z, 
           q.muon_leadingp4_H, q.muon_subleadingp4_H, q.lepton_leadingp4_Z, q.lepton_subleadingp4_Z],
    output=[q.met_p4_leptoncorrected],
    scopes=["eemm","eemm_cr","mmmm","mmmm_cr"],
)
PropagateThreeLeptonsToMet_e2m = Producer(
    name="PropagateThreeLeptonsToMet",
    call="met::propagateLeptonsToMet({df}, {input}, {output}, {propagateLeptons})",
    input=[q.met_p4_uncorrected, q.muon_p4_1, q.muon_p4_2, q.extra_lep_p4, q.muon_p4_1, q.muon_p4_2, q.extra_lep_p4],
    output=[q.met_p4_leptoncorrected],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

PropagateThreeLeptonsToMet_m2m = Producer(
    name="PropagateThreeLeptonsToMet",
    call="met::propagateLeptonsToMet({df}, {input}, {output}, {propagateLeptons})",
    input=[q.met_p4_uncorrected, q.muon_p4_1, q.muon_p4_2, q.muon_p4_3, q.muon_p4_1, q.muon_p4_2, q.muon_p4_3],
    output=[q.met_p4_leptoncorrected],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)

PropagateTwoLeptonsToMet = Producer(
    name="PropagateTwoLeptonsToMet",
    call="met::propagateLeptonsToMet({df}, {input}, {output}, {propagateLeptons})",
    input=[q.met_p4_uncorrected, q.muon_p4_1, q.muon_p4_2, q.muon_p4_1, q.muon_p4_2],
    output=[q.met_p4_leptoncorrected],
    scopes=["fjmm_cr"],
)
PropagateTwoLeptonsToMet_TopCR = Producer(
    name="PropagateTwoLeptonsToMet_TopCR",
    call="met::propagateLeptonsToMet({df}, {input}, {output}, {propagateLeptons})",
    input=[q.met_p4_uncorrected, q.ele_Top_CR, q.muon_p4_1, q.ele_Top_CR, q.muon_Top_CR_corrected],
    output=[q.met_p4_leptoncorrected],
    scopes=["nnmm_topcontrol"],
)

PropagateTwoLeptonsToMet_corrected = Producer(
    name="PropagateTwoLeptonsToMet_corrected",
    call="met::propagateLeptonsToMet({df}, {input}, {output}, {propagateLeptons})",
    input=[q.met_p4_uncorrected, q.muon_leadingp4_H, q.muon_subleadingp4_H, q.muon_leadingp4_H_corrected, q.muon_subleadingp4_H_corrected],
    output=[q.met_p4_leptoncorrected],
    scopes=["nnmm","fjmm"],
)

PropagateJetsToMet = Producer(
    name="PropagateJetsToMet",
    call="met::propagateJetsToMet({df}, {input}, {output}, {propagateJets}, {min_jetpt_met_propagation})",
    input=[
        q.met_p4_leptoncorrected,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.good_jets_mask,
        q.Jet_mass_corrected,
        nanoAOD.Jet_pt,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        nanoAOD.Jet_mass,
    ],
    output=[q.met_p4_jetcorrected],
    scopes=["e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

MetPt = Producer(
    name="MetPt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.met_p4_jetcorrected],
    output=[q.met_pt_corrected],
    scopes=["e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MetPhi = Producer(
    name="MetPhi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.met_p4_jetcorrected],
    output=[q.met_phi_corrected],
    scopes=["e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

MetCorrections = ProducerGroup(
    name="MetCorrections",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers={
        "e2m": [
            PropagateThreeLeptonsToMet_e2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "e2m_dyfakeinge_regionb": [
            PropagateThreeLeptonsToMet_e2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "e2m_dyfakeinge_regionc": [
            PropagateThreeLeptonsToMet_e2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "e2m_dyfakeinge_regiond": [
            PropagateThreeLeptonsToMet_e2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "m2m": [
            PropagateThreeLeptonsToMet_m2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "m2m_dyfakeingmu_regionb": [
            PropagateThreeLeptonsToMet_m2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "m2m_dyfakeingmu_regionc": [
            PropagateThreeLeptonsToMet_m2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "m2m_dyfakeingmu_regiond": [
            PropagateThreeLeptonsToMet_m2m,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "eemm": [
            PropagateFourLeptonsToMet,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "eemm_cr": [
            PropagateFourLeptonsToMet,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "mmmm": [
            PropagateFourLeptonsToMet,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "mmmm_cr": [
            PropagateFourLeptonsToMet,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "nnmm": [
            PropagateTwoLeptonsToMet_corrected,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "fjmm": [
            PropagateTwoLeptonsToMet_corrected,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "fjmm_cr": [
            PropagateTwoLeptonsToMet,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ],
        "nnmm_topcontrol": [
            PropagateTwoLeptonsToMet_TopCR,
            PropagateJetsToMet,
            MetPt,
            MetPhi,
        ]
    },
)

Rename_PropagateThreeLeptons = Producer(
    name="Rename_PropagateThreeLeptons",
    call='physicsobject::renameMET({df}, {output}, {input})',
    input=[
        q.met_p4_uncorrected,
    ],
    output=[q.met_p4_leptoncorrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
Rename_PropagateJetsToMet = Producer(
    name="Rename_PropagateJetsToMet",
    call='physicsobject::renameMET({df}, {output}, {input})',
    input=[
        q.met_p4_leptoncorrected,
    ],
    output=[q.met_p4_jetcorrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

RenameMetCorrections = ProducerGroup(
    name="RenameMetCorrections",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers={
        Rename_PropagateThreeLeptons,
        Rename_PropagateJetsToMet,
        MetPt,
        MetPhi,
    },
)
