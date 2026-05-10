from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
from code_generation.producer import ExtendedVectorProducer

MuonPtCorrection = Producer(
    name="MuonPtCorrection",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[
        nanoAOD.Muon_pt,
    ],
    output=[q.Muon_pt_uncorrected],
    scopes=["nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
    # scopes=["global"],
)
RenameMuonPt = Producer(
    name="RenameMuonPt",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[
        nanoAOD.Muon_pt,
    ],
    output=[q.Muon_pt_uncorrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    # scopes=["global"],
)

######################################## BSC and tuneP ################################################
MuonPtPreCorrectionData = Producer(
    name="MuonPtPreCorrectionData",
    call='scalefactor::muon::HighPtScaleData({df}, {input}, "{muon_momentum_BSC_variation}", "{muon_momentum_scale_variation}", {output}, "{muon_momentum_scale_corr_file}", "{muon_momentum_scale_name}")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_bsConstrainedPt,
        nanoAOD.Muon_tunepRelPt,
        nanoAOD.Muon_bsConstrainedPtErr,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_ptBSC_partial],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MuonPtPreCorrection = Producer(
    name="MuonPtPreCorrection",
    call='scalefactor::muon::HighPtScale({df}, {input}, "{muon_momentum_BSC_variation}", "{muon_momentum_scale_variation}", {output}, "{muon_momentum_scale_corr_file}", "{muon_momentum_scale_name}")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_bsConstrainedPt,
        nanoAOD.Muon_tunepRelPt,
        nanoAOD.Muon_bsConstrainedPtErr,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_ptBSC_partial],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MuonPtPreSmear = Producer(
    name="MuonPtPreSmear",
    call="scalefactor::muon::HighPtSmear({df}, {input}, {output}, {a_barrel}, {b_barrel}, {c_barrel}, {d_barrel}, {a_endcap}, {b_endcap}, {c_endcap}, {d_endcap})",
    input=[
        q.Muon_ptBSC_partial,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_nTrackerLayers,
        nanoAOD.event,
        nanoAOD.luminosityBlock,
    ],
    output=[q.Muon_ptBSC],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
######################################## KIT ################################################
Data_KIT_MuonPt_Scale = Producer(
    name="Data_KIT_MuonPt_Scale",
    call='scalefactor::muon::KIT_MuonPtScale({df}, {input}, {output}, "{KIT_sf_file}", "data")',
    input=[
        nanoAOD.Muon_pt,
        q.Muon_ptBSC_partial,
        nanoAOD.Muon_phi, 
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

MC_KIT_MuonPt_ScaleRes = Producer(
    name="MC_KIT_MuonPt_ScaleRes",
    call='scalefactor::muon::KIT_MuonPtRes({df}, {input}, {output}, "{KIT_sf_file}", "{KIT_Muon_Pt_Res_variation}", "mc", "{KIT_Muon_Pt_Scale_variation}")',
    input=[
        nanoAOD.Muon_pt,
        q.Muon_ptBSC,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_nTrackerLayers,
        nanoAOD.event,
        nanoAOD.luminosityBlock,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
####### pureBSC #########
Data_KIT_MuonPt_Scale_pureBSC = Producer(
    name="Data_KIT_MuonPt_Scale_pureBSC",
    call='scalefactor::muon::KIT_MuonPtScale({df}, {input}, {output}, "{KIT_sf_file}", "data")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_bsConstrainedPt,
        nanoAOD.Muon_phi, 
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_pureBSC],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

MC_KIT_MuonPt_ScaleRes_pureBSC = Producer(
    name="MC_KIT_MuonPt_ScaleRes_pureBSC",
    call='scalefactor::muon::KIT_MuonPtRes({df}, {input}, {output}, "{KIT_sf_file}", "{KIT_Muon_Pt_Res_variation}", "mc", "{KIT_Muon_Pt_Scale_variation}")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_bsConstrainedPt,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_nTrackerLayers,
        nanoAOD.event,
        nanoAOD.luminosityBlock,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_pureBSC],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
##################### raw #############################
Data_KIT_MuonPt_Scale_raw = Producer(
    name="Data_KIT_MuonPt_Scale_raw",
    call='scalefactor::muon::KIT_MuonPtScale({df}, {input}, {output}, "{KIT_sf_file}", "data")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_phi, 
        nanoAOD.Muon_eta,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_raw],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

MC_KIT_MuonPt_ScaleRes_raw = Producer(
    name="MC_KIT_MuonPt_ScaleRes_raw",
    call='scalefactor::muon::KIT_MuonPtRes({df}, {input}, {output}, "{KIT_sf_file}", "{KIT_Muon_Pt_Res_variation}", "mc", "{KIT_Muon_Pt_Scale_variation}")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_nTrackerLayers,
        nanoAOD.event,
        nanoAOD.luminosityBlock,
        nanoAOD.Muon_charge,
    ],
    output=[q.Muon_pt_corrected_raw],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
################################ KIT End ####################################################
######################################## Rochester ################################################
# Data_Rochester_MuonPt_ScaleRes = Producer(
#     name="Data_Rochester_MuonPt_ScaleRes",
#     call='scalefactor::muon::Rochester_MuonPtRes({df}, {input}, {output}, "{Rochester_sf_file}", "{Rochester_Muon_Pt_Res_variation}", "data")',
#     input=[
#         nanoAOD.Muon_pt,
#         q.Muon_ptBSC,
#         nanoAOD.Muon_indexToGen,
#         nanoAOD.GenParticle_pt,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_charge,
#         nanoAOD.Muon_nTrackerLayers,
#         nanoAOD.event,
#         nanoAOD.luminosityBlock,
#     ],
#     output=[q.Muon_pt_corrected],
#     scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
#             "nnmm_dycontrol","nnmm_topcontrol",
#             "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
#             "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
# )
# MC_Rochester_MuonPt_ScaleRes = Producer(
#     name="MC_Rochester_MuonPt_ScaleRes",
#     call='scalefactor::muon::Rochester_MuonPtRes({df}, {input}, {output}, "{Rochester_sf_file}", "{Rochester_Muon_Pt_Res_variation}", "mc")',
#     input=[
#         nanoAOD.Muon_pt,
#         q.Muon_ptBSC,
#         nanoAOD.Muon_indexToGen,
#         nanoAOD.GenParticle_pt,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_charge,
#         nanoAOD.Muon_nTrackerLayers,
#         nanoAOD.event,
#         nanoAOD.luminosityBlock,
#     ],
#     output=[q.Muon_pt_corrected],
#     scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
#             "nnmm_dycontrol","nnmm_topcontrol",
#             "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
#             "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
# )
################################ Rochester End ####################################################
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
