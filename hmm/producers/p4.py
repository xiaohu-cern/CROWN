from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers used for get pt, eta, phi, mass from p4
####################

##### for mu1 from Higgs
#####
mu1_fromH_pt = Producer(
    name="mu1_fromH_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
    ],
    output=[q.mu1_fromH_pt],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu1_fromH_eta = Producer(
    name="mu1_fromH_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
    ],
    output=[q.mu1_fromH_eta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu1_fromH_phi = Producer(
    name="mu1_fromH_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
    ],
    output=[q.mu1_fromH_phi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu1_fromH_mass = Producer(
    name="mu1_fromH_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
    ],
    output=[q.mu1_fromH_mass],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

##### for mu2 from Higgs
#####
mu2_fromH_pt = Producer(
    name="mu2_fromH_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_H,
    ],
    output=[q.mu2_fromH_pt],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu2_fromH_eta = Producer(
    name="mu2_fromH_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_H,
    ],
    output=[q.mu2_fromH_eta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu2_fromH_phi = Producer(
    name="mu2_fromH_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_H,
    ],
    output=[q.mu2_fromH_phi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu2_fromH_mass = Producer(
    name="mu2_fromH_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_H,
    ],
    output=[q.mu2_fromH_mass],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

##### Higgs 
#####
H_pt = Producer(
    name="H_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.dimuon_p4_Higgs,
    ],
    output=[q.H_pt],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
H_eta = Producer(
    name="H_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.dimuon_p4_Higgs,
    ],
    output=[q.H_eta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
H_phi = Producer(
    name="H_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.dimuon_p4_Higgs,
    ],
    output=[q.H_phi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
H_mass = Producer(
    name="H_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.dimuon_p4_Higgs,
    ],
    output=[q.H_mass],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

##### for met pt and phi
#####
met_pt = Producer(
    name="met_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.met_p4,
    ],
    output=[q.met_pt],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
met_phi = Producer(
    name="met_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.met_p4,
    ],
    output=[q.met_phi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

##### for gen met pt and phi
#####
genmet_pt = Producer(
    name="genmet_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.genmet_p4,
    ],
    output=[q.genmet_pt],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
genmet_phi = Producer(
    name="genmet_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.genmet_p4,
    ],
    output=[q.genmet_phi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

##### for extra lepton
#####
extra_lep_pt = Producer(
    name="extra_lep_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
    ],
    output=[q.extra_lep_pt],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
extra_lep_eta = Producer(
    name="extra_lep_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
    ],
    output=[q.extra_lep_eta],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
extra_lep_phi = Producer(
    name="extra_lep_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
    ],
    output=[q.extra_lep_phi],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)
extra_lep_mass = Producer(
    name="extra_lep_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
    ],
    output=[q.extra_lep_mass],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
)

##### for muOS from Higgs
#####
muOS_pt = Producer(
    name="muOS_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.mu_p4_OSwithLep,
    ],
    output=[q.muOS_pt],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionc","m2m_dyfakeingmu_regionc"],
)
muOS_eta = Producer(
    name="muOS_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.mu_p4_OSwithLep,
    ],
    output=[q.muOS_eta],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionc","m2m_dyfakeingmu_regionc"],
)
muOS_phi = Producer(
    name="muOS_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.mu_p4_OSwithLep,
    ],
    output=[q.muOS_phi],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionc","m2m_dyfakeingmu_regionc"],
)
# muOS_mass = Producer(
#     name="muOS_mass",
#     call='quantities::mass({df}, {output}, {input})',
#     input=[
#       q.mu_p4_OSwithLep,
#     ],
#     output=[q.muOS_mass],
#     scopes=["e2m","m2m"],
# )

##### for muSS from Higgs
#####
muSS_pt = Producer(
    name="muSS_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.mu_p4_SSwithLep,
    ],
    output=[q.muSS_pt],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionc","m2m_dyfakeingmu_regionc"],
)
muSS_eta = Producer(
    name="muSS_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.mu_p4_SSwithLep,
    ],
    output=[q.muSS_eta],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionc","m2m_dyfakeingmu_regionc"],
)
muSS_phi = Producer(
    name="muSS_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.mu_p4_SSwithLep,
    ],
    output=[q.muSS_phi],
    scopes=["e2m","m2m","e2m_dyfakeinge_regionc","m2m_dyfakeingmu_regionc"],
)
# muSS_mass = Producer(
#     name="muSS_mass",
#     call='quantities::mass({df}, {output}, {input})',
#     input=[
#       q.mu_p4_SSwithLep,
#     ],
#     output=[q.muSS_mass],
#     scopes=["e2m","m2m"],
# )

