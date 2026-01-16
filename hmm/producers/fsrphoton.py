from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

leadingmuon_FsrPhotonIdx = Producer(
    name="leading_muon_FsrPhotonIdx",
    call='physicsobject::FsrPhoton_idx({df}, {output}, {input}, 0)',
    input=[
        q.dimuon_HiggsCand_collection,
        nanoAOD.Muon_fsrPhotonIdx,
        nanoAOD.FsrPhoton_relIso03,
        nanoAOD.FsrPhoton_dROverEt2,
        nanoAOD.FsrPhoton_pt,
        q.Muon_pt_corrected,
    ],
    output=[q.FsrPhotonIdx_1],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
leadingmuon_FsrPhotonIdx_4m = Producer(
    name="leadingmuon_FsrPhotonIdx_4m",
    call='physicsobject::FsrPhoton_idx({df}, {output}, {input}, 0)',
    input=[
        q.quadmuon_HiggsZCand_collection,
        nanoAOD.Muon_fsrPhotonIdx,
        nanoAOD.FsrPhoton_relIso03,
        nanoAOD.FsrPhoton_dROverEt2,
        nanoAOD.FsrPhoton_pt,
        q.Muon_pt_corrected,
    ],
    output=[q.FsrPhotonIdx_1],
    scopes=["mmmm", "mmmm_cr"],
)
subleadingmuon_FsrPhotonIdx = Producer(
    name="subleadingmuon_FsrPhotonIdx",
    call='physicsobject::FsrPhoton_idx({df}, {output}, {input}, 1)',
    input=[
        q.dimuon_HiggsCand_collection,
        nanoAOD.Muon_fsrPhotonIdx,
        nanoAOD.FsrPhoton_relIso03,
        nanoAOD.FsrPhoton_dROverEt2,
        nanoAOD.FsrPhoton_pt,
        q.Muon_pt_corrected,
    ],
    output=[q.FsrPhotonIdx_2],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
subleadingmuon_FsrPhotonIdx_4m = Producer(
    name="subleadingmuon_FsrPhotonIdx_4m",
    call='physicsobject::FsrPhoton_idx({df}, {output}, {input}, 1)',
    input=[
        q.quadmuon_HiggsZCand_collection,
        nanoAOD.Muon_fsrPhotonIdx,
        nanoAOD.FsrPhoton_relIso03,
        nanoAOD.FsrPhoton_dROverEt2,
        nanoAOD.FsrPhoton_pt,
        q.Muon_pt_corrected,
    ],
    output=[q.FsrPhotonIdx_2],
    scopes=["mmmm", "mmmm_cr"],
)

leadingmuon_FsrPhoton_pt = Producer(
    name="leadingmuon_FsrPhoton_pt",
    call="basefunctions::getvar<float>({df}, {output}, {input})",
    input=[q.FsrPhotonIdx_1, nanoAOD.FsrPhoton_pt],
    output=[q.FsrPhoton1_pt],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc", "mmmm", "mmmm_cr"],
)
leadingmuon_FsrPhoton_eta = Producer(
    name="leadingmuon_FsrPhoton_eta",
    call="basefunctions::getvar<float>({df}, {output}, {input})",
    input=[q.FsrPhotonIdx_1, nanoAOD.FsrPhoton_eta],
    output=[q.FsrPhoton1_eta],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc", "mmmm", "mmmm_cr"],
)
leadingmuon_FsrPhoton_phi = Producer(
    name="leadingmuon_FsrPhoton_phi",
    call="basefunctions::getvar<float>({df}, {output}, {input})",
    input=[q.FsrPhotonIdx_1, nanoAOD.FsrPhoton_phi],
    output=[q.FsrPhoton1_phi],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc", "mmmm", "mmmm_cr"],
)

subleadingmuon_FsrPhoton_pt = Producer(
    name="subleadingmuon_FsrPhoton_pt",
    call="basefunctions::getvar<float>({df}, {output}, {input})",
    input=[q.FsrPhotonIdx_2, nanoAOD.FsrPhoton_pt],
    output=[q.FsrPhoton2_pt],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc", "mmmm", "mmmm_cr"],
)
subleadingmuon_FsrPhoton_eta = Producer(
    name="subleadingmuon_FsrPhoton_eta",
    call="basefunctions::getvar<float>({df}, {output}, {input})",
    input=[q.FsrPhotonIdx_2, nanoAOD.FsrPhoton_eta],
    output=[q.FsrPhoton2_eta],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc", "mmmm", "mmmm_cr"],
)
subleadingmuon_FsrPhoton_phi = Producer(
    name="subleadingmuon_FsrPhoton_phi",
    call="basefunctions::getvar<float>({df}, {output}, {input})",
    input=[q.FsrPhotonIdx_2, nanoAOD.FsrPhoton_phi],
    output=[q.FsrPhoton2_phi],
    scopes=["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc", "mmmm", "mmmm_cr"],
)