from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import event as event
from .producers import triggers as triggers
from .producers import genparticles as genparticles
from .producers import muons as muons
from .producers import jets as jets
from .producers import scalefactors as scalefactors
# add by botao
from .producers import lepton as lepton
from .producers import electrons as electrons
from .producers import met as met
from .producers import p4 as p4
from .producers import cr as cr
from .producers import fatjets as fatjets
from .producers import momentumscale as momentumscale
from .producers import fsrphoton as fsrphoton
# end 
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
# shift
from .jet_variations import add_jetVariations
from .fatjet_variations import add_fatjetVariations
from .btag_variations import add_btagVariations

from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import RemoveProducer, AppendProducer, ReplaceProducer
from code_generation.systematics import SystematicShift, SystematicShiftByQuantity


def build_config(
    era: str,
    sample: str,
    scopes: List[str],
    shifts: List[str],
    available_sample_types: List[str],
    available_eras: List[str],
    available_scopes: List[str],
):

    configuration = Configuration(
        era,
        sample,
        scopes,
        shifts,
        available_sample_types,
        available_eras,
        available_scopes,
    )

    configuration.add_config_parameters(
        "global",
        {
            "PU_reweighting_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/LUM/2016preVFP_UL/puWeights.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/LUM/2016postVFP_UL/puWeights.json.gz",
                    "2017": "data/jsonpog-integration/POG/LUM/2017_UL/puWeights.json.gz",
                    "2018": "data/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz",
                    "2022preEE": "data/jsonpog-integration/POG/LUM/2022_Summer22/puWeights.json.gz",
                    "2022postEE": "data/jsonpog-integration/POG/LUM/2022_Summer22EE/puWeights.json.gz",
                    "2023preBPix": "data/jsonpog-integration/POG/LUM/2023_Summer23/puWeights.json.gz",
                    "2023postBPix": "data/jsonpog-integration/POG/LUM/2023_Summer23BPix/puWeights.json.gz",
                    "2024": "data/2024_correction/puWeights_BCDEFGHI.json.gz",
                    "2025": "data/2025_correction/puWeights_2025pp_Golden_Summer24_25ns_69200ub.json.gz",
                }
            ),
            "PU_reweighting_era": EraModifier(
                {
                    "2016preVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2016postVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2017": "Collisions17_UltraLegacy_goldenJSON",
                    "2018": "Collisions18_UltraLegacy_goldenJSON",
                    "2022preEE": "Collisions2022_355100_357900_eraBCD_GoldenJson", 
                    "2022postEE": "Collisions2022_359022_362760_eraEFG_GoldenJson", 
                    "2023preBPix": "Collisions2023_366403_369802_eraBC_GoldenJson",
                    "2023postBPix": "Collisions2023_369803_370790_eraD_GoldenJson",
                    "2024": "Collisions24_BCDEFGHI_goldenJSON",
                    "2025": "Collisions25_goldenJSON",
                }
            ),
            "PU_reweighting_variation": "nominal",
            # "PU_reweighting_file": EraModifier(
            #     {
            #         "2016preVFP": "data/pileup/Data_Pileup_2016_271036-284044_13TeVMoriond17_23Sep2016ReReco_69p2mbMinBiasXS.root",
            #         "2016postVFP": "data/pileup/Data_Pileup_2016_271036-284044_13TeVMoriond17_23Sep2016ReReco_69p2mbMinBiasXS.root",
            #         "2017": "data/pileup/Data_Pileup_2017_294927-306462_13TeVSummer17_PromptReco_69p2mbMinBiasXS.root",
            #         "2018": "data/pileup/Data_Pileup_2018_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18.root",
            #         # "2022": need to update now
            #         "2022preEE": "data/pileup/Data_Pileup_2018_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18.root",
            #         "2022postEE": "data/pileup/Data_Pileup_2018_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18.root",
            #     }
            # ),
            "golden_json_file": EraModifier(
                {
                    "2016preVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2016postVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2017": "data/golden_json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                    "2018": "data/golden_json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                    "2022preEE": "data/golden_json/Cert_Collisions2022_355100_362760_GoldenJSON.txt",
                    "2022postEE": "data/golden_json/Cert_Collisions2022_355100_362760_GoldenJSON.txt",
                    "2023preBPix": "data/golden_json/Cert_Collisions2023_366442_370790_Golden.txt",
                    "2023postBPix": "data/golden_json/Cert_Collisions2023_366442_370790_Golden.txt",
                    "2024": "data/golden_json/Cert_Collisions2024_378981_386951_Golden.txt",
                    "2025": "data/golden_json/Cert_Collisions2025_391658_398903_Golden.txt",
                }
            ),
            "PU_reweighting_hist": "pileup",
            "met_filters": EraModifier(
                {
                    "2016preVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                    ],
                    "2016postVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                    ],
                    "2017": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    "2018": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Run_3_2022_and_2023_data_and_MC
                    "2022preEE": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        # "Flag_HBHENoiseFilter",
                        # "Flag_HBHENoiseIsoFilter", # HBHE and HBHEiso noise filters are no longer needed.
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_hfNoisyHitsFilter",
                        "Flag_eeBadScFilter",
                        # "Flag_ecalBadCalibFilter",
                    ],
                    "2022postEE": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_hfNoisyHitsFilter",
                        "Flag_eeBadScFilter",
                        # "Flag_ecalBadCalibFilter",
                    ],
                    "2023preBPix": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_hfNoisyHitsFilter",
                        "Flag_eeBadScFilter",
                        # "Flag_ecalBadCalibFilter",
                    ],
                    "2023postBPix": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_hfNoisyHitsFilter",
                        "Flag_eeBadScFilter",
                        # "Flag_ecalBadCalibFilter",
                    ],
                    ##### Mingxuan added
                    "2024": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_BadPFMuonDzFilter",
                        "Flag_hfNoisyHitsFilter",
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    "2025": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_BadPFMuonDzFilter",
                        "Flag_hfNoisyHitsFilter",
                        "Flag_eeBadScFilter",
                        # "Flag_ecalBadCalibFilter", ### work in progress, under construction
                    ],
                }
            ),
        },
    )
    ### DY ptll reweighting
    configuration.add_config_parameters(
        scopes,
        {
            "zptmass_file": EraModifier(
                {
                    "2016preVFP": "data/zpt/htt_scalefactors_legacy_2016.root",  # ToDO: Measured in legacy, therefore the same for pre- and postVFP for now
                    "2016postVFP": "data/zpt/htt_scalefactors_legacy_2016.root",  # ToDO: Measured in legacy, therefore the same for pre- and postVFP for now
                    "2017": "data/zpt/htt_scalefactors_legacy_2017.root",
                    "2018": "data/zpt/htt_scalefactors_legacy_2018.root",
                    "2022preEE": "data/zpt/DY_pTll_weights_2022preEE_v5.json.gz", ## This correction is also applied when we derived DY control region, so keep it
                    "2022postEE": "data/zpt/DY_pTll_weights_2022postEE_v5.json.gz",
                    "2023preBPix": "data/zpt/DY_pTll_weights_2023preBPix_v5.json.gz", 
                    "2023postBPix": "data/zpt/DY_pTll_weights_2023postBPix_v5.json.gz", ### still not found for 2024
                    "2024": "data/zpt/DY_pTll_weights_2024_v5.json.gz",
                    "2025": "data/zpt/DY_pTll_weights_2024_v5.json.gz", ### TODO need to update for 2025
                }
            ),
            # "zptmass_functor": "zptmass_weight_nom",
            # "zptmass_arguments": "z_gen_mass,z_gen_pt",
            "DY_pTll_reweighting_syst" : "nom",
        },
    )
    
    # vh add triggers (copying htautau mtau TODO)
    configuration.add_config_parameters(
        scopes,
        # ["e2m","m2m","eemm","mmmm","nnmm","fjmm","nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb"],
        {
            "singlemuon_trigger": EraModifier(
                {
                # vh TODO update pT threshold in trigger matching
                ### Mingxuan added for 2024 TODO need to check the exact number and name
                    "2025": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 26,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 29,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu50",
                            "hlt_path": "HLT_Mu50",
                            "ptcut": 52,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tkmu100",
                            "hlt_path": "HLT_HighPtTkMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_casmu100",
                            "hlt_path": "HLT_CascadeMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2024": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 26,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 29,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu50",
                            "hlt_path": "HLT_Mu50",
                            "ptcut": 52,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tkmu100",
                            "hlt_path": "HLT_HighPtTkMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_casmu100",
                            "hlt_path": "HLT_CascadeMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2023preBPix": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 26,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 29,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu50",
                            "hlt_path": "HLT_Mu50",
                            "ptcut": 52,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tkmu100",
                            "hlt_path": "HLT_HighPtTkMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_casmu100",
                            "hlt_path": "HLT_CascadeMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2023postBPix": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 26,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 29,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu50",
                            "hlt_path": "HLT_Mu50",
                            "ptcut": 52,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tkmu100",
                            "hlt_path": "HLT_HighPtTkMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_casmu100",
                            "hlt_path": "HLT_CascadeMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022preEE": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 26,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 29,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu50",
                            "hlt_path": "HLT_Mu50",
                            "ptcut": 52,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tkmu100",
                            "hlt_path": "HLT_HighPtTkMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_casmu100",
                            "hlt_path": "HLT_CascadeMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 26,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 29,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu50",
                            "hlt_path": "HLT_Mu50",
                            "ptcut": 52,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tkmu100",
                            "hlt_path": "HLT_HighPtTkMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_casmu100",
                            "hlt_path": "HLT_CascadeMu100",
                            "ptcut": 102,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )

    configuration.add_config_parameters(
        ["nnmm"],
        # ["e2m","m2m","eemm","mmmm","nnmm","fjmm","nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb"],
        {
            "MET_trigger": EraModifier(
                {
                    "2025": [
                        {
                            "flagname": "trg_MET110_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight",
                        },
                        {
                            "flagname": "trg_MET120_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight_PFHT60",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                        },
                        {
                            "flagname": "trg_MET130_Tight",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight",
                        },
                        {
                            "flagname": "trg_MET130_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET140_Tight",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight",
                        },
                        {
                            "flagname": "trg_MET140_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF",
                        },
                    ],
                    "2024": [
                        {
                            "flagname": "trg_MET110_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight",
                        },
                        {
                            "flagname": "trg_MET120_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight_PFHT60",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                        },
                        {
                            "flagname": "trg_MET130_Tight",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight",
                        },
                        {
                            "flagname": "trg_MET130_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET140_Tight",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight",
                        },
                        {
                            "flagname": "trg_MET140_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF",
                        },
                    ],
                    "2023preBPix": [
                        {
                            "flagname": "trg_MET110_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight",
                        },
                        {
                            "flagname": "trg_MET120_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight_PFHT60",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                        },
                        {
                            "flagname": "trg_MET130_Tight",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight",
                        },
                        {
                            "flagname": "trg_MET130_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET140_Tight",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight",
                        },
                        {
                            "flagname": "trg_MET140_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF",
                        },
                    ],
                    "2023postBPix": [
                        {
                            "flagname": "trg_MET110_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight",
                        },
                        {
                            "flagname": "trg_MET120_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight_PFHT60",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                        },
                        {
                            "flagname": "trg_MET130_Tight",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight",
                        },
                        {
                            "flagname": "trg_MET130_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET140_Tight",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight",
                        },
                        {
                            "flagname": "trg_MET140_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF",
                        },
                    ],
                    "2022preEE": [
                        {
                            "flagname": "trg_MET110_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight",
                        },
                        {
                            "flagname": "trg_MET120_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight_PFHT60",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                        },
                        {
                            "flagname": "trg_MET130_Tight",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight",
                        },
                        {
                            "flagname": "trg_MET130_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET140_Tight",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight",
                        },
                        {
                            "flagname": "trg_MET140_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF",
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_MET110_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight",
                        },
                        {
                            "flagname": "trg_MET120_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET120_Tight_PFHT60",
                            "hlt_path": "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                        },
                        {
                            "flagname": "trg_MET130_Tight",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight",
                        },
                        {
                            "flagname": "trg_MET130_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF",
                        },
                        {
                            "flagname": "trg_MET140_Tight",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight",
                        },
                        {
                            "flagname": "trg_MET140_Tight_FilterHF",
                            "hlt_path": "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF",
                        },
                    ],
                }
            ),
        },
    )
    
    # add muon trigger scalefactors
    # 
    configuration.add_config_parameters(
        scopes,
        {
            # muon hlt trigger sfs for 2022
            # https://gitlab.cern.ch/cms-muonPOG/muonefficiencies/-/blob/master/Run3/2022/2022_Z/HLT/json/ScaleFactors_Muon_Z_HLT_2022_abseta_pt_schemaV2.json
            "mc_muon_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/muon_2016preVFPUL.json.gz",
                    "2016postVFP": "data/embedding/muon_2016postVFPUL.json.gz",
                    "2017": "data/embedding/muon_2017UL.json.gz",
                    "2018": "data/embedding/muon_2018UL.json.gz",
                    "2022preEE": "data/muon_corrections/HLT/2022preEE/ScaleFactors_Muon_Z_HLT_2022_abseta_pt_schemaV2.json.gz",
                    "2022postEE": "data/muon_corrections/HLT/2022postEE/ScaleFactors_Muon_Z_HLT_2022_EE_abseta_pt_schemaV2.json.gz",
                    "2023preBPix": "data/muon_corrections/HLT/2023preBPix/ScaleFactors_Muon_Z_HLT_2023_abseta_pt_schemaV2.json.gz",
                    "2023postBPix": "data/muon_corrections/HLT/2023postBPix/ScaleFactors_Muon_Z_HLT_2023_BPix_abseta_pt_schemaV2.json.gz",
                    "2024": "data/muon_corrections/HLT/2024/ScaleFactors_Muon_Z_HLT_2024_eta_pt_schemaV2.json.gz",
                    "2025": "data/muon_corrections/HLT/2025/ScaleFactors_Muon_Z_HLT_2025_eta_pt_schemaV2.json.gz",
                }
            ),
            # "KIT_sf_file": EraModifier(
            #     {
            #         "2022preEE": "data/muon_corrections/KIT_Corr/2022_Summer22.json",
            #         "2022postEE": "data/muon_corrections/KIT_Corr/2022_Summer22EE.json",
            #         "2023preBPix": "data/muon_corrections/KIT_Corr/2023_Summer23.json",
            #         "2023postBPix": "data/muon_corrections/KIT_Corr/2023_Summer23BPix.json",
            #     }
            # ),
            # "Rochester_sf_file": EraModifier(
            #     {
            #         "2022preEE": "data/muon_corrections/RoccoR/RoccoR2022.txt",
            #         "2022postEE": "data/muon_corrections/RoccoR/RoccoR2022EE.txt",
            #         "2023preBPix": "data/muon_corrections/RoccoR/RoccoR2023.txt",
            #         "2023postBPix": "data/muon_corrections/RoccoR/RoccoR2023BPix.txt",
            #     }
            # ),
            "singlemuon_trigger_sf_mc": EraModifier(
                {   
                    "2025": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2024": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2023preBPix": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2023postBPix": [
                        {   
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2022preEE": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2022postEE": [
                        {   
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_trigger_sf": "Trg_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_trigger_sf": "Trg_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                }
            ),
            "singlemuon_trigger_sf_mc_highPt": EraModifier(
                {   
                    "2025": [
                        {
                            "flagname": "trg_wgt_single_mu50",
                            "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                    "2024": [
                        {
                            "flagname": "trg_wgt_single_mu50",
                            "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                    "2023preBPix": [
                        {
                            "flagname": "trg_wgt_single_mu50",
                            "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                    "2023postBPix": [
                        {
                            "flagname": "trg_wgt_single_mu50",
                            "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                    "2022preEE": [
                        {
                            "flagname": "trg_wgt_single_mu50",
                            "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_wgt_single_mu50",
                            "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                            "mc_muon_sf_correctiontype": "nominal",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                }
            ),
            
            # "mc_muon_id_extrapolation": 1.0,  # for nominal case
            # "mc_muon_iso_extrapolation": 1.0,  # for nominal case
        },
    )

    # muon base selection:
    configuration.add_config_parameters(
        ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr", "fjmm_cr", "fjmm", "nnmm",
            "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
        {
            "min_muon_pt": 20, # vh change muon min pt 20 to 5
            "max_muon_eta": 2.4, # vh
            "max_muon_dxy": 0.05, # vh
            "max_muon_dz": 0.10, # vh
            "muon_max_sip3d" : 8.0, # vh
            "base_muon_id" : "Muon_looseId",
            "base_muon_iso_cut" : 0.7,
            
            # for good muon
            "min_goodmuon_mvaTTH" : 0.4,
            "PromptMVA_BDT_muon_name" : "BDTG",
            "muon_xml_path": "data/22-23_correction_new/MUO/Muon-mvaTTH.2022EE.weights.xml",
            "good_muon_id_medium": "Muon_mediumId", # vh cut-based atm https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#Medium_Muon
            "good_muon_id_highpt": "Muon_highPtId", # vh high pt muon ID
            "good_muon_id_highpt_bit": 1, #### 1 tracker high pt, 2 global high pt. require >=1
            "good_muon_iso_cut": 0.25, # vh PFIsoLoose dR=0.4 https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#Particle_Flow_isolation
        },
    )
    # electron base selection:
    configuration.add_config_parameters(
        "global",
        {
            # for base ele v1, 
            "min_ele_pt": 20,
            "max_ele_eta": 2.5,
            "upper_threshold_barrel": 1.444,
            "lower_threshold_endcap": 1.566,
            "max_ele_dxy": 0.05,
            "max_ele_dz": 0.10,
            "ele_conv_veto": "Electron_convVeto",
            "ele_missing_hits": 2,
            "ele_max_sip3d" : 8.0, # vh
            
            # extract from base ele v1 for base ele v2
            # UChar_t for v12, Int_t for v9
            "base_ele_cutbaseid": 2, # cut-based ID RunIII Winter22 (0:fail, 1:veto, 2:loose, 3:medium, 4:tight)
            
            # extract from base ele v1 for good ele
            "min_goodelectron_mvaTTH" : 0.4,
            "PromptMVA_BDT_electron_name" : "BDTG",
            "electron_xml_path": "data/22-23_correction_new/EGM/Electron-mvaTTH.2022EE.weights_mvaISO.xml",
            "good_ele_id": EraModifier(
                {
                    "2016preVFP": "Electron_mvaFall17V2Iso_WP90",
                    "2016postVFP": "Electron_mvaFall17V2Iso_WP90",
                    "2017": "Electron_mvaFall17V2Iso_WP90",
                    "2018": "Electron_mvaFall17V2Iso_WP90",
                    "2022preEE": "Electron_mvaIso_WP90",
                    "2022postEE": "Electron_mvaIso_WP90",
                    "2023preBPix": "Electron_mvaIso_WP90",
                    "2023postBPix": "Electron_mvaIso_WP90",
                    "2024": "Electron_mvaIso_WP90",
                    "2025": "Electron_mvaIso_WP90",
                }
            ),
        }
    )
    # Muon scale factors configuration
    configuration.add_config_parameters(
        scopes,
        # ["e2m","m2m","eemm","mmmm","nnmm","nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","e2m_dyfakeinge_regionb"],
        {
            "muon_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/MUO/2016preVFP_UL/muon_Z.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/MUO/2016postVFP_UL/muon_Z.json.gz",
                    "2017": "data/jsonpog-integration/POG/MUO/2017_UL/muon_Z.json.gz",
                    "2018": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z.json.gz",
                    # "2022preEE": "data/jsonpog-integration/POG/MUO/2022_27Jun2023/muon_Z.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    # "2022postEE": "data/jsonpog-integration/POG/MUO/2022EE_27Jun2023/muon_Z.json.gz",
                    "2022preEE": "data/jsonpog-integration/POG/MUO/2022_Summer22/muon_Z.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    "2022postEE": "data/jsonpog-integration/POG/MUO/2022_Summer22EE/muon_Z.json.gz",
                    "2023preBPix": "data/jsonpog-integration/POG/MUO/2023_Summer23/muon_Z.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    "2023postBPix": "data/jsonpog-integration/POG/MUO/2023_Summer23BPix/muon_Z.json.gz",
                    "2024": "data/2024_correction/MUO/muon_Z.json.gz",
                    "2025": "data/2025_correction/MUO/muon_Z.json.gz",
                }
            ),
            "muon_sf_file_JPsi": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/MUO/2016preVFP_UL/muon_JPsi.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/MUO/2016postVFP_UL/muon_JPsi.json.gz",
                    "2017": "data/jsonpog-integration/POG/MUO/2017_UL/muon_JPsi.json.gz",
                    "2018": "data/jsonpog-integration/POG/MUO/2018_UL/muon_JPsi.json.gz",
                    # "2022preEE": "data/jsonpog-integration/POG/MUO/2022_27Jun2023/muon_JPsi.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    # "2022postEE": "data/jsonpog-integration/POG/MUO/2022EE_27Jun2023/muon_JPsi.json.gz",
                    "2022preEE": "data/jsonpog-integration/POG/MUO/2022_Summer22/muon_JPsi.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    "2022postEE": "data/jsonpog-integration/POG/MUO/2022_Summer22EE/muon_JPsi.json.gz",
                    "2023preBPix": "data/jsonpog-integration/POG/MUO/2023_Summer23/muon_JPsi.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    "2023postBPix": "data/jsonpog-integration/POG/MUO/2023_Summer23BPix/muon_JPsi.json.gz",
                    "2024": "data/2024_correction/MUO/muon_JPsi.json.gz",
                    "2025": "data/2024_correction/MUO/muon_JPsi.json.gz", ### no such file for 2025, using 2024 version first
                }
            ),
            "muon_sf_file_HighPt": EraModifier(
                {
                    "2022preEE": "data/jsonpog-integration/POG/MUO/2022_Summer22/muon_HighPt.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    "2022postEE": "data/jsonpog-integration/POG/MUO/2022_Summer22EE/muon_HighPt.json.gz", # HighPt for 200+
                    "2023preBPix": "data/jsonpog-integration/POG/MUO/2023_Summer23/muon_HighPt.json.gz", # muon_JPsi for pt < 30, muon_Z.json.gz for 15-200, both needed
                    "2023postBPix": "data/jsonpog-integration/POG/MUO/2023_Summer23BPix/muon_HighPt.json.gz", # HighPt for 200+
                    "2024": "data/2024_correction/MUO/muon_HighPt.json.gz",
                    "2025": "data/2025_correction/MUO/muon_HighPt.json.gz",
                }
            ),
            "muon_sf_file_mvaTTH": EraModifier(
                {
                    "2022preEE": "data/muon_corrections/mvaTTH/Run2022_mvaTTH_SF.json.gz",
                    "2022postEE": "data/muon_corrections/mvaTTH/Run2022_EE_mvaTTH_SF.json.gz",
                    "2023preBPix": "data/muon_corrections/mvaTTH/Run2023_mvaTTH_SF.json.gz",
                    "2023postBPix": "data/muon_corrections/mvaTTH/Run2023_BPix_mvaTTH_SF.json.gz", ### TODO waiting to be calculated for 2024
                    "2024": "data/muon_corrections/mvaTTH/Run2023_BPix_mvaTTH_SF.json.gz", #### !!!!effect is small, using 2023 version first!!!
                    "2025": "data/muon_corrections/mvaTTH/Run2023_BPix_mvaTTH_SF.json.gz", #### !!!!effect is small, using 2023 version first!!!
                }
            ),
            "muon_sf_file_dxydz3dsip": EraModifier(
                {
                    "2022preEE": "data/muon_corrections/dxydz3dsipCut/Run2022_dxydz3dsip_SF.json.gz", 
                    "2022postEE": "data/muon_corrections/dxydz3dsipCut/Run2022_EE_dxydz3dsip_SF.json.gz", 
                    "2023preBPix": "data/muon_corrections/dxydz3dsipCut/Run2023_dxydz3dsip_SF.json.gz", 
                    "2023postBPix": "data/muon_corrections/dxydz3dsipCut/Run2023_BPix_dxydz3dsip_SF.json.gz", ### TODO waiting to be calculated for 2024
                    "2024": "data/muon_corrections/dxydz3dsipCut/Run2023_BPix_dxydz3dsip_SF.json.gz", #### !!!!effect is small, using 2023 version first!!!
                    "2025": "data/muon_corrections/dxydz3dsipCut/Run2023_BPix_dxydz3dsip_SF.json.gz", #### !!!!effect is small, using 2023 version first!!!
                }
            ),
            "muon_id_sf_name": "NUM_MediumID_DEN_TrackerMuons",
            "muon_highptid_sf_name": "NUM_HighPtID_DEN_TrackerMuons",
            "muon_id_sf_name_mvaTTH": "NUM_goodMuon_DEN_goodMuon_others",
            "muon_id_sf_name_dxydz3dsip": "NUM_baseMuon_3Dcut_DEN_baseMuon",
            # "muon_iso_sf_name": "NUM_TightRelIso_DEN_MediumID", # for run2?
            "muon_iso_sf_name": EraModifier(
                {
                    # Z file has id and Iso type
                    "2016preVFP": "NUM_TightRelIso_DEN_MediumID",
                    "2016postVFP": "NUM_TightRelIso_DEN_MediumID",
                    "2017": "NUM_TightRelIso_DEN_MediumID",
                    "2018": "NUM_TightRelIso_DEN_MediumID",
                    
                    "2022preEE": "NUM_TightPFIso_DEN_MediumID",
                    "2022postEE": "NUM_TightPFIso_DEN_MediumID",
                    "2023preBPix": "NUM_TightPFIso_DEN_MediumID",
                    "2023postBPix": "NUM_TightPFIso_DEN_MediumID",
                    "2024": "NUM_TightPFIso_DEN_MediumID",
                    "2025": "NUM_TightPFIso_DEN_MediumID",
                }
            ),
            "muon_highpt_iso_sf_name": EraModifier(
                {
                    # Z file has id and Iso type
                    "2016preVFP": "NUM_TightRelIso_DEN_HighPtID",
                    "2016postVFP": "NUM_TightRelIso_DEN_HighPtID",
                    "2017": "NUM_TightRelIso_DEN_HighPtID",
                    "2018": "NUM_TightRelIso_DEN_HighPtID",
                    
                    "2022preEE": "NUM_TightRelTkIso_DEN_HighPtID",
                    "2022postEE": "NUM_TightRelTkIso_DEN_HighPtID",
                    "2023preBPix": "NUM_TightRelTkIso_DEN_HighPtID",
                    "2023postBPix": "NUM_TightRelTkIso_DEN_HighPtID",
                    "2024": "NUM_TightRelTkIso_DEN_HighPtID",
                    "2025": "NUM_TightRelTkIso_DEN_HighPtID",
                }
            ),
            # JPsi file only has id type, no Iso, add a id name and apply the JPsi SF's value = 1.
            # now remove this Iso type at low pt, 2025-04-07
            # "muon_iso_sf_name_JPsi": "NUM_MediumID_DEN_TrackerMuons",
            
            ######################
            ##### for HighPt #####
            ######################
            "muon_id_sf_name_HighPt": "NUM_MediumID_DEN_GlobalMuonProbes", 
            "muon_highptid_sf_name_HighPt": "NUM_HighPtID_DEN_GlobalMuonProbes",
            "muon_iso_sf_name_HighPt": "NUM_probe_TightRelTkIso_DEN_MediumIDProbes",
            "muon_highpt_iso_sf_name_HighPt": "NUM_probe_TightRelTkIso_DEN_HighPtProbes",
            "muon_sf_varation_HighPt": "nominal",
            "muon_reco_sf_name_HighPt": "NUM_GlobalMuons_DEN_TrackerMuonProbes",
            
            # below HighPt Momentum Scale, only for fjmm, nnmm and fjmm_cr
            # "muon_momentum_scale_name": "HighPtMuon_Momentum_Scale",
            # "muon_momentum_scale_variation": "nominal",
            # "muon_momentum_BSC_variation": "nominal",
            # "muon_momentum_scale_corr_file": EraModifier(
            #     {
            #         "2022preEE": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2022preEE.json.gz",
            #         "2022postEE": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2022postEE.json.gz",
            #         "2023preBPix": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2023preBPix.json.gz",
            #         "2023postBPix": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2023postBPix.json.gz",
            #     }
            # ),
            ######################
            ##### for HighPt #####
            ######################
            "muon_sf_year_id": EraModifier(
                {
                    "2016preVFP": "2016preVFP_UL",
                    "2016postVFP": "2016postVFP_UL",
                    "2017": "2017_UL",
                    "2018": "2018_UL",
                    "2022preEE": "2022preEE", # 2022 year_id no need
                    "2022postEE": "2022postEE",
                    "2023preBPix": "2023preBPix", # 2022 year_id no need
                    "2023postBPix": "2023postBPix",
                    "2024": "2024",
                    "2025": "2025",
                }
            ),
            # "muon_sf_varation": "sf",  # "sf" is nominal, "systup"/"systdown" are up/down variations
            # run2 Z sf, run2 JPsi nominal
            # 2022 Z nominal, 2022 JPsi nominal
            "muon_sf_varation": EraModifier(
                {
                    "2016preVFP": "sf",
                    "2016postVFP": "sf",
                    "2017": "sf",
                    "2018": "sf",
                    "2022preEE": "nominal",
                    "2022postEE": "nominal",
                    "2023preBPix": "nominal",
                    "2023postBPix": "nominal",
                    "2024": "nominal",
                    "2025": "nominal",
                }
            ),
            "muon_sf_varation_JPsi": "nominal",
            "a_barrel" : EraModifier(
                {
                    "2022preEE": 0.01152,
                    "2022postEE": 0.0126,
                    "2023preBPix": 0.0172,
                    "2023postBPix": 0.0118,
                    "2024": 0.0104,
                    "2025": 0.0104,
                }
            ),
            "b_barrel" : EraModifier(
                {
                    "2022preEE": 5.95e-05,
                    "2022postEE": 5.89e-05,
                    "2023preBPix": 6.15e-05,
                    "2023postBPix": 6.14e-05,
                    "2024": 6.653e-05,
                    "2025": 6.653e-05,
                }
            ),
            "c_barrel" : EraModifier(
                {
                    "2022preEE": -2.92e-08,
                    "2022postEE": -2.85e-08,
                    "2023preBPix": -3.14e-08,
                    "2023postBPix": -3.12e-08,
                    "2024": -3.635e-08,
                    "2025": -3.635e-08,
                }
            ),
            "d_barrel" : EraModifier(
                {
                    "2022preEE": 5.14e-12,
                    "2022postEE": 4.92e-12,
                    "2023preBPix": 5.82e-12,
                    "2023postBPix": 5.74e-12,
                    "2024": 7.15e-12,
                    "2025": 7.15e-12,
                }
            ),
            "a_endcap" : EraModifier(
                {
                    "2022preEE": 0.01405,
                    "2022postEE": 0.0150,
                    "2023preBPix": 0.01424,
                    "2023postBPix": 0.0141,
                    "2024": 0.000689,
                    "2025": 0.000689,
                }
            ),
            "b_endcap" : EraModifier(
                {
                    "2022preEE": 5.28e-05,
                    "2022postEE": 4.81e-05,
                    "2023preBPix": 5.31e-05,
                    "2023postBPix": 5.38e-05,
                    "2024": 10.12e-05,
                    "2025": 10.12e-05,
                }
            ),
            "c_endcap" : EraModifier(
                {
                    "2022preEE": -1.9e-08,
                    "2022postEE": -1.42e-08,
                    "2023preBPix": -1.92e-08,
                    "2023postBPix": -2.0e-08,
                    "2024": -5.361e-08,
                    "2025": -5.361e-08,
                }
            ),
            "d_endcap" : EraModifier(
                {
                    "2022preEE": 3.01e-12,
                    "2022postEE": 1.95e-12,
                    "2023preBPix": 3.21e-12,
                    "2023postBPix": 3.42e-12,
                    "2024": 1.268e-12,
                    "2025": 1.268e-12,
                }
            ),
            "highpt_smear_factor" : EraModifier(
                {
                    "2022preEE": 0.32,
                    "2022postEE": 0.32,
                    "2023preBPix": 0.32,
                    "2023postBPix": 0.568,
                    "2024": 0.568,
                    "2025": 0.75,
                }
            ),
        },
    )
    #################### KIT and Rochester Correction config parameters #####################
    ## comments from Mingxuan: Doing this aims to set these parameters at "global" level #### 
    ## separately from other parameters. If so, corrected muon pt can be used to select #####
    ## good muons using the good muon mask. But there is something wrong existing which #####
    ## results the minus mass calculated using different mass correction set. Debuging and ##
    ## waiting to be fixed. #################################################################
    configuration.add_config_parameters(
        scopes,
        {
            "muon_momentum_BSC_variation": "nominal",
            "muon_momentum_scale_variation": "nominal",
            "muon_momentum_scale_name": "HighPtMuon_Momentum_Scale",
            "KIT_Muon_Pt_Scale_variation": "none",
            "KIT_Muon_Pt_Res_variation": "none",
            "Rochester_Muon_Pt_Res_variation": "none",
            "KIT_sf_file": EraModifier( #########this is for BSC pt, if you want to use json file for pt, change JSON_VXBS to JSON
                {
                    "2022preEE": "data/muon_corrections/KIT_Corr/JSON_VXBS/2022_Summer22/schemaV2.json",
                    "2022postEE": "data/muon_corrections/KIT_Corr/JSON_VXBS/2022_Summer22EE/schemaV2.json",
                    "2023preBPix": "data/muon_corrections/KIT_Corr/JSON_VXBS/2023_Summer23/schemaV2.json",
                    "2023postBPix": "data/muon_corrections/KIT_Corr/JSON_VXBS/2023_Summer23BPix/schemaV2.json",
                    "2024": "data/muon_corrections/KIT_Corr/JSON_VXBS/2024/schemaV2.json",
                    "2025": "data/muon_corrections/KIT_Corr/JSON_VXBS/2025/schemaV2.json",
                }
            ),
            "RandomSeed_file": "data/muon_corrections/KIT_Corr/RandomSeed.json",
            "muon_momentum_scale_corr_file": EraModifier(
                {
                    "2022preEE": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2022preEE.json.gz",
                    "2022postEE": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2022postEE.json.gz",
                    "2023preBPix": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2023preBPix.json.gz",
                    "2023postBPix": "data/muon_corrections/HighPtMuonMomentumScale/HighPt_2023postBPix.json.gz", 
                    "2024": "data/2024_correction/MUO/HighPt_2024.json.gz", ########### no such file for 2026, maybe use 2025 first?
                    "2025": "data/2025_correction/MUO/HighPt_2025.json.gz",
                }
            ),
            ### Rochester is not recommended by MUO POG now
            "Rochester_sf_file": EraModifier(
                {
                    "2022preEE": "data/muon_corrections/RoccoR/RoccoR2022.txt",
                    "2022postEE": "data/muon_corrections/RoccoR/RoccoR2022EE.txt",
                    "2023preBPix": "data/muon_corrections/RoccoR/RoccoR2023.txt",
                    "2023postBPix": "data/muon_corrections/RoccoR/RoccoR2023BPix.txt",
                    ######## no such file for 2024,2025,2026 
                    "2024": "data/muon_corrections/RoccoR/RoccoR2023BPix.txt",
                    "2025": "data/muon_corrections/RoccoR/RoccoR2023BPix.txt",
                }
            ),
        }
    )
    # electron scale factors configuration
    configuration.add_config_parameters(
        scopes,
        {
            "Smear_variation": "smear",
            "electron_SS_file" : EraModifier(
                {
                    "2022preEE": "data/22-23_correction_new/EGM/2022preEE/electronSS_EtDependent.json.gz",
                    "2022postEE": "data/22-23_correction_new/EGM/2022postEE/electronSS_EtDependent.json.gz",
                    "2023preBPix": "data/22-23_correction_new/EGM/2023preBPix/electronSS_EtDependent.json.gz",
                    "2023postBPix": "data/22-23_correction_new/EGM/2023postBPix/electronSS_EtDependent.json.gz",
                    "2024": "data/2024_correction/EGM/electronSS_EtDependent.json.gz",
                    "2025": "data/2025_correction/EGM/electronSS_EtDependent.json.gz",
                    # "2024": "data/jsonpog-integration/POG/EGM/2023_Summer23BPix/electronSS_EtDependent.json.gz",
                }
            ),
            "electron_SS_scale_name": "Scale",
            "electron_SS_smear_name": EraModifier(
                {
                    "2022preEE": "EGMSmearAndSyst_ElePT_2022",
                    "2022postEE": "EGMSmearAndSyst_ElePT_2022",
                    "2023preBPix": "EGMSmearAndSyst_ElePT_2023",
                    "2023postBPix": "EGMSmearAndSyst_ElePT_2023",
                    "2024": "EGMSmearAndSyst_ElePT_2024",
                    "2025": "EGMSmearAndSyst_ElePT_2025",
                    # "2024": "EGMSmearAndSyst_ElePTsplit_2023postBPIX",
                },  
            ),
            "ele_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/EGM/2016preVFP_UL/electron.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/EGM/2016postVFP_UL/electron.json.gz",
                    "2017": "data/jsonpog-integration/POG/EGM/2017_UL/electron.json.gz",
                    "2018": "data/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz",
                    "2022preEE": "data/jsonpog-integration/POG/EGM/2022_Summer22/electron.json.gz", # correction for pt >= 10
                    "2022postEE": "data/jsonpog-integration/POG/EGM/2022_Summer22EE/electron.json.gz",
                    "2023preBPix": "data/jsonpog-integration/POG/EGM/2023_Summer23/electron.json.gz", # correction for pt >= 10
                    "2023postBPix": "data/jsonpog-integration/POG/EGM/2023_Summer23BPix/electron.json.gz",
                    "2024": "data/2024_correction/EGM/electron.json.gz",
                    "2025": "data/2025_correction/EGM/electron.json.gz",
                }
            ),
            "custom_ele_sf_file": EraModifier(
                {
                    "2022preEE": "data/ele_corrections/custom_ele_sf/2022preEE/electron.json.gz", # correction for pt >= 10
                    "2022postEE": "data/ele_corrections/custom_ele_sf/2022postEE/electron.json.gz",
                    "2023preBPix": "data/ele_corrections/custom_ele_sf/2023preBPix/electron.json.gz", # correction for pt >= 10
                    "2023postBPix": "data/ele_corrections/custom_ele_sf/2023postBPix/electron.json.gz", ### TODO waiting to be calculated for 2024
                    "2024": "data/ele_corrections/custom_ele_sf/2023postBPix/electron.json.gz", ###### using 2023postBPix first
                    "2025": "data/ele_corrections/custom_ele_sf/2023postBPix/electron.json.gz", ###### using 2023postBPix first
                }
            ),
            # "ele_id_sf_name": "UL-Electron-ID-SF",
            "ele_id_sf_name": EraModifier(
                {
                    "2016preVFP": "UL-Electron-ID-SF",
                    "2016postVFP": "UL-Electron-ID-SF",
                    "2017": "UL-Electron-ID-SF",
                    "2018": "UL-Electron-ID-SF",
                    "2022preEE": "Electron-ID-SF",
                    "2022postEE": "Electron-ID-SF",
                    "2023preBPix": "Electron-ID-SF",
                    "2023postBPix": "Electron-ID-SF",
                    "2024": "Electron-ID-SF",
                    "2025": "Electron-ID-SF",
                }
            ),
            "ele_sf_year_id": EraModifier(
                {
                    "2016preVFP": "2016preVFP",
                    "2016postVFP": "2016postVFP",
                    "2017": "2017",
                    "2018": "2018",
                    "2022preEE": "2022Re-recoBCD",
                    "2022postEE": "2022Re-recoE+PromptFG",
                    "2023preBPix": "2023PromptC",
                    "2023postBPix": "2023PromptD",
                    "2024": "2024Prompt",
                    "2025": "2025Prompt",
                }
            ),
            "custom_ele_sf_year_id": EraModifier(
                {
                    "2022preEE": "2022preEE",
                    "2022postEE": "2022postEE",
                    "2023preBPix": "2023preBPix",
                    "2023postBPix": "2023postBPix",
                    "2024": "2023postBPix", ###### using 2023postBPix first
                    "2025": "2023postBPix", ###### using 2023postBPix first
                }
            ),
            "ele_sf_varation": "sf",  # "sf" is nominal, "sfup"/"sfdown" are up/down variations
        },
    )

    ## all scopes MET selection
    configuration.add_config_parameters(
        scopes,
        {
            "propagateLeptons": SampleModifier(
                {"data": False},
                default=True,
            ),
            "propagateJets": SampleModifier(
                {"data": False},
                default=True,
            ),
            "min_jetpt_met_propagation": 15,
        },
    )

    # jet base selection:
    configuration.add_config_parameters(
        "global",
        {
            "jet_reapplyJES": True,
            "jet_jes_sources": '{""}',
            "jet_jes_shift": 0,
            "jet_jer_shift": '"nom"',  # or '"up"', '"down"'
            "year_id": EraModifier(
                {
                    "2022preEE": '"2022preEE"', # 2022 year_id no need
                    "2022postEE": '"2022postEE"',
                    "2023preBPix": '"2023preBPix"', # 2022 year_id no need
                    "2023postBPix": '"2023postBPix"',
                    "2024": '"2024"',
                    "2025": '"2025"',
                }
            ),
            "jet_veto_map": EraModifier(
                {
                    "2016preVFP" : '"data/jsonpog-integration/POG/JME/2016preVFP_UL/jetvetomaps.json.gz"',
                    "2016postVFP" : '"data/jsonpog-integration/POG/JME/2016postVFP_UL/jetvetomaps.json.gz"',
                    "2017" : '"data/jsonpog-integration/POG/JME/2017_UL/jetvetomaps.json.gz"',
                    "2018" : '"data/jsonpog-integration/POG/JME/2018_UL/jetvetomaps.json.gz"',
                    "2022preEE": '"data/22-23_correction_new/JME/2022preEE/jetvetomaps.json.gz"', 
                    "2022postEE": '"data/22-23_correction_new/JME/2022postEE/jetvetomaps.json.gz"',
                    "2023preBPix": '"data/22-23_correction_new/JME/2023preBPix/jetvetomaps.json.gz"',
                    "2023postBPix": '"data/22-23_correction_new/JME/2023postBPix/jetvetomaps.json.gz"',
                    "2024": '"data/2024_correction/JME/jetvetomaps.json.gz"',
                    "2025": '"data/2025_correction/JME/jetvetomaps.json.gz"',
                }
            ),
            "jet_veto_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16_V1"',
                    "2016postVFP": '"Summer19UL16_V1"',
                    "2017": '"Summer19UL17_V1"',
                    "2018": '"Summer19UL18_V1"',
                    "2022preEE": '"Summer22_23Sep2023_RunCD_V1"',
                    "2022postEE": '"Summer22EE_23Sep2023_RunEFG_V1"',
                    "2023preBPix": '"Summer23Prompt23_RunC_V1"',
                    "2023postBPix": '"Summer23BPixPrompt23_RunD_V1"',
                    "2024": '"Summer24Prompt24_RunBCDEFGHI_V1"',
                    "2025": '"Summer24Prompt25_RunCDEFG_V1"',
                }
            ),
            "jet_jec_file": EraModifier(
                {
                    "2016preVFP": '"data/jsonpog-integration/POG/JME/2016preVFP_UL/jet_jerc.json.gz"',
                    "2016postVFP": '"data/jsonpog-integration/POG/JME/2016postVFP_UL/jet_jerc.json.gz"',
                    "2017": '"data/jsonpog-integration/POG/JME/2017_UL/jet_jerc.json.gz"',
                    "2018": '"data/jsonpog-integration/POG/JME/2018_UL/jet_jerc.json.gz"',
                    # "2022preEE": '"data/jsonpog-integration/POG/JME/2022_Prompt/jet_jerc.json.gz"',
                    # "2022postEE": '"data/jsonpog-integration-beforeCorr/POG/JME/2022_Summer22EE-zhiyuan/jet_jerc.json.gz"',
                    "2022preEE": '"data/22-23_correction_new/JME/2022preEE/jet_jerc.json.gz"',
                    "2022postEE": '"data/22-23_correction_new/JME/2022postEE/jet_jerc.json.gz"',
                    "2023preBPix": '"data/22-23_correction_new/JME/2023preBPix/jet_jerc.json.gz"',
                    "2023postBPix": '"data/22-23_correction_new/JME/2023postBPix/jet_jerc.json.gz"',
                    "2024": '"data/2024_correction/JME/jet_jerc.json.gz"',
                    "2025": '"data/2025_correction/JME/jet_jerc.json.gz"', ### for 2025, JEC should use Summer24Prompt24_V3_MC
                }
            ),
            "jet_jer_tag": EraModifier(
                {
                    "2016preVFP": '"Summer20UL16APV_JRV3_MC"',
                    "2016postVFP": '"Summer20UL16_JRV3_MC"',
                    "2017": '"Summer19UL17_JRV2_MC"',
                    "2018": '"Summer19UL18_JRV2_MC"',
                    # "2022preEE": '"JR_Winter22Run3_V1_MC"',
                    # "2022postEE": '"Summer22EEPrompt22_JRV1_MC"',
                    "2022preEE": '"Summer22_22Sep2023_JRV2_MC"', # just for testing (TBD) 2022_Prompt: JR_Winter22Run3_V1_MC
                    "2022postEE": '"Summer22EE_22Sep2023_JRV2_MC"', # just for testing (TBD) beforeCorr: Summer22EEPrompt22_JRV1_MC
                    "2023preBPix": '"Summer23Prompt23_RunCv123_JRV2_MC"',
                    "2023postBPix": '"Summer23BPixPrompt23_RunD_JRV2_MC"',
                    "2024": '"Summer24Prompt24_JRV1_MC"', ## TODO JER for 2024 will be announced soon
                    "2025": '"Summer24Prompt25_JRV1_MC"',
                }
            ),
            "jet_jes_tag_data": EraModifier(
                {
                    "2022preEE": '"Summer22_22Sep2023_V4_DATA"', # just for testing (TBD) 2022_Prompt:  Winter22Run3_V2_MC
                    "2022postEE": '"Summer22EE_22Sep2023_V4_DATA"', # just for testing (TBD) beforeCorr: Summer22EEPrompt22_V1_MC
                    "2023preBPix": '"Summer23Prompt23_V4_DATA"',
                    "2023postBPix": '"Summer23BPixPrompt23_V4_DATA"',
                    "2024": '"Summer24Prompt24_V3_DATA"',
                    "2025": '"Summer24Prompt25_V1_DATA"',
                }
            ),
            "Phi_in_L2Relative": EraModifier(
                {
                    "2022preEE": False, # just for testing (TBD) 2022_Prompt:  Winter22Run3_V2_MC
                    "2022postEE": False, # just for testing (TBD) beforeCorr: Summer22EEPrompt22_V1_MC
                    "2023preBPix": False,
                    "2023postBPix": True,
                    "2024": True,
                    "2025": True,
                }
            ),
            "jet_jes_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16APV_V7_MC"',
                    "2016postVFP": '"Summer19UL16_V7_MC"',
                    "2017": '"Summer19UL17_V5_MC"',
                    "2018": '"Summer19UL18_V5_MC"',
                    # "2022preEE": '"Winter22Run3_V2_MC"',
                    # "2022postEE": '"Summer22EEPrompt22_V1_MC"',
                    "2022preEE": '"Summer22_22Sep2023_V4_MC"', # just for testing (TBD) 2022_Prompt:  Winter22Run3_V2_MC
                    "2022postEE": '"Summer22EE_22Sep2023_V4_MC"', # just for testing (TBD) beforeCorr: Summer22EEPrompt22_V1_MC
                    "2023preBPix": '"Summer23Prompt23_V4_MC"',
                    "2023postBPix": '"Summer23BPixPrompt23_V4_MC"',
                    "2024": '"Summer24Prompt24_V3_MC"', ###### Following previous era, L1L2L3Res is used.
                    "2025": '"Summer24Prompt25_V1_MC"', ###### Following previous era, L1L2L3Res is used.
                }
            ),
            # "jet_jec_algo": '"AK4PFPuppi"', # AK4PFchs for run2?
            "jet_jec_algo": EraModifier(
                {
                    "2016preVFP": '"AK4PFchs"',
                    "2016postVFP": '"AK4PFchs"',
                    "2017": '"AK4PFchs"',
                    "2018": '"AK4PFchs"',
                    "2022preEE": '"AK4PFPuppi"',
                    "2022postEE": '"AK4PFPuppi"',
                    "2023preBPix": '"AK4PFPuppi"',
                    "2023postBPix": '"AK4PFPuppi"',
                    "2024": '"AK4PFPuppi"',
                    "2025": '"AK4PFPuppi"',
                }    
            )
        },
    )
    configuration.add_config_parameters(
        scopes,
        {
            "min_jet_pt": 25, # vh
            "max_jet_eta": 4.7, # vh
            # "jet_id": 2,  # default: 2==pass tight ID and fail tightLepVeto
            "jet_id": EraModifier(
                {
                    # Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto
                    "2016preVFP": 1,  # 1==pass(loose)
                    "2016postVFP": 1,  # 1==pass(loose)
                    "2017": 2,  # 2==pass(tight)
                    "2018": 2,  # 2==pass(tight)
                    "2022preEE": 2,  # 2==pass(tight)
                    "2022postEE": 2,  # 2==pass(tight)
                    "2023preBPix": 2,  # 2==pass(tight)
                    "2023postBPix": 2,  # 2==pass(tight)
                    "2024": 2, ###### FAKE ID, because we calculate it by hand!!!!!! DON'T USE IT !!!!!!!! Will not be used in the producer
                    "2025": 2, ###### FAKE ID, because we calculate it by hand!!!!!! DON'T USE IT !!!!!!!! Will not be used in the producer
                }
            ),
            "jet_puid": EraModifier(
                {
                    "2016preVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2016postVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2017": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2018": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2022preEE": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2022postEE": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2023preBPix": 4,
                    "2023postBPix": 4,
                    "2024": 4, ##### also FAKE ID, DON'T USE IT!!!!!!! Will not be used in the producer!!!!!!!!!!!!
                    "2025": 4, ##### also FAKE ID, DON'T USE IT!!!!!!! Will not be used in the producer!!!!!!!!!!!!
                }
            ),
            "jet_puid_max_pt": 50,  # recommended to apply puID only for jets below 50 GeV
            "deltaR_jet_veto": 0.4, # vh jet-muon dR<0.4 overlap removal
        },
    )
    # fat jet base selection:
    # vhbb run2 approval link: fatjet in slide 4
    # https://indico.cern.ch/event/1198083/contributions/5039217/attachments/2507086/4309256/Calandri_HIGPAG_13092022.pdf
    # lower fatjet selection for fatjet correction
    configuration.add_config_parameters(
        "global",
        {
            "fatjet_reapplyJES": True,
            "fatjet_jes_sources": '{""}',
            "fatjet_jes_shift": 0,
            "fatjet_jer_shift": '"nom"',  # or '"up"', '"down"'
            "fatjet_veto_map": EraModifier(
                {
                    "2016preVFP" : '"data/jsonpog-integration/POG/JME/2016preVFP_UL/jetvetomaps.json.gz"',
                    "2016postVFP" : '"data/jsonpog-integration/POG/JME/2016postVFP_UL/jetvetomaps.json.gz"',
                    "2017" : '"data/jsonpog-integration/POG/JME/2017_UL/jetvetomaps.json.gz"',
                    "2018" : '"data/jsonpog-integration/POG/JME/2018_UL/jetvetomaps.json.gz"',
                    "2022preEE": '"data/22-23_correction_new/JME/2022preEE/jetvetomaps.json.gz"', 
                    "2022postEE": '"data/22-23_correction_new/JME/2022postEE/jetvetomaps.json.gz"',
                    "2023preBPix": '"data/22-23_correction_new/JME/2023preBPix/jetvetomaps.json.gz"',
                    "2023postBPix": '"data/22-23_correction_new/JME/2023postBPix/jetvetomaps.json.gz"',
                    "2024": '"data/2024_correction/JME/jetvetomaps.json.gz"',
                    "2025": '"data/2025_correction/JME/jetvetomaps.json.gz"',
                }
            ),
            "fatjet_veto_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16_V1"',
                    "2016postVFP": '"Summer19UL16_V1"',
                    "2017": '"Summer19UL17_V1"',
                    "2018": '"Summer19UL18_V1"',
                    "2022preEE": '"Summer22_23Sep2023_RunCD_V1"',
                    "2022postEE": '"Summer22EE_23Sep2023_RunEFG_V1"',
                    "2023preBPix": '"Summer23Prompt23_RunC_V1"',
                    "2023postBPix": '"Summer23BPixPrompt23_RunD_V1"',
                    "2024": '"Summer24Prompt24_RunBCDEFGHI_V1"',
                    "2025": '"Summer24Prompt25_RunCDEFG_V1"',
                }
            ),
            "fatjet_jec_file": EraModifier(
                {
                    "2016preVFP": '"data/jsonpog-integration/POG/JME/2016preVFP_UL/fatJet_jerc.json.gz"',
                    "2016postVFP": '"data/jsonpog-integration/POG/JME/2016postVFP_UL/fatJet_jerc.json.gz"',
                    "2017": '"data/jsonpog-integration/POG/JME/2017_UL/fatJet_jerc.json.gz"',
                    "2018": '"data/jsonpog-integration/POG/JME/2018_UL/fatJet_jerc.json.gz"',
                    # "2022preEE": '"data/jsonpog-integration/POG/JME/2022_Prompt/fatJet_jerc.json.gz"',
                    # "2022postEE": '"data/jsonpog-integration-beforeCorr/POG/JME/2022_Summer22EE-zhiyuan/fatJet_jerc.json.gz"',
                    "2022preEE": '"data/22-23_correction_new/JME/2022preEE/fatJet_jerc.json.gz"',
                    "2022postEE": '"data/22-23_correction_new/JME/2022postEE/fatJet_jerc.json.gz"',
                    "2023preBPix": '"data/22-23_correction_new/JME/2023preBPix/fatJet_jerc.json.gz"',
                    "2023postBPix": '"data/22-23_correction_new/JME/2023postBPix/fatJet_jerc.json.gz"',
                    "2024": '"data/2024_correction/JME/fatJet_jerc.json.gz"',
                    "2025": '"data/2025_correction/JME/fatJet_jerc.json.gz"', ####### waiting to be changed
                }
            ),
            "fatjet_jer_tag": EraModifier(
                {
                    "2016preVFP": '"Summer20UL16APV_JRV3_MC"', # TODO JER tag
                    "2016postVFP": '"Summer20UL16_JRV3_MC"',
                    "2017": '"Summer19UL17_JRV2_MC"',
                    "2018": '"Summer19UL18_JRV2_MC"',
                    # "2022preEE": '"JR_Winter22Run3_V1_MC"', # just for testing (TBD)
                    # "2022postEE": '"Summer22EEPrompt22_JRV1_MC"', # just for testing (TBD)
                    "2022preEE": '"Summer22_22Sep2023_JRV2_MC"', # just for testing (TBD)
                    "2022postEE": '"Summer22EE_22Sep2023_JRV2_MC"', # just for testing (TBD)
                    "2023preBPix": '"Summer23Prompt23_RunCv123_JRV2_MC"',
                    "2023postBPix": '"Summer23BPixPrompt23_RunD_JRV2_MC"',
                    "2024": '"Summer24Prompt24_JRV1_MC"', 
                    "2025": '"Summer24Prompt25_JRV1_MC"',
                }
            ),
            "fatjet_jes_tag_data": EraModifier(
                {
                    "2022preEE": '"Summer22_22Sep2023_V4_DATA"', # just for testing (TBD)
                    "2022postEE": '"Summer22EE_22Sep2023_V4_DATA"', # just for testing (TBD)
                    "2023preBPix": '"Summer23Prompt23_V4_DATA"',
                    "2023postBPix": '"Summer23BPixPrompt23_V4_DATA"',
                    "2024": '"Summer24Prompt24_V3_DATA"',
                    "2025": '"Summer24Prompt25_V1_DATA"',
                }
            ),
            "fatjet_jes_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16APV_V7_MC"', # TODO JES tag
                    "2016postVFP": '"Summer19UL16_V7_MC"',
                    "2017": '"Summer19UL17_V5_MC"',
                    "2018": '"Summer19UL18_V5_MC"',
                    # "2022preEE": '"Winter22Run3_V2_MC"', # just for testing (TBD)
                    # "2022postEE": '"Summer22EEPrompt22_V1_MC"', # just for testing (TBD)
                    "2022preEE": '"Summer22_22Sep2023_V4_MC"', # just for testing (TBD)
                    "2022postEE": '"Summer22EE_22Sep2023_V4_MC"', # just for testing (TBD)
                    "2023preBPix": '"Summer23Prompt23_V4_MC"',
                    "2023postBPix": '"Summer23BPixPrompt23_V4_MC"',
                    "2024": '"Summer24Prompt24_V3_MC"',
                    "2025": '"Summer24Prompt25_V1_MC"',
                }
            ),
            "fatjet_jec_algo": '"AK8PFPuppi"',
        },
    )
    # lower fatjet selection for fajet cut and overlap removal
    configuration.add_config_parameters(
        scopes,
        {
            "min_fatjet_pt": 150, # vhbb selection 250
            "max_fatjet_eta": 2.5, # vhbb selection
            "min_fatjet_MSD": 50, # soft drop mass > 50 GeV
            # "fatjet_id": 2,  # default: 2==pass tight ID and fail tightLepVeto
            "fatjet_id": EraModifier(
                {
                    # Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto
                    "2016preVFP": 1,  # 1==pass(loose)
                    "2016postVFP": 1,  # 1==pass(loose)
                    "2017": 2,  # 2==pass(tight)
                    "2018": 2,  # 2==pass(tight)
                    "2022preEE": 2,  # 2==pass(tight)
                    "2022postEE": 2,  # 2==pass(tight)
                    "2023preBPix": 2,  # 2==pass(tight)
                    "2023postBPix": 2,  # 2==pass(tight)
                    "2024": 2, ###### also FAKE ID, DON'T USE IT!!!!!!!!!!!! Will not be used in the Producer!!!!!!!!
                    "2025": 2, ###### also FAKE ID, DON'T USE IT!!!!!!!!!!!! Will not be used in the Producer!!!!!!!!
                }
            ),
            # may no need fatjet_puid
            "deltaR_fatjet_veto": 0.8, # vh fatjet-muon dR<0.8 overlap removal
        },
    )
    ##################################################################
    #### below fjmm WvsQCD ###########################################
    ##################################################################
    configuration.add_config_parameters(
        ["fjmm","fjmm_cr"],
        {
            "fjmm_WvsQCD_sf_file": EraModifier(
                {
                    "2022preEE": "data/muon_corrections/WvsQCD/PNet_LooseWP_2022preEE.json.gz",
                    "2022postEE": "data/muon_corrections/WvsQCD/PNet_LooseWP_2022postEE.json.gz",
                    "2023preBPix": "data/muon_corrections/WvsQCD/PNet_LooseWP_2023preBPix.json.gz",
                    "2023postBPix": "data/muon_corrections/WvsQCD/PNet_LooseWP_2023postBPix.json.gz",
                    "2024": "data/muon_corrections/WvsQCD/PNet_LooseWP_2023postBPix.json.gz", ######## TODO For 2024, GloParT calibration files are needed. Using 2023postBPix first!!!!!!!
                    "2025": "data/muon_corrections/WvsQCD/PNet_LooseWP_2023postBPix.json.gz", ######## TODO For 2025, GloParT calibration files are needed. Using 2023postBPix first!!!!!!!
                }
            ),
            "fatjet_sf_varation" : "nominal",
            "fjmm_WvsQCD_sf_name": "PNet_LooseWP",
        },
    )    
    # bjet scale factors
    configuration.add_config_parameters(
        scopes,
        {
            "btag_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/BTV/2016preVFP_UL/btagging.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/BTV/2016postVFP_UL/btagging.json.gz",
                    "2017": "data/jsonpog-integration/POG/BTV/2017_UL/btagging.json.gz",
                    "2018": "data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",
                    "2022preEE": "data/jsonpog-integration/POG/BTV/2022_Summer22/btagging.json.gz",
                    "2022postEE": "data/jsonpog-integration/POG/BTV/2022_Summer22EE/btagging.json.gz",
                    # "2023preBPix": "data/jsonpog-integration/POG/BTV/2023_Summer23/btagging.json.gz",## Remember jsonpog will not update anymore, please find the correct json in wiki page !!!!!!!!!!
                    # "2023postBPix": "data/jsonpog-integration/POG/BTV/2023_Summer23BPix/btagging.json.gz",
                    "2023preBPix": "data/btag_corrections/new_json_2023/2023_Summer23/btagging.json.gz",
                    "2023postBPix": "data/btag_corrections/new_json_2023/2023_Summer23BPix/btagging.json.gz",
                    "2024": "data/2024_correction/BTV/btagging.json.gz",
                    "2025": "data/2025_correction/BTV/btagging.json.gz",
                }
            ),
            ######## TODO In general, the efficiency files should be re-calculated for RobustParticleTransformer/UParT !!!!!!!!!!!!!
            "loose_btag_eff_file_ttbar": EraModifier(
                {
                    "2022preEE": "data/btag_corrections/loose_ttbar/2022preEE/btagging_efficiency.json",
                    "2022postEE": "data/btag_corrections/loose_ttbar/2022postEE/btagging_efficiency.json",
                    "2023preBPix": "data/btag_corrections/loose_ttbar/2023preBPix/btagging_efficiency.json",
                    "2023postBPix": "data/btag_corrections/loose_ttbar/2023postBPix/btagging_efficiency.json", #### TODO waiting to be calulated for 2024 2025 2026
                    "2024": "data/btag_corrections/loose_ttbar/2023postBPix/btagging_efficiency.json",
                    "2025": "data/btag_corrections/loose_ttbar/2023postBPix/btagging_efficiency.json",
                }
            ),
            "medium_btag_eff_file_ttbar": EraModifier(
                {
                    "2022preEE": "data/btag_corrections/medium_ttbar/2022preEE/btagging_efficiency.json",
                    "2022postEE": "data/btag_corrections/medium_ttbar/2022postEE/btagging_efficiency.json",
                    "2023preBPix": "data/btag_corrections/medium_ttbar/2023preBPix/btagging_efficiency.json",
                    "2023postBPix": "data/btag_corrections/medium_ttbar/2023postBPix/btagging_efficiency.json", #### TODO waiting to be calculated for 2024 2025 2026
                    "2024": "data/btag_corrections/medium_ttbar/2023postBPix/btagging_efficiency.json",
                    "2025": "data/btag_corrections/medium_ttbar/2023postBPix/btagging_efficiency.json",
                }
            ),
            "loose_btag_eff_file_dy": EraModifier(
                {
                    "2022preEE": "data/btag_corrections/loose_dy/2022preEE/btagging_efficiency.json",
                    "2022postEE": "data/btag_corrections/loose_dy/2022postEE/btagging_efficiency.json",
                    "2023preBPix": "data/btag_corrections/loose_dy/2023preBPix/btagging_efficiency.json",
                    "2023postBPix": "data/btag_corrections/loose_dy/2023postBPix/btagging_efficiency.json", #### TODO waiting to be calculated for 2024
                    "2024": "data/btag_corrections/loose_dy/2023postBPix/btagging_efficiency.json",
                    "2025": "data/btag_corrections/loose_dy/2023postBPix/btagging_efficiency.json",
                }
            ),
            "medium_btag_eff_file_dy": EraModifier(
                {
                    "2022preEE": "data/btag_corrections/medium_dy/2022preEE/btagging_efficiency.json",
                    "2022postEE": "data/btag_corrections/medium_dy/2022postEE/btagging_efficiency.json",
                    "2023preBPix": "data/btag_corrections/medium_dy/2023preBPix/btagging_efficiency.json",
                    "2023postBPix": "data/btag_corrections/medium_dy/2023postBPix/btagging_efficiency.json", #### TODO waiting to be calculated for 2024
                    "2024": "data/btag_corrections/medium_dy/2023postBPix/btagging_efficiency.json",
                    "2025": "data/btag_corrections/medium_dy/2023postBPix/btagging_efficiency.json",
                }
            ),
            "loose_btag_eff_file_vhmm": EraModifier(
                {
                    "2022preEE": "data/btag_corrections/loose_vhmm/2022preEE/btagging_efficiency.json",
                    "2022postEE": "data/btag_corrections/loose_vhmm/2022postEE/btagging_efficiency.json",
                    "2023preBPix": "data/btag_corrections/loose_vhmm/2023preBPix/btagging_efficiency.json",
                    "2023postBPix": "data/btag_corrections/loose_vhmm/2023postBPix/btagging_efficiency.json", #### TODO waiting to be calculated for 2024
                    "2024": "data/btag_corrections/loose_vhmm/2023postBPix/btagging_efficiency.json",
                    "2025": "data/btag_corrections/loose_vhmm/2023postBPix/btagging_efficiency.json",
                }
            ),
            "medium_btag_eff_file_vhmm": EraModifier(
                {
                    "2022preEE": "data/btag_corrections/medium_vhmm/2022preEE/btagging_efficiency.json",
                    "2022postEE": "data/btag_corrections/medium_vhmm/2022postEE/btagging_efficiency.json",
                    "2023preBPix": "data/btag_corrections/medium_vhmm/2023preBPix/btagging_efficiency.json",
                    "2023postBPix": "data/btag_corrections/medium_vhmm/2023postBPix/btagging_efficiency.json", #### TODO waiting to be calculated for 2024
                    "2024": "data/btag_corrections/medium_vhmm/2023postBPix/btagging_efficiency.json",
                    "2025": "data/btag_corrections/medium_vhmm/2023postBPix/btagging_efficiency.json",
                }
            ),
            "era_name": EraModifier(
                {
                    "2022preEE": "2022preEE",
                    "2022postEE": "2022postEE",
                    "2023preBPix": "2023preBPix",
                    "2023postBPix": "2023postBPix",
                    "2024": "2023postBPix", ######## when efficiency is ready, this should be changed to 2024!!!!!!!
                    "2025": "2023postBPix", ######## when efficiency is ready, this should be changed to 2025!!!!!!!
                }
            ),
            "btag_sf_label": EraModifier(
                {
                    "2022preEE": "particleNet",
                    "2022postEE": "particleNet",
                    "2023preBPix": "particleNet",
                    "2023postBPix": "particleNet",
                    "2024": "UParTAK4", 
                    "2025": "UParTAK4", 
                }
            ),
            "btag_sf_variation": "central",## TODO: Remember to add the uncertainty to the final BtagWeight!!!!!!!!!
            "BtagWeightVariation": "central",
            # "KIT_Muon_Pt_Scale_variation": "none",
            # "KIT_Muon_Pt_Res_variation": "none",
            # "Rochester_Muon_Pt_Res_variation": "none",
            # "btag_corr_algo": EraModifier(
            #     {
            #         "2016preVFP": "deepJet_shape",
            #         "2016postVFP": "deepJet_shape",
            #         "2017": "deepJet_shape",
            #         "2018": "deepJet_shape",
            #         "2022preEE": "particleNet_shape",## TODO: update to 2022 recommendation when available. These lines only for testing
            #         "2022postEE": "particleNet_shape",
            #         "2023preBPix": "particleNet_shape",## TODO: update to 2022 recommendation when available. These lines only for testing
            #         "2023postBPix": "particleNet_shape",
            #     }    
            # ),
            "btag_corr_algo": EraModifier(
                {
                    "2022preEE": "robustParticleTransformer_shape",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "robustParticleTransformer_shape",
                    "2023preBPix": "robustParticleTransformer_shape",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2023postBPix": "robustParticleTransformer_shape",
                    "2024": "UParTAK4_comb",
                    "2025": "UParTAK4_comb",
                }    
            ),
        },
    )
    # bjet base selection:
    configuration.add_config_parameters(
        # "global",
        scopes,
        {
            "min_bjet_pt": 25, # vh
            "max_bjet_eta": 2.5,
            # "btag_cut_loose": EraModifier(  # loose # (vhmm Run2 use DeepCSV) https://btv-wiki.docs.cern.ch/ScaleFactors/UL2018/
            #     {
            #         "2016preVFP": 0.2027, # 2016preVFP: 0.2027, 2016postVFP: 0.1918 (DeepCSV)
            #         "2016postVFP": 0.1918, # 2016preVFP: 0.2027, 2016postVFP: 0.1918 (DeepCSV)
            #         "2017": 0.1355, # 2017: 0.1355 (DeepCSV)
            #         "2018": 0.1208, # 2018: 0.1208 (DeepCSV)
            #         "2022preEE": 0.047, # (PNet)
            #         "2022postEE": 0.0499, # (PNet)
            #         "2023preBPix": 0.0358, # PNet
            #         "2023postBPix":0.0359, # PNet
            #     }
            # ),
            "btag_cut_loose": EraModifier(  
                {
                    "2022preEE": 0.0849, # RobustParticleTransformer
                    "2022postEE": 0.0897, # RobustParticleTransformer
                    "2023preBPix": 0.0681, # RobustParticleTransformer
                    "2023postBPix":0.0683, # RobustParticleTransformer
                    "2024":0.0246, ###### for 2024, only WP for UParTAK4 is provided
                    "2025":0.0246, ###### for 2024, only WP for UParTAK4 is provided
                }
            ),
            # "btag_cut_medium": EraModifier(  # medium
            #     {
            #         "2016preVFP": 0.6001, # 2016preVFP: 0.6001, 2016postVFP: 0.5847
            #         "2016postVFP": 0.5847, # 2016preVFP: 0.6001, 2016postVFP: 0.5847
            #         "2017": 0.4506, # 2017: 0.4506
            #         "2018": 0.4168, # 2018: 0.4168
            #         "2022preEE": 0.245, # (PNet)
            #         "2022postEE": 0.2605, # (PNet)
            #         "2023preBPix": 0.1917, # PNet
            #         "2023postBPix": 0.1919, # PNet
            #     }
            # ),
            "btag_cut_medium": EraModifier(  # medium
                {
                    "2022preEE": 0.4319, # RobustParticleTransformer
                    "2022postEE": 0.451, # RobustParticleTransformer
                    "2023preBPix": 0.3487, # RobustParticleTransformer
                    "2023postBPix": 0.3494, # RobustParticleTransformer
                    "2024":0.1272, ###### for 2024, only WP for UParTAK4 is provided
                    "2025":0.1272, ###### for 2025, only WP for UParTAK4 is provided
                }
            ),
        },
    )

    # veto ttH
    configuration.add_config_parameters(
        # "global",
        scopes,
        {
            "vetottH_max_nbjets_loose" : 1,
            "vetottH_max_nbjets_medium" : 0,
            "min_dimuon_mass" : 12,
        }
    )
    # m2m cuts
    # m2m regionB: pass 3 medium muons and fail m(mm) in [110,150], actually in [70,110]
    configuration.add_config_parameters(
        ["e2m","e2m_dyfakeinge_regionc","m2m","m2m_dyfakeingmu_regionc",
         "eemm","mmmm","nnmm","fjmm",
         "eemm_cr","mmmm_cr"],
        {
            "flag_DiMuonFromHiggs" : 1,
        }
    )
    # m2m regionC: fail 3 medium muons (actually 2 muons) and pass m(mm) in [110,150]
    # Region D: fail 3 medium muons (actually 2 muons) and fail m(mm) in [110,150], actually in [70,110]
    configuration.add_config_parameters(
        ["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond","nnmm_dycontrol","fjmm_cr",],
        {
            "flag_DiMuonFromCR" : 1, # m(mm) in [70,110]
        }
    )
    configuration.add_config_parameters(
        ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "mmmm","mmmm_cr","nnmm","fjmm","nnmm_dycontrol","fjmm_cr",],
        {
            "flag_GoodEle_Veto" : 1, # no good ele
        }
    )
    configuration.add_config_parameters(
        ["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
         "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",],
        {
            "flag_LeptonChargeSumVeto" : 1, # 1 stands pm1
        }
    )
    configuration.add_config_parameters(
        ["eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","nnmm_dycontrol","nnmm_topcontrol","fjmm_cr",],
        {
            "flag_LeptonChargeSumVeto" : 2, # 2 stands 0
        }
    )
    # cut the flag dimuonfromZ in 3L
    configuration.add_config_parameters(
        ["m2m","m2m_dyfakeingmu_regionc",],
        {
            "Flag_dimuon_Zmass_veto" : 1, # 1 stands no dimuon mass fromZ in 3l
        }
    )
    configuration.add_config_parameters(
        ["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
         "eemm","nnmm","fjmm","nnmm_dycontrol","fjmm_cr","eemm_cr",],
        {
            "vh_good_nmuons" : 2, # 2 good muons
        }
    )
    configuration.add_config_parameters(
        ["nnmm","fjmm","fjmm_cr"],
        {
            "vh_2l_veto_nmuons" : 3, # 2 good muons
        }
    )
    configuration.add_config_parameters(
        ["m2m","m2m_dyfakeingmu_regionb"],
        {
            "vh_good_nmuons" : 3,
        }
    )
    configuration.add_config_parameters(
        ["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
        {
            "vh_base_nmuons": 3,
        }
    )
    # e2m cuts
    # Region B: pass 2 medium muons, 1 ele and fail m(mm) in [110,150], actually in [70,110]
    configuration.add_config_parameters(
        ["e2m","e2m_dyfakeinge_regionb","nnmm_topcontrol"],
        {
            "vh_good_nelectrons" : 1,
        }
    )
    configuration.add_config_parameters(
        ["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
        {
            "vh_good_nelectrons" : 0, # good ele mva in (0.4, 1), no good ele
            "vh_base_nelectrons" : 1, # base ele mva in (-1, 0.4)
            "vh_base_nmuons" : 2, # need good muons and base muons both ==2, removal double counting in m2m_regionc
        }
    )
    configuration.add_config_parameters(
        "eemm",
        {
            "vh_good_nelectrons" : 2,
            "min_dielectron_mass" : 12,
            "flag_DiEleFromZ" : 1,
        }
    )
    configuration.add_config_parameters(
        "eemm_cr",
        {
            "vh_base_nelectrons" : 2,
            "min_dielectron_mass" : 12,
            "flag_DiEleFromZ" : 1,
        }
    )
    configuration.add_config_parameters(
        "mmmm",
        {
            "vh_good_nmuons" : 4,
        }
    )
    configuration.add_config_parameters(
        "mmmm_cr",
        {
            "vh_base_nmuons" : 4,
            "vh_good_nmuons" : 3,
        }
    )
    configuration.add_config_parameters(
        "nnmm",
        {
            # change to 50, to check the met for MET channel
            # change to 100, to contain the DNN cr for MET,
            # but remember to keep nfatjet<=0, to remove the overlap with fjmm
            "min_met" : 100.0,
            "flag_MetCut" : 1,
        }
    )
    configuration.add_config_parameters(
        ["fjmm","fjmm_cr"],
        {
            "vh_good_nfatjets" : 1,
            "max_met" : 150.0,
            "flag_MaxMetCut" : 1,
        }
    )
    configuration.add_config_parameters(
        ["e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
        {
            "vh_good_nfatjets" : 1,
            "max_met" : 150.0,
            "flag_MaxMetCut" : 1,
        }
    )
    configuration.add_config_parameters(
        "nnmm_dycontrol", # DY control region m(mumu) from 70 to 110
        {
            "min_met" : 100.0,            
            "flag_MetCut" : 1,
        }
    )
    configuration.add_config_parameters(
        "nnmm_topcontrol", # Top control reigon e mu final state
        {
            "vh_good_nmuons" : 1,
            "min_met" : 100.0,
            "flag_EleMuFromTopCR" : 1,
            "flag_MetCut" : 1,
        }
    )
    
    configuration.add_producers(
        "global",
        [
            event.SampleFlags,
            event.PUweights,
            event.Lumi,
            event.MetFilter,
            # muons.BaseMuons, # vh
            # muons.GoodMuons, # vh tighter selections on muons
            # muons.NumberOfBaseMuons,
            # muons.NumberOfGoodMuons,
            # muons.BaseMuonCollection, # collect ordered by pt
            # muons.MC_KIT_MuonPt_ScaleRes,
            # muons.MuonCollection, # collect the good muon
            # vh muon Rochester corr, FSR recovery, GeoFit? TODO
            # vh muon FSR recovery
            
            # need use data driven, collect the low mva ele at scopes
            electrons.BaseElectrons,
            electrons.BaseElectrons_v2, # v2 add cutbaseID from base ele
            # electrons.GoodElectrons, # good ele add mvaTTH and mvaIsoID from base ele
            
            electrons.NumberOfBaseElectrons,
            electrons.NumberOfGoodElectrons,
            electrons.BaseElectronCollection, # collect ordered by pt
            electrons.ElectronCollection,

            met.MetBasics, # build met vector for calculation
            met.BuildGenMetVector,
        ],
    )
    if era == "2022preEE" or era == "2022postEE" or era == "2023preBPix" or era == "2023postBPix":
        configuration.add_producers(
            "global",
            electrons.GoodElectrons_22To23, # good ele add mvaTTH and mvaIsoID from base ele
        )
        configuration.add_producers(
            ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
            [
                muons.GoodMuons_22To23,
            ],
        )
    if era == "2024" or era == "2025":
        configuration.add_producers(
            "global",
            electrons.GoodElectrons, # good ele add mvaTTH and mvaIsoID from base ele
        )
        configuration.add_producers(
            ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
            [
                muons.GoodMuons,
            ],
        )
    configuration.add_producers(
        ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
        [
            muons.BaseMuons,
            # muons.GoodMuons,
            muons.NumberOfBaseMuons,
            muons.NumberOfGoodMuons,
            muons.BaseMuonCollection,
            muons.MuonCollection,
        ],
    )
    if era == "2022preEE" or era == "2022postEE" or era =="2023preBPix" or era == "2023postBPix":
        configuration.add_producers(
            ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
            [
                muons.Calculate_MuonPromptMVA22To23,
            ],
        )
        configuration.add_producers(
            ["global"],
            [
                electrons.Calculate_ElePromptMVA22To23,
            ],
        )
    configuration.add_producers(
        ["fjmm_cr", "fjmm", "nnmm"],
        [
            muons.BaseMuons_HighPt,
            muons.GoodMuons_HighPt,
            muons.NumberOfBaseMuons,
            muons.NumberOfGoodMuons,
            muons.BaseMuonCollection,
            muons.MuonCollection,
        ],
    )
    # as different lepton in final state, so need to overlap at each scope
    if era == "2022preEE" or era == "2022postEE" or era =="2023preBPix" or era == "2023postBPix":
        configuration.add_producers(
            "global",
            [
                jets.Create_JetTightID_v12,
                jets.Create_JetTightLepVetoID,
                jets.JetEnergyCorrection, # vh include pt corr and mass corr
                fatjets.FatJetEnergyCorrection,
                # fatjets.Create_FatJetTightLepVetoID,
                jets.FlagVetoMap,
                fatjets.FlagFatJetVetoMap,
            ]
        )
        configuration.add_producers(
            # overlap with good muon and good ele
            ["m2m","e2m","mmmm","eemm","nnmm","fjmm",
             "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb","fjmm_cr"],
            [
                jets.GoodJets_2022_GoodMu_GoodEle, 
                # jets.GoodJets_2022,
            ]
        )
        configuration.add_producers(
            # overlap with base muon
            ["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
            [
                jets.GoodJets_2022_BaseMu, 
            ]
        )
        configuration.add_producers(
            # overlap with good muon and base ele
            ["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm_cr"],
            [
                jets.GoodJets_2022_BaseEle_GoodMu, 
            ]
        )
    elif era == "2024" or era == "2025":
        configuration.add_producers(
            "global",
            [
                jets.Create_JetTightID_v15,
                jets.Create_JetTightLepVetoID,
                fatjets.Create_FatJetTightID_v15,
                # fatjets.Create_FatJetTightLepVetoID,
                jets.JetEnergyCorrection,
                fatjets.FatJetEnergyCorrection,
                jets.FlagVetoMap,
                fatjets.FlagFatJetVetoMap,
            ]
        )
        configuration.add_producers(
            # overlap with good muon and good ele
            ["m2m","e2m","mmmm","eemm","nnmm","fjmm",
             "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb","fjmm_cr"],
            [
                jets.GoodJets_2022_GoodMu_GoodEle, 
            ]
        )
        configuration.add_producers(
            # overlap with base muon
            ["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm_cr"],
            [
                jets.GoodJets_2022_BaseMu, 
            ]
        )
        configuration.add_producers(
            # overlap with good muon and base ele
            ["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm_cr"],
            [
                jets.GoodJets_2022_BaseEle_GoodMu, 
            ]
        )
    elif era == "2018" or era == "2017" or era == "2016preVFP" or era == "2016postVFP":
        configuration.add_producers(
            "global",
            [
                jets.JetEnergyCorrection_run2, # vh include pt corr and mass corr
                fatjets.FatJetEnergyCorrection_run2,
                jets.FlagVetoMap,
                fatjets.FlagFatJetVetoMap,
            ]
        )
        configuration.add_producers(
            # overlap with good muon and good ele
            ["m2m","e2m","mmmm","eemm","nnmm","fjmm",
             "nnmm_dycontrol","nnmm_topcontrol","m2m_dyfakeingmu_regionb","e2m_dyfakeinge_regionb","fjmm_cr"],
            [
                jets.GoodJets_run2_GoodMu_GoodEle, 
            ]
        )
        configuration.add_producers(
            # overlap with base muon
            ["m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
            [
                jets.GoodJets_run2_BaseMu, 
            ]
        )
        configuration.add_producers(
            # overlap with good muon and base ele
            ["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
            [
                jets.GoodJets_run2_BaseEle_GoodMu, 
            ]
        )
    configuration.add_producers(
        ["nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
        [
            momentumscale.MuonPtCorrection,
        ]
    )
    configuration.add_producers(
        ["e2m","m2m", "eemm","mmmm","eemm_cr","mmmm_cr",
         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
        [
            momentumscale.RenameMuonPt,
            scalefactors.btagging_SF_2WPs_3l_4l, ###update btag sf by Mingxuan
            # scalefactors.btagging_SF_2WPs_3l_4l_dy,
            # scalefactors.btagging_SF_2WPs_3l_4l_vhmm,
        ]
    )
    configuration.add_producers(
        ["nnmm","fjmm","fjmm_cr"],
        [
            momentumscale.MuonPtPreCorrection,
            momentumscale.MuonPtPreSmear,
        ]
    )
    configuration.add_producers(
        ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm_dycontrol","nnmm_topcontrol",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
        [
            momentumscale.MC_KIT_MuonPt_ScaleRes,
            # momentumscale.MC_KIT_MuonPt_ScaleRes_pureBSC,
            # momentumscale.MC_KIT_MuonPt_ScaleRes_raw,
        ]
    )
    configuration.add_producers(
        ["nnmm","fjmm","fjmm_cr"],
        [
            momentumscale.MC_KIT_MuonPt_ScaleRes_HighPt,
        ]
    )
    # configuration.add_producers(
    #     ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    #     [
    #         momentumscale.MC_Rochester_MuonPt_ScaleRes,
    #     ]
    # )
    configuration.add_producers(
        scopes,
        [
            jets.NumberOfGoodJets,
            jets.JetCollection,

            jets.Calc_MHT_all_corrected,

            jets.GoodBJetsLoose_PNet, 
            jets.GoodBJetsMedium_PNet, 
            jets.NumberOfLooseB, # vh count loose bjets for ttH veto
            jets.NumberOfMediumB, # vh count medium bjets for ttH veto
            jets.VetottHLooseB, # vh veto ttH no more than 1 loose bjet
            jets.VetottHMediumB, # vh veto ttH no more than 1 medium bjet   
            # scalefactors.btaggingloose_SF,

            p4.MHTALL_pt,
            p4.MHTALL_eta,
            p4.MHTALL_phi,
            p4.MHTALL_mass,
            met.MetCorrections,
        ]
    )
    if era == "2022preEE" or era == "2022postEE" or era =="2023preBPix" or era == "2023postBPix":
        configuration.add_producers(
            ["fjmm","fjmm_cr","nnmm","e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
            fatjets.GoodFatJets,
        )
    if era == "2024" or era == "2025":
        configuration.add_producers(
            ["fjmm","fjmm_cr","nnmm","e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
            fatjets.GoodFatJets_v15,
        )
    configuration.add_producers(
        ["fjmm","fjmm_cr"],
        [
            fatjets.NumberOfGoodFatJets,
            fatjets.FatJetCollection,
            fatjets.FilterNFatjets_fjmm, # vh fjmm >=1 fatjet
            fatjets.LVFatJet1,
            scalefactors.btagging_SF_2WPs_fjmm, ###update btag sf by Mingxuan
            # scalefactors.btagging_SF_2WPs_fjmm_dy,
            # scalefactors.btagging_SF_2WPs_fjmm_vhmm,
            fatjets.Pnet_Fatjet_Mass_Corr,
            fatjets.GoodFatjet_RawFactor,
        ]
    )
    configuration.add_producers(
        ["e2m_dyfakeinge_regionc", "m2m_dyfakeingmu_regionc"],
        [
            fatjets.NumberOfGoodFatJets,
            fatjets.FilterVetoNFatjets_fjmm, ### use to be othorgnal with fjmm
        ]
    )
    configuration.add_producers(
        ["nnmm"],
        [
            fatjets.NumberOfGoodFatJets,
            scalefactors.btagging_SF_2WPs_met, ###update btag sf by Mingxuan
            # scalefactors.btagging_SF_2WPs_met_dy,
            # scalefactors.btagging_SF_2WPs_met_vhmm,
        ]
    )
    configuration.add_producers(
        "m2m",
        [
            event.FilterNGoodMuons, # vh ==3 muons
            # write by botao
            lepton.CalcSmallestDiMuonMass,  # SFOS, m2m only has m
            event.DimuonMinMassCut,
            ###
            event.Mask_DiMuonPair, # dimuonHiggs index
            event.Flag_DiMuonFromHiggs,
            event.HiggsToDiMuonPair_p4_noFSR, # select the dimuon pairs in [110,150] and order by pt
            ###FSR###
            fsrphoton.leadingmuon_FsrPhotonIdx,
            fsrphoton.subleadingmuon_FsrPhotonIdx,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
            ###
            event.DiMuonMassFromZVeto,  # has dimuon from Z return mask equal to 0, otherwise return 1
            lepton.LeptonChargeSumVeto,
            ###
            electrons.GoodEle_Veto,
            # flag cut
            event.FilterFlagDiMuFromH,
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            event.FilterFlagDiMuonZVeto,
            ###
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            muons.LVMu3,
            muons.LVMu3_uncorrected,
            muons.Mu1_H, # vh
            # muons.Mu1_H_pureBSC,
            # muons.Mu1_H_raw,
            muons.Mu1_H_noFSR,
            # muons.Mu1_H_noFSR_pureBSC,
            # muons.Mu1_H_noFSR_raw,
            muons.Mu1_H_uncorrected,
            muons.Mu2_H, # vh
            # muons.Mu2_H_pureBSC,
            # muons.Mu2_H_raw,
            muons.Mu2_H_noFSR,
            # muons.Mu2_H_noFSR_pureBSC,
            # muons.Mu2_H_noFSR_raw,
            muons.Mu2_H_uncorrected,
            ### extra muon in m2m
            lepton.Mu1_W_m2m_index, # extra muon index
            lepton.Mu1_W_m2m, # extra muon p4 (From W)
            lepton.Mu1_W_m2m_noCorr, 
            
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars
            
            ###
            lepton.Calc_MT_W,
            event.lepton_H_dR,
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            ###
            event.muSSwithMuonW_p4,
            event.muOSwithMuonW_p4,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            ### 
            event.lepton_H_deta,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,
            ###            
            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,
            ###
            event.mumuH_MHTALL_dphi,
            event.mu1_MHTALL_dphi,
            event.mu2_MHTALL_dphi,

            # event.mu1_mu2_dphi,
            event.lep_mu1_dphi,
            event.lep_mu2_dphi,
            event.lep_H_dphi,
            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,
            #
            #muons.LVMu3, # vh 
            # vh check trigger matching TODO
            # vh the trigger-matched muon should have pT > 29 (26) for 2017 (2016,18)
            
            #
            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,            
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            p4.muOS_pt,
            p4.muOS_eta,
            p4.muOS_phi,
            p4.muSS_pt,
            p4.muSS_eta,
            p4.muSS_phi,
            
            p4.genmet_pt,
            p4.genmet_phi,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            
            ### hack
            p4.ThreeLepQuantities,
            # p4.calc_pz_nu,
            # p4.mu1_H_dR,
        ],
    )
    configuration.add_producers(
        # Region B: pass 3 medium muons and fail m(mm) in [110,150], actually in [70,110]
        "m2m_dyfakeingmu_regionb",
        [
            event.FilterNGoodMuons, # vh ==3 muons
            # write by botao
            lepton.CalcSmallestDiMuonMass,
            event.DimuonMinMassCut,
            ###
            lepton.LeptonChargeSumVeto,
            electrons.GoodEle_Veto,
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            ### dimuon pairs in [70,110] OR [150,Inf)
            cr.DY_DiMuonPair_CR_HighMass,
            cr.Flag_DiMuonFromCR,
            cr.FilterFlag_DiMuonFromCR,
            cr.DiMuonPairCR_p4,
            cr.dimuonCR_pt,
            cr.dimuonCR_eta,
            cr.dimuonCR_phi,
            cr.dimuonCR_mass,
            ###
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            muons.LVMu3,
            muons.LVMu3_uncorrected,
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################
            lepton.Mu1_W_m2m_index_regionb,
            lepton.Mu1_W_m2m,
            lepton.Mu1_W_m2m_noCorr,
            lepton.Calc_MT_W,
            event.lepton_Z_dR,
            event.lep_Z_dphi,
            event.muSSwithMuonW_p4_regionbd,
            event.muOSwithMuonW_p4_regionbd,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,
            
            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,
            
            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,
            # flag cut
            # event.FilterFlagDiMuFromH,
            ###
            muons.Mu1_Z_CR,
            muons.Mu1_Z_CR_uncorrected,
            muons.Mu2_Z_CR,
            muons.Mu2_Z_CR_uncorrected,
            event.mumuZCR_dR,
            event.mumuZCR_dphi,
            event.mumuZCR_deta,
            event.ZCR_MHTALL_dphi,
            event.mu1_fromZCR_MHTALL_dphi,
            event.mu2_fromZCR_MHTALL_dphi,
            event.mu1_mu2_fromZCR_dphi,
            event.met_mm_fromZCR_dphi,
            p4.mu1_fromZCR_pt,
            p4.mu1_fromZCR_eta,
            p4.mu1_fromZCR_phi,
            p4.mu2_fromZCR_pt,
            p4.mu2_fromZCR_eta,
            p4.mu2_fromZCR_phi,
            # vh check trigger matching TODO
            # # vh the trigger-matched muon should have pT > 29 (26) for 2017 (2016,18)
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
        ],
    )
    configuration.add_producers(
        "m2m_dyfakeingmu_regionc",
        [
            event.FilterNBaseMuons,
            event.FilterNGoodMuons, # vh reigon c, d ==2 medium good muons
            # lepton.CalcSmallestDiMuonMass,
            lepton.CalcSmallestBaseDiMuonMass,
            event.DimuonMinMassCut, # filter cut dimuon mass < 12 GeV
            lepton.BaseLeptonChargeSumVeto,
            # lepton.BaseLeptonChargeSumVeto,
            event.BaseDiMuonMassFromZVeto,
            lepton.Mu1_W_m2m_index_regionc,
            # lepton.Mu1_W_m2m_index_regionc,
            lepton.Mu1_W_m2m,
            lepton.Mu1_W_m2m_noCorr,
            electrons.GoodEle_Veto,
            # flag cut
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            event.FilterFlagDiMuonZVeto,
            event.Flag_MaxMetCut,
            event.FilterFlagMaxMetCut,
            ###
            event.Mask_DiMuonPair, # select the dimuon index in [110,150]
            ####FSR#####
            fsrphoton.leadingmuon_FsrPhotonIdx,
            fsrphoton.subleadingmuon_FsrPhotonIdx,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
            # event.Mask_BaseDiMuonPair, # select the dimuon index in [110,150]
            event.Flag_DiMuonFromHiggs, # create the flag
            event.HiggsToDiMuonPair_p4_noFSR, # make dimuon p4
            event.FilterFlagDiMuFromH, # flag dimuon Higgs cut
            ###
            muons.Mu1_H,
            # muons.Mu1_H_pureBSC,
            # muons.Mu1_H_raw,
            muons.Mu1_H_noFSR,
            # muons.Mu1_H_noFSR_pureBSC,
            # muons.Mu1_H_noFSR_raw,
            muons.Mu1_H_uncorrected,
            muons.Mu2_H,
            # muons.Mu2_H_pureBSC,
            # muons.Mu2_H_raw,
            muons.Mu2_H_noFSR,
            # muons.Mu2_H_noFSR_pureBSC,
            # muons.Mu2_H_noFSR_raw,
            muons.Mu2_H_uncorrected,
            # muons.LVMu1,
            # muons.LVMu2,
            # muons.LVMu3,
            muons.BaseLVMu1,
            muons.BaseLVMu1_uncorrected,
            muons.BaseLVMu2,
            muons.BaseLVMu2_uncorrected,
            muons.BaseLVMu3,
            muons.BaseLVMu3_uncorrected,
            
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################            
            
            ###
            lepton.Calc_MT_W,
            event.lepton_H_dR,
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            event.muSSwithMuonW_p4,
            event.muOSwithMuonW_p4,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            event.lepton_H_deta,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,
            
            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,

            event.mumuH_MHTALL_dphi,
            event.mu1_MHTALL_dphi,
            event.mu2_MHTALL_dphi,
            
            # event.mu1_mu2_dphi,
            event.lep_mu1_dphi,
            event.lep_mu2_dphi,
            event.lep_H_dphi,
            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,
            ###
            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            p4.muOS_pt,
            p4.muOS_eta,
            p4.muOS_phi,
            p4.muSS_pt,
            p4.muSS_eta,
            p4.muSS_phi,

            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            
            p4.ThreeLepQuantities,
        ]
    )
    # Region D: fail 3 medium muons (actually 2 muons) and fail m(mm) in [110,150], actually in [70,110]
    configuration.add_producers(
        "m2m_dyfakeingmu_regiond",
        [
            event.FilterNBaseMuons,
            event.FilterNGoodMuons, # vh reigon c, d ==2 muons
            # lepton.CalcSmallestDiMuonMass,
            lepton.CalcSmallestBaseDiMuonMass,
            event.DimuonMinMassCut, # filter cut dimuon mass < 12 GeV
            lepton.BaseLeptonChargeSumVeto,
            # lepton.BaseLeptonChargeSumVeto,
            # lepton.Mu1_W_m2m_index_regionc,
            # lepton.Mu1_W_m2m,
            electrons.GoodEle_Veto,
            # flag cut
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            # m(mm) in [70,110] OR [150,Inf)
            cr.DY_DiMuonPair_CR_HighMass,
            cr.Flag_DiMuonFromCR,
            cr.FilterFlag_DiMuonFromCR,
            cr.DiMuonPairCR_p4,
            cr.dimuonCR_pt,
            cr.dimuonCR_eta,
            cr.dimuonCR_phi,
            cr.dimuonCR_mass,
            ###
            lepton.Mu1_W_m2m_index_regiond,
            lepton.Mu1_W_m2m,
            lepton.Mu1_W_m2m_noCorr,

            muons.BaseLVMu1,
            muons.BaseLVMu1_uncorrected,
            muons.BaseLVMu2,
            muons.BaseLVMu2_uncorrected,
            muons.BaseLVMu3,
            muons.BaseLVMu3_uncorrected,

            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################
            
            lepton.Calc_MT_W,
            event.lepton_Z_dR,
            event.lep_Z_dphi,
            event.muSSwithMuonW_p4_regionbd,
            event.muOSwithMuonW_p4_regionbd,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,
            
            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,

            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,
            muons.Mu1_Z_CR,
            muons.Mu1_Z_CR_uncorrected,
            muons.Mu2_Z_CR,
            muons.Mu2_Z_CR_uncorrected,
            event.mumuZCR_dR,
            event.mumuZCR_dphi,
            event.mumuZCR_deta,
            event.ZCR_MHTALL_dphi,
            event.mu1_fromZCR_MHTALL_dphi,
            event.mu2_fromZCR_MHTALL_dphi,
            event.mu1_mu2_fromZCR_dphi,
            event.met_mm_fromZCR_dphi,
            p4.mu1_fromZCR_pt,
            p4.mu1_fromZCR_eta,
            p4.mu1_fromZCR_phi,
            p4.mu2_fromZCR_pt,
            p4.mu2_fromZCR_eta,
            p4.mu2_fromZCR_phi,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
        ]
    )
    configuration.add_producers(
        "e2m",
        [
            event.FilterNGoodMuons, # nmuons == 2
            event.FilterNGoodElectrons, # nelectrons == 1
            ###
            lepton.CalcSmallestDiMuonMass,  # SFOS, e2m only has 2m
            event.DimuonMinMassCut,
            ###
            event.Mask_DiMuonPair,
            event.Flag_DiMuonFromHiggs,
            event.HiggsToDiMuonPair_p4_noFSR, # select the first dimuon pairs in [110,150] that ordered by pt
            ###FSR####
            fsrphoton.leadingmuon_FsrPhotonIdx,
            fsrphoton.subleadingmuon_FsrPhotonIdx,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
            ###
            lepton.LeptonChargeSumVeto_elemu, # only in e2m and 2e2m channel
            # flag cut
            event.FilterFlagDiMuFromH,
            event.FilterFlagLepChargeSum,
            # Pass same Flag, be consistent with m2m channel
            event.PassFlagZmassVeto,
            event.PassFlagGoodEleVeto,
            ###
            muons.Mu1_H,
            # muons.Mu1_H_pureBSC,
            # muons.Mu1_H_raw,
            muons.Mu1_H_noFSR,
            # muons.Mu1_H_noFSR_pureBSC,
            # muons.Mu1_H_noFSR_raw,
            muons.Mu1_H_uncorrected,
            muons.Mu2_H,
            # muons.Mu2_H_pureBSC,
            # muons.Mu2_H_raw,
            muons.Mu2_H_noFSR,
            # muons.Mu2_H_noFSR_pureBSC,
            # muons.Mu2_H_noFSR_raw,
            muons.Mu2_H_uncorrected,

            lepton.Ele1_W_e2m, # output extra lep p4
            lepton.Ele1_W_e2m_noCorr,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################

            lepton.Calc_MT_W,
            event.lepton_H_dR,
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            ###
            event.muSSwithElectronW_p4,
            event.muOSwithElectronW_p4,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            ###
            event.lepton_H_deta,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,
            ###            
            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,

            event.mumuH_MHTALL_dphi,
            event.mu1_MHTALL_dphi,
            event.mu2_MHTALL_dphi,
            
            # event.mu1_mu2_dphi,
            event.lep_mu1_dphi,
            event.lep_mu2_dphi,
            event.lep_H_dphi,
            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,
            #

            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            p4.muOS_pt,
            p4.muOS_eta,
            p4.muOS_phi,
            p4.muSS_pt,
            p4.muSS_eta,
            p4.muSS_phi,
            
            p4.genmet_pt,
            p4.genmet_phi,            
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.EleID_SF,
            scalefactors.EleReco_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            
            # hack
            p4.ThreeLepQuantities,
            # p4.calc_pz_nu,
            # p4.mu1_H_dR,
        ],
    )
    # Region B: pass 2 medium muons, 1 ele and fail m(mm) in [110,150], actually in [70,110]
    configuration.add_producers(
        "e2m_dyfakeinge_regionb", #####maybe
        [
            event.FilterNGoodMuons, # nmuons == 2
            event.FilterNGoodElectrons, # nelectrons == 1
            ###
            lepton.CalcSmallestDiMuonMass,  # SFOS, e2m only has 2m
            lepton.LeptonChargeSumVeto_elemu, # only in e2m and 2e2m channel
            event.FilterFlagLepChargeSum,
            event.DimuonMinMassCut,
            # m(mm) in [70,110] OR [150,Inf)
            cr.DY_DiMuonPair_CR_HighMass,
            cr.Flag_DiMuonFromCR,
            cr.FilterFlag_DiMuonFromCR,
            cr.DiMuonPairCR_p4,
            cr.dimuonCR_pt,
            cr.dimuonCR_eta,
            cr.dimuonCR_phi,
            cr.dimuonCR_mass,
            ###
            lepton.Ele1_W_e2m,
            lepton.Ele1_W_e2m_noCorr,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################

            lepton.Calc_MT_W,
            event.lepton_Z_dR,
            event.lep_Z_dphi,
            event.muOSwithElectronW_p4_e2m_regionb,
            event.muSSwithElectronW_p4_e2m_regionb,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,
            
            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,

            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,

            ###
            muons.Mu1_Z_CR,
            muons.Mu1_Z_CR_uncorrected,
            muons.Mu2_Z_CR,
            muons.Mu2_Z_CR_uncorrected,
            event.mumuZCR_dR,
            event.mumuZCR_dphi,
            event.mumuZCR_deta,
            event.ZCR_MHTALL_dphi,
            event.mu1_fromZCR_MHTALL_dphi,
            event.mu2_fromZCR_MHTALL_dphi,
            event.mu1_mu2_fromZCR_dphi,
            event.met_mm_fromZCR_dphi,
            p4.mu1_fromZCR_pt,
            p4.mu1_fromZCR_eta,
            p4.mu1_fromZCR_phi,
            p4.mu2_fromZCR_pt,
            p4.mu2_fromZCR_eta,
            p4.mu2_fromZCR_phi,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.EleID_SF,
            scalefactors.EleReco_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
        ]
    )
    configuration.add_producers(
        "e2m_dyfakeinge_regionc",
        [
            event.FilterNGoodMuons, # n good muons == 2
            event.FilterNBaseMuons, # n base muons == 2
            event.FilterNGoodElectrons, # n good electrons == 0
            event.FilterNBaseElectrons, # n base ele == 1
            ###
            lepton.CalcSmallestDiMuonMass,  # SFOS, e2m only has 2m
            lepton.LeptonChargeSumVeto_baseelegoodmu_regioncd, # only in e2m and 2e2m channel
            event.FilterFlagLepChargeSum,
            event.DimuonMinMassCut,
            event.PassFlagZmassVeto,
            event.PassFlagGoodEleVeto,
            ###
            event.Mask_DiMuonPair, # select the dimuon index in [110,150]
            event.Flag_DiMuonFromHiggs, # create the flag
            event.HiggsToDiMuonPair_p4_noFSR, # make dimuon p4
            event.FilterFlagDiMuFromH, # flag dimuon Higgs cut
            event.Flag_MaxMetCut,
            event.FilterFlagMaxMetCut,
            muons.Mu1_H,
            # muons.Mu1_H_pureBSC,
            # muons.Mu1_H_raw,
            muons.Mu1_H_noFSR,
            # muons.Mu1_H_noFSR_pureBSC,
            # muons.Mu1_H_noFSR_raw,
            muons.Mu1_H_uncorrected,
            muons.Mu2_H,
            # muons.Mu2_H_pureBSC,
            # muons.Mu2_H_raw,
            muons.Mu2_H_noFSR,
            # muons.Mu2_H_noFSR_pureBSC,
            # muons.Mu2_H_noFSR_raw,
            muons.Mu2_H_uncorrected,
            ###FSR####
            fsrphoton.leadingmuon_FsrPhotonIdx,
            fsrphoton.subleadingmuon_FsrPhotonIdx,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
            ###
            lepton.Ele1_W_e2m_regioncd,
            lepton.Ele1_W_e2m_regioncd_noCorr,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################

            lepton.Calc_MT_W,
            event.lepton_H_dR,
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            event.muSSwithElectronW_p4_e2m_regionc,
            event.muOSwithElectronW_p4_e2m_regionc,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            event.lepton_H_deta,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,

            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,

            event.mumuH_MHTALL_dphi,
            event.mu1_MHTALL_dphi,
            event.mu2_MHTALL_dphi,
            
            # event.mu1_mu2_dphi,
            event.lep_mu1_dphi,
            event.lep_mu2_dphi,
            event.lep_H_dphi,
            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,
            
            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,
            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            p4.muOS_pt,
            p4.muOS_eta,
            p4.muOS_phi,
            p4.muSS_pt,
            p4.muSS_eta,
            p4.muSS_phi,

            ###
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.EleID_SF,
            scalefactors.EleReco_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            
            p4.ThreeLepQuantities,
        ]
    )
    configuration.add_producers(
        "e2m_dyfakeinge_regiond",
        [
            event.FilterNGoodMuons, # n good muons == 2
            event.FilterNBaseMuons, # n base muons == 2
            event.FilterNGoodElectrons, # n good electrons == 0
            event.FilterNBaseElectrons, # n base ele == 1
            ###
            lepton.CalcSmallestDiMuonMass,  # SFOS, e2m only has 2m
            lepton.LeptonChargeSumVeto_baseelegoodmu_regioncd, # only in e2m and 2e2m channel
            event.FilterFlagLepChargeSum,
            event.DimuonMinMassCut,
            ###
            # m(mm) in [70,110] OR [150,Inf)
            cr.DY_DiMuonPair_CR_HighMass,
            cr.Flag_DiMuonFromCR,
            cr.FilterFlag_DiMuonFromCR,
            cr.DiMuonPairCR_p4,
            cr.dimuonCR_pt,
            cr.dimuonCR_eta,
            cr.dimuonCR_phi,
            cr.dimuonCR_mass,
            ###
            lepton.Ele1_W_e2m_regioncd,
            lepton.Ele1_W_e2m_regioncd_noCorr,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################
            
            lepton.Calc_MT_W,
            event.lepton_Z_dR,
            event.lep_Z_dphi,
            event.muOSwithElectronW_p4_e2m_regiond,
            event.muSSwithElectronW_p4_e2m_regiond,
            event.lepton_muSS_dR,
            event.lepton_muOS_dR,
            event.lepton_muSS_deta,
            event.lepton_muOS_deta,

            event.lepW_MHTALL_dphi,
            event.Calc_MT_muSS_MHTALL,
            event.Calc_MT_muOS_MHTALL,
            event.Calc_MT_lepton_MHTALL,

            event.Calc_CosThStar_lep_muOS,
            event.Calc_CosThStar_lep_muSS,
            
            ###
            muons.Mu1_Z_CR,
            muons.Mu1_Z_CR_uncorrected,
            muons.Mu2_Z_CR,
            muons.Mu2_Z_CR_uncorrected,
            event.mumuZCR_dR,
            event.mumuZCR_dphi,
            event.mumuZCR_deta,
            event.ZCR_MHTALL_dphi,
            event.mu1_fromZCR_MHTALL_dphi,
            event.mu2_fromZCR_MHTALL_dphi,
            event.mu1_mu2_fromZCR_dphi,
            event.met_mm_fromZCR_dphi,
            p4.mu1_fromZCR_pt,
            p4.mu1_fromZCR_eta,
            p4.mu1_fromZCR_phi,
            p4.mu2_fromZCR_pt,
            p4.mu2_fromZCR_eta,
            p4.mu2_fromZCR_phi,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            p4.extra_lep_pt,
            p4.extra_lep_eta,
            p4.extra_lep_phi,
            p4.extra_lep_mass,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.EleID_SF,
            scalefactors.EleReco_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
        ]
    )
    # configuration.add_producers(
    #     ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
    #     [
    #         # extra mu
    #         lepton.extra_muon_mvaTTH,
    #     ]
    # )
    # configuration.add_producers(
    #     ["e2m","e2m_dyfakeinge_regionb"],
    #     [
    #         # extra good ele
    #         lepton.extra_goodele_mvaTTH,
    #     ]
    # )
    # configuration.add_producers(
    #     ["e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    #     [
    #         # extra base ele
    #         lepton.extra_baseele_mvaTTH,
    #     ]
    # )
    configuration.add_producers(
        ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
        [
            p4.W_pt,
            p4.W_phi,
        ]
    )
    configuration.add_producers(
        "eemm",
        [
            # private for eemm
            event.FilterNGoodElectrons,
            event.Mask_DiElectronPair,
            lepton.LeptonChargeSumVeto_elemu, # only in e2m and 2e2m channel
        ]
    )
    configuration.add_producers(
        "eemm_cr",
        [
            # private for eemm_cr
            event.FilterNBaseElectrons,
            event.Mask_DiBaseElectronPair,
            lepton.LeptonChargeSumVeto_mubaseele, # only in e2m and 2e2m channel
        ]
    )
    configuration.add_producers(
        ["eemm","eemm_cr"],
        [            
            # common for eemm and eemm_cr
            event.FilterNGoodMuons,
            lepton.CalcSmallestDiMuonMass,  # both dimuon and diele
            lepton.CalcSmallestDiElectronMass,
            event.DimuonMinMassCut,
            event.DielectronMinMassCut,
            ###
            event.Mask_DiMuonPair,
            event.Flag_DiMuonFromHiggs,
            event.HiggsToDiMuonPair_p4_noFSR, # select the first dimuon pairs in [110,150] that ordered by pt
            ###
            event.Flag_DiEleFromZ,  ### need ZCand m(ee) in [70,110]
            event.ZToDiElectronPair_p4,
            ###FSR####
            fsrphoton.leadingmuon_FsrPhotonIdx,
            fsrphoton.subleadingmuon_FsrPhotonIdx,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
            # flag cut
            event.FilterFlagDiMuFromH,
            event.FilterFlagLepChargeSum,
            event.FilterFlagDiEleZMassVeto,
            ### Pass same flag,
            event.PassFlagGoodEleVeto,
            event.PassFlagZZVeto,
            #
            muons.Mu1_H,
            # muons.Mu1_H_pureBSC,
            # muons.Mu1_H_raw,
            muons.Mu1_H_noFSR,
            # muons.Mu1_H_noFSR_pureBSC,
            # muons.Mu1_H_noFSR_raw,
            muons.Mu1_H_uncorrected,
            muons.Mu2_H,
            # muons.Mu2_H_pureBSC,
            # muons.Mu2_H_raw,
            muons.Mu2_H_noFSR,
            # muons.Mu2_H_noFSR_pureBSC,
            # muons.Mu2_H_noFSR_raw,
            muons.Mu2_H_uncorrected,
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            electrons.LVEle1,  # leading lep from Z
            electrons.LVEle1_uncorrected,
            electrons.LVEle2,  # subleading lep from Z
            electrons.LVEle2_uncorrected,
            ###
            event.leplepZ_dR,
            lepton.RenameZlepID_eemm, # using pdgId to lep_ID
            event.llZ_mmH_deta,
            event.llZ_mmH_dphi,
            event.Calc_CosThStar_Z_H,
            #
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,

            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            p4.lep1_fromZ_pt,
            p4.lep1_fromZ_eta,
            p4.lep1_fromZ_phi,
            p4.lep1_fromZ_mass,
            p4.lep2_fromZ_pt,
            p4.lep2_fromZ_eta,
            p4.lep2_fromZ_phi,
            p4.lep2_fromZ_mass,
            p4.Z_pt,
            p4.Z_eta,
            p4.Z_phi,
            p4.Z_mass,

            p4.genmet_pt,
            p4.genmet_phi,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.EleID_SF,
            scalefactors.EleReco_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            p4.FourLepQuantities, # hackathon
        ],
    )
    configuration.add_producers(
        "mmmm",
        [
            event.FilterNGoodMuons, # vh == 4 muons
            lepton.CalcSmallestDiMuonMass,
            event.Mask_QuadMuonPair,
            lepton.LeptonChargeSumVeto,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            muons.LVMu3,
            muons.LVMu3_uncorrected,
            muons.LVMu4,
            muons.LVMu4_uncorrected,
        ]
    )
    configuration.add_producers(
        "mmmm_cr",
        [
            # mmmm_cr private
            event.FilterNBaseMuons, # vh == 4 base muons,
            event.FilterNGoodMuons, # vh == 3 muons
            event.FlagGoodMuonsFromHiggs, # need to add flag == 1 at post process
            lepton.CalcSmallestBaseDiMuonMass,
            event.Mask_QuadBaseMuonPair,
            lepton.BaseLeptonChargeSumVeto,
            muons.BaseLVMu1,
            muons.BaseLVMu1_uncorrected,
            muons.BaseLVMu2,
            muons.BaseLVMu2_uncorrected,
            muons.BaseLVMu3,
            muons.BaseLVMu3_uncorrected,
            muons.BaseLVMu4,
            muons.BaseLVMu4_uncorrected,
        ]
    )
    configuration.add_producers(
        ["mmmm","mmmm_cr"],
        [            
            event.DimuonMinMassCut,
            ###
            ### need make dimuon pair from Higgs and pair from Z
            
            event.Flag_ZZVeto,
            # Higgs p4
            event.HiggsToDiMuonPair_p4_4m_noFSR,
            event.ZToDiMuonPair_p4_4m,
            # Z p4
            ###
            
            electrons.GoodEle_Veto,
            # flag cut
            # event.FilterFlagDiMuFromH,
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            ###
            muons.Mu1_H_4m,
            # muons.Mu1_H_4m_pureBSC,
            # muons.Mu1_H_4m_raw,
            muons.Mu1_H_4m_noFSR,
            # muons.Mu1_H_4m_noFSR_pureBSC,
            # muons.Mu1_H_4m_noFSR_raw,
            muons.Mu1_H_4m_uncorrected,
            muons.Mu2_H_4m,
            # muons.Mu2_H_4m_pureBSC,
            # muons.Mu2_H_4m_raw,
            muons.Mu2_H_4m_noFSR,
            # muons.Mu2_H_4m_noFSR_pureBSC,
            # muons.Mu2_H_4m_noFSR_raw,
            muons.Mu2_H_4m_uncorrected,
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            muons.Mu1_Z_4m, # leading lep from Z
            muons.Mu1_Z_4m_uncorrected,
            muons.Mu2_Z_4m, # subleading lep from Z
            muons.Mu2_Z_4m_uncorrected,
            ###
            event.leplepZ_dR,
            lepton.RenameZlepID_mmmm, # using pdgId to lep_ID
            event.llZ_mmH_deta,
            event.llZ_mmH_dphi,
            event.Calc_CosThStar_Z_H,
            # pass flag, be consistent with eemm
            event.PassFlagDiEleFromZ,
            event.PassFlagDiMuonHiggs,
            event.PassMinDiEleMass,
            # Muon collection for trigger
            # triggers.GenerateSingleMuonTriggerFlagsForQuadMuChannel,
            
            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            p4.lep1_fromZ_pt,
            p4.lep1_fromZ_eta,
            p4.lep1_fromZ_phi,
            p4.lep1_fromZ_mass,
            p4.lep2_fromZ_pt,
            p4.lep2_fromZ_eta,
            p4.lep2_fromZ_phi,
            p4.lep2_fromZ_mass,
            p4.Z_pt,
            p4.Z_eta,
            p4.Z_phi,
            p4.Z_mass,

            p4.genmet_pt,
            p4.genmet_phi,            
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            p4.FourLepQuantities, # hackathon

            ###FSR###
            fsrphoton.leadingmuon_FsrPhotonIdx_4m,
            fsrphoton.subleadingmuon_FsrPhotonIdx_4m,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
        ],
    )
    configuration.add_producers(
        "nnmm",
        [
            event.FilterNGoodMuons, # vh nnmm ==2 muons
            # muons.Muons_use_for_Veto,
            muons.NumberOfVetoMuons,
            event.Filter2lTriGoodMuons,
            # event.Flag_MetCut,
            # event.FilterFlagMetCut, # MET >= 50
            event.LowMetCut, # FlagsAny MET >= 150
            # write by botao
            lepton.CalcSmallestDiMuonMass,  # SFOS, m2m only has m
            event.DimuonMinMassCut,
            ###
            event.Mask_DiMuonPair, # dimuonHiggs index
            event.Flag_DiMuonFromHiggs,
            event.HiggsToDiMuonPair_p4_noFSR,
            # event.HiggsToDiMuonPair_p4_corrected, # select the dimuon pairs in [110,150] and order by pt
            ###FSR###
            fsrphoton.leadingmuon_FsrPhotonIdx,
            fsrphoton.subleadingmuon_FsrPhotonIdx,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
            ###
            lepton.LeptonChargeSumVeto,
            ###
            electrons.GoodEle_Veto,
            # flag cut
            event.FilterFlagDiMuFromH,
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            ###
            muons.Mu1_H, # vh
            # muons.Mu1_H_pureBSC,
            # muons.Mu1_H_raw,
            muons.Mu1_H_noFSR,
            # muons.Mu1_H_noFSR_pureBSC,
            # muons.Mu1_H_noFSR_raw,
            muons.Mu2_H, # vh
            # muons.Mu2_H_pureBSC,
            # muons.Mu2_H_raw,
            muons.Mu2_H_noFSR,
            # muons.Mu2_H_noFSR_pureBSC,
            # muons.Mu2_H_noFSR_raw,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,

            muons.Mu1_H_uncorrected,
            muons.Mu2_H_uncorrected,

            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################

            ###
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            ###
            event.mumuH_MHTALL_dphi,
            event.mu1_MHTALL_dphi,
            event.mu2_MHTALL_dphi,
            
            event.mu1_mu2_dphi,
            event.met_mmH_dphi_corrected,
            #
            #muons.LVMu3, # vh 
            # vh the trigger-matched muon should have pT > 29 (26) for 2017 (2016,18)
            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            
            p4.genmet_pt,
            p4.genmet_phi,
            # genparticles.dimuon_gen_collection,
            # genparticles.genMu1_H,
            # genparticles.genMu2_H,
            # p4.genmu1_fromH_pt,
            # p4.genmu1_fromH_eta,
            # p4.genmu1_fromH_phi,
            # p4.genmu1_fromH_mass,
            # p4.genmu2_fromH_pt,
            # p4.genmu2_fromH_eta,
            # p4.genmu2_fromH_phi,
            # p4.genmu2_fromH_mass,
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            # add HighPtMuon RECO SF here
            scalefactors.MuonRECO_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            scalefactors.GenerateSingleMuonTriggerSF_MC_highPt,
            p4.METMuMuQuantities, # hackathon
        ],
    )
    configuration.add_producers(
        "fjmm",
        [
            event.FilterNGoodMuons, # vh fjmm ==2 muons
            # event.FilterNFatjets_fjmm, # vh fjmm >=1 fatjet
            # muons.Muons_use_for_Veto,
            muons.NumberOfVetoMuons,
            event.Filter2lTriGoodMuons,
            
            event.HighMetCut, # keep MET < 150 events
            # event.Flag_MaxMetCut,
            # event.FilterFlagMaxMetCut, # MET <= 150
            
            # write by botao
            lepton.CalcSmallestDiMuonMass,  # SFOS, m2m only has m
            event.DimuonMinMassCut,
            ###
            event.Mask_DiMuonPair, # dimuonHiggs index
            event.Flag_DiMuonFromHiggs,
            event.HiggsToDiMuonPair_p4_noFSR,
            # event.HiggsToDiMuonPair_p4_corrected, # select the dimuon pairs in [110,150] and order by pt
            ###FSR###
            fsrphoton.leadingmuon_FsrPhotonIdx,
            fsrphoton.subleadingmuon_FsrPhotonIdx,
            fsrphoton.leadingmuon_FsrPhoton_pt,
            fsrphoton.leadingmuon_FsrPhoton_eta,
            fsrphoton.leadingmuon_FsrPhoton_phi,
            fsrphoton.leadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.leadingmuon_FsrPhoton_relIso03,
            fsrphoton.subleadingmuon_FsrPhoton_pt,
            fsrphoton.subleadingmuon_FsrPhoton_eta,
            fsrphoton.subleadingmuon_FsrPhoton_phi,
            fsrphoton.subleadingmuon_FsrPhoton_dROverEt2,
            fsrphoton.subleadingmuon_FsrPhoton_relIso03,
            event.HiggsToDiMuonPair_p4,
            ###
            lepton.LeptonChargeSumVeto,
            ###
            electrons.GoodEle_Veto,
            # flag cut
            event.FilterFlagDiMuFromH,
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            ###
            muons.Mu1_H, # vh
            # muons.Mu1_H_pureBSC,
            # muons.Mu1_H_raw,
            muons.Mu1_H_noFSR,
            # muons.Mu1_H_noFSR_pureBSC,
            # muons.Mu1_H_noFSR_raw,
            muons.Mu2_H, # vh
            # muons.Mu2_H_pureBSC,
            # muons.Mu2_H_raw,
            muons.Mu2_H_noFSR,
            # muons.Mu2_H_noFSR_pureBSC,
            # muons.Mu2_H_noFSR_raw,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,
            
            muons.Mu1_H_uncorrected,
            muons.Mu2_H_uncorrected,
            
            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################

            # ###
            event.mumuH_dR,
            event.mumuH_dphi,
            event.mumuH_deta,
            # ###
            event.mumuH_MHTALL_dphi,
            event.mu1_MHTALL_dphi,
            event.mu2_MHTALL_dphi,
            
            event.mu1_mu2_dphi,
            # event.met_mmH_dphi_corrected, # due to limited importance, drop it
            # #
            # #muons.LVMu3, # vh 
            # # vh the trigger-matched muon should have pT > 29 (26) for 2017 (2016,18)
            p4.mu1_fromH_pt,
            # p4.mu1_fromH_pt_pureBSC,
            # p4.mu1_fromH_pt_raw,
            p4.mu1_fromH_eta,
            p4.mu1_fromH_phi,
            p4.mu2_fromH_pt,
            # p4.mu2_fromH_pt_pureBSC,
            # p4.mu2_fromH_pt_raw,
            p4.mu2_fromH_eta,
            p4.mu2_fromH_phi,
            p4.mu1_fromH_mass,
            p4.mu2_fromH_mass,
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.H_pt,
            p4.H_eta,
            p4.H_phi,
            p4.H_mass,
            
            p4.genmet_pt,
            p4.genmet_phi,
            # genparticles.BosonDecayMode,
            p4.fatjet_pt,
            p4.fatjet_eta,
            p4.fatjet_phi,
            p4.fatjet_mass,
            fatjets.BuildSubJet1,
            fatjets.BuildSubJet2,
            p4.subjet1_pt,
            p4.subjet1_eta,
            p4.subjet1_phi,
            p4.subjet1_mass,
            p4.subjet2_pt,
            p4.subjet2_eta,
            p4.subjet2_phi,
            p4.subjet2_mass,
            p4.subjet1_mu1_deltaR,
            p4.subjet1_mu2_deltaR,
            p4.subjet2_mu1_deltaR,
            p4.subjet2_mu2_deltaR,
            p4.subjet1_mu1_deltaEta,
            p4.subjet1_mu2_deltaEta,
            p4.subjet2_mu1_deltaEta,
            p4.subjet2_mu2_deltaEta,
            p4.subjet1_mu1_deltaPhi,
            p4.subjet1_mu2_deltaPhi,
            p4.subjet2_mu1_deltaPhi,
            p4.subjet2_mu2_deltaPhi,
            event.fatjet_mmH_deta_corrected,
            event.fatjet_mmH_dphi_corrected,
            event.fatjet_mmH_dR_corrected,
            event.fatjet_mu1_deta_corrected,
            event.fatjet_mu1_dphi_corrected,
            event.fatjet_mu1_dR_corrected,
            event.fatjet_mu2_deta_corrected,
            event.fatjet_mu2_dphi_corrected,
            event.fatjet_mu2_dR_corrected,
            event.fatjetSoftDropMass,
            
            # event.fatjet_PNet_withMass_QCD_Nanov9,
            # event.fatjet_PNet_withMass_WvsQCD_Nanov9,
            # event.fatjet_PNet_withMass_ZvsQCD_Nanov9,
            # event.fatjet_PNet_withMass_TvsQCD_Nanov9,
            # event.fatjet_PNet_QCD,
            # event.fatjet_PNet_withMass_QCD,
            event.fatjet_PNet_withMass_WvsQCD,
            # event.fatjet_PNet_withMass_ZvsQCD,
            # event.fatjet_PNet_withMass_TvsQCD,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            # add HighPtMuon RECO SF here
            scalefactors.MuonRECO_SF,
            # add PNet WvsQCD SF here
            scalefactors.PNetWvsQCD_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            scalefactors.GenerateSingleMuonTriggerSF_MC_highPt,
            p4.FatJetMuMuQuantities, # hackathon
            # event.FatJetQuantities, # tau1,2,3,4...
        ],
    )
    configuration.add_producers(
        "fjmm_cr",
        [
            event.FilterNGoodMuons, # vh fjmm ==2 muons
            # event.FilterNFatjets_fjmm, # vh fjmm >=1 fatjet
            muons.NumberOfVetoMuons,
            # muons.Muons_use_for_Veto,
            event.Filter2lTriGoodMuons,
            event.Flag_MaxMetCut,
            event.FilterFlagMaxMetCut, # MET <= 150
            lepton.CalcSmallestDiMuonMass,  # SFOS, m2m only has m
            event.DimuonMinMassCut,
            ###
            cr.DY_DiMuonPair_CR,
            cr.Flag_DiMuonFromCR,
            cr.FilterFlag_DiMuonFromCR,
            
            lepton.LeptonChargeSumVeto,
            electrons.GoodEle_Veto,
            # flag cut
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,
            muons.LVMu1,
            muons.LVMu1_uncorrected,
            muons.LVMu2,
            muons.LVMu2_uncorrected,

            cr.DiMuonPairCR_p4,
            cr.dimuonCR_pt,
            cr.dimuonCR_eta,
            cr.dimuonCR_phi,
            cr.dimuonCR_mass,
            
            # cr.DiMuonPairCR_p4,
            # muons.Mu1_Z_CR_uncorrected,
            # muons.Mu2_Z_CR_uncorrected,
            # p4.mu1_fromZCR_pt,
            # p4.mu2_fromZCR_pt,
            # cr.dimuonCR_pt,

            ##############################
            # met.MetCorrections,
            ##############################
            ### bwlow start to calc vars #
            ##############################

            # ###
            event.mumuZCR_dR,
            event.mumuZCR_dphi,
            event.mumuZCR_deta,
            event.ZCR_MHTALL_dphi,
            event.mu1_fromZCR_MHTALL_dphi,
            event.mu2_fromZCR_MHTALL_dphi,
            event.mu1_mu2_fromZCR_dphi,
            event.met_mm_fromZCR_dphi,

            muons.Mu1_Z_CR,
            muons.Mu1_Z_CR_uncorrected,
            muons.Mu2_Z_CR,
            muons.Mu2_Z_CR_uncorrected,
            p4.mu1_fromZCR_pt,
            p4.mu1_fromZCR_eta,
            p4.mu1_fromZCR_phi,
            p4.mu2_fromZCR_pt,
            p4.mu2_fromZCR_eta,
            p4.mu2_fromZCR_phi,
            
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,            
            p4.genmet_pt,
            p4.genmet_phi,
            p4.fatjet_pt,
            p4.fatjet_eta,
            p4.fatjet_phi,
            p4.fatjet_mass,
            fatjets.BuildSubJet1,
            fatjets.BuildSubJet2,
            p4.subjet1_pt,
            p4.subjet1_eta,
            p4.subjet1_phi,
            p4.subjet1_mass,
            p4.subjet2_pt,
            p4.subjet2_eta,
            p4.subjet2_phi,
            p4.subjet2_mass,
            p4.subjet1_mu1_deltaR,
            p4.subjet1_mu2_deltaR,
            p4.subjet2_mu1_deltaR,
            p4.subjet2_mu2_deltaR,
            p4.subjet1_mu1_deltaEta,
            p4.subjet1_mu2_deltaEta,
            p4.subjet2_mu1_deltaEta,
            p4.subjet2_mu2_deltaEta,
            p4.subjet1_mu1_deltaPhi,
            p4.subjet1_mu2_deltaPhi,
            p4.subjet2_mu1_deltaPhi,
            p4.subjet2_mu2_deltaPhi,
            event.fatjet_ZCR_deta,
            event.fatjet_ZCR_dphi,
            event.fatjet_ZCR_dR,
            event.fatjet_mu1_fromZCR_deta,
            event.fatjet_mu1_fromZCR_dphi,
            event.fatjet_mu1_fromZCR_dR,
            event.fatjet_mu2_fromZCR_deta,
            event.fatjet_mu2_fromZCR_dphi,
            event.fatjet_mu2_fromZCR_dR,
            event.fatjetSoftDropMass,

            event.fatjet_PNet_withMass_WvsQCD,            
            # genparticles.BosonDecayMode,
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            # add HighPtMuon RECO SF here
            scalefactors.MuonRECO_SF,
            # add PNet WvsQCD SF here
            scalefactors.PNetWvsQCD_SF,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            scalefactors.GenerateSingleMuonTriggerSF_MC_highPt,
            # event.FatJetQuantities, # tau1,2,3,4... # drop it
        ],
    )
    if era == "2022preEE" or era == "2022postEE" or era == "2023preBPix" or era == "2023postBPix":
        configuration.add_producers(
            ["e2m","eemm","eemm_cr","nnmm","fjmm","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","fjmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForDiMuChannel,
            ],
        )
        configuration.add_producers(
            ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
            [
                triggers.GenerateSingleMuonTriggerFlags,
            ],
        )
        configuration.add_producers(
            ["mmmm","mmmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForQuadMuChannel,
            ],
        )
        configuration.add_producers(
            ["nnmm_topcontrol"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForEleMuChannel,
            ],
        )
        # configuration.add_producers(
        #     ["nnmm"],
        #     [
        #         triggers.GenerateMETTriggerFlags,
        #     ],
        # )
        configuration.add_producers(
            ["fjmm_cr", "fjmm", "nnmm"],
            [
                muons.Muons_use_for_Veto_22To23,
            ],
        )
    if era == "2024" or era == "2025":
        configuration.add_producers(
            ["e2m","eemm","eemm_cr","nnmm","fjmm","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","fjmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForDiMuChannel_v15,
            ],
        )
        configuration.add_producers(
            ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
            [
                triggers.GenerateSingleMuonTriggerFlags_v15,
            ],
        )
        configuration.add_producers(
            ["mmmm","mmmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForQuadMuChannel_v15,
            ],
        )
        configuration.add_producers(
            ["nnmm_topcontrol"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForEleMuChannel_v15,
            ],
        )
        # configuration.add_producers(
        #     ["nnmm"],
        #     [
        #         triggers.GenerateMETTriggerFlags_v15,
        #     ],
        # )
        configuration.add_producers(
            ["fjmm_cr", "fjmm", "nnmm"],
            [
                muons.Muons_use_for_Veto,
            ],
        )
    configuration.add_producers(
        "nnmm_dycontrol",
        [
            event.FilterNGoodMuons, # vh nnmm ==2 muons
            event.Flag_MetCut,
            event.FilterFlagMetCut, # MET >= 50
            # write by botao
            lepton.CalcSmallestDiMuonMass,  # SFOS, m2m only has m
            event.DimuonMinMassCut,
            lepton.LeptonChargeSumVeto,
            ###
            electrons.GoodEle_Veto,
            # flag cut
            event.FilterFlagLepChargeSum,
            event.FilterFlagGoodEleVeto,

            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            
            cr.DY_DiMuonPair_CR,
            cr.Flag_DiMuonFromCR,
            cr.FilterFlag_DiMuonFromCR,
            cr.DiMuonPairCR_p4,
            cr.dimuonCR_pt,
            cr.dimuonCR_eta,
            cr.dimuonCR_phi,
            cr.dimuonCR_mass,
        ],
    )
    configuration.add_producers(
        "nnmm_topcontrol",
        [
            event.Flag_MetCut,
            event.FilterFlagMetCut, # MET >= 150
            event.FilterNGoodMuons,
            event.FilterNGoodElectrons,
            lepton.LeptonChargeSumVeto_elemu,
            event.FilterFlagLepChargeSum,
            
            p4.met_pt_uncorrected,
            p4.met_phi_uncorrected,
            p4.genmet_pt,
            p4.genmet_phi,
            
            cr.TOP_EleMuPair_CR_corrected,
            cr.Flag_EleMuFromCR,
            cr.FilterFlag_EleMuFromCR,
            cr.EleMuPairCR_p4,
            cr.EleMuPairCR_p4_corrected,
            
            cr.Mu_Top_CR,
            cr.Mu_Top_CR_uncorrected,
            momentumscale.Mu_Top_CR_corrected,
            cr.Ele_Top_CR,
            cr.Ele_Top_CR_uncorrected,
            
            cr.elemuCR_pt_corrected,
            cr.elemuCR_pt,
            cr.elemuCR_eta,
            cr.elemuCR_phi,
            cr.elemuCR_mass,
            # genparticles.BosonDecayMode,
            scalefactors.GenerateSingleMuonTriggerSF_MC,
            scalefactors.GenerateSingleMuonTriggerSF_MC_highPt,
            
            scalefactors.MuonID_SF,
            scalefactors.MuonIso_SF,
            # add HighPtMuon RECO SF here
            scalefactors.MuonRECO_SF,
            scalefactors.EleID_SF,
            scalefactors.EleReco_SF,
        ],
    )
    ##electron pt scale and smearing#####
    configuration.add_producers(
        ["e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"],
        # scopes,
        [electrons.ElectronPtCorrectionSmearing],
    )

    configuration.add_outputs(
        scopes,
        [
            ########test unc############
            # q.Muon_pt_uncorrected,
            ############################
            q.is_data,
            q.is_embedding,
            q.is_top,
            q.is_dyjets,
            q.is_wjets,
            q.is_diboson,
            q.is_vhmm,
            q.is_zjjew,
            q.is_triboson,
            q.is_singlehiggs,
            nanoAOD.run,
            q.lumi,
            nanoAOD.event,
            q.puweight,
            q.JetFlag_pass_veto_map,
            q.FatJetFlag_pass_veto_map,
            
            q.nbasemuons,
            q.nmuons,
            q.nbaseelectrons,
            q.nelectrons,
            q.njets,
            q.nbjets_loose,
            q.nbjets_medium,
            q.btag_weight,

            q.MHTALL_pt,
            q.MHTALL_eta,
            q.MHTALL_phi,
            q.MHTALL_mass,

            q.met_pt_uncorrected,
            q.met_phi_uncorrected,
            q.metSumEt,
            q.met_pt_corrected,
            q.met_phi_corrected,
            
            q.genmet_pt,
            q.genmet_phi,
            scalefactors.GenerateSingleMuonTriggerSF_MC.output_group,
        ],
    )
    configuration.add_outputs(
        ["e2m","m2m","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
        [
            q.pz_nu,
            q.mu1_H_dR,
            q.HT,   #add by Leyan 2024/12/20
            q.HT_met,      #add by Leyan 2024/12/20
            # q.nu_H_dR,    # add by Leyan 2024/12/20
            # q.nu_H_deta,  # add by Leyan 2024/12/20
            # q.nu_H_dphi,  # add by Leyan 2024/12/20
            q.lep_nu_dR,  # add by Leyan 2024/12/20
            # q.lep_nu_deta,  # add by Leyan 2024/12/20
            # q.lep_nu_dphi,  # add by Leyan 2024/12/20
            # q.W_p4,
            q.mu1_H_deta,
            q.mu1_H_dphi,
            q.mu2_H_dR,
            q.mu2_H_deta,
            q.mu2_H_dphi,
	        q.mu1_mu2_dR,
	        q.mu1_mu2_deta,
	        q.mu1_mu2_dphi,
            q.ptH_ov_massH,
            q.ptmu1_ov_ptH,
            q.ptmu2_ov_ptH,
            q.ptmu1_ov_massH,
            q.ptmu2_ov_massH,
            # q.mu1_nu_dR,
            # q.mu1_nu_deta,
            # q.mu1_nu_dphi,
            # q.mu2_nu_dR,
            # q.mu2_nu_deta,
            # q.mu2_nu_dphi,
            
            # q.W_eta,
            # q.W_H_dR,
            # q.W_H_deta,
            # q.W_H_dphi,
            # q.W_mu1_dR,
            # q.W_mu1_deta,
            # q.W_mu1_dphi,
            # q.W_mu2_dR,
            # q.W_mu2_deta,
            # q.W_mu2_dphi,
            q.W_lep_dR,
            # q.W_lep_deta,
            # q.W_lep_dphi,
            q.W_nu_dR,
            # q.W_nu_deta,
            # q.W_nu_dphi,
            q.ptW_ov_ptH,
            q.met_ov_ptW,
            q.ptl_ov_ptW,
            
            q.lep_W_cosThStar,
            q.mu1_H_cosThStar,
            q.H_WH_cosThStar,
            # q.mu1_mu2_kT,
            # q.mu1_mu2_antikT,
        ]
    )
    # hackathon
    configuration.add_outputs(
        ["eemm","eemm_cr","mmmm","mmmm_cr"],
        [
            q.ptH_ov_massH,
            q.Z_H_dR, ## mingxuan add 2024/12/24
            q.lep1_lep2_cosThStar,
            q.mu1_H_cosThStar,
            
            # q.lep1_mu1_dR,
            # q.lep1_mu1_deta,
            # q.lep1_mu1_dphi,
            # q.lep1_mu2_dR,
            # q.lep1_mu2_deta,
            # q.lep1_mu2_dphi,

            # q.lep2_mu1_dR,
            # q.lep2_mu1_deta,
            # q.lep2_mu1_dphi,
            # q.lep2_mu2_dR,
            # q.lep2_mu2_deta,
            # q.lep2_mu2_dphi,

            # q.lep1_lep2_dR,
            # q.lep1_lep2_deta,
            # q.lep1_lep2_dphi,

            q.ptmu1_ov_ptH, ##mingxuan add 2024/12/25
            q.ptmu2_ov_ptH,
            q.ptmu1_ov_massH,
            q.ptmu2_ov_massH,

            q.ptZ_ov_massZ,
            q.ptlep1_ov_massZ,
            q.ptlep1_ov_ptZ,
            q.ptlep2_ov_massZ,
            q.ptlep2_ov_ptZ,

            # q.cosThStar_4l_hzz, ##mingxuan add 2024/12/27
            # q.cosTh1_4l_hzz,
            # q.cosphi_4l_hzz,
            # q.cosphi1_4l_hzz,
        ]
    )
    # hackathon
    configuration.add_outputs(
        ["nnmm"],
        [
            q.ptH_ov_massH,
            q.ptmu1_ov_massH,
            q.ptmu1_ov_ptH,
            q.ptmu2_ov_massH,
            q.ptmu2_ov_ptH,

            q.mu1_H_cosThStar,

            q.met_ov_massH,
            q.met_ov_ptH,
            q.met_mu1_dphi,
            q.met_mu2_dphi,

            q.Mct, ##mingxuan add 2024/12/28

            q.MT2, ##mingxuan add 2025/1/1
        ]
    )
    # hackathon
    configuration.add_outputs(
        ["fjmm"],
        [
            q.ptH_ov_massH,
            q.ptmu1_ov_massH,
            # q.ptmu1_ov_ptH, # due to limited importance, drop it
            q.ptmu2_ov_massH,
            q.ptmu2_ov_ptH,

            q.mu1_H_cosThStar,

            q.ptfj_ov_ptH,
            q.mfj_ov_massH,
            
            ###Mingxuan 2025.07.23
            q.MT2_fjmm,
            q.Mct_fjmm,
            q.msdfj_ov_massH,
            q.ptfj_ov_massH,

            # q.cosphi1_fj_hzz, ##mingxuan add 2024/12/28
            # q.cosTh1_fj_hzz,
            # q.cosThStar_fj_hzz, # drop it
        ]
    )
    configuration.add_outputs(
        ["fjmm","fjmm_cr"],
        [
            # q.fatjet_tau1, # drop it
            # q.fatjet_tau2, # drop it
            # q.fatjet_tau3, # drop it
            # q.fatjet_tau4, # drop it
            q.pnet_wqcd_wgt,
        ]
    )
    ### HighPtMuon RECO SF 
    configuration.add_outputs(
        ["nnmm","fjmm","fjmm_cr"],
        [
            q.reco_wgt_mu_1_above200,
            q.reco_wgt_mu_2_above200,
        ]
    )
    
    configuration.add_outputs(
        ["e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc"],
        [
            q.mu1_fromH_pt,
            # q.mu1_fromH_pt_pureBSC,
            # q.mu1_fromH_pt_raw,
            q.mu1_fromH_eta,
            q.mu1_fromH_phi,
            q.mu1_fromH_mass,

            q.mu2_fromH_pt,
            # q.mu2_fromH_pt_pureBSC,
            # q.mu2_fromH_pt_raw,
            q.mu2_fromH_eta,
            q.mu2_fromH_phi,
            q.mu2_fromH_mass,
            
            q.H_pt,
            q.H_eta,
            q.H_phi,
            q.H_mass,
        ],
    )
    configuration.add_outputs(
        ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
         "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr"],
        [            
            q.id_wgt_mu_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_1,
            q.iso_wgt_mu_2,
            
            q.id_wgt_mu_1_above200,
            q.id_wgt_mu_2_above200,
            q.iso_wgt_mu_1_above200,
            q.iso_wgt_mu_2_above200,

            q.id_wgt_mu_mvatth_1,
            q.id_wgt_mu_mvatth_2,
            # q.iso_wgt_mu_1_below15,
            # q.iso_wgt_mu_2_below15,
            q.id_wgt_mu_dxydz3dsip_1,
            q.id_wgt_mu_dxydz3dsip_2,
        ],
    )
    configuration.add_outputs(
        ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
         "eemm","eemm_cr","mmmm","mmmm_cr"],
        [
            q.id_wgt_mu_1_below15,
            q.id_wgt_mu_2_below15,
        ],
    )
    configuration.add_outputs(
        ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond","mmmm","mmmm_cr"],
        [
            q.id_wgt_mu_3,
            q.iso_wgt_mu_3,
            
            q.id_wgt_mu_3_below15,
            
            q.id_wgt_mu_3_above200,
            q.iso_wgt_mu_3_above200,
            
            q.id_wgt_mu_mvatth_3,
            q.id_wgt_mu_dxydz3dsip_3,
            
            # q.iso_wgt_mu_3_below15,
        ],
    )
    configuration.add_outputs(
        ["mmmm","mmmm_cr"],
        [
            q.id_wgt_mu_4,
            q.iso_wgt_mu_4,
            
            q.id_wgt_mu_4_below15,
            
            q.id_wgt_mu_4_above200,
            q.iso_wgt_mu_4_above200,
            
            q.id_wgt_mu_mvatth_4,
            q.id_wgt_mu_dxydz3dsip_4,

            # q.iso_wgt_mu_4_below15,
        ],
    )
    configuration.add_outputs(
        ["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm","eemm_cr","nnmm_topcontrol"],
        [
            q.id_wgt_ele_loose_1,
            q.id_wgt_ele_loose_1_below10,
            q.id_wgt_ele_wp90Iso_1,
            q.id_wgt_ele_wp90Iso_1_below10,
            q.reco_wgt_ele_1,
            q.reco_wgt_ele_1_below10,
            q.id_wgt_ele_mvatth_1,
        ],
    )
    configuration.add_outputs(
        ["eemm","eemm_cr"],
        [
            q.id_wgt_ele_loose_2,
            q.id_wgt_ele_loose_2_below10,
            q.id_wgt_ele_wp90Iso_2,
            q.id_wgt_ele_wp90Iso_2_below10,
            q.reco_wgt_ele_2,
            q.reco_wgt_ele_2_below10,
            q.id_wgt_ele_mvatth_2,
        ],
    )
    configuration.add_outputs(
        ["e2m","m2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
        [
            q.W_pt,
            q.W_phi,

            q.mt_W,
            
            q.lep_MHTALL_dphi,
            q.mt_muSSAndMHTALL,
            q.mt_muOSAndMHTALL,
            q.mt_lepWAndMHTALL,
            
            q.extra_lep_pt,
            q.extra_lep_eta,
            q.extra_lep_phi,
            q.extra_lep_mass,
            # q.extra_lep_mvaTTH,
            q.lep_muOS_cosThStar,
            q.lep_muSS_cosThStar,
            q.lep_muSS_dR,
            q.lep_muOS_dR,
            q.lep_muSS_deta,
            q.lep_muOS_deta,
        ]
    )
    configuration.add_outputs(
        ["e2m","m2m","e2m_dyfakeinge_regionc","m2m_dyfakeingmu_regionc"],
        [            
            q.lep_H_dR,
            q.lep_H_deta,
            q.lep_H_dphi,
            q.mumuH_dR,
            q.mumuH_dphi,
            q.mumuH_deta,

            q.muOS_pt,
            q.muOS_eta,
            q.muOS_phi,
            q.muSS_pt,
            q.muSS_eta,
            q.muSS_phi,            
            ###
            q.mumuH_MHTALL_dphi,
            q.mu1_MHTALL_dphi,
            q.mu2_MHTALL_dphi,
            
            q.mu1_mu2_dphi,
            q.lep_mu1_dphi,
            q.lep_mu2_dphi,
            q.smallest_dimuon_mass,
            
            q.Flag_dimuon_Zmass_veto,
            q.Flag_LeptonChargeSumVeto,
            q.Flag_GoodEle_Veto,
            q.Flag_DiMuonFromHiggs,
        ],
    )
    configuration.add_outputs(
        # Region B: pass 3 medium muons and fail m(mm) in [110,150], actually in [70,110]
        ["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
        [
            q.lep_Z_dR,
            q.lep_Z_dphi,            
        ],
    )
    configuration.add_outputs(
        ["e2m_dyfakeinge_regionb","e2m_dyfakeinge_regiond",
         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond",
         "fjmm_cr"],
        [
            q.smallest_dimuon_mass,
            q.Flag_LeptonChargeSumVeto,
            q.Flag_DiMuonFromCR,
            q.dimuonCR_pt,
            q.dimuonCR_eta,
            q.dimuonCR_phi,
            q.dimuonCR_mass,
            q.mu1_fromZCR_pt,
            q.mu1_fromZCR_eta,
            q.mu1_fromZCR_phi,
            q.mu2_fromZCR_pt,
            q.mu2_fromZCR_eta,
            q.mu2_fromZCR_phi,
            q.mumuZCR_dR,
            q.mumuZCR_dphi,
            q.mumuZCR_deta,
            q.ZCR_MHTALL_dphi,
            q.mu1_fromZCR_MHTALL_dphi,
            q.mu2_fromZCR_MHTALL_dphi,
            q.mu1_mu2_fromZCR_dphi,
            q.met_mm_fromZCR_dphi,
        ],
    )
    if era == "2022preEE" or era == "2022postEE" or era == "2023preBPix" or era == "2023postBPix":
        configuration.add_outputs(
            ["m2m","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
            [
                triggers.GenerateSingleMuonTriggerFlags.output_group,
            ],
        )
        configuration.add_outputs(
            ["e2m","eemm","eemm_cr","nnmm","fjmm","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","fjmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForDiMuChannel.output_group,
            ],
        )
        configuration.add_outputs(
            ["mmmm","mmmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForQuadMuChannel.output_group,
            ],
        )
        configuration.add_outputs(
            ["nnmm_topcontrol"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForEleMuChannel.output_group,
            ],
        
        )
        # configuration.add_outputs(
        #     ["nnmm"],
        #     [
        #         triggers.GenerateMETTriggerFlags.output_group,
        #     ],
        # )
    if era == "2024" or era == "2025":
        configuration.add_outputs(
            ["m2m","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
            [
                triggers.GenerateSingleMuonTriggerFlags_v15.output_group,
            ],
        )
        configuration.add_outputs(
            ["e2m","eemm","eemm_cr","nnmm","fjmm","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","fjmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForDiMuChannel_v15.output_group,
            ],
        )
        configuration.add_outputs(
            ["mmmm","mmmm_cr"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForQuadMuChannel_v15.output_group,
            ],
        )
        configuration.add_outputs(
            ["nnmm_topcontrol"],
            [
                triggers.GenerateSingleMuonTriggerFlagsForEleMuChannel_v15.output_group,
            ],
        )
        # configuration.add_outputs(
        #     ["nnmm"],
        #     [
        #         triggers.GenerateMETTriggerFlags_v15.output_group,
        #     ],
        # )
    configuration.add_outputs(
        ["m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regiond"],
        [
            q.Flag_GoodEle_Veto,   
        ]
    )
    configuration.add_outputs(
        ["eemm","eemm_cr","mmmm","mmmm_cr"],
        [
            q.mumuH_dR,
            q.mumuH_dphi,
            q.mumuH_deta,
            #
            q.lep1_fromZ_pt,
            q.lep1_fromZ_eta,
            q.lep1_fromZ_phi,
            q.lep1_fromZ_mass,

            q.lep2_fromZ_pt,
            q.lep2_fromZ_eta,
            q.lep2_fromZ_phi,
            q.lep2_fromZ_mass,
            ###
            q.llZ_dR,
            q.Zlep_ID,
            q.Z_H_deta,
            q.Z_H_dphi,
            q.Z_H_cosThStar,
            ###
            q.smallest_dimuon_mass,
            q.smallest_dielectron_mass,
            q.Flag_LeptonChargeSumVeto,

            q.Z_pt,
            q.Z_eta,
            q.Z_phi,
            q.Z_mass,

            q.Flag_GoodEle_Veto, # all pass flag ele veto, all 1
            q.Flag_ZZVeto, # all pass flag ZZ veto, all 1
            q.Flag_DiEleFromZ,
            q.Flag_DiMuonFromHiggs,            
        ]
    )
    configuration.add_outputs(
        "mmmm_cr",
        [
            q.FlagGoodMuonsFromHiggs,
        ],
    )
    configuration.add_outputs(
        "nnmm",
        [
            q.mumuH_dR,
            q.mumuH_dphi,
            q.mumuH_deta,
            ###
            q.mumuH_MHTALL_dphi,
            q.mu1_MHTALL_dphi,
            q.mu2_MHTALL_dphi,
            q.mu1_mu2_dphi,
            q.met_H_dphi,
            # q.MHTALL_p4,
            # add cut nfatjet<=0 to remove the overlap with fjmm
            q.nfatjets,
            q.smallest_dimuon_mass,
            # q.Flag_MetCut,
            q.Flag_LeptonChargeSumVeto,
            q.Flag_GoodEle_Veto,
            q.Flag_DiMuonFromHiggs,
            # triggers.GenerateSingleMuonTriggerFlagsForDiMuChannel.output_group,
            scalefactors.GenerateSingleMuonTriggerSF_MC_highPt.output_group,
            
            # q.genmu1_fromH_pt,
            # q.genmu1_fromH_eta,
            # q.genmu1_fromH_phi,
            # q.genmu1_fromH_mass,
            # q.genmu2_fromH_pt,
            # q.genmu2_fromH_eta,
            # q.genmu2_fromH_phi,
            # q.genmu2_fromH_mass,
        ],
    )
    configuration.add_outputs(
        "fjmm",
        [
            q.mumuH_dR,
            q.mumuH_dphi,
            q.mumuH_deta,
            q.nfatjets,

            q.mumuH_MHTALL_dphi,
            q.mu1_MHTALL_dphi,
            q.mu2_MHTALL_dphi,
            q.mu1_mu2_dphi,
            # q.met_H_dphi, # due to limited importance, drop it

            q.smallest_dimuon_mass,
            # q.Flag_MaxMetCut,
            q.Flag_LeptonChargeSumVeto,
            q.Flag_GoodEle_Veto,
            q.Flag_DiMuonFromHiggs,
            scalefactors.GenerateSingleMuonTriggerSF_MC_highPt.output_group,
            
            q.fatjet_msoftdrop,
            q.fatjet_pt,
            q.fatjet_eta,
            q.fatjet_phi,
            q.fatjet_mass,
            q.subjet1_pt,
            q.subjet1_eta,
            q.subjet1_phi,
            q.subjet1_mass,
            q.subjet2_pt,
            q.subjet2_eta,
            q.subjet2_phi,
            q.subjet2_mass,
            q.subjet1_mu1_deltaR,
            q.subjet1_mu2_deltaR,
            q.subjet2_mu1_deltaR,
            q.subjet2_mu2_deltaR,
            q.subjet1_mu1_deltaEta,
            q.subjet1_mu2_deltaEta,
            q.subjet2_mu1_deltaEta,
            q.subjet2_mu2_deltaEta,
            q.subjet1_mu1_deltaPhi,
            q.subjet1_mu2_deltaPhi,
            q.subjet2_mu1_deltaPhi,
            q.subjet2_mu2_deltaPhi,
            q.good_FatJet_particleNet_massCorr,
            q.good_FatJet_rawfactor,
            q.fatjet_mmH_deta,
            q.fatjet_mmH_dphi,
            q.fatjet_mmH_dR,
            q.fatjet_mu1_deta,
            q.fatjet_mu1_dphi,
            q.fatjet_mu1_dR,
            q.fatjet_mu2_deta,
            q.fatjet_mu2_dphi,
            q.fatjet_mu2_dR,
            q.fatjet_PNet_withMass_WvsQCD,
        ],
    )
    configuration.add_outputs(
        "fjmm_cr",
        [
            q.nfatjets,
            q.Flag_MaxMetCut,
            q.Flag_GoodEle_Veto,
            q.fatjet_msoftdrop,
            q.fatjet_pt,
            q.fatjet_eta,
            q.fatjet_phi,
            q.fatjet_mass,
            q.subjet1_pt,
            q.subjet1_eta,
            q.subjet1_phi,
            q.subjet1_mass,
            q.subjet2_pt,
            q.subjet2_eta,
            q.subjet2_phi,
            q.subjet2_mass,
            q.subjet1_mu1_deltaR,
            q.subjet1_mu2_deltaR,
            q.subjet2_mu1_deltaR,
            q.subjet2_mu2_deltaR,
            q.subjet1_mu1_deltaEta,
            q.subjet1_mu2_deltaEta,
            q.subjet2_mu1_deltaEta,
            q.subjet2_mu2_deltaEta,
            q.subjet1_mu1_deltaPhi,
            q.subjet1_mu2_deltaPhi,
            q.subjet2_mu1_deltaPhi,
            q.subjet2_mu2_deltaPhi,
            q.good_FatJet_particleNet_massCorr,
            q.good_FatJet_rawfactor,
            q.fatjet_PNet_withMass_WvsQCD,
            scalefactors.GenerateSingleMuonTriggerSF_MC_highPt.output_group,
            
            q.dimuonCR_pt,
            q.mu1_fromZCR_pt,
            q.mu2_fromZCR_pt,
        ],
    )
    configuration.add_outputs(
        "nnmm_dycontrol",
        [
            q.smallest_dimuon_mass,
            q.Flag_MetCut,
            q.Flag_LeptonChargeSumVeto,
            q.Flag_GoodEle_Veto,
            q.Flag_DiMuonFromCR,
            # q.dimuon_p4_CR,
            q.dimuonCR_pt,
            q.dimuonCR_eta,
            q.dimuonCR_phi,
            q.dimuonCR_mass,
        ],
    )
    configuration.add_outputs(
        "nnmm_topcontrol",
        [
            
            q.Flag_MetCut,
            q.Flag_LeptonChargeSumVeto,
            q.Flag_EleMuFromCR,
            # q.elemu_p4_CR,
            q.elemuCR_pt,
            q.elemuCR_pt_corrected,
            q.elemuCR_eta,
            q.elemuCR_phi,
            q.elemuCR_mass,

            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,
            q.id_wgt_mu_1_below15,
            q.id_wgt_mu_mvatth_1,
            q.id_wgt_mu_dxydz3dsip_1,
            
            q.id_wgt_mu_1_above200,
            q.iso_wgt_mu_1_above200,
            q.reco_wgt_mu_1_above200

        ],
    )
    ### FSR ###
    configuration.add_outputs(
        ["e2m","m2m","eemm","eemm_cr","nnmm","fjmm","m2m_dyfakeingmu_regionc","e2m_dyfakeinge_regionc", "mmmm", "mmmm_cr"],
        [
            q.FsrPhotonIdx_1,
            q.FsrPhotonIdx_2,
        ]
    )
    configuration.add_outputs(
        ["e2m","m2m","eemm","nnmm","fjmm","mmmm"],
        [
            q.FsrPhoton1_pt,
            q.FsrPhoton1_eta,
            q.FsrPhoton1_phi,
            q.FsrPhoton1_dROverEt2,
            q.FsrPhoton1_relIso03,
            q.FsrPhoton2_pt,
            q.FsrPhoton2_eta,
            q.FsrPhoton2_phi,
            q.FsrPhoton2_dROverEt2,
            q.FsrPhoton2_relIso03,
        ]
    )
    # configuration.add_outputs(
    #     ["mmmm", "mmmm_cr"],
    #     [
    #         q.FsrPhoton1_pt,
    #         q.FsrPhoton1_eta,
    #         q.FsrPhoton1_phi,
    #     ]
    # )
    # add genWeight for everything but data
    if sample != "data":
        configuration.add_outputs(
            scopes,
            nanoAOD.genWeight,
        )
    # update the metfilter flag here
    if era == "2022preEE" or era == "2022postEE" or era =="2023preBPix" or era == "2023postBPix":
        if sample == "data":
            configuration.add_outputs(
                scopes,
                q.Flag_ecalBadCalibFilter_cuttomized,
            )
    ##### debug on 2017 AK8 jet
    if era == "2017" and sample != "data":
        configuration.add_modification_rule(
            "global",
            RemoveProducer(
                producers=[fatjets.FatJetEnergyCorrection_run2,],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            "global",
            AppendProducer(
                producers=[fatjets.FatJetEnergyCorrection_2017_noPtCorr,],
                samples=sample,
                update_output=False,
            ),
        )
    # ParticleNet Vars are different in v9 and v12
    if era == "2018" or era == "2017" or era == "2016preVFP" or era == "2016postVFP":
        configuration.add_modification_rule(
            "global",
            RemoveProducer(
                producers=[
                    electrons.BaseElectrons_v2,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            "global",
            AppendProducer(
                producers=[
                    electrons.BaseElectrons_v2_run2,
                ],
                samples=sample,
                update_output=False, # false , no need the internal mask to output
            ),
        )
        configuration.add_modification_rule(
            ["fjmm","fjmm_cr"],
            RemoveProducer(
                producers=[
                    fatjets.GoodFatJets,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            ["fjmm","fjmm_cr"],
            AppendProducer(
                producers=[
                    fatjets.GoodFatJets_run2,
                ],
                samples=sample,
                update_output=False, # false , no need the internal mask to output
            ),
        )
        configuration.add_modification_rule(
            scopes,
            RemoveProducer(
                producers=[
                    jets.GoodBJetsLoose_PNet, 
                    jets.GoodBJetsMedium_PNet,
                    # scalefactors.btaggingloose_SF,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            scopes,
            AppendProducer(
                producers=[
                    jets.GoodBJetsLoose, 
                    jets.GoodBJetsMedium,
                    # scalefactors.btaggingloose_SF_run2,
                ],
                samples=sample,
                update_output=False, # false , no need the internal mask to output
            ),
        )
        configuration.add_modification_rule(
            ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
            RemoveProducer(
                producers=[
                    triggers.GenerateSingleMuonTriggerFlags,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            ["m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond"],
            AppendProducer(
                producers=[
                    triggers.GenerateSingleMuonTriggerFlags_run2,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            ["e2m","eemm","nnmm","fjmm","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","fjmm_cr"],
            RemoveProducer(
                producers=[
                    triggers.GenerateSingleMuonTriggerFlagsForDiMuChannel,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            ["e2m","eemm","nnmm","fjmm","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","fjmm_cr"],
            AppendProducer(
                producers=[
                    triggers.GenerateSingleMuonTriggerFlagsForDiMuChannel_run2,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            "mmmm",
            RemoveProducer(
                producers=[
                    triggers.GenerateSingleMuonTriggerFlagsForQuadMuChannel,
                ],
                samples=sample,
            ),
        )
        configuration.add_modification_rule(
            "mmmm",
            AppendProducer(
                producers=[
                    triggers.GenerateSingleMuonTriggerFlagsForQuadMuChannel_run2,
                ],
                samples=sample,
            ),
        )
        # for data
        configuration.add_modification_rule(
            "global",
            RemoveProducer(
                producers=[event.PUweights, jets.JetEnergyCorrection_run2, fatjets.FatJetEnergyCorrection_run2, met.BuildGenMetVector,],
                samples=["data"],
            ),
        )
        # configuration.add_modification_rule(
        #     scopes,
        #     RemoveProducer(
        #         producers=[
        #             scalefactors.btaggingloose_SF_run2,
        #         ],
        #         samples=["data"],
        #     ),
        # )
    if era == "2022preEE" or era == "2022postEE" or era =="2023preBPix" or era == "2023postBPix":
        configuration.add_modification_rule(
            "global",
            RemoveProducer(
                producers=[event.PUweights, met.BuildGenMetVector,],
                samples=["data"],
            ),
        )
        configuration.add_modification_rule(
            "global",
            ReplaceProducer(
                producers=[jets.JetEnergyCorrection, jets.JetEnergyCorrection_data],
                samples=["data"],
            )
        )
        configuration.add_modification_rule(
            "global",
            ReplaceProducer(
                producers=[fatjets.FatJetEnergyCorrection, fatjets.FatJetEnergyCorrection_data],
                samples=["data"],
            )
        )
    if era == "2024" or era == "2025":
        configuration.add_modification_rule(
            "global",
            RemoveProducer(
                producers=[event.PUweights, met.BuildGenMetVector,],
                samples=["data"],
            ),
        )
        configuration.add_modification_rule(
            "global",
            ReplaceProducer(
                producers=[jets.JetEnergyCorrection, jets.JetEnergyCorrection_data],
                samples=["data"],
            )
        )
        configuration.add_modification_rule(
            "global",
            ReplaceProducer(
                producers=[fatjets.FatJetEnergyCorrection, fatjets.FatJetEnergyCorrection_data],
                samples=["data"],
            )
        )
        # configuration.add_modification_rule(
        #     scopes,
        #     RemoveProducer(
        #         producers=[
        #             # genparticles.BosonDecayMode,
        #             scalefactors.btaggingloose_SF,
        #         ],
        #         samples=["data"],
        #     ),
        # )
    ### DY pt reweight
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=event.ZPtMassReweighting, samples=["dyjets"]
        ),
    )
    # global scope
    ### add the "Flag_ecalBadCalibFilter" update here:
    ### https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Run_3_2022_and_2023_data_and_MC
    if era == "2022preEE" or era == "2022postEE" or era =="2023preBPix" or era == "2023postBPix":
        configuration.add_modification_rule(
            "global",
            AppendProducer(
                producers=[
                    # jets.RenameJetsData, 
                    # fatjets.RenameFatJetsData, 
                    event.JSONFilter,
                    jets.cutsomized_Flag_ecalBadCalibFilter,
                ],
                samples=["data"],
                update_output=False,
            ),
        )
    if era == "2024" or era == "2025":
        configuration.add_modification_rule(
            "global",
            AppendProducer(
                producers=[
                    # jets.RenameJetsData_v15, 
                    # fatjets.RenameFatJetsData, 
                    event.JSONFilter,
                ],
                samples=["data"],
                update_output=False,
            ),
        )
    configuration.add_modification_rule(
        scopes,
        RemoveProducer(
            producers=[
                p4.genmet_pt,
                p4.genmet_phi,
            ],
            samples=["data"],
        ),
    )
    # configuration.add_modification_rule(
    #     ["nnmm"],
    #     RemoveProducer(
    #         producers=[
    #             genparticles.dimuon_gen_collection,
    #             genparticles.genMu1_H,
    #             genparticles.genMu2_H,
    #             p4.genmu1_fromH_pt,
    #             p4.genmu1_fromH_eta,
    #             p4.genmu1_fromH_phi,
    #             p4.genmu1_fromH_mass,
    #             p4.genmu2_fromH_pt,
    #             p4.genmu2_fromH_eta,
    #             p4.genmu2_fromH_phi,
    #             p4.genmu2_fromH_mass,
    #         ],
    #         samples=["data"],
    #     ),
    # )
    configuration.add_modification_rule(
        ["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm","nnmm_topcontrol"],
        RemoveProducer(
            producers=[
                scalefactors.EleID_SF,
                scalefactors.EleReco_SF,
            ],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
         "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "eemm","mmmm","nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
        RemoveProducer(
            producers=[
                scalefactors.MuonID_SF,
                scalefactors.MuonIso_SF,
                scalefactors.GenerateSingleMuonTriggerSF_MC,
            ],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
        RemoveProducer(
            producers=[
                scalefactors.MuonRECO_SF,
            ],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["fjmm","fjmm_cr"],
        RemoveProducer(
            producers=[
                scalefactors.PNetWvsQCD_SF,
            ],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["nnmm","fjmm","fjmm_cr","nnmm_topcontrol"],
        ReplaceProducer(
            producers=[momentumscale.MuonPtCorrection,momentumscale.RenameMuonPt],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
        ReplaceProducer(
            producers=[momentumscale.MC_KIT_MuonPt_ScaleRes, momentumscale.Data_KIT_MuonPt_Scale],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["nnmm","fjmm","fjmm_cr",],
        ReplaceProducer(
            producers=[momentumscale.MC_KIT_MuonPt_ScaleRes_HighPt, momentumscale.Data_KIT_MuonPt_Scale_HighPt],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["nnmm","fjmm","fjmm_cr"],
        ReplaceProducer(
            producers=[momentumscale.MuonPtPreCorrection, momentumscale.MuonPtPreCorrectionData],
            samples=["data"],
        ),
    )
    # configuration.add_modification_rule(
    #     ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #     "nnmm_dycontrol","nnmm_topcontrol",
    #     "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #     "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    #     ReplaceProducer(
    #         producers=[momentumscale.MC_KIT_MuonPt_ScaleRes_pureBSC, momentumscale.Data_KIT_MuonPt_Scale_pureBSC],
    #         samples=["data"],
    #     ),
    # )
    # configuration.add_modification_rule(
    #     ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #     "nnmm_dycontrol","nnmm_topcontrol",
    #     "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #     "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    #     ReplaceProducer(
    #         producers=[momentumscale.MC_KIT_MuonPt_ScaleRes_raw, momentumscale.Data_KIT_MuonPt_Scale_raw],
    #         samples=["data"],
    #     ),
    # )
    # configuration.add_modification_rule(
    #     ["e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
    #     ReplaceProducer(
    #         producers=[momentumscale.MC_Rochester_MuonPt_ScaleRes, momentumscale.Data_Rochester_MuonPt_ScaleRes],
    #         samples=["data"],
    #     ),
    # )
    configuration.add_modification_rule(
        ["e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"],
        ReplaceProducer(
            producers=[electrons.ElectronPtCorrectionSmearing, electrons.ElectronPtCorrectionScaling],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        ["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"],
            ReplaceProducer(
                producers=[scalefactors.btagging_SF_2WPs_3l_4l, scalefactors.btagging_SF_2WPs_3l_4l_dy],
                samples=["dyjets"],
            ),
    )
    configuration.add_modification_rule(
        ["e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"],
            ReplaceProducer(
                producers=[scalefactors.btagging_SF_2WPs_3l_4l, scalefactors.btagging_SF_2WPs_3l_4l_vhmm],
                samples=["vhmm", "singlehiggs"],
            ),
    )

    configuration.add_modification_rule(
        ["fjmm","fjmm_cr"],
            ReplaceProducer(
                producers=[scalefactors.btagging_SF_2WPs_fjmm, scalefactors.btagging_SF_2WPs_fjmm_dy],
                samples=["dyjets"],
            ),
    )
    configuration.add_modification_rule(
        ["fjmm","fjmm_cr"],
            ReplaceProducer(
                producers=[scalefactors.btagging_SF_2WPs_fjmm, scalefactors.btagging_SF_2WPs_fjmm_vhmm],
                samples=["vhmm", "singlehiggs"],
            ),
    )

    configuration.add_modification_rule(
        ["nnmm"],
            ReplaceProducer(
                producers=[scalefactors.btagging_SF_2WPs_met, scalefactors.btagging_SF_2WPs_met_dy],
                samples=["dyjets"],
            ),
    )
    configuration.add_modification_rule(
        ["nnmm"],
            ReplaceProducer(
                producers=[scalefactors.btagging_SF_2WPs_met, scalefactors.btagging_SF_2WPs_met_vhmm],
                samples=["vhmm", "singlehiggs"],
            ),
    )
    #### update btag sf by Mingxuan ####
    configuration.add_modification_rule(
        ["e2m","m2m", "eemm","mmmm","eemm_cr","mmmm_cr",
         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"],
         RemoveProducer(
            producers=[
                scalefactors.btagging_SF_2WPs_3l_4l,
            ],
            samples=["data"],
         ),
    )
    configuration.add_modification_rule(
        ["fjmm", "fjmm_cr"],
         RemoveProducer(
            producers=[
                scalefactors.btagging_SF_2WPs_fjmm,
            ],
            samples=["data"],
         ),
    )
    configuration.add_modification_rule(
        ["nnmm"],
         RemoveProducer(
            producers=[
                scalefactors.btagging_SF_2WPs_met,
            ],
            samples=["data"],
         ),
    )
    ##########################################################
    # configuration.add_modification_rule(
    #     ["nnmm","fjmm"],
    #     ReplaceProducer(
    #         producers=[jets.Calc_MHT_all,jets.Calc_MHT_all_corrected],
    #         samples=sample,
    #     ),
    # )
    
    #######################
    #### Pileup Shifts ####
    #######################
    configuration.add_shift(
        SystematicShift(
            name="PileUpUp",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "up"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="PileUpDown",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "down"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    #########################
    # MET Shifts
    #########################
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnUp",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredUp",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredUp",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnDown",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredDown",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredDown",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    ##########################
    #### DY ptll reweight shift ####
    ##########################
    if "dyjets" in sample:
        for n in range(1,11):
            ## NLO contains 10 Uncs. 
            configuration.add_shift(
                SystematicShift(
                    name="DY_pTll_reweighting" + str(n) + "Up",
                    shift_config={
                        ("e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
                         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"DY_pTll_reweighting_syst": "up" + str(n)},
                    },
                    producers={("e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
                                "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                                "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [event.ZPtMassReweighting]},
                )
            )
            configuration.add_shift(
                SystematicShift(
                    name="DY_pTll_reweighting" + str(n) + "Down",
                    shift_config={
                        ("e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
                         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"DY_pTll_reweighting_syst": "down" + str(n)},
                    },
                    producers={("e2m","m2m","eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr","nnmm_topcontrol",
                                "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                                "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [event.ZPtMassReweighting]},
                )
            )
    ##########################
    #### btag weight shift ###
    ##########################
    configuration.add_shift(
        SystematicShift(
            name="BtagWeightUp",
            shift_config={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"): {
                "BtagWeightVariation": "up"
                }
            },
            producers={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"): {
                scalefactors.btagging_SF_2WPs_3l_4l,
                scalefactors.btagging_SF_2WPs_3l_4l_dy,
                scalefactors.btagging_SF_2WPs_3l_4l_vhmm,
                }
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="BtagWeightUp",
            shift_config={
                ("fjmm", "fjmm_cr"): {
                "BtagWeightVariation": "up"
                }
            },
            producers={
                ("fjmm", "fjmm_cr"): {
                scalefactors.btagging_SF_2WPs_fjmm,
                scalefactors.btagging_SF_2WPs_fjmm_dy,
                scalefactors.btagging_SF_2WPs_fjmm_vhmm,
                }
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="BtagWeightUp",
            shift_config={
                ("nnmm"): {
                "BtagWeightVariation": "up"
                }
            },
            producers={
                ("nnmm"): {
                scalefactors.btagging_SF_2WPs_met,
                scalefactors.btagging_SF_2WPs_met_dy,
                scalefactors.btagging_SF_2WPs_met_vhmm,
                }
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="BtagWeightDown",
            shift_config={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"): {
                "BtagWeightVariation": "down"
                }
            },
            producers={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
            "m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
            "eemm","mmmm", "eemm_cr", "mmmm_cr"): {
                scalefactors.btagging_SF_2WPs_3l_4l,
                scalefactors.btagging_SF_2WPs_3l_4l_dy,
                scalefactors.btagging_SF_2WPs_3l_4l_vhmm,
                }
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="BtagWeightDown",
            shift_config={
                ("fjmm", "fjmm_cr"): {
                "BtagWeightVariation": "down"
                }
            },
            producers={
                ("fjmm", "fjmm_cr"): {
                scalefactors.btagging_SF_2WPs_fjmm,
                scalefactors.btagging_SF_2WPs_fjmm_dy,
                scalefactors.btagging_SF_2WPs_fjmm_vhmm,
                }
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="BtagWeightDown",
            shift_config={
                ("nnmm"): {
                "BtagWeightVariation": "down"
                }
            },
            producers={
                ("nnmm"): {
                scalefactors.btagging_SF_2WPs_met,
                scalefactors.btagging_SF_2WPs_met_dy,
                scalefactors.btagging_SF_2WPs_met_vhmm,
                }
            },
        )
    )
    ##########################
    #### Muon ID shift ####
    ##########################
    configuration.add_shift(
        SystematicShift(
            name="MuonIDUp",
            shift_config={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): {
                    "muon_sf_varation": "systup",
                    "muon_sf_varation_JPsi": "systup",
                    "muon_sf_varation_HighPt": "systup",
                }
            },
            producers={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): [
                    scalefactors.MuonID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonIDDown",
            shift_config={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): {
                    "muon_sf_varation": "systdown",
                    "muon_sf_varation_JPsi": "systdown",
                    "muon_sf_varation_HighPt": "systdown",
                }
            },
            producers={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): [
                    scalefactors.MuonID_SF,
                ]
            },
        )
    )
    ##########################
    #### Muon Iso shift ####
    ##########################
    configuration.add_shift(
        SystematicShift(
            name="MuonIsoUp",
            shift_config={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): {
                    "muon_sf_varation": "systup",
                    "muon_sf_varation_JPsi": "systup",
                    "muon_sf_varation_HighPt": "systup",
                }
            },
            producers={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): [
                    scalefactors.MuonIso_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonIsoDown",
            shift_config={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): {
                    "muon_sf_varation": "systdown",
                    "muon_sf_varation_JPsi": "systdown",
                    "muon_sf_varation_HighPt": "systdown",
                }
            },
            producers={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): [
                    scalefactors.MuonIso_SF,
                ]
            },
        )
    )
    ###############################
    #### HighPtMuon RECO shift ####
    ###############################
    configuration.add_shift(
        SystematicShift(
            name="MuonRECOUp",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "muon_sf_varation_HighPt": "systup",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    scalefactors.MuonRECO_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonRECODown",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "muon_sf_varation_HighPt": "systdown",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    scalefactors.MuonRECO_SF,
                ]
            },
        )
    )

    #########################################
    ######  Muon BSC pt systematics   #######
    #########################################
    # configuration.add_shift(
    #     SystematicShift(
    #         name="MuonBSCpt_Up",
    #         shift_config={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
    #                 "muon_momentum_BSC_variation": "Up",
    #                 "muon_momentum_scale_variation": "nominal",
    #             }
    #         },
    #         producers={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
    #                 momentumscale.MuonPtPreCorrection,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="MuonBSCpt_Down",
    #         shift_config={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
    #                 "muon_momentum_BSC_variation": "Down",
    #                 "muon_momentum_scale_variation": "nominal",
    #             }
    #         },
    #         producers={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
    #                 momentumscale.MuonPtPreCorrection,
    #             ]
    #         },
    #     )
    # )

    #########################################
    #### HighPtMuon Momentum Scale shift ####
    #########################################
    configuration.add_shift(
        SystematicShift(
            name="MuonHighPtScaleUp",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "muon_momentum_BSC_variation": "nominal",
                    "muon_momentum_scale_variation": "systup",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MuonPtPreCorrection,
                ]
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonHighPtScaleDown",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "muon_momentum_BSC_variation": "nominal",
                    "muon_momentum_scale_variation": "systdown",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MuonPtPreCorrection,
                ]
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="MuonHighPtSmearSystUp",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "highpt_smear_factor" : EraModifier(
                        {
                            "2022preEE": 0.46,
                            "2022postEE": 0.46,
                            "2023preBPix": 0.46,
                            "2023postBPix": 0.46,
                            "2024": 0.46,
                            "2025": 0.568,
                        }
                    ),
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MuonPtPreSmear,
                ]
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="MuonHighPtSmearSystDown",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "highpt_smear_factor" : EraModifier(
                        {
                            "2022preEE": 0.46,
                            "2022postEE": 0.46,
                            "2023preBPix": 0.46,
                            "2023postBPix": 0.46,
                            "2024": 0.46,
                            "2025": 0.568,
                        }
                    ),
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MuonPtPreSmear,
                ]
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    #########################################
    ## RoccoR MuonPt Momentum Scale shift ###
    #########################################
    # configuration.add_shift(
    #     SystematicShift(
    #         name="RochesterMuonPtScaleUp",
    #         shift_config={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
    #                 "Rochester_Muon_Pt_Res_variation": "Up",
    #             }
    #         },
    #         producers={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
    #                 momentumscale.MC_Rochester_MuonPt_ScaleRes,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="RochesterMuonPtScaleDown",
    #         shift_config={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
    #                 "Rochester_Muon_Pt_Res_variation": "Down",
    #             }
    #         },
    #         producers={
    #             ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr","nnmm","fjmm","fjmm_cr",
    #         "nnmm_dycontrol","nnmm_topcontrol",
    #         "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
    #         "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
    #                 momentumscale.MC_Rochester_MuonPt_ScaleRes,
    #             ]
    #         },
    #     )
    # )

    #########################################
    #### KIT MuonPt Momentum Scale shift ####
    #########################################
    configuration.add_shift(
        SystematicShift(
            name="KITMuonPtScaleUp",
            shift_config={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
                    "KIT_Muon_Pt_Scale_variation": "Up",
                    "KIT_Muon_Pt_Res_variation": "none",
                }
            },
            producers={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="KITMuonPtScaleDown",
            shift_config={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
                    "KIT_Muon_Pt_Scale_variation": "Down",
                    "KIT_Muon_Pt_Res_variation": "none",
                }
            },
            producers={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes,
                ]
            },
        )
    )

    configuration.add_shift(
        SystematicShift(
            name="KITMuonPtScaleHighPtUp",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "KIT_Muon_Pt_Scale_variation": "Up",
                    "KIT_Muon_Pt_Res_variation": "none",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes_HighPt,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="KITMuonPtScaleHighPtDown",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "KIT_Muon_Pt_Scale_variation": "Down",
                    "KIT_Muon_Pt_Res_variation": "none",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes_HighPt,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="KITMuonPtResHighPtUp",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "KIT_Muon_Pt_Scale_variation": "none",
                    "KIT_Muon_Pt_Res_variation": "Up",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes_HighPt,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="KITMuonPtResHighPtDown",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "KIT_Muon_Pt_Scale_variation": "none",
                    "KIT_Muon_Pt_Res_variation": "Down",
                }
            },
            producers={
                ("nnmm","fjmm","fjmm_cr"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes_HighPt,
                ]
            },
        )
    )
    
    #########################################
    ## KIT MuonPt Momentum Resolution shift #
    #########################################
    configuration.add_shift(
        SystematicShift(
            name="KITMuonResUp",
            shift_config={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
                    "KIT_Muon_Pt_Scale_variation": "none",
                    "KIT_Muon_Pt_Res_variation": "Up",
                }
            },
            producers={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="KITMuonResDown",
            shift_config={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {
                    "KIT_Muon_Pt_Scale_variation": "none",
                    "KIT_Muon_Pt_Res_variation": "Down",
                }
            },
            producers={
                ("e2m","m2m", "eemm","eemm_cr","mmmm","mmmm_cr",
        "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
        "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): [
                    momentumscale.MC_KIT_MuonPt_ScaleRes,
                ]
            },
        )
    )
    
    ###########################
    #### Electron ID shift ####
    ###########################
    configuration.add_shift(
        SystematicShift(
            name="EleIDUp",
            shift_config={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): {
                    "ele_sf_varation": "sfup",
                }
            },
            producers={("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): [
                scalefactors.EleID_SF,
            ]},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="EleIDDown",
            shift_config={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): {
                    "ele_sf_varation": "sfdown",
                }
            },
            producers={("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): [
                scalefactors.EleID_SF,
            ]},
        )
    )
    
    ###########################
    #### Electron Reco shift ####
    ###########################
    configuration.add_shift(
        SystematicShift(
            name="EleRecoUp",
            shift_config={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): {
                    "ele_sf_varation": "sfup",
                }
            },
            producers={("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): [
                scalefactors.EleReco_SF,
            ]},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="EleRecoDown",
            shift_config={
                ("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): {
                    "ele_sf_varation": "sfdown",
                }
            },
            producers={("e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond","eemm"): [
                scalefactors.EleReco_SF,
            ]},
        )
    )
    ########################
    # Electron pT shifts
    ########################
    configuration.add_shift(
        SystematicShift(
            name="ElectronSmearUp",
            scopes=["e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"],
            shift_config={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): {
                    "Smear_variation": "esmearUp"},
            },
            producers={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): [
                    electrons.ElectronPtCorrectionSmearing,
                ],
            },
        ),
    )
    configuration.add_shift(
        SystematicShift(
            name="ElectronSmearDown",
            scopes=["e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"],
            shift_config={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): {
                    "Smear_variation": "esmearDown"},
            },
            producers={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): [
                    electrons.ElectronPtCorrectionSmearing,
                ],
            },
        ),
    )
    configuration.add_shift(
        SystematicShift(
            name="ElectronScaleUp",
            scopes=["e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"],
            shift_config={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): {
                    "Smear_variation": "escaleUp"},
            },
            producers={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): [
                    electrons.ElectronPtCorrectionSmearing,
                ],
            },
        ),
    )
    configuration.add_shift(
        SystematicShift(
            name="ElectronScaleDown",
            scopes=["e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"],
            shift_config={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): {
                    "Smear_variation": "escaleDown"},
            },
            producers={
                ("e2m", "eemm", "eemm_cr", "e2m_dyfakeinge_regionb", "e2m_dyfakeinge_regionc", "e2m_dyfakeinge_regiond"): [
                    electrons.ElectronPtCorrectionSmearing,
                ],
            },
        ),
    )

    ###########################
    #### PNet WvsQCD shift ####
    ###########################
    configuration.add_shift(
        SystematicShift(
            name="fatjet_PNetSFUp",
            shift_config={
                ("fjmm","fjmm_cr"): {
                    "fatjet_sf_varation": "systup",
                }
            },
            producers={("fjmm","fjmm_cr"): [
                scalefactors.PNetWvsQCD_SF,
            ]},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjet_PNetSFDown",
            shift_config={
                ("fjmm","fjmm_cr"): {
                    "fatjet_sf_varation": "systdown",
                }
            },
            producers={("fjmm","fjmm_cr"): [
                scalefactors.PNetWvsQCD_SF,
            ]},
        )
    )
    
    #########################
    ### Muon Trigger Shift ##
    #########################
    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFUp",
            shift_config={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): {
                    "singlemuon_trigger_sf_mc": EraModifier(
                        {   
                            "2025": [
                                {
                                    # adjust the correction type from nominal to systup or down
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2024": [
                                {
                                    # adjust the correction type from nominal to systup or down
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2023preBPix": [
                                {
                                    # adjust the correction type from nominal to systup or down
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                             "2023postBPix": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2022preEE": [
                                {
                                    # adjust the correction type from nominal to systup or down
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                             "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2018": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                            "2017": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                            "2016postVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                            "2016preVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                        }
                    )
                }
            },
            producers={("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                        "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                        "eemm","mmmm","nnmm","fjmm","fjmm_cr"): scalefactors.GenerateSingleMuonTriggerSF_MC},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFDown",
            shift_config={
                ("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                 "eemm","mmmm","nnmm","fjmm","fjmm_cr"): {
                    "singlemuon_trigger_sf_mc": EraModifier(
                        {   
                            "2025": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2024": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2023preBPix": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2023postBPix": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2022preEE": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,
                                },
                            ],
                            "2018": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2017": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2016postVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2016preVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                        }
                    )
                }
            },
            producers={("m2m","m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                        "e2m","e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond",
                        "eemm","mmmm","nnmm","fjmm","fjmm_cr"): scalefactors.GenerateSingleMuonTriggerSF_MC},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFhighPtUp",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "singlemuon_trigger_sf_mc_highPt": EraModifier(
                        {   
                            "2025": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2024": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2023preBPix": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                             "2023postBPix": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2022preEE": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                             "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systup",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                        }
                    )
                }
            },
            producers={("nnmm","fjmm","fjmm_cr"): scalefactors.GenerateSingleMuonTriggerSF_MC_highPt},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFDown",
            shift_config={
                ("nnmm","fjmm","fjmm_cr"): {
                    "singlemuon_trigger_sf_mc_highPt": EraModifier(
                        {   
                            "2025": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2024": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2023preBPix": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2023postBPix": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2022preEE": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                            "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_mu50",
                                    "mc_trigger_sf": "NUM_Mu50_or_CascadeMu100_or_HighPtTkMu100_DEN_CutBasedIdTrkHighPt_and_TkIsoLoose",
                                    "mc_muon_sf_correctiontype": "systdown",
                                    "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                                },
                            ],
                        }
                    )
                }
            },
            producers={("nnmm","fjmm","fjmm_cr"): scalefactors.GenerateSingleMuonTriggerSF_MC_highPt},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    #########################
    # Jet energy resolution and jet energy scale
    #########################
    add_jetVariations(configuration, available_sample_types, era)
    add_fatjetVariations(configuration, available_sample_types, era)
    
    #########################
    # btagging scale factor shape variation
    #########################
    add_btagVariations(configuration, available_sample_types)
        
    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()