##### for lep1 from Z
#####
lep1_fromZ_pt = Producer(
    name="lep1_fromZ_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.lepton_leadingp4_Z,
    ],
    output=[q.lep1_fromZ_pt],
    scopes=["eemm","mmmm"],
)
lep1_fromZ_eta = Producer(
    name="lep1_fromZ_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.lepton_leadingp4_Z,
    ],
    output=[q.lep1_fromZ_eta],
    scopes=["eemm","mmmm"],
)
lep1_fromZ_phi = Producer(
    name="lep1_fromZ_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.lepton_leadingp4_Z,
    ],
    output=[q.lep1_fromZ_phi],
    scopes=["eemm","mmmm"],
)
lep1_fromZ_mass = Producer(
    name="lep1_fromZ_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.lepton_leadingp4_Z,
    ],
    output=[q.lep1_fromZ_mass],
    scopes=["eemm","mmmm"],
)

##### for lep2 from Z
#####
lep2_fromZ_pt = Producer(
    name="lep2_fromZ_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.lepton_subleadingp4_Z,
    ],
    output=[q.lep2_fromZ_pt],
    scopes=["eemm","mmmm"],
)
lep2_fromZ_eta = Producer(
    name="lep2_fromZ_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.lepton_subleadingp4_Z,
    ],
    output=[q.lep2_fromZ_eta],
    scopes=["eemm","mmmm"],
)
lep2_fromZ_phi = Producer(
    name="lep2_fromZ_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.lepton_subleadingp4_Z,
    ],
    output=[q.lep2_fromZ_phi],
    scopes=["eemm","mmmm"],
)
lep2_fromZ_mass = Producer(
    name="lep2_fromZ_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.lepton_subleadingp4_Z,
    ],
    output=[q.lep2_fromZ_mass],
    scopes=["eemm","mmmm"],
)

##### for Z in 4l category
#####
Z_pt = Producer(
    name="Z_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.dilepton_p4_Z,
    ],
    output=[q.Z_pt],
    scopes=["eemm","mmmm"],
)
Z_eta = Producer(
    name="Z_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.dilepton_p4_Z,
    ],
    output=[q.Z_eta],
    scopes=["eemm","mmmm"],
)
Z_phi = Producer(
    name="Z_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.dilepton_p4_Z,
    ],
    output=[q.Z_phi],
    scopes=["eemm","mmmm"],
)
Z_mass = Producer(
    name="Z_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.dilepton_p4_Z,
    ],
    output=[q.Z_mass],
    scopes=["eemm","mmmm"],
)

genmu1_fromH_pt = Producer(
    name="genmu1_fromH_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.genmuon_leadingp4_H,
    ],
    output=[q.genmu1_fromH_pt],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)
genmu1_fromH_eta = Producer(
    name="genmu1_fromH_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.genmuon_leadingp4_H,
    ],
    output=[q.genmu1_fromH_eta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)
genmu1_fromH_phi = Producer(
    name="genmu1_fromH_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.genmuon_leadingp4_H,
    ],
    output=[q.genmu1_fromH_phi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)
genmu1_fromH_mass = Producer(
    name="genmu1_fromH_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.genmuon_leadingp4_H,
    ],
    output=[q.genmu1_fromH_mass],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)

genmu2_fromH_pt = Producer(
    name="genmu2_fromH_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.genmuon_subleadingp4_H,
    ],
    output=[q.genmu2_fromH_pt],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)
genmu2_fromH_eta = Producer(
    name="genmu2_fromH_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.genmuon_subleadingp4_H,
    ],
    output=[q.genmu2_fromH_eta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)
genmu2_fromH_phi = Producer(
    name="genmu2_fromH_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.genmuon_subleadingp4_H,
    ],
    output=[q.genmu2_fromH_phi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)
genmu2_fromH_mass = Producer(
    name="genmu2_fromH_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.genmuon_subleadingp4_H,
    ],
    output=[q.genmu2_fromH_mass],
    scopes=["e2m","m2m","eemm","mmmm","nnmm"],
)
## for fatjet + mm channel
fatjet_pt = Producer(
    name="fatjet_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_pt],
    scopes=["fjmm","fjmm_cr"],
)
fatjet_eta = Producer(
    name="fatjet_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_eta],
    scopes=["fjmm","fjmm_cr"],
)
fatjet_phi = Producer(
    name="fatjet_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_phi],
    scopes=["fjmm","fjmm_cr"],
)
fatjet_mass = Producer(
    name="fatjet_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_mass],
    scopes=["fjmm","fjmm_cr"],
)
# Zmass CR's mu1, mu2
mu1_fromZCR_pt = Producer(
    name="mu1_fromZCR_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_Z_CR,
    ],
    output=[q.mu1_fromZCR_pt],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
mu1_fromZCR_eta = Producer(
    name="mu1_fromZCR_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_Z_CR,
    ],
    output=[q.mu1_fromZCR_eta],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
mu1_fromZCR_phi = Producer(
    name="mu1_fromZCR_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_Z_CR,
    ],
    output=[q.mu1_fromZCR_phi],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
##### mu2 #####
mu2_fromZCR_pt = Producer(
    name="mu2_fromZCR_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_Z_CR,
    ],
    output=[q.mu2_fromZCR_pt],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
mu2_fromZCR_eta = Producer(
    name="mu2_fromZCR_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_Z_CR,
    ],
    output=[q.mu2_fromZCR_eta],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)
mu2_fromZCR_phi = Producer(
    name="mu2_fromZCR_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_Z_CR,
    ],
    output=[q.mu2_fromZCR_phi],
    scopes=["fjmm_cr",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond"],
)

jet1_pt = Producer(
    name="jet1_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.jet_p4_1,
    ],
    output=[q.jet1_pt],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
jet1_eta = Producer(
    name="jet1_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.jet_p4_1,
    ],
    output=[q.jet1_eta],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
jet1_phi = Producer(
    name="jet1_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.jet_p4_1,
    ],
    output=[q.jet1_phi],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
jet1_mass = Producer(
    name="jet1_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.jet_p4_1,
    ],
    output=[q.jet1_mass],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

jet2_pt = Producer(
    name="jet2_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.jet_p4_2,
    ],
    output=[q.jet2_pt],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
jet2_eta = Producer(
    name="jet2_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.jet_p4_2,
    ],
    output=[q.jet2_eta],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
jet2_phi = Producer(
    name="jet2_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.jet_p4_2,
    ],
    output=[q.jet2_phi],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
jet2_mass = Producer(
    name="jet2_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.jet_p4_2,
    ],
    output=[q.jet2_mass],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
#### MHT_p4 ####
MHT_pt = Producer(
    name="MHT_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.MHT_p4,
    ],
    output=[q.MHT_pt],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MHT_eta = Producer(
    name="MHT_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.MHT_p4,
    ],
    output=[q.MHT_eta],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MHT_phi = Producer(
    name="MHT_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.MHT_p4,
    ],
    output=[q.MHT_phi],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MHT_mass = Producer(
    name="MHT_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.MHT_p4,
    ],
    output=[q.MHT_mass],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
#### MHTALL_p4 ####
MHTALL_pt = Producer(
    name="MHTALL_pt",
    call='quantities::pt({df}, {output}, {input})',
    input=[
      q.MHTALL_p4,
    ],
    output=[q.MHTALL_pt],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MHTALL_eta = Producer(
    name="MHTALL_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.MHTALL_p4,
    ],
    output=[q.MHTALL_eta],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MHTALL_phi = Producer(
    name="MHTALL_phi",
    call='quantities::phi({df}, {output}, {input})',
    input=[
      q.MHTALL_p4,
    ],
    output=[q.MHTALL_phi],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
MHTALL_mass = Producer(
    name="MHTALL_mass",
    call='quantities::mass({df}, {output}, {input})',
    input=[
      q.MHTALL_p4,
    ],
    output=[q.MHTALL_mass],
    scopes=["e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
            "nnmm_dycontrol","nnmm_topcontrol",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
### pt W and phi W
W_pt = Producer(
    name="W_pt",
    call='physicsobject::pt_W({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
      q.met_p4,
    ],
    output=[q.W_pt],
    scopes=["e2m","m2m",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)
W_phi = Producer(
    name="W_phi",
    call='physicsobject::phi_W({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
      q.met_p4,
    ],
    output=[q.W_phi],
    scopes=["e2m","m2m",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
)

calc_pz_nu = Producer(
    name="calc_pz_nu",
    call='quantities::calculateNeutrinoPz({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
      q.met_p4,
    ],
    output=[q.pz_nu],
    scopes=["e2m","m2m"],
)

calc_nu_p4 = Producer(
    name="calc_nu_p4",
    call='physicsobject::build_nup4({df}, {output}, {input})',
    input=[
      q.met_p4,
      q.pz_nu,
    ],
    output=[q.nu_p4],
    scopes=["e2m","m2m"],
)

calc_W_p4 = Producer(
    name="calc_W_p4",
    call='physicsobject::build_Wp4({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
      q.nu_p4,
    ],
    output=[q.W_p4],
    scopes=["e2m","m2m"],
)

W_eta = Producer(
    name="W_eta",
    call='quantities::eta({df}, {output}, {input})',
    input=[
      q.W_p4,
    ],
    output=[q.W_eta],
    scopes=["e2m","m2m"],
)

### mu1_H_dR

mu1_H_dR = Producer(
    name="mu1_H_dR",
    call='quantities::deltaR({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
      q.dimuon_p4_Higgs,
    ],
    output=[q.mu1_H_dR],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)



### add by Leyan 2024/12/20
HT = Producer(
    name="HT",
    call='quantities::scalarPtSum({df}, {output}, {input})',
    input=[
      q.extra_lep_pt,
      q.mu1_fromH_pt,
      q.mu2_fromH_pt,
    ],
    output=[q.HT],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

### add by Leyan 2024/12/20
HT_met = Producer(
    name="HT_met",
    call='quantities::scalarPtSum_met({df}, {output}, {input})',
    input=[
      q.extra_lep_pt,
      q.mu1_fromH_pt,
      q.mu2_fromH_pt,
      q.met_pt
    ],
    output=[q.HT_met],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)




mu1_H_deta = Producer(
  name = "mu1_H_deta",
  call = "quantities::deltaEta({df}, {output}, {input})",
  input = [
    q.muon_leadingp4_H,
    q.dimuon_p4_Higgs,
  ],
  output = [q.mu1_H_deta],
  scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu1_H_dphi = Producer(
  name = "mu1_H_dphi",
  call = "quantities::deltaPhi({df}, {output}, {input})",
  input = [
    q.muon_leadingp4_H,
    q.dimuon_p4_Higgs,
  ],
  output = [q.mu1_H_dphi],
  scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu2_H_dR = Producer(
    name="mu2_H_dR",
    call='quantities::deltaR({df}, {output}, {input})',
    input=[
      q.muon_subleadingp4_H,
      q.dimuon_p4_Higgs,
    ],
    output=[q.mu2_H_dR],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu2_H_deta = Producer(
  name = "mu2_H_deta",
  call = "quantities::deltaEta({df}, {output}, {input})",
  input = [
    q.muon_subleadingp4_H,
    q.dimuon_p4_Higgs,
  ],
  output = [q.mu2_H_deta],
  scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu2_H_dphi = Producer(
  name = "mu2_H_dphi",
  call = "quantities::deltaPhi({df}, {output}, {input})",
  input = [
    q.muon_subleadingp4_H,
    q.dimuon_p4_Higgs,
  ],
  output = [q.mu2_H_dphi],
  scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu1_mu2_dR = Producer(
    name="mu1_mu2_dR",
    call='quantities::deltaR({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
      q.muon_subleadingp4_H,
    ],
    output=[q.mu1_mu2_dR],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu1_mu2_deta = Producer(
    name="mu1_mu2_deta",
    call='quantities::deltaEta({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
      q.muon_subleadingp4_H,
    ],
    output=[q.mu1_mu2_deta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
mu1_mu2_dphi = Producer(
    name="mu1_mu2_dphi",
    call='quantities::deltaPhi({df}, {output}, {input})',
    input=[
      q.muon_leadingp4_H,
      q.muon_subleadingp4_H,
    ],
    output=[q.mu1_mu2_dphi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

ptH_ov_massH = Producer(
    name = "ptH_ov_massH",
    call = "quantities::calc_ratio({df}, {output}, {input})",
    input = [
      q.H_pt,
      q.H_mass,
    ],
    output = [q.ptH_ov_massH],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

ptmu1_ov_ptH = Producer(
     name = "ptmu1_ov_ptH",
     call = "quantities::calc_ratio({df}, {output}, {input})",
     input = [
       q.mu1_fromH_pt,
       q.H_pt,
     ],
     output = [q.ptmu1_ov_ptH],
     scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

ptmu2_ov_ptH = Producer(
     name = "ptmu2_ov_ptH",
     call = "quantities::calc_ratio({df}, {output}, {input})",
     input = [
       q.mu2_fromH_pt,
       q.H_pt,
     ],
     output = [q.ptmu2_ov_ptH],
     scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

ptmu1_ov_massH = Producer(
     name = "ptmu1_ov_massH",
     call = "quantities::calc_ratio({df}, {output}, {input})",
     input = [
       q.mu1_fromH_pt,
       q.H_mass,
     ],
     output = [q.ptmu1_ov_massH],
     scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

ptmu2_ov_massH = Producer(
     name = "ptmu2_ov_massH",
     call = "quantities::calc_ratio({df}, {output}, {input})",
     input = [
       q.mu2_fromH_pt,
       q.H_mass,
     ],
     output = [q.ptmu2_ov_massH],
     scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)



### add by Leyan 2024/12/20
nu_H_dR = Producer(
    name="nu_H_dR",
    call='quantities::deltaR({df}, {output}, {input})',
    input=[
      q.dimuon_p4_Higgs,
      q.nu_p4,
    ],
    output=[q.nu_H_dR],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu1_nu_dR = Producer(
    name = "mu1_nu_dR",
    call = "quantities::deltaR({df}, {output}, {input})",
    input = [
      q.muon_leadingp4_H,
      q.nu_p4,
    ],
    output = [q.mu1_nu_dR],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu1_nu_deta = Producer(
    name = "mu1_nu_deta",
    call = "quantities::deltaEta({df}, {output}, {input})",
    input = [
      q.muon_leadingp4_H,
      q.nu_p4,
    ],
    output = [q.mu1_nu_deta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu1_nu_dphi = Producer(
    name = "mu1_nu_dphi",
    call = "quantities::deltaPhi({df}, {output}, {input})",
    input = [
      q.muon_leadingp4_H,
      q.nu_p4,
    ],
    output = [q.mu1_nu_dphi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu2_nu_dR = Producer(
    name = "mu2_nu_dR",
    call = "quantities::deltaR({df}, {output}, {input})",
    input = [
      q.muon_subleadingp4_H,
      q.nu_p4,
    ],
    output = [q.mu2_nu_dR],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)
### add by Leyan 2024/12/20
nu_H_deta =  Producer(
    name="nu_H_deta",
    call='quantities::deltaEta({df}, {output}, {input})',
    input=[
      q.dimuon_p4_Higgs,
      q.nu_p4,
    ],
    output=[q.nu_H_deta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

### add by Leyan 2024/12/20
nu_H_dphi = Producer(
    name="nu_H_dphi",
    call='quantities::deltaPhi({df}, {output}, {input})',
    input=[
      q.dimuon_p4_Higgs,
      q.nu_p4,
    ],
    output=[q.nu_H_dphi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)



### add by Leyan 2024/12/20
lep_nu_dR = Producer(
    name="lep_nu_dR",
    call='quantities::deltaR({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
      q.nu_p4,
    ],
    output=[q.lep_nu_dR],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

lep_nu_deta = Producer(
    name="lep_nu_deta",
    call='quantities::deltaEta({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
      q.nu_p4,
    ],
    output=[q.lep_nu_deta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)


lep_nu_dphi = Producer(
    name="lep_nu_dphi",
    call='quantities::deltaPhi({df}, {output}, {input})',
    input=[
      q.extra_lep_p4,
      q.nu_p4,
    ],
    output=[q.lep_nu_dphi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)





mu2_nu_deta = Producer(
    name = "mu2_nu_deta",
    call = "quantities::deltaEta({df}, {output}, {input})",
    input = [
      q.muon_subleadingp4_H,
      q.nu_p4,
    ],
    output = [q.mu2_nu_deta],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

mu2_nu_dphi = Producer(
    name = "mu2_nu_dphi",
    call = "quantities::deltaPhi({df}, {output}, {input})",
    input = [
      q.muon_subleadingp4_H,
      q.nu_p4,
    ],
    output = [q.mu2_nu_dphi],
    scopes=["e2m","m2m","eemm","mmmm","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
)

ThreeLepQuantities = ProducerGroup(
    name="ThreeLepQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["e2m", "m2m"],
    subproducers=[
      mu1_H_dR,
      mu1_H_deta,
      mu1_H_dphi,
      mu2_H_dR,
      mu2_H_deta,
      mu2_H_dphi,
      calc_pz_nu,
      mu1_mu2_dR,
      mu1_mu2_deta,
      mu1_mu2_dphi,
      HT,          ### add by Leyan 2024/12/20
      ptH_ov_massH,
      ptmu1_ov_ptH,
      ptmu2_ov_ptH,
      ptmu1_ov_massH,
      ptmu2_ov_massH,
      calc_nu_p4,
      mu1_nu_dR,
      mu1_nu_deta,
      mu1_nu_dphi,
      mu2_nu_dR,
      mu2_nu_deta,
      mu2_nu_dphi,
      HT_met,    ### add by Leyan 2024/12/20
      nu_H_deta,  ### add by Leyan 2024/12/20
      nu_H_dphi,  ### add by Leyan 2024/12/20
      nu_H_dR,   ### add by Leyan 2024/12/20
      lep_nu_dR,  ### add by Leyan 2024/12/20
      lep_nu_dphi, ### add by Leyan 2024/12/20
      lep_nu_deta, ### add by Leyan 2024/12/20
      
      calc_W_p4,
      W_eta, # W_pt, W_phi already finished
    ],
)
