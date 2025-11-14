from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
from code_generation.producer import ExtendedVectorProducer

MuonPtCorrection = Producer(
    name="MuonPtCorrection",
    call='scalefactor::muon::Muonmomentumscale({df}, {input}, "{muon_momentum_scale_variation}", {output}, "{muon_momentum_scale_corr_file}", "{muon_momentum_scale_name}")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_woKIT],
    scopes=["nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
    # scopes=["global"],
)
RenameMuonPt = Producer(
    name="RenameMuonPt",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[
        nanoAOD.Muon_pt,
    ],
    output=[q.Muon_pt_corrected_woKIT],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    # scopes=["global"],
)
Data_KIT_MuonPt_Scale = Producer(
    name="Data_KIT_MuonPt_Scale",
    call='scalefactor::muon::KIT_MuonPtScale({df}, {input}, {output}, "{KIT_sf_file}", "data", " ")',
    input=[
        q.Muon_pt_corrected_woKIT,
        nanoAOD.Muon_phi, 
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MC_KIT_MuonPt_Scale_no2l = Producer(
    name="Data_KIT_MuonPt_Scale_no2l",
    call='scalefactor::muon::KIT_MuonPtScale({df}, {input}, {output}, "{KIT_sf_file}", "mc", "3l_4l")',
    input=[
        q.Muon_pt_corrected_woKIT,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_scale],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MC_KIT_MuonPt_Scale_2l = Producer(
    name="Data_KIT_MuonPt_Scale_2l",
    call='scalefactor::muon::KIT_MuonPtScale({df}, {input}, {output}, "{KIT_sf_file}", "mc", "2l")',
    input=[
        q.Muon_pt_corrected_woKIT,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_scale],
    scopes=["nnmm", "fjmm", "fjmm_cr"],
)
MC_KIT_MuonPt_Res = Producer(
    name="MC_KIT_MuonPt_Res",
    call='scalefactor::muon::KIT_MuonPtRes({df}, {input}, {output}, "{KIT_sf_file}")',
    input=[
        q.Muon_pt_corrected_scale,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_nTrackerLayers,
        nanoAOD.event,
        nanoAOD.luminosityBlock,
    ],
    output=[q.Muon_pt_corrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MC_KIT_MuonPt_Scale_Var_no2l = Producer(
    name="MC_KIT_MuonPt_Scale_Var_no2l",
    call='scalefactor::muon::KIT_MuonPtScale_Var({df}, {input}, {output}, "{KIT_sf_file}", "{KIT_Muon_Pt_Scale_variation}", "3l_4l")',
    input=[
        q.Muon_pt_corrected,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_scale],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MC_KIT_MuonPt_Scale_Var_2l = Producer(
    name="MC_KIT_MuonPt_Scale_Var_2l",
    call='scalefactor::muon::KIT_MuonPtScale_Var({df}, {input}, {output}, "{KIT_sf_file}", "{KIT_Muon_Pt_Scale_variation}", "2l")',
    input=[
        q.Muon_pt_corrected,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_scale],
    scopes=["nnmm", "fjmm", "fjmm_cr"],
)
MC_KIT_MuonPt_Res_Var = Producer(
    name="MC_KIT_MuonPt_Res_Var",
    call='scalefactor::muon::KIT_MuonPtRes_Var({df}, {input}, {output}, "{KIT_sf_file}", "{KIT_Muon_Pt_Res_variation}")',
    input=[
        q.Muon_pt_corrected_scale,
        q.Muon_pt_corrected,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
    ],
    output=[q.Muon_pt_corrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

#####################################################################################
Mu1_H_corrected = Producer(
    name="Mu1_H_corrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.dimuon_HiggsCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_H_corrected],
    scopes=["nnmm","fjmm"],
)
Mu2_H_corrected = Producer(
    name="Mu2_H_corrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.dimuon_HiggsCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_H_corrected],
    scopes=["nnmm","fjmm"],
)
Mu1_Z_CR_corrected = Producer(
    name="Mu1_Z_CR_corrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.dimuon_ZControl_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_Z_CR_corrected],
    scopes=["fjmm_cr"],
)
Mu2_Z_CR_corrected = Producer(
    name="Mu2_Z_CR_corrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.dimuon_ZControl_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_Z_CR_corrected],
    scopes=["fjmm_cr"],
)
Mu_Top_CR_corrected = Producer(
    name="Mu_Top_CR_corrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.elemu_TopControl_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_Top_CR_corrected],
    scopes=["nnmm_topcontrol"],
)
