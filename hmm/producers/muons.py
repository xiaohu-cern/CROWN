from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers used for loosest selection of muons
####################

MuonPtCut = Producer(
    name="MuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_muon_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MuonEtaCut = Producer(
    name="MuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_muon_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MuonDxyCut = Producer(
    name="MuonDxyCut",
    call="physicsobject::CutDxy({df}, {input}, {output}, {max_muon_dxy})",
    input=[nanoAOD.Muon_dxy],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MuonDzCut = Producer(
    name="MuonDzCut",
    call="physicsobject::CutDz({df}, {input}, {output}, {max_muon_dz})",
    input=[nanoAOD.Muon_dz],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MuonSIP3DCut = Producer(
    name="MuonSIP3DCut",
    call="physicsobject::CutVarMax({df}, {input}, {output}, {muon_max_sip3d})", # vh developed CutVarMax/Min, TODO apply to others
    input=[nanoAOD.Muon_sip3d],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
# TODO vh LepMVA
# Muon_mvaTTH_Cut = Producer(
#     name="Muon_mvaTTH_Cut",
#     call="physicsobject::CutVarMin({df}, {input}, {output}, {min_muon_mvaTTH})",
#     input=[nanoAOD.Muon_mvaTTH],
#     output=[],
#     scopes=["global"],
# )
MuonIDCut = Producer(
    name="MuonIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{base_muon_id}")',
    input=[],
    output=[],
    # scopes=["global"],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MuonIsoCut = Producer(
    name="MuonIsoCut",
    call="physicsobject::muon::CutIsolation({df}, {output}, {input}, {base_muon_iso_cut})",
    input=[nanoAOD.Muon_pfRelIso04_all], # vh
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
# change basemuon id cut to loose, goodmuon cut to medium
BaseMuons = ProducerGroup(
    name="BaseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_muons_mask],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    # scopes=["global"],
    subproducers=[
        MuonPtCut,
        MuonEtaCut,
        MuonDxyCut,
        MuonDzCut,
        MuonSIP3DCut,
        # these 3 cut used as good muon
        # Muon_mvaTTH_Cut,
        MuonIDCut,
        MuonIsoCut,
    ],
)
####################
# Set of producers used for more specific selection of muons in channels
####################

# vh just in case different muon selections are needed (e.g. loose vs tight id for fakes)
# do cuts again for ALL the channels

GoodMuonIsoCut = Producer(
    name="GoodMuonIsoCut",
    call="physicsobject::electron::CutIsolation({df}, {output}, {input}, {good_muon_iso_cut})",
    input=[nanoAOD.Muon_pfRelIso04_all],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
GoodMuonIDCut = Producer(
    name="MuonIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{good_muon_id_medium}")',
    input=[],
    output=[],
    # scopes=["global"],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
GoodMuonIDCut_HighPt = Producer(
    name="MuonIDCut",
    call='physicsobject::muon::CutUCharID({df}, {output}, {input}, {good_muon_id_highpt_bit})',
    input=[nanoAOD.Muon_highPtId],
    output=[q.mu_uchar_id_mask],
    scopes=["fjmm_cr", "fjmm", "nnmm"],
)
# GoodMuonIDCut_HighPt = Producer(
#     name="MuonIDCut",
#     call='physicsobject::muon::CutID({df}, {output}, "{good_muon_id_highpt}")',
#     input=[],
#     output=[],
#     scopes=["fjmm_cr", "fjmm", "nnmm"],
# )
GoodMuon_mvaTTH_Cut = Producer(
    name="GoodMuon_mvaTTH_Cut",
    call="physicsobject::CutVarMin({df}, {input}, {output}, {min_goodmuon_mvaTTH})",
    input=[nanoAOD.Muon_mvaTTH],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
GoodMuon_mvaTTH_Cut_22To23 = Producer(
    name="GoodMuon_mvaTTH_Cut_22To23",
    call="physicsobject::CutVarMin({df}, {input}, {output}, {min_goodmuon_mvaTTH})",
    input=[q.new_MuonPromptMVA],
    output=[],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
# here actually goodmuon ptcut etacut and isocut are same as base muon, so no need to do now
# only need to add medium id cut
GoodMuons = ProducerGroup(
    name="GoodMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.good_muons_mask], # vh these are the final selection muons' mask
    # scopes=["global"],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[
        GoodMuon_mvaTTH_Cut,
        GoodMuonIDCut,
        GoodMuonIsoCut,
    ],
)

GoodMuons_22To23 = ProducerGroup(
    name="GoodMuons_22To23",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.good_muons_mask], # vh these are the final selection muons' mask
    # scopes=["global"],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    subproducers=[
        GoodMuon_mvaTTH_Cut_22To23,
        GoodMuonIDCut,
        GoodMuonIsoCut,
    ],
)

BaseMuons_HighPt = ProducerGroup(
    name="BaseMuons_HighPt",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_muons_mask],
    scopes=["fjmm_cr", "fjmm", "nnmm"],
    subproducers=[
        MuonPtCut,
        MuonEtaCut,
        MuonDxyCut,
        MuonDzCut,
        MuonSIP3DCut,
        MuonIsoCut,
        GoodMuonIsoCut,
    ],
)
GoodMuons_HighPt = ProducerGroup(
    name="GoodMuons_HighPt",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.good_muons_mask], # vh these are the final selection muons' mask
    scopes=["fjmm_cr", "fjmm", "nnmm"],
    subproducers=[
        GoodMuonIDCut_HighPt,
    ],
)

Muons_use_for_Veto = ProducerGroup(
    name = "Muons_use_for_Veto",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.veto_2l_muons_mask],
    scopes=["fjmm_cr", "fjmm", "nnmm"],
    subproducers=[
        MuonIDCut,
        GoodMuon_mvaTTH_Cut,
        GoodMuonIDCut,
    ],
)
Muons_use_for_Veto_22To23 = ProducerGroup(
    name = "Muons_use_for_Veto_22To23",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.veto_2l_muons_mask],
    scopes=["fjmm_cr", "fjmm", "nnmm"],
    subproducers=[
        MuonIDCut,
        GoodMuon_mvaTTH_Cut_22To23,
        GoodMuonIDCut,
    ],
)

