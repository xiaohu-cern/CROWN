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
Muon_1_ID_SF_vhmm = Producer(
    name="Muon_1_ID_SF_vhmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_H],
    output=[q.id_wgt_mu_1],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_1_ID_SF_vhmm_regionbd = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_p4_1],
    output=[q.id_wgt_mu_1],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_1_ID_SF_vhmm_below15 = Producer(
    name="Muon_1_ID_SF_vhmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_leadingp4_H],
    output=[q.id_wgt_mu_1_below15],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_1_ID_SF_vhmm_regionbd_below15 = Producer(
    name="Muon_1_ID_SF_vhmm_regionbd_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_p4_1],
    output=[q.id_wgt_mu_1_below15],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_2_ID_SF_vhmm = Producer(
    name="Muon_2_ID_SF_vhmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_H],
    output=[q.id_wgt_mu_2],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_2_ID_SF_vhmm_regionbd = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.muon_p4_2],
    output=[q.id_wgt_mu_2],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_2_ID_SF_vhmm_below15 = Producer(
    name="Muon_2_ID_SF_vhmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_subleadingp4_H],
    output=[q.id_wgt_mu_2_below15],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_2_ID_SF_vhmm_regionbd_below15 = Producer(
    name="Muon_2_ID_SF_vhmm_regionbd_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.muon_p4_2],
    output=[q.id_wgt_mu_2_below15],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_3_ID_SF_vhmm_m2m = Producer(
    name="Muon_3_ID_SF_vhmm_m2m",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.extra_lep_p4],
    output=[q.id_wgt_mu_3],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_ID_SF_vhmm_m2m_below15 = Producer(
    name="Muon_3_ID_SF_vhmm_m2m_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.extra_lep_p4],
    output=[q.id_wgt_mu_3_below15],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_ID_SF_vhmm_mmmm = Producer(
    name="Muon_3_ID_SF_vhmm_mmmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.lepton_leadingp4_Z],
    output=[q.id_wgt_mu_3],
    scopes=["mmmm"],
)
Muon_3_ID_SF_vhmm_mmmm_below15 = Producer(
    name="Muon_3_ID_SF_vhmm_mmmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.lepton_leadingp4_Z],
    output=[q.id_wgt_mu_3_below15],
    scopes=["mmmm"],
)
Muon_4_ID_SF_vhmm_mmmm = Producer(
    name="Muon_4_ID_SF_vhmm_mmmm",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z],
    output=[q.id_wgt_mu_4],
    scopes=["mmmm"],
)
Muon_4_ID_SF_vhmm_mmmm_below15 = Producer(
    name="Muon_4_ID_SF_vhmm_mmmm_below15",
    call='scalefactor::muon::id_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z],
    output=[q.id_wgt_mu_4_below15],
    scopes=["mmmm"],
)

#################################
############ Iso SF #############
#################################
Muon_1_Iso_SF_vhmm = Producer(
    name="Muon_1_Iso_SF_vhmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_leadingp4_H],
    output=[q.iso_wgt_mu_1],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_1_Iso_SF_vhmm_regionbd = Producer(
    name="Muon_1_Iso_SF_vhmm_regionbd",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_p4_1],
    output=[q.iso_wgt_mu_1],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_1_Iso_SF_vhmm_below15 = Producer(
    name="Muon_1_Iso_SF_vhmm_below15",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
    input=[q.muon_leadingp4_H],
    output=[q.iso_wgt_mu_1_below15],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_1_Iso_SF_vhmm_regionbd_below15 = Producer(
    name="Muon_1_Iso_SF_vhmm_regionbd_below15",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
    input=[q.muon_p4_1],
    output=[q.iso_wgt_mu_1_below15],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_2_Iso_SF_vhmm = Producer(
    name="Muon_2_Iso_SF_vhmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_subleadingp4_H],
    output=[q.iso_wgt_mu_2],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_2_Iso_SF_vhmm_regionbd = Producer(
    name="Muon_2_Iso_SF_vhmm_regionbd",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.muon_p4_2],
    output=[q.iso_wgt_mu_2],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_2_Iso_SF_vhmm_below15 = Producer(
    name="Muon_2_Iso_SF_vhmm_below15",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
    input=[q.muon_subleadingp4_H],
    output=[q.iso_wgt_mu_2_below15],
    scopes=["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc","eemm","mmmm","nnmm","fjmm"],
)
Muon_2_Iso_SF_vhmm_regionbd_below15 = Producer(
    name="Muon_2_Iso_SF_vhmm_regionbd_below15",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
    input=[q.muon_p4_2],
    output=[q.iso_wgt_mu_2_below15],
    scopes=["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","fjmm_cr"],
)
Muon_3_Iso_SF_vhmm_m2m = Producer(
    name="Muon_3_Iso_SF_vhmm_m2m",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.extra_lep_p4],
    output=[q.iso_wgt_mu_3],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_Iso_SF_vhmm_m2m_below15 = Producer(
    name="Muon_3_Iso_SF_vhmm_m2m_below15",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
    input=[q.extra_lep_p4],
    output=[q.iso_wgt_mu_3_below15],
    scopes=["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
Muon_3_Iso_SF_vhmm_mmmm = Producer(
    name="Muon_3_Iso_SF_vhmm_mmmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.lepton_leadingp4_Z],
    output=[q.iso_wgt_mu_3],
    scopes=["mmmm"],
)
Muon_3_Iso_SF_vhmm_mmmm_below15 = Producer(
    name="Muon_3_Iso_SF_vhmm_mmmm_below15",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
    input=[q.lepton_leadingp4_Z],
    output=[q.iso_wgt_mu_3_below15],
    scopes=["mmmm"],
)
Muon_4_Iso_SF_vhmm_mmmm = Producer(
    name="Muon_4_Iso_SF_vhmm_mmmm",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.lepton_subleadingp4_Z],
    output=[q.iso_wgt_mu_4],
    scopes=["mmmm"],
)
Muon_4_Iso_SF_vhmm_mmmm_below15 = Producer(
    name="Muon_4_Iso_SF_vhmm_mmmm_below15",
    call='scalefactor::muon::iso_vhmm({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation_JPsi}", {output}, "{muon_sf_file_JPsi}", "{muon_iso_sf_name_JPsi}")',
    input=[q.lepton_subleadingp4_Z],
    output=[q.iso_wgt_mu_4_below15],
    scopes=["mmmm"],
)
MuonIDIso_SF = ProducerGroup(
    name="MuonIDIso_SF",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm","nnmm","fjmm","fjmm_cr"],
    subproducers={
        "e2m": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
        ],
        "e2m_dyfakeinge_regionb": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_1_Iso_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            Muon_2_Iso_SF_vhmm_regionbd_below15,
        ],
        "e2m_dyfakeinge_regionc": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
        ],
        "e2m_dyfakeinge_regiond": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_1_Iso_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            Muon_2_Iso_SF_vhmm_regionbd_below15,
        ],
        "m2m": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            Muon_3_ID_SF_vhmm_m2m,
            Muon_3_Iso_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            Muon_3_Iso_SF_vhmm_m2m_below15,
        ],
        "m2m_dyfakeingmu_regionb": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            Muon_3_ID_SF_vhmm_m2m,
            Muon_3_Iso_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_1_Iso_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            Muon_2_Iso_SF_vhmm_regionbd_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            Muon_3_Iso_SF_vhmm_m2m_below15,
        ],
        "m2m_dyfakeingmu_regionc": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            Muon_3_ID_SF_vhmm_m2m,
            Muon_3_Iso_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            Muon_3_Iso_SF_vhmm_m2m_below15,
        ],
        "m2m_dyfakeingmu_regiond": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            Muon_3_ID_SF_vhmm_m2m,
            Muon_3_Iso_SF_vhmm_m2m,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_1_Iso_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            Muon_2_Iso_SF_vhmm_regionbd_below15,
            Muon_3_ID_SF_vhmm_m2m_below15,
            Muon_3_Iso_SF_vhmm_m2m_below15,
        ],
        "eemm": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
        ],
        "mmmm": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            Muon_3_ID_SF_vhmm_mmmm,
            Muon_3_Iso_SF_vhmm_mmmm,
            Muon_4_ID_SF_vhmm_mmmm,
            Muon_4_Iso_SF_vhmm_mmmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
            Muon_3_ID_SF_vhmm_mmmm_below15,
            Muon_3_Iso_SF_vhmm_mmmm_below15,
            Muon_4_ID_SF_vhmm_mmmm_below15,
            Muon_4_Iso_SF_vhmm_mmmm_below15,
        ],
        "nnmm": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
        ],
        "fjmm": [
            Muon_1_ID_SF_vhmm,
            Muon_1_Iso_SF_vhmm,
            Muon_2_ID_SF_vhmm,
            Muon_2_Iso_SF_vhmm,
            # below 15
            Muon_1_ID_SF_vhmm_below15,
            Muon_1_Iso_SF_vhmm_below15,
            Muon_2_ID_SF_vhmm_below15,
            Muon_2_Iso_SF_vhmm_below15,
        ],
        "fjmm_cr": [
            Muon_1_ID_SF_vhmm_regionbd,
            Muon_1_Iso_SF_vhmm_regionbd,
            Muon_2_ID_SF_vhmm_regionbd,
            Muon_2_Iso_SF_vhmm_regionbd,
            # below 15
            Muon_1_ID_SF_vhmm_regionbd_below15,
            Muon_1_Iso_SF_vhmm_regionbd_below15,
            Muon_2_ID_SF_vhmm_regionbd_below15,
            Muon_2_Iso_SF_vhmm_regionbd_below15,
        ],
    },
)
MuonIDIso_SF_RooWorkspace = ProducerGroup(
    name="MuonIDIso_SF_RooWorkspace",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","m2m", "eemm","mmmm"],
    subproducers={
        "e2m": [
            Muon_1_ID_SF_RooWorkspace,
            Muon_1_Iso_SF_RooWorkspace,
            Muon_2_ID_SF_RooWorkspace,
            Muon_2_Iso_SF_RooWorkspace,
        ],
        "m2m": [
            Muon_1_ID_SF_RooWorkspace,
            Muon_1_Iso_SF_RooWorkspace,
            Muon_2_ID_SF_RooWorkspace,
            Muon_2_Iso_SF_RooWorkspace,
        ],
        "eemm": [
            Muon_1_ID_SF_RooWorkspace,
            Muon_1_Iso_SF_RooWorkspace,
            Muon_2_ID_SF_RooWorkspace,
            Muon_2_Iso_SF_RooWorkspace,
        ],
        # 4m TODO
        "mmmm": [
            Muon_1_ID_SF_RooWorkspace,
            Muon_1_Iso_SF_RooWorkspace,
            Muon_2_ID_SF_RooWorkspace,
            Muon_2_Iso_SF_RooWorkspace,
        ],
    },
)

#########################
# Electron ID/ISO SF
#########################
Ele_1_IDWP80_SF_e2m = Producer(
    name="Ele_1_IDWP80_SF_e2m",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp80noiso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4],
    output=[q.id_wgt_ele_wp80nonIso_1],
    scopes=["e2m"],
)
Ele_1_IDWP80_SF_eemm = Producer(
    name="Ele_1_IDWP80_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp80noiso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z],
    output=[q.id_wgt_ele_wp80nonIso_1],
    scopes=["eemm"],
)
Ele_2_IDWP80_SF = Producer(
    name="Ele_2_IDWP80_SF",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp80noiso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z],
    output=[q.id_wgt_ele_wp80nonIso_2],
    scopes=["eemm"],
)

#################### id SF for ele ####################
Ele_1_Loose_SF_e2m = Producer(
    name="Ele_1_Loose_SF_e2m",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4],
    output=[q.id_wgt_ele_loose_1],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
Ele_1_IDWP90_SF_e2m = Producer(
    name="Ele_1_IDWP90_SF_e2m",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.extra_lep_p4],
    output=[q.id_wgt_ele_wp90Iso_1],
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
################
## for 2 eles ##
################
Ele_1_Loose_SF_eemm = Producer(
    name="Ele_1_Loose_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z],
    output=[q.id_wgt_ele_loose_1],
    scopes=["eemm"],
)
Ele_1_IDWP90_SF_eemm = Producer(
    name="Ele_1_IDWP90_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_leadingp4_Z],
    output=[q.id_wgt_ele_wp90Iso_1],
    scopes=["eemm"],
)
Ele_2_Loose_SF_eemm = Producer(
    name="Ele_2_Loose_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "Loose", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z],
    output=[q.id_wgt_ele_loose_2],
    scopes=["eemm"],
)
Ele_2_IDWP90_SF_eemm = Producer(
    name="Ele_2_IDWP90_SF_eemm",
    call='scalefactor::electron::id_e_vhmm({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.lepton_subleadingp4_Z],
    output=[q.id_wgt_ele_wp90Iso_2],
    scopes=["eemm"],
)

EleID_SF = ProducerGroup(
    name="EleID_SF",
    call=None,
    input=None,
    output=None,
    scopes=["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"],
    subproducers={
        "e2m": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_IDWP90_SF_e2m, # for run2
        ],
        "e2m_dyfakeinge_regionb": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_IDWP90_SF_e2m, # for run2
        ],
        "e2m_dyfakeinge_regionc": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_IDWP90_SF_e2m, # for run2
        ],
        "e2m_dyfakeinge_regiond": [
            Ele_1_Loose_SF_e2m, # for 2022
            Ele_1_IDWP90_SF_e2m, # for run2
        ],
        "eemm": [
            Ele_1_Loose_SF_eemm,
            Ele_2_Loose_SF_eemm,
            Ele_1_IDWP90_SF_eemm,
            Ele_2_IDWP90_SF_eemm,
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
            "eemm","mmmm","nnmm","fjmm","fjmm_cr"],
)
btaggingloose_SF_run2 = Producer(
    name="btaggingloose_SF_run2",
    call='scalefactor::jet::btagSF({df}, {input}, "{btag_sf_variation}", {output}, "{btag_sf_file}", "{btag_corr_algo}")',
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