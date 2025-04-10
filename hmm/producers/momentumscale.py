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
    output=[q.Muon_pt_corrected],
    scopes=["nnmm","fjmm"],
    # scopes=["global"],
)
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