NumberOfGoodMuons = Producer(
    name="NumberOfGoodMuons",
    call="quantities::NumberOfGoodObjects({df}, {output}, {input})",
    input=[q.good_muons_mask],
    output=[q.nmuons],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
NumberOfVetoMuons = Producer(
    name="NumberOfVetoMuons",
    call="quantities::NumberOfGoodObjects({df}, {output}, {input})",
    input=[q.veto_2l_muons_mask],
    output=[q.nvetomuons],
    scopes=["fjmm_cr", "fjmm", "nnmm"],
)
NumberOfBaseMuons = Producer(
    name="NumberOfBaseMuons",
    call="quantities::NumberOfGoodObjects({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.nbasemuons],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
VetoMuons = Producer(
    name="VetoMuons",
    call="physicsobject::VetoCandInMask({df}, {output}, {input}, {muon_index_in_pair})",
    input=[q.base_muons_mask, q.dileptonpair],
    output=[q.veto_muons_mask],
    scopes=["mm"],
)
VetoSecondMuon = Producer(
    name="VetoSecondMuon",
    call="physicsobject::VetoCandInMask({df}, {output}, {input}, {second_muon_index_in_pair})",
    input=[q.veto_muons_mask, q.dileptonpair],
    output=[q.veto_muons_mask_2],
    scopes=["mm"],
)

ExtraMuonsVeto = Producer(
    name="ExtraMuonsVeto",
    call="physicsobject::LeptonVetoFlag({df}, {output}, {input})",
    input={
        "mm": [q.veto_muons_mask_2],
    },
    output=[q.muon_veto_flag],
    scopes=["mm"],
)

####################
# Set of producers used for di-muon veto
####################

DiMuonVetoPtCut = Producer(
    name="DiMuonVetoPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_dimuonveto_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["global"],
)
DiMuonVetoIDCut = Producer(
    name="DiMuonVetoIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{dimuonveto_id}")',
    input=[],
    output=[],
    scopes=["global"],
)
DiMuonVetoMuons = ProducerGroup(
    name="DiMuonVetoMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=MuonEtaCut.output + MuonDxyCut.output + MuonDzCut.output + MuonIsoCut.output,
    output=[],
    scopes=["global"],
    subproducers=[
        DiMuonVetoPtCut,
        DiMuonVetoIDCut,
    ],
)
DiMuonVeto = ProducerGroup(
    name="DiMuonVeto",
    call="physicsobject::CheckForDiLeptonPairs({df}, {output}, {input}, {dileptonveto_dR})",
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_charge,
    ],
    output=[q.dimuon_veto],
    scopes=["global"],
    subproducers=[DiMuonVetoMuons],
)

