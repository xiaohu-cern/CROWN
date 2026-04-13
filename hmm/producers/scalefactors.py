from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
from code_generation.producer import ExtendedVectorProducer


############################
# Muon ID, ISO SF
# The readout is done via correctionlib
############################

Muon_1_ID_SF_RooWorkspace = Producer(
    name="MuonID_SF_RooWorkspace",
    call='scalefactor::muon::id_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_id_name}", "{muon_sf_id_args}")',
    input=[q.pt_1, q.eta_1],
    output=[q.id_wgt_mu_1],
    scopes=["e2m","m2m", "eemm","mmmm"],
)
Muon_1_Iso_SF_RooWorkspace = Producer(
    name="MuonIso_SF_RooWorkspace",
    call='scalefactor::muon::iso_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_iso_name}", "{muon_sf_iso_args}")',
    input=[q.pt_1, q.eta_1, q.iso_1],
    output=[q.iso_wgt_mu_1],
    scopes=["e2m","m2m", "eemm","mmmm"],
)
Muon_1_ID_SF = Producer(
    name="MuonID_SF",
    call='scalefactor::muon::id({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.id_wgt_mu_1],
    scopes=["e2m","m2m", "eemm","mmmm"],
)
Muon_1_Iso_SF = Producer(
    name="MuonIso_SF",
    call='scalefactor::muon::iso({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.iso_wgt_mu_1],
    scopes=["e2m","m2m", "eemm","mmmm"],
)
Muon_2_ID_SF_RooWorkspace = Producer(
    name="MuonID_SF_RooWorkspace",
    call='scalefactor::muon::id_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_id_name}", "{muon_sf_id_args}")',
    input=[q.pt_2, q.eta_2],
    output=[q.id_wgt_mu_2],
    scopes=["e2m","m2m", "eemm","mmmm"],
)
Muon_2_Iso_SF_RooWorkspace = Producer(
    name="MuonIso_SF_RooWorkspace",
    call='scalefactor::muon::iso_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_iso_name}", "{muon_sf_iso_args}")',
    input=[q.pt_2, q.eta_2, q.iso_2],
    output=[q.iso_wgt_mu_2],
    scopes=["e2m","m2m", "eemm","mmmm"],
)
Muon_2_ID_SF = Producer(
    name="MuonID_SF",
    call='scalefactor::muon::id({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.id_wgt_mu_2],
    scopes=["e2m","m2m", "eemm","mmmm"],
)
Muon_2_Iso_SF = Producer(
    name="MuonIso_SF",
    call='scalefactor::muon::iso({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.iso_wgt_mu_2],
    scopes=["e2m","m2m", "eemm","mmmm"],
)

######### vhmm SF #########
###########################
######### muon 1 ##########
###########################
Muon_1_ID_SF_vhmm = Producer(
    name="Muon_1_ID_SF_vhmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_1],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_1_ID_SF_vhmm_below15 = Producer(
    name="Muon_1_ID_SF_vhmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_1_below15],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_1_ID_SF_vhmm_above200 = Producer(
    name="Muon_1_ID_SF_vhmm_above200",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_1_above200],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
#############################
###### Muon mvaTTH SF #######
#############################
Muon_1_mvaTTH_SF_vhmm = Producer(
    name="Muon_1_mvaTTH_SF_vhmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_mvatth_1],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_1_mvaTTH_SF_vhmm_corrected = Producer(
    name="Muon_1_mvaTTH_SF_vhmm_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_mvatth_1],
    scopes=["nnmm","fjmm"],
)
Muon_1_mvaTTH_SF_vhmm_TopCR_corrected = Producer(
    name="Muon_1_mvaTTH_SF_vhmm_TopCR_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.id_wgt_mu_mvatth_1],
    scopes=["nnmm_topcontrol"],
)

Muon_1_dxydz3dsip_SF_vhmm = Producer(
    name="Muon_1_dxydz3dsip_SF_vhmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_1],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_1_dxydz3dsip_SF_vhmm_corrected = Producer(
    name="Muon_1_dxydz3dsip_SF_vhmm_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_1],
    scopes=["nnmm","fjmm"],
)
Muon_1_dxydz3dsip_SF_vhmm_TopCR_corrected = Producer(
    name="Muon_1_dxydz3dsip_SF_vhmm_TopCR_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_1],
    scopes=["nnmm_topcontrol"],
)
#################################
###### End Muon mvaTTH SF #######
#################################
Muon_1_ID_SF_vhmm_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_1],
    scopes=["nnmm","fjmm"],
)
Muon_1_ID_SF_vhmm_below15_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_below15_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_1_below15],
    scopes=["nnmm","fjmm"],
)
Muon_1_ID_SF_vhmm_above200_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_above200_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.id_wgt_mu_1_above200],
    scopes=["nnmm","fjmm"],
)

Muon_1_ID_SF_vhmm_TopCR_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_TopCR_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.id_wgt_mu_1],
    scopes=["nnmm_topcontrol"],
)
Muon_1_ID_SF_vhmm_TopCR_below15_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_TopCR_below15_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.id_wgt_mu_1_below15],
    scopes=["nnmm_topcontrol"],
)
Muon_1_ID_SF_vhmm_TopCR_above200_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_TopCR_above200_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.id_wgt_mu_1_above200],
    scopes=["nnmm_topcontrol"],
)

###########################
######### muon 2 ##########
###########################
Muon_2_ID_SF_vhmm = Producer(
    name="Muon_2_ID_SF_vhmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_2],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_2_ID_SF_vhmm_below15 = Producer(
    name="Muon_2_ID_SF_vhmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_2_below15],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_2_ID_SF_vhmm_above200 = Producer(
    name="Muon_2_ID_SF_vhmm_above200",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_2_above200],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
#############################
###### Muon mvaTTH SF #######
#############################
Muon_2_mvaTTH_SF_vhmm = Producer(
    name="Muon_2_mvaTTH_SF_vhmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_mvatth_2],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_2_mvaTTH_SF_vhmm_corrected = Producer(
    name="Muon_2_mvaTTH_SF_vhmm_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_mvatth_2],
    scopes=["nnmm","fjmm"],
)