### Muon collection and their properties
MuonCollection = Producer(
    name="MuonCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    # input=[nanoAOD.Muon_pt, q.good_muons_mask],
    input=[nanoAOD.Muon_pt, q.good_muons_mask],
    output=[q.good_muon_collection],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BaseMuonCollection = Producer(
    name="BaseMuonCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    input=[nanoAOD.Muon_pt, q.base_muons_mask],
    output=[q.base_muon_collection],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BaseLVMu1 = Producer(
    name="BaseLVMu1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_1],
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
)
BaseLVMu1_uncorrected = Producer(
    name="BaseLVMu1_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_1_uncorrected],
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
)
LVMu1 = Producer(
    name="LVMu1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_1],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","nnmm","fjmm","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
LVMu1_uncorrected = Producer(
    name="LVMu1_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_1_uncorrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","nnmm","fjmm","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BaseLVMu2 = Producer(
    name="BaseLVMu2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_2],
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
)
BaseLVMu2_uncorrected = Producer(
    name="BaseLVMu2_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_2_uncorrected],
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
)
LVMu2 = Producer(
    name="LVMu2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_2],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","nnmm","fjmm","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
LVMu2_uncorrected = Producer(
    name="LVMu2_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_2_uncorrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","mmmm","nnmm","fjmm","fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
BaseLVMu3 = Producer(
    name="BaseLVMu3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_3],
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
)
BaseLVMu3_uncorrected = Producer(
    name="BaseLVMu3_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_3_uncorrected],
    scopes=["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
)
LVMu3 = Producer(
    name="LVMu3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_3],
    scopes=["m2m", "mmmm","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
LVMu3_uncorrected = Producer(
    name="LVMu3_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_3_uncorrected],
    scopes=["m2m", "mmmm","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
LVMu4 = Producer(
    name="LVMu4",
    call="lorentzvectors::build({df}, {input_vec}, 3, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_4],
    scopes=["mmmm"],
)
LVMu4_uncorrected = Producer(
    name="LVMu4_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 3, {output})",
    input=[
        q.good_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_4_uncorrected],
    scopes=["mmmm"],
)
BaseLVMu4 = Producer(
    name="BaseLVMu4",
    call="lorentzvectors::build({df}, {input_vec}, 3, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_4],
    scopes=["mmmm_cr"],
)
BaseLVMu4_uncorrected = Producer(
    name="BaseLVMu4_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 3, {output})",
    input=[
        q.base_muon_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_p4_4_uncorrected],
    scopes=["mmmm_cr"],
)
##### 
##### The leading muon from Higgs
Mu1_H_noFSR = Producer(
    name="Mu1_H_noFSR",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.dimuon_HiggsCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_H_noFSR],
    scopes=["e2m","m2m", "eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
Mu1_H = Producer(
    name="Mu1_H",
    call="physicsobject::FSR_Recovery_singlemuon({df}, {output}, {input})",
    input=[
        q.muon_leadingp4_H_noFSR,
        q.FsrPhoton1_pt,
        q.FsrPhoton1_eta,
        q.FsrPhoton1_phi,
    ],
    output=[q.muon_leadingp4_H],
    scopes=["e2m","m2m", "eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

#####################################################
Mu1_H_uncorrected = Producer(
    name="Mu1_H_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.dimuon_HiggsCand_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_H_uncorrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
##### The sub leading muon form Higgs
Mu2_H_noFSR = Producer(
    name="Mu2_H_noFSR",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.dimuon_HiggsCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_H_noFSR],
    scopes=["e2m","m2m", "eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
Mu2_H = Producer(
    name="Mu2_H",
    call="physicsobject::FSR_Recovery_singlemuon({df}, {output}, {input})",
    input=[
        q.muon_subleadingp4_H_noFSR,
        q.FsrPhoton2_pt,
        q.FsrPhoton2_eta,
        q.FsrPhoton2_phi,
    ],
    output=[q.muon_subleadingp4_H],
    scopes=["e2m","m2m", "eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
#####################################################
Mu2_H_uncorrected = Producer(
    name="Mu2_H_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.dimuon_HiggsCand_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_H_uncorrected],
    scopes=["e2m","m2m", "eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
##### The leading muon from Higgs in 4m channel
# Mu1_H_4m = Producer(
#     name="Mu1_H_4m",
#     call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
#     input=[
#         q.quadmuon_HiggsZCand_collection,
#         q.Muon_pt_corrected,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_mass,
#     ],
#     output=[q.muon_leadingp4_H],
#     scopes=["mmmm","mmmm_cr"],
# )
Mu1_H_4m_noFSR = Producer(
    name="Mu1_H_4m_noFSR",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_H_noFSR],
    scopes=["mmmm","mmmm_cr"],
)
Mu1_H_4m = Producer(
    name="Mu1_H_4m",
    call="physicsobject::FSR_Recovery_singlemuon({df}, {output}, {input})",
    input=[
        q.muon_leadingp4_H_noFSR,
        q.FsrPhoton1_pt,
        q.FsrPhoton1_eta,
        q.FsrPhoton1_phi,
    ],
    output=[q.muon_leadingp4_H],
    scopes=["mmmm","mmmm_cr"],
)
Mu1_H_4m_uncorrected = Producer(
    name="Mu1_H_4m_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_H_uncorrected],
    scopes=["mmmm","mmmm_cr"],
)
##### The sub leading muon from Higgs in 4m channel
# Mu2_H_4m = Producer(
#     name="Mu2_H_4m",
#     call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
#     input=[
#         q.quadmuon_HiggsZCand_collection,
#         q.Muon_pt_corrected,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_mass,
#     ],
#     output=[q.muon_subleadingp4_H],
#     scopes=["mmmm","mmmm_cr"],
# )
Mu2_H_4m_noFSR = Producer(
    name="Mu2_H_4m_noFSR",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_H_noFSR],
    scopes=["mmmm","mmmm_cr"],
)
Mu2_H_4m = Producer(
    name="Mu2_H_4m",
    call="physicsobject::FSR_Recovery_singlemuon({df}, {output}, {input})",
    input=[
        q.muon_subleadingp4_H_noFSR,
        q.FsrPhoton2_pt,
        q.FsrPhoton2_eta,
        q.FsrPhoton2_phi,
    ],
    output=[q.muon_subleadingp4_H],
    scopes=["mmmm","mmmm_cr"],
)

Mu2_H_4m_uncorrected = Producer(
    name="Mu2_H_4m_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_H_uncorrected],
    scopes=["mmmm","mmmm_cr"],
)
##### The leading muon from Z Cand in 4m channel
Mu1_Z_4m = Producer(
    name="Mu1_Z_4m",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.lepton_leadingp4_Z],
    scopes=["mmmm","mmmm_cr"],
)
Mu1_Z_4m_uncorrected = Producer(
    name="Mu1_Z_4m_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.lepton_leadingp4_Z_uncorrected],
    scopes=["mmmm","mmmm_cr"],
)
Mu2_Z_4m = Producer(
    name="Mu2_Z_4m",
    call="lorentzvectors::build({df}, {input_vec}, 3, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.lepton_subleadingp4_Z],
    scopes=["mmmm","mmmm_cr"],
)
Mu2_Z_4m_uncorrected = Producer(
    name="Mu2_Z_4m_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 3, {output})",
    input=[
        q.quadmuon_HiggsZCand_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.lepton_subleadingp4_Z_uncorrected],
    scopes=["mmmm","mmmm_cr"],
)
##### The leading muon from Z Cand in Z_CR region (fjmm_cr, regionbd)
Mu1_Z_CR = Producer(
    name="Mu1_Z_CR",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.dimuon_ZControl_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_Z_CR],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
Mu1_Z_CR_uncorrected = Producer(
    name="Mu1_Z_CR_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.dimuon_ZControl_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_leadingp4_Z_CR_uncorrected],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
Mu2_Z_CR = Producer(
    name="Mu2_Z_CR",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.dimuon_ZControl_collection,
        q.Muon_pt_corrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_Z_CR],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
Mu2_Z_CR_uncorrected = Producer(
    name="Mu2_Z_CR_uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.dimuon_ZControl_collection,
        q.Muon_pt_uncorrected,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.muon_subleadingp4_Z_CR_uncorrected],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
##### dimuon_ZControl_collection 0,1  -> scopes=["fjmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
##### mu1_ptErr = Quantity("mu1_ptErr")
##### mu2_ptErr = Quantity("mu2_ptErr")
mu1_ZCR_mvaTTH = Producer(
    name="mu1_ZCR_mvaTTH",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the dimuon_ZControl_collection[0]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.dimuon_ZControl_collection,
    ],
    output=[q.mu1_mvaTTH],
    scopes=["fjmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
mu2_ZCR_mvaTTH = Producer(
    name="mu2_ZCR_mvaTTH",
    call="physicsobject::Muon_var({df}, {output}, {input}, 1)", # 1 stands the dimuon_ZControl_collection[1]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.dimuon_ZControl_collection,
    ],
    output=[q.mu2_mvaTTH],
    scopes=["fjmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
##### dimuon_HiggsCand_collection 0,1 -> scopes=["e2m","m2m","eemm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
mu1_Higgs_mvaTTH = Producer(
    name="mu1_Higgs_mvaTTH",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the dimuon_HiggsCand_collection[0]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.dimuon_HiggsCand_collection,
    ],
    output=[q.mu1_mvaTTH],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu2_Higgs_mvaTTH = Producer(
    name="mu2_Higgs_mvaTTH",
    call="physicsobject::Muon_var({df}, {output}, {input}, 1)", # 1 stands the dimuon_HiggsCand_collection[1]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.dimuon_HiggsCand_collection,
    ],
    output=[q.mu2_mvaTTH],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
##### q.quadmuon_HiggsZCand_collection 0, 1 -> scopes=["mmmm"]
mu1_Higgs_mvaTTH_mmmm = Producer(
    name="mu1_Higgs_mvaTTH_mmmm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the quadmuon_HiggsZCand_collection[0]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.quadmuon_HiggsZCand_collection,
    ],
    output=[q.mu1_mvaTTH],
    scopes=["mmmm","mmmm_cr"]
)
mu2_Higgs_mvaTTH_mmmm = Producer(
    name="mu2_Higgs_mvaTTH_mmmm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 1)", # 1 stands the quadmuon_HiggsZCand_collection[1]
    input=[
        nanoAOD.Muon_mvaTTH,
        q.quadmuon_HiggsZCand_collection,
    ],
    output=[q.mu2_mvaTTH],
    scopes=["mmmm","mmmm_cr"]
)
#############
#############
#############
mu1_ZCR_ptErr = Producer(
    name="mu1_ZCR_ptErr",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the dimuon_ZControl_collection[0]
    input=[
        nanoAOD.Muon_ptErr,
        q.dimuon_ZControl_collection,
    ],
    output=[q.mu1_ptErr],
    scopes=["fjmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
mu2_ZCR_ptErr = Producer(
    name="mu2_ZCR_ptErr",
    call="physicsobject::Muon_var({df}, {output}, {input}, 1)", # 1 stands the dimuon_ZControl_collection[1]
    input=[
        nanoAOD.Muon_ptErr,
        q.dimuon_ZControl_collection,
    ],
    output=[q.mu2_ptErr],
    scopes=["fjmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
##### dimuon_HiggsCand_collection 0,1 -> scopes=["e2m","m2m","eemm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
mu1_Higgs_ptErr = Producer(
    name="mu1_Higgs_ptErr",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the dimuon_HiggsCand_collection[0]
    input=[
        nanoAOD.Muon_ptErr,
        q.dimuon_HiggsCand_collection,
    ],
    output=[q.mu1_ptErr],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu2_Higgs_ptErr = Producer(
    name="mu2_Higgs_ptErr",
    call="physicsobject::Muon_var({df}, {output}, {input}, 1)", # 1 stands the dimuon_HiggsCand_collection[1]
    input=[
        nanoAOD.Muon_ptErr,
        q.dimuon_HiggsCand_collection,
    ],
    output=[q.mu2_ptErr],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
##### q.quadmuon_HiggsZCand_collection 0, 1 -> scopes=["mmmm"]
mu1_Higgs_ptErr_mmmm = Producer(
    name="mu1_Higgs_ptErr_mmmm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 0)", # 0 stands the quadmuon_HiggsZCand_collection[0]
    input=[
        nanoAOD.Muon_ptErr,
        q.quadmuon_HiggsZCand_collection,
    ],
    output=[q.mu1_ptErr],
    scopes=["mmmm","mmmm_cr"]
)
mu2_Higgs_ptErr_mmmm = Producer(
    name="mu2_Higgs_ptErr_mmmm",
    call="physicsobject::Muon_var({df}, {output}, {input}, 1)", # 1 stands the quadmuon_HiggsZCand_collection[1]
    input=[
        nanoAOD.Muon_ptErr,
        q.quadmuon_HiggsZCand_collection,
    ],
    output=[q.mu2_ptErr],
    scopes=["mmmm","mmmm_cr"]
)

Calculate_MuonPromptMVA22To23 = Producer(
    name="Calculate_MuonPromptMVA22To23",
    call='physicsobject::muon::Calculate_MuonPromptMVA22To23({df}, {output}, {input}, "{PromptMVA_BDT_muon_name}", "{muon_xml_path}")',
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_pfRelIso03_all,
        nanoAOD.Muon_miniPFRelIso_chg,
        nanoAOD.Muon_miniPFRelIso_all,
        nanoAOD.Muon_jetNDauCharged,
        nanoAOD.Muon_jetPtRelv2,
        nanoAOD.Muon_jetIdx,
        nanoAOD.Jet_btagDeepFlavB,
        nanoAOD.Muon_jetRelIso,
        nanoAOD.Muon_sip3d,
        nanoAOD.Muon_dxy,
        nanoAOD.Muon_dz,
        nanoAOD.Muon_segmentComp,
    ],
    output=[q.new_MuonPromptMVA],
    scopes=["e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc",
            "m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb", "m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regiond",
            "fjmm_cr","fjmm","nnmm"
            ],
)