Muon_2_dxydz3dsip_SF_vhmm = Producer(
    name="Muon_2_dxydz3dsip_SF_vhmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_2],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_2_dxydz3dsip_SF_vhmm_corrected = Producer(
    name="Muon_2_dxydz3dsip_SF_vhmm_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_2],
    scopes=["nnmm","fjmm"],
)
#################################
###### End Muon mvaTTH SF #######
#################################
Muon_2_ID_SF_vhmm_corrected = Producer(
    name="Muon_2_ID_SF_vhmm_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_2],
    scopes=["nnmm","fjmm"],
)
Muon_2_ID_SF_vhmm_below15_corrected = Producer(
    name="Muon_2_ID_SF_vhmm_below15_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_2_below15],
    scopes=["nnmm","fjmm"],
)
Muon_2_ID_SF_vhmm_above200_corrected = Producer(
    name="Muon_2_ID_SF_vhmm_above200_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.id_wgt_mu_2_above200],
    scopes=["nnmm","fjmm"],
)

###########################
######### muon 3 ##########
###########################
Muon_3_ID_SF_vhmm_m2m = Producer(
    name="Muon_3_ID_SF_vhmm_m2m",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_mu_3],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_ID_SF_vhmm_m2m_below15 = Producer(
    name="Muon_3_ID_SF_vhmm_m2m_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_mu_3_below15],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_ID_SF_vhmm_m2m_above200 = Producer(
    name="Muon_3_ID_SF_vhmm_m2m_above200",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_mu_3_above200],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
#############################
###### Muon mvaTTH SF #######
#############################
Muon_3_mvaTTH_SF_vhmm_m2m = Producer(
    name="Muon_3_mvaTTH_SF_vhmm_m2m",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_mu_mvatth_3],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_mvaTTH_SF_vhmm_mmmm = Producer(
    name="Muon_3_mvaTTH_SF_vhmm_mmmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_mvatth_3],
    scopes=["mmmm","mmmm_cr"],
)

Muon_3_dxydz3dsip_SF_vhmm_m2m = Producer(
    name="Muon_3_dxydz3dsip_SF_vhmm_m2m",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_mu_dxydz3dsip_3],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_dxydz3dsip_SF_vhmm_mmmm = Producer(
    name="Muon_3_dxydz3dsip_SF_vhmm_mmmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_3],
    scopes=["mmmm","mmmm_cr"],
)
#################################
###### End Muon mvaTTH SF #######
#################################
Muon_3_ID_SF_vhmm_mmmm = Producer(
    name="Muon_3_ID_SF_vhmm_mmmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_3],
    scopes=["mmmm","mmmm_cr"],
)
Muon_3_ID_SF_vhmm_mmmm_below15 = Producer(
    name="Muon_3_ID_SF_vhmm_mmmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_3_below15],
    scopes=["mmmm","mmmm_cr"],
)
Muon_3_ID_SF_vhmm_mmmm_above200 = Producer(
    name="Muon_3_ID_SF_vhmm_mmmm_above200",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_3_above200],
    scopes=["mmmm","mmmm_cr"],
)

###########################
######### muon 4 ##########
###########################
Muon_4_ID_SF_vhmm_mmmm = Producer(
    name="Muon_4_ID_SF_vhmm_mmmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_4],
    scopes=["mmmm","mmmm_cr"],
)
Muon_4_ID_SF_vhmm_mmmm_below15 = Producer(
    name="Muon_4_ID_SF_vhmm_mmmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_4_below15],
    scopes=["mmmm","mmmm_cr"],
)
Muon_4_ID_SF_vhmm_mmmm_above200 = Producer(
    name="Muon_4_ID_SF_vhmm_mmmm_above200",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_4_above200],
    scopes=["mmmm","mmmm_cr"],
)
#############################
###### Muon mvaTTH SF #######
#############################
Muon_4_mvaTTH_SF_vhmm_mmmm = Producer(
    name="Muon_4_mvaTTH_SF_vhmm_mmmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_mvatth_4],
    scopes=["mmmm","mmmm_cr"],
)

Muon_4_dxydz3dsip_SF_vhmm_mmmm = Producer(
    name="Muon_4_dxydz3dsip_SF_vhmm_mmmm",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_4],
    scopes=["mmmm","mmmm_cr"],
)
#################################
###### End Muon mvaTTH SF #######
#################################

###########################
######### muon 1 ##########
###########################
Muon_1_ID_SF_vhmm_regionbd = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_Z_CR],
    output=[q.id_wgt_mu_1],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_1_ID_SF_vhmm_regionbd_below15 = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_Z_CR],
    output=[q.id_wgt_mu_1_below15],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_1_ID_SF_vhmm_regionbd_above200 = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd_above200",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_leadingp4_Z_CR],
    output=[q.id_wgt_mu_1_above200],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
#############################
###### Muon mvaTTH SF #######
#############################
Muon_1_mvaTTH_SF_vhmm_regionbd = Producer(
    name="Muon_1_mvaTTH_SF_vhmm_regionbd",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_leadingp4_Z_CR],
    output=[q.id_wgt_mu_mvatth_1],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_1_mvaTTH_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_1_mvaTTH_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_mvatth_1],
    scopes=["fjmm_cr"],
)

Muon_1_dxydz3dsip_SF_vhmm_regionbd = Producer(
    name="Muon_1_dxydz3dsip_SF_vhmm_regionbd",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_leadingp4_Z_CR],
    output=[q.id_wgt_mu_dxydz3dsip_1],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_1_dxydz3dsip_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_1_dxydz3dsip_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_1],
    scopes=["fjmm_cr"],
)
#################################
###### End Muon mvaTTH SF #######
#################################
Muon_1_ID_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_1],
    scopes=["fjmm_cr"],
)
Muon_1_ID_SF_vhmm_regionbd_below15_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd_below15_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_1_below15],
    scopes=["fjmm_cr"],
)
Muon_1_ID_SF_vhmm_regionbd_above200_corrected = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd_above200_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_1_above200],
    scopes=["fjmm_cr"],
)

###########################
######### muon 2 ##########
###########################
Muon_2_ID_SF_vhmm_regionbd = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_Z_CR],
    output=[q.id_wgt_mu_2],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_2_ID_SF_vhmm_regionbd_below15 = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_Z_CR],
    output=[q.id_wgt_mu_2_below15],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_2_ID_SF_vhmm_regionbd_above200 = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd_above200",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_Z_CR],
    output=[q.id_wgt_mu_2_above200],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
#############################
###### Muon mvaTTH SF #######
#############################
Muon_2_mvaTTH_SF_vhmm_regionbd = Producer(
    name="Muon_2_mvaTTH_SF_vhmm_regionbd",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_subleadingp4_Z_CR],
    output=[q.id_wgt_mu_mvatth_2],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_2_mvaTTH_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_2_mvaTTH_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_mvaTTH}", "{muon_id_sf_name_mvaTTH}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_mvatth_2],
    scopes=["fjmm_cr"],
)

Muon_2_dxydz3dsip_SF_vhmm_regionbd = Producer(
    name="Muon_2_dxydz3dsip_SF_vhmm_regionbd",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_subleadingp4_Z_CR],
    output=[q.id_wgt_mu_dxydz3dsip_2],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
)
Muon_2_dxydz3dsip_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_2_dxydz3dsip_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::mvatth_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file_dxydz3dsip}", "{muon_id_sf_name_dxydz3dsip}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_dxydz3dsip_2],
    scopes=["fjmm_cr"],
)
#################################
###### End Muon mvaTTH SF #######
#################################

Muon_2_ID_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_2],
    scopes=["fjmm_cr"],
)
Muon_2_ID_SF_vhmm_regionbd_below15_corrected = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd_below15_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_2_below15],
    scopes=["fjmm_cr"],
)
Muon_2_ID_SF_vhmm_regionbd_above200_corrected = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd_above200_corrected",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_id_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.id_wgt_mu_2_above200],
    scopes=["fjmm_cr"],
)

#################################
############ Iso SF #############
#################################
###########################
######### muon 1 ##########
###########################
Muon_1_Iso_SF_vhmm = Producer(
    name="Muon_1_Iso_SF_vhmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_1],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_1_Iso_SF_vhmm_above200 = Producer(
    name="Muon_1_Iso_SF_vhmm_above200",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_1_above200],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_1_Iso_SF_vhmm_corrected = Producer(
    name="Muon_1_Iso_SF_vhmm_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_1],
    scopes=["nnmm","fjmm"],
)
Muon_1_Iso_SF_vhmm_above200_corrected = Producer(
    name="Muon_1_Iso_SF_vhmm_above200_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_1_above200],
    scopes=["nnmm","fjmm"],
)
###### for top CR
Muon_1_Iso_SF_vhmm_TopCR_corrected = Producer(
    name="Muon_1_Iso_SF_vhmm_TopCR_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.iso_wgt_mu_1],
    scopes=["nnmm_topcontrol"],
)
Muon_1_Iso_SF_vhmm_TopCR_above200_corrected = Producer(
    name="Muon_1_Iso_SF_vhmm_TopCR_above200_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.iso_wgt_mu_1_above200],
    scopes=["nnmm_topcontrol"],
)

###########################
######### muon 2 ##########
###########################
Muon_2_Iso_SF_vhmm = Producer(
    name="Muon_2_Iso_SF_vhmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_2],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)
Muon_2_Iso_SF_vhmm_above200 = Producer(
    name="Muon_2_Iso_SF_vhmm_above200",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_2_above200],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","eemm_cr","mmmm","mmmm_cr"],
)

Muon_2_Iso_SF_vhmm_corrected = Producer(
    name="Muon_2_Iso_SF_vhmm_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_2],
    scopes=["nnmm","fjmm"],
)
Muon_2_Iso_SF_vhmm_above200_corrected = Producer(
    name="Muon_2_Iso_SF_vhmm_above200_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.iso_wgt_mu_2_above200],
    scopes=["nnmm","fjmm"],
)

###########################
######### muon 3 ##########
###########################
Muon_3_Iso_SF_vhmm_m2m = Producer(
    name="Muon_3_Iso_SF_vhmm_m2m",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.iso_wgt_mu_3],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_Iso_SF_vhmm_m2m_above200 = Producer(
    name="Muon_3_Iso_SF_vhmm_m2m_above200",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.iso_wgt_mu_3_above200],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)


Muon_3_Iso_SF_vhmm_mmmm = Producer(
    name="Muon_3_Iso_SF_vhmm_mmmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.iso_wgt_mu_3],
    scopes=["mmmm","mmmm_cr"],
)
Muon_3_Iso_SF_vhmm_mmmm_above200 = Producer(
    name="Muon_3_Iso_SF_vhmm_mmmm_above200",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.iso_wgt_mu_3_above200],
    scopes=["mmmm","mmmm_cr"],
)

###########################
######### muon 4 ##########
###########################
Muon_4_Iso_SF_vhmm_mmmm = Producer(
    name="Muon_4_Iso_SF_vhmm_mmmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.iso_wgt_mu_4],
    scopes=["mmmm","mmmm_cr"],
)
Muon_4_Iso_SF_vhmm_mmmm_above200 = Producer(
    name="Muon_4_Iso_SF_vhmm_mmmm_above200",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.iso_wgt_mu_4_above200],
    scopes=["mmmm","mmmm_cr"],
)

###########################
######### muon 1 ##########
###########################
Muon_1_Iso_SF_vhmm_regionbd = Producer(
    name="Muon_1_Iso_SF_vhmm_regionbd",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_leadingp4_Z_CR],
    output=[q.iso_wgt_mu_1],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_1_Iso_SF_vhmm_regionbd_above200 = Producer(
    name="Muon_1_Iso_SF_vhmm_regionbd_above200",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_leadingp4_Z_CR],
    output=[q.iso_wgt_mu_1_above200],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_1_Iso_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_1_Iso_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.iso_wgt_mu_1],
    scopes=["fjmm_cr"],
)
Muon_1_Iso_SF_vhmm_regionbd_above200_corrected = Producer(
    name="Muon_1_Iso_SF_vhmm_regionbd_above200_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.iso_wgt_mu_1_above200],
    scopes=["fjmm_cr"],
)

###########################
######### muon 2 ##########
###########################
Muon_2_Iso_SF_vhmm_regionbd = Producer(
    name="Muon_2_Iso_SF_vhmm_regionbd",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_subleadingp4_Z_CR],
    output=[q.iso_wgt_mu_2],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_2_Iso_SF_vhmm_regionbd_above200 = Producer(
    name="Muon_2_Iso_SF_vhmm_regionbd_above200",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_Z_CR],
    output=[q.iso_wgt_mu_2_above200],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_2_Iso_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_2_Iso_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.iso_wgt_mu_2],
    scopes=["fjmm_cr"],
)
Muon_2_Iso_SF_vhmm_regionbd_above200_corrected = Producer(
    name="Muon_2_Iso_SF_vhmm_regionbd_above200_corrected",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_iso_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.iso_wgt_mu_2_above200],
    scopes=["fjmm_cr"],
)


# Muon_1_Iso_SF_vhmm_below15 = Producer(
#     name="Muon_1_Iso_SF_vhmm_below15",
#     call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
#     input=[q.muon_leadingp4_H],
#     output=[q.iso_wgt_mu_1_below15],
#     scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
# )
# Muon_1_Iso_SF_vhmm_regionbd_below15 = Producer(
#     name="Muon_1_Iso_SF_vhmm_regionbd_below15",
#     call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
#     input=[q.muon_p4_1],
#     output=[q.iso_wgt_mu_1_below15],
#     scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
# )
# Muon_2_Iso_SF_vhmm_below15 = Producer(
#     name="Muon_2_Iso_SF_vhmm_below15",
#     call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
#     input=[q.muon_subleadingp4_H],
#     output=[q.iso_wgt_mu_2_below15],
#     scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
# )
# Muon_2_Iso_SF_vhmm_regionbd_below15 = Producer(
#     name="Muon_2_Iso_SF_vhmm_regionbd_below15",
#     call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
#     input=[q.muon_p4_2],
#     output=[q.iso_wgt_mu_2_below15],
#     scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
# )
# Muon_3_Iso_SF_vhmm_m2m_below15 = Producer(
#     name="Muon_3_Iso_SF_vhmm_m2m_below15",
#     call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
#     input=[q.extra_lep_p4_noCorr],
#     output=[q.iso_wgt_mu_3_below15],
#     scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
# )
# Muon_3_Iso_SF_vhmm_mmmm_below15 = Producer(
#     name="Muon_3_Iso_SF_vhmm_mmmm_below15",
#     call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
#     input=[q.lepton_leadingp4_Z],
#     output=[q.iso_wgt_mu_3_below15],
#     scopes=["mmmm"],
# )
# Muon_4_Iso_SF_vhmm_mmmm_below15 = Producer(
#     name="Muon_4_Iso_SF_vhmm_mmmm_below15",
#     call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
#     input=[q.lepton_subleadingp4_Z],
#     output=[q.iso_wgt_mu_4_below15],
#     scopes=["mmmm"],
# )
MuonID_SF = ProducerGroup(
    name="MuonID_SF",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
    subproducers={
        "e2m": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
        ],
        "e2m_dyfakeinge_regionb": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            # above 200
            Muon_1_ID_SF_vhmm_regionbd_above200,
            Muon_2_ID_SF_vhmm_regionbd_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_regionbd,
            Muon_2_mvaTTH_SF_vhmm_regionbd,
            Muon_1_dxydz3dsip_SF_vhmm_regionbd,
            Muon_2_dxydz3dsip_SF_vhmm_regionbd,
        ],
        "e2m_dyfakeinge_regionc": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
        ],
        "e2m_dyfakeinge_regiond": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            # above 200
            Muon_1_ID_SF_vhmm_regionbd_above200,
            Muon_2_ID_SF_vhmm_regionbd_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_regionbd,
            Muon_2_mvaTTH_SF_vhmm_regionbd,
            Muon_1_dxydz3dsip_SF_vhmm_regionbd,
            Muon_2_dxydz3dsip_SF_vhmm_regionbd,
        ],
        "m2m": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_3_ID_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            Muon_3_ID_SF_vhmm_m2m_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_3_mvaTTH_SF_vhmm_m2m,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
            Muon_3_dxydz3dsip_SF_vhmm_m2m,
        ],
        "m2m_dyfakeingmu_regionb": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            Muon_3_ID_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            # above 200
            Muon_1_ID_SF_vhmm_regionbd_above200,
            Muon_2_ID_SF_vhmm_regionbd_above200,
            Muon_3_ID_SF_vhmm_m2m_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_regionbd,
            Muon_2_mvaTTH_SF_vhmm_regionbd,
            Muon_3_mvaTTH_SF_vhmm_m2m,
            Muon_1_dxydz3dsip_SF_vhmm_regionbd,
            Muon_2_dxydz3dsip_SF_vhmm_regionbd,
            Muon_3_dxydz3dsip_SF_vhmm_m2m,
        ],
        "m2m_dyfakeingmu_regionc": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_3_ID_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            Muon_3_ID_SF_vhmm_m2m_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_3_mvaTTH_SF_vhmm_m2m,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
            Muon_3_dxydz3dsip_SF_vhmm_m2m,
        ],
        "m2m_dyfakeingmu_regiond": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            Muon_3_ID_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            # above 200
            Muon_1_ID_SF_vhmm_regionbd_above200,
            Muon_2_ID_SF_vhmm_regionbd_above200,
            Muon_3_ID_SF_vhmm_m2m_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_regionbd,
            Muon_2_mvaTTH_SF_vhmm_regionbd,
            Muon_3_mvaTTH_SF_vhmm_m2m,
            Muon_1_dxydz3dsip_SF_vhmm_regionbd,
            Muon_2_dxydz3dsip_SF_vhmm_regionbd,
            Muon_3_dxydz3dsip_SF_vhmm_m2m,
        ],
        "eemm": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
        ],
        "eemm_cr": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
        ],
        "mmmm": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_3_ID_SF_vhmm_mmmm,
            Muon_4_ID_SF_vhmm_mmmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_3_ID_SF_vhmm_mmmm_below15,
            Muon_4_ID_SF_vhmm_mmmm_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            Muon_3_ID_SF_vhmm_mmmm_above200,
            Muon_4_ID_SF_vhmm_mmmm_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_3_mvaTTH_SF_vhmm_mmmm,
            Muon_4_mvaTTH_SF_vhmm_mmmm,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
            Muon_3_dxydz3dsip_SF_vhmm_mmmm,
            Muon_4_dxydz3dsip_SF_vhmm_mmmm,
        ],
        "mmmm_cr": [
            Muon_1_ID_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_3_ID_SF_vhmm_mmmm,
            Muon_4_ID_SF_vhmm_mmmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_3_ID_SF_vhmm_mmmm_below15,
            Muon_4_ID_SF_vhmm_mmmm_below15,
            # above 200
            Muon_1_ID_SF_vhmm_above200,
            Muon_2_ID_SF_vhmm_above200,
            Muon_3_ID_SF_vhmm_mmmm_above200,
            Muon_4_ID_SF_vhmm_mmmm_above200,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm,
            Muon_2_mvaTTH_SF_vhmm,
            Muon_3_mvaTTH_SF_vhmm_mmmm,
            Muon_4_mvaTTH_SF_vhmm_mmmm,
            Muon_1_dxydz3dsip_SF_vhmm,
            Muon_2_dxydz3dsip_SF_vhmm,
            Muon_3_dxydz3dsip_SF_vhmm_mmmm,
            Muon_4_dxydz3dsip_SF_vhmm_mmmm,
        ],
        "nnmm": [
            Muon_1_ID_SF_vhmm_corrected,
            Muon_2_ID_SF_vhmm_corrected,
            # below 15
            Muon_1_ID_SF_vhmm_below15_corrected,
            Muon_2_ID_SF_vhmm_below15_corrected,
            # above 200
            Muon_1_ID_SF_vhmm_above200_corrected,
            Muon_2_ID_SF_vhmm_above200_corrected,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_corrected,
            Muon_2_mvaTTH_SF_vhmm_corrected,
            Muon_1_dxydz3dsip_SF_vhmm_corrected,
            Muon_2_dxydz3dsip_SF_vhmm_corrected,
        ],
        "fjmm": [
            Muon_1_ID_SF_vhmm_corrected,
            Muon_2_ID_SF_vhmm_corrected,
            # below 15
            Muon_1_ID_SF_vhmm_below15_corrected,
            Muon_2_ID_SF_vhmm_below15_corrected,
            # above 200
            Muon_1_ID_SF_vhmm_above200_corrected,
            Muon_2_ID_SF_vhmm_above200_corrected,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_corrected,
            Muon_2_mvaTTH_SF_vhmm_corrected,
            Muon_1_dxydz3dsip_SF_vhmm_corrected,
            Muon_2_dxydz3dsip_SF_vhmm_corrected,
        ],
        "fjmm_cr": [
            Muon_1_ID_SF_vhmm_regionbd_corrected,
            Muon_2_ID_SF_vhmm_regionbd_corrected,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15_corrected,
            Muon_2_ID_SF_vhmm_regionbd_below15_corrected,
            # above 200
            Muon_1_ID_SF_vhmm_regionbd_above200_corrected,
            Muon_2_ID_SF_vhmm_regionbd_above200_corrected,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_regionbd_corrected,
            Muon_2_mvaTTH_SF_vhmm_regionbd_corrected,
            Muon_1_dxydz3dsip_SF_vhmm_regionbd_corrected,
            Muon_2_dxydz3dsip_SF_vhmm_regionbd_corrected,
        ],
        "nnmm_topcontrol": [
            Muon_1_ID_SF_vhmm_TopCR_corrected,
            # below 15
            Muon_1_ID_SF_vhmm_TopCR_below15_corrected,
            # above 200
            Muon_1_ID_SF_vhmm_TopCR_above200_corrected,
            # mvatth
            Muon_1_mvaTTH_SF_vhmm_TopCR_corrected,
            Muon_1_dxydz3dsip_SF_vhmm_TopCR_corrected,
        ],
    },
)

MuonIso_SF = ProducerGroup(
    name="MuonIso_SF",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
    subproducers={
        "e2m": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
        ],
        "e2m_dyfakeinge_regionb": [
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            # above 200
            Muon_1_Iso_SF_vhmm_regionbd_above200,
            Muon_2_Iso_SF_vhmm_regionbd_above200,
        ],
        "e2m_dyfakeinge_regionc": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
        ],
        "e2m_dyfakeinge_regiond": [
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            # above 200
            Muon_1_Iso_SF_vhmm_regionbd_above200,
            Muon_2_Iso_SF_vhmm_regionbd_above200,
        ],
        "m2m": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            Muon_3_Iso_SF_vhmm_m2m,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
            Muon_3_Iso_SF_vhmm_m2m_above200,
        ],
        "m2m_dyfakeingmu_regionb": [
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            Muon_3_Iso_SF_vhmm_m2m,
            # above 200
            Muon_1_Iso_SF_vhmm_regionbd_above200,
            Muon_2_Iso_SF_vhmm_regionbd_above200,
            Muon_3_Iso_SF_vhmm_m2m_above200,
        ],
        "m2m_dyfakeingmu_regionc": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            Muon_3_Iso_SF_vhmm_m2m,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
            Muon_3_Iso_SF_vhmm_m2m_above200,
        ],
        "m2m_dyfakeingmu_regiond": [
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            Muon_3_Iso_SF_vhmm_m2m,
            # above 200
            Muon_1_Iso_SF_vhmm_regionbd_above200,
            Muon_2_Iso_SF_vhmm_regionbd_above200,
            Muon_3_Iso_SF_vhmm_m2m_above200,
        ],
        "eemm": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
        ],
        "eemm_cr": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
        ],
        "mmmm": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            Muon_3_Iso_SF_vhmm_mmmm,
            Muon_4_Iso_SF_vhmm_mmmm,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
            Muon_3_Iso_SF_vhmm_mmmm_above200,
            Muon_4_Iso_SF_vhmm_mmmm_above200,
        ],
        "mmmm_cr": [
            Muon_1_Iso_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            Muon_3_Iso_SF_vhmm_mmmm,
            Muon_4_Iso_SF_vhmm_mmmm,
            # above 200
            Muon_1_Iso_SF_vhmm_above200,
            Muon_2_Iso_SF_vhmm_above200,
            Muon_3_Iso_SF_vhmm_mmmm_above200,
            Muon_4_Iso_SF_vhmm_mmmm_above200,
        ],
        "nnmm": [
            Muon_1_Iso_SF_vhmm_corrected,
            Muon_2_Iso_SF_vhmm_corrected,
            # above 200
            Muon_1_Iso_SF_vhmm_above200_corrected,
            Muon_2_Iso_SF_vhmm_above200_corrected,
        ],
        "fjmm": [
            Muon_1_Iso_SF_vhmm_corrected,
            Muon_2_Iso_SF_vhmm_corrected,
            # above 200
            Muon_1_Iso_SF_vhmm_above200_corrected,
            Muon_2_Iso_SF_vhmm_above200_corrected,
        ],
        "fjmm_cr": [
            Muon_1_Iso_SF_vhmm_regionbd_corrected,
            Muon_2_Iso_SF_vhmm_regionbd_corrected,
            # above 200
            Muon_1_Iso_SF_vhmm_regionbd_above200_corrected,
            Muon_2_Iso_SF_vhmm_regionbd_above200_corrected,
        ],
        "nnmm_topcontrol": [
            Muon_1_Iso_SF_vhmm_TopCR_corrected,
            # above 200
            Muon_1_Iso_SF_vhmm_TopCR_above200_corrected,
        ],
    },
)

###################################
########## HighPt Muon RECO #######
###################################
Muon_1_RECO_SF_vhmm_corrected = Producer(
    name="Muon_1_RECO_SF_vhmm_corrected",
    call='scalefactor::muon::reco_mu_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_reco_sf_name_HighPt}")',
    input=[q.muon_leadingp4_H_uncorrected],
    output=[q.reco_wgt_mu_1_above200],
    scopes=["nnmm","fjmm"],
)
Muon_2_RECO_SF_vhmm_corrected = Producer(
    name="Muon_2_RECO_SF_vhmm_corrected",
    call='scalefactor::muon::reco_mu_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_reco_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_H_uncorrected],
    output=[q.reco_wgt_mu_2_above200],
    scopes=["nnmm","fjmm"],
)
### top CR
Muon_1_RECO_SF_vhmm_TopCR_corrected = Producer(
    name="Muon_1_RECO_SF_vhmm_TopCR_corrected",
    call='scalefactor::muon::reco_mu_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_reco_sf_name_HighPt}")',
    input=[q.muon_Top_CR_uncorrected],
    output=[q.reco_wgt_mu_1_above200],
    scopes=["nnmm_topcontrol"],
)

Muon_1_RECO_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_1_RECO_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::reco_mu_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_reco_sf_name_HighPt}")',
    input=[q.muon_leadingp4_Z_CR_uncorrected],
    output=[q.reco_wgt_mu_1_above200],
    scopes=["fjmm_cr"],
)
Muon_2_RECO_SF_vhmm_regionbd_corrected = Producer(
    name="Muon_2_RECO_SF_vhmm_regionbd_corrected",
    call='scalefactor::muon::reco_mu_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_HighPt}", {output}, "{muon_sf_file_HighPt}", "{muon_reco_sf_name_HighPt}")',
    input=[q.muon_subleadingp4_Z_CR_uncorrected],
    output=[q.reco_wgt_mu_2_above200],
    scopes=["fjmm_cr"],
)

MuonRECO_SF = ProducerGroup(
    name="MuonRECO_SF",
    call=None,
    input=None,
    output=None,
    scopes=["nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
    subproducers={
        "nnmm": [
            Muon_1_RECO_SF_vhmm_corrected,
            Muon_2_RECO_SF_vhmm_corrected,
        ],
        "fjmm": [
            Muon_1_RECO_SF_vhmm_corrected,
            Muon_2_RECO_SF_vhmm_corrected,
        ],
        "fjmm_cr": [
            Muon_1_RECO_SF_vhmm_regionbd_corrected,
            Muon_2_RECO_SF_vhmm_regionbd_corrected,
        ],
        "nnmm_topcontrol": [
            Muon_1_RECO_SF_vhmm_TopCR_corrected,
        ],
    },
)
#########################
### FatJet WvsQCD SF ###
#########################
PNetWvsQCD_SF = Producer(
    name="PNetWvsQCD_SF",
    call='scalefactor::jet::pnet_wqcd_sf({df}, {input}, "{fatjet_sf_varation}", {output}, "{fjmm_WvsQCD_sf_file}", "{fjmm_WvsQCD_sf_name}")',
    input=[q.fatjet_p4_1],
    output=[q.pnet_wqcd_wgt],
    scopes=["fjmm","fjmm_cr"],
)

# PNetWvsQCD_SF = ProducerGroup(
#     name="PNetWvsQCD_SF",
#     call=None,
#     input=None,
#     output=None,
#     scopes=["fjmm","fjmm_cr"],
#     subproducers={
#         Muon_1_PNet_SF_vhmm,
#         Muon_2_PNet_SF_vhmm,
#     },
# )

#########################
# Electron ID/ISO SF
#########################
# Ele_1_IDWP80_SF_e2m = Producer(
#     name="Ele_1_IDWP80_SF_e2m",
#     call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp80noiso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
#     input=[q.extra_lep_p4_noCorr],
#     output=[q.id_wgt_ele_wp80nonIso_1],
#     scopes=["e2m"],
# )
# Ele_1_IDWP80_SF_eemm = Producer(
#     name="Ele_1_IDWP80_SF_eemm",
#     call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp80noiso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
#     input=[q.lepton_leadingp4_Z_uncorrected],
#     output=[q.id_wgt_ele_wp80nonIso_1],
#     scopes=["eemm"],
# )
# Ele_2_IDWP80_SF = Producer(
#     name="Ele_2_IDWP80_SF",
#     call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp80noiso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
#     input=[q.lepton_subleadingp4_Z_uncorrected],
#     output=[q.id_wgt_ele_wp80nonIso_2],
#     scopes=["eemm"],
# )

#################### id SF for ele ####################
Ele_1_Loose_SF_e2m = Producer(
    name="Ele_1_Loose_SF_e2m",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_ele_loose_1],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
Ele_1_Loose_SF_e2m_below10 = Producer(
    name="Ele_1_Loose_SF_e2m_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_ele_loose_1_below10],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

Ele_1_IDWP90_SF_e2m = Producer(
    name="Ele_1_IDWP90_SF_e2m",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_ele_wp90Iso_1],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
Ele_1_IDWP90_SF_e2m_below10 = Producer(
    name="Ele_1_IDWP90_SF_e2m_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_ele_wp90Iso_1_below10],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
Ele_1_mvaTTH_SF_e2m = Producer(
    name="Ele_1_mvaTTH_SF_e2m",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "mvaTTH", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.id_wgt_ele_mvatth_1],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
############### Top CR
Ele_1_Loose_SF_TopCR = Producer(
    name="Ele_1_Loose_SF_TopCR",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.ele_Top_CR],
    output=[q.id_wgt_ele_loose_1],
    scopes=["nnmm_topcontrol"],
)
Ele_1_Loose_SF_TopCR_below10 = Producer(
    name="Ele_1_Loose_SF_TopCR_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.ele_Top_CR],
    output=[q.id_wgt_ele_loose_1_below10],
    scopes=["nnmm_topcontrol"],
)

Ele_1_IDWP90_SF_TopCR = Producer(
    name="Ele_1_IDWP90_SF_TopCR",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.ele_Top_CR],
    output=[q.id_wgt_ele_wp90Iso_1],
    scopes=["nnmm_topcontrol"],
)
Ele_1_IDWP90_SF_TopCR_below10 = Producer(
    name="Ele_1_IDWP90_SF_TopCR_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.ele_Top_CR],
    output=[q.id_wgt_ele_wp90Iso_1_below10],
    scopes=["nnmm_topcontrol"],
)
Ele_1_mvaTTH_SF_TopCR = Producer(
    name="Ele_1_mvaTTH_SF_TopCR",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "mvaTTH", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.ele_Top_CR],
    output=[q.id_wgt_ele_mvatth_1],
    scopes=["nnmm_topcontrol"],
)

################
## for 2 eles ##
################
Ele_1_Loose_SF_eemm = Producer(
    name="Ele_1_Loose_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_loose_1],
    scopes=["eemm","eemm_cr"],
)
Ele_1_Loose_SF_eemm_below10 = Producer(
    name="Ele_1_Loose_SF_eemm_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_loose_1_below10],
    scopes=["eemm","eemm_cr"],
)

Ele_1_IDWP90_SF_eemm = Producer(
    name="Ele_1_IDWP90_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_wp90Iso_1],
    scopes=["eemm","eemm_cr"],
)
Ele_1_IDWP90_SF_eemm_below10 = Producer(
    name="Ele_1_IDWP90_SF_eemm_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_wp90Iso_1_below10],
    scopes=["eemm","eemm_cr"],
)
Ele_1_mvaTTH_SF_eemm = Producer(
    name="Ele_1_mvaTTH_SF_eemm",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "mvaTTH", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_mvatth_1],
    scopes=["eemm","eemm_cr"],
)

Ele_2_Loose_SF_eemm = Producer(
    name="Ele_2_Loose_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_loose_2],
    scopes=["eemm","eemm_cr"],
)
Ele_2_Loose_SF_eemm_below10 = Producer(
    name="Ele_2_Loose_SF_eemm_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_loose_2_below10],
    scopes=["eemm","eemm_cr"],
)

Ele_2_IDWP90_SF_eemm = Producer(
    name="Ele_2_IDWP90_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_wp90Iso_2],
    scopes=["eemm","eemm_cr"],
)
Ele_2_IDWP90_SF_eemm_below10 = Producer(
    name="Ele_2_IDWP90_SF_eemm_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_wp90Iso_2_below10],
    scopes=["eemm","eemm_cr"],
)
Ele_2_mvaTTH_SF_eemm = Producer(
    name="Ele_2_mvaTTH_SF_eemm",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "mvaTTH", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.id_wgt_ele_mvatth_2],
    scopes=["eemm","eemm_cr"],
)

EleID_SF = ProducerGroup(
    name="EleID_SF",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm","eemm_cr","nnmm_topcontrol"],
    subproducers={
        "e2m": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_Loose_SF_e2m_below10,
            Ele_1_IDWP90_SF_e2m,
            Ele_1_IDWP90_SF_e2m_below10,
            Ele_1_mvaTTH_SF_e2m,
        ],
        "e2m_dyfakeinge_regionb": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_Loose_SF_e2m_below10,
            Ele_1_IDWP90_SF_e2m,
            Ele_1_IDWP90_SF_e2m_below10,
            Ele_1_mvaTTH_SF_e2m,
        ],
        "e2m_dyfakeinge_regionc": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_Loose_SF_e2m_below10,
            Ele_1_IDWP90_SF_e2m,
            Ele_1_IDWP90_SF_e2m_below10,
            Ele_1_mvaTTH_SF_e2m,
        ],
        "e2m_dyfakeinge_regiond": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_Loose_SF_e2m_below10,
            Ele_1_IDWP90_SF_e2m,
            Ele_1_IDWP90_SF_e2m_below10,
            Ele_1_mvaTTH_SF_e2m,
        ],
        "eemm": [
            Ele_1_Loose_SF_eemm,
            Ele_1_Loose_SF_eemm_below10,
            Ele_2_Loose_SF_eemm,
            Ele_2_Loose_SF_eemm_below10,
            Ele_1_IDWP90_SF_eemm,
            Ele_1_IDWP90_SF_eemm_below10,
            Ele_2_IDWP90_SF_eemm,
            Ele_2_IDWP90_SF_eemm_below10,
            Ele_1_mvaTTH_SF_eemm,
            Ele_2_mvaTTH_SF_eemm,
        ],
        "eemm_cr": [
            Ele_1_Loose_SF_eemm,
            Ele_1_Loose_SF_eemm_below10,
            Ele_2_Loose_SF_eemm,
            Ele_2_Loose_SF_eemm_below10,
            Ele_1_IDWP90_SF_eemm,
            Ele_1_IDWP90_SF_eemm_below10,
            Ele_2_IDWP90_SF_eemm,
            Ele_2_IDWP90_SF_eemm_below10,
            Ele_1_mvaTTH_SF_eemm,
            Ele_2_mvaTTH_SF_eemm,
        ],
        "nnmm_topcontrol": [
            Ele_1_Loose_SF_TopCR,
            Ele_1_Loose_SF_TopCR_below10,
            Ele_1_IDWP90_SF_TopCR,
            Ele_1_IDWP90_SF_TopCR_below10,
            Ele_1_mvaTTH_SF_TopCR
        ]
    },
)

################
## for 1 eles ##
################
Ele_1_Reco_SF_e2m = Producer(
    name="Ele_1_Reco_SF_e2m",
    call='scalefactor::electron::reco_e_vhmm({df}, {input}, "{ele_sf_year_id}", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.reco_wgt_ele_1],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
Ele_1_Reco_SF_e2m_below10 = Producer(
    name="Ele_1_Reco_SF_e2m_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Reco", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4_noCorr],
    output=[q.reco_wgt_ele_1_below10],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
### for top CR
Ele_1_Reco_SF_TopCR = Producer(
    name="Ele_1_Reco_SF_TopCR",
    call='scalefactor::electron::reco_e_vhmm({df}, {input}, "{ele_sf_year_id}", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.ele_Top_CR],
    output=[q.reco_wgt_ele_1],
    scopes=["nnmm_topcontrol"],
)
Ele_1_Reco_SF_TopCR_below10 = Producer(
    name="Ele_1_Reco_SF_TopCR_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Reco", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.ele_Top_CR],
    output=[q.reco_wgt_ele_1_below10],
    scopes=["nnmm_topcontrol"],
)

################
## for 2 eles ##
################
Ele_1_Reco_SF_eemm = Producer(
    name="Ele_1_Reco_SF_eemm",
    call='scalefactor::electron::reco_e_vhmm({df}, {input}, "{ele_sf_year_id}", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.reco_wgt_ele_1],
    scopes=["eemm","eemm_cr"],
)
Ele_1_Reco_SF_eemm_below10 = Producer(
    name="Ele_1_Reco_SF_eemm_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Reco", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z_uncorrected],
    output=[q.reco_wgt_ele_1_below10],
    scopes=["eemm","eemm_cr"],
)

Ele_2_Reco_SF_eemm = Producer(
    name="Ele_2_Reco_SF_eemm",
    call='scalefactor::electron::reco_e_vhmm({df}, {input}, "{ele_sf_year_id}", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.reco_wgt_ele_2],
    scopes=["eemm","eemm_cr"],
)
Ele_2_Reco_SF_eemm_below10 = Producer(
    name="Ele_2_Reco_SF_eemm_below10",
    call='scalefactor::electron::custom_e_vhmm({df}, {input}, "{custom_ele_sf_year_id}", "Reco", "{ele_sf_varation}", {output}, "{custom_ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z_uncorrected],
    output=[q.reco_wgt_ele_2_below10],
    scopes=["eemm","eemm_cr"],
)

EleReco_SF = ProducerGroup(
    name="EleReco_SF",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm","eemm_cr","nnmm_topcontrol"],
    subproducers={
        "e2m": [
            Ele_1_Reco_SF_e2m,
            Ele_1_Reco_SF_e2m_below10,
        ],
        "e2m_dyfakeinge_regionb": [
            Ele_1_Reco_SF_e2m,
            Ele_1_Reco_SF_e2m_below10,
        ],
        "e2m_dyfakeinge_regionc": [
            Ele_1_Reco_SF_e2m,
            Ele_1_Reco_SF_e2m_below10,
        ],
        "e2m_dyfakeinge_regiond": [
            Ele_1_Reco_SF_e2m,
            Ele_1_Reco_SF_e2m_below10,
        ],
        "eemm": [
            Ele_1_Reco_SF_eemm,
            Ele_1_Reco_SF_eemm_below10,
            Ele_2_Reco_SF_eemm,
            Ele_2_Reco_SF_eemm_below10,
        ],
        "eemm_cr": [
            Ele_1_Reco_SF_eemm,
            Ele_1_Reco_SF_eemm_below10,
            Ele_2_Reco_SF_eemm,
            Ele_2_Reco_SF_eemm_below10,
        ],
        "nnmm_topcontrol": [
            Ele_1_Reco_SF_TopCR,
            Ele_1_Reco_SF_TopCR_below10,
        ],
    },
)

#########################
# b-tagging SF
#########################
btaggingloose_SF = Producer(
    name="btaggingloose_SF",
    call='scalefactor::jet::btagSF({df}, {input}, "{btag_sf_variation}", {output}, "{btag_sf_file}", "{btag_corr_algo}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask, # since bjet_mask belongs to goodjet_mask, belongs to veto_mask(for muon), so bjet_mask is the tightest mask
    ],
    output=[q.btag_weight],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",],
)
btaggingloose_SF_run2 = Producer(
    name="btaggingloose_SF_run2",
    call='scalefactor::jet::btagSF_run2({df}, {input}, "{btag_sf_variation}", {output}, "{btag_sf_file}", "{btag_corr_algo}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask, # since bjet_mask belongs to goodjet_mask, belongs to veto_mask(for muon), so bjet_mask is the tightest mask
    ],
    output=[q.btag_weight],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm","nnmm","fjmm","fjmm_cr"],
)

#### to calculate btag weight for different channels (by Mingxuan) #####
########### ttbar sample ################
btagging_SF_2WPs_3l_4l = Producer(
    name="btagging_SF_2WPs_3l_4l",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_ttbar}", "{medium_btag_eff_file_ttbar}", "{era_name}", "3l_4l", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"],
)

btagging_SF_2WPs_fjmm = Producer(
    name="btagging_SF_2WPs_fjmm",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_ttbar}", "{medium_btag_eff_file_ttbar}", "{era_name}", "fjmm", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["fjmm","fjmm_cr"],
)

btagging_SF_2WPs_met = Producer(
    name="btagging_SF_2WPs_met",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_ttbar}", "{medium_btag_eff_file_ttbar}", "{era_name}", "met", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["nnmm"],
)
########### DY sample ################
btagging_SF_2WPs_3l_4l_dy = Producer(
    name="btagging_SF_2WPs_3l_4l_dy",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_dy}", "{medium_btag_eff_file_dy}", "{era_name}", "3l_4l", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"],
)

btagging_SF_2WPs_fjmm_dy = Producer(
    name="btagging_SF_2WPs_fjmm_dy",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_dy}", "{medium_btag_eff_file_dy}", "{era_name}", "fjmm", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["fjmm","fjmm_cr"],
)

btagging_SF_2WPs_met_dy = Producer(
    name="btagging_SF_2WPs_met_dy",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_dy}", "{medium_btag_eff_file_dy}", "{era_name}", "met", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["nnmm"],
)
########### VHmm sample ################
btagging_SF_2WPs_3l_4l_vhmm = Producer(
    name="btagging_SF_2WPs_3l_4l_vhmm",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_vhmm}", "{medium_btag_eff_file_vhmm}", "{era_name}", "3l_4l", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"],
)

btagging_SF_2WPs_fjmm_vhmm = Producer(
    name="btagging_SF_2WPs_fjmm_vhmm",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_vhmm}", "{medium_btag_eff_file_vhmm}", "{era_name}", "fjmm", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["fjmm","fjmm_cr"],
)

btagging_SF_2WPs_met_vhmm = Producer(
    name="btagging_SF_2WPs_met_vhmm",
    call='scalefactor::jet::btagSF_2WPs({df}, {input}, "{BtagWeightVariation}", {output}, "{btag_sf_file}", "{loose_btag_eff_file_vhmm}", "{medium_btag_eff_file_vhmm}", "{era_name}", "met", {btag_cut_loose}, {btag_cut_medium}, "{btag_sf_label}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator_PNet,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask_loose,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["nnmm"],
)
#######################
##### trigger SFs #####
#######################

GenerateSingleMuonTriggerSF_MC = ExtendedVectorProducer(
    name="GenerateSingleMuonTriggerSF_MC",
    call='scalefactor::muon::muon_sf_vhmm({df}, {input}, {output}, "{mc_muon_sf_file}", "{mc_muon_sf_correctiontype}", "{mc_trigger_sf}", {mc_muon_trg_extrapolation})',
    input=[q.muon_p4_1], # using leading muon
    output="flagname",
    scope=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
    vec_config="singlemuon_trigger_sf_mc",
)