from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from code_generation.configuration import Configuration
from code_generation.systematics import SystematicShift
from .producers import jets as jets
from .producers import scalefactors as scalefactors

def add_jetVariations(
    configuration: Configuration, available_sample_types: List[str], era: str
):
    #########################
    # Jet energy resolution
    #########################
    configuration.add_shift(
        SystematicShift(
            name="jerUncUp",
            shift_config={
                "global": {"jet_jer_shift": '"up"'},
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jerUncDown",
            shift_config={
                "global": {"jet_jer_shift": '"down"'},
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    #########################
    # Jet energy scale - Total
    #########################
    JEC_sources = '{"Total"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncTotalUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                },
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_jes"},
            },
            producers={
                "global": {
                    jets.JetEnergyCorrection,
                },
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {scalefactors.btaggingloose_SF,},
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
            name="jesUncTotalDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                },
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_jes"},
            },
            producers={
                "global": {
                    jets.JetEnergyCorrection,
                },
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {scalefactors.btaggingloose_SF},
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    #########################
    # HEM 15/16 issue
    #########################
    if era == "2018":
        JEC_sources = '{"HEMIssue"}'
        configuration.add_shift(
            SystematicShift(
                name="jesUncHEMIssueUp",
                shift_config={
                    "global": {
                        "jet_jes_shift": 1,
                        "jet_jes_sources": JEC_sources,
                    }
                },
                producers={"global": jets.JetEnergyCorrection},
            ),
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["data"]
            ],
        )
        configuration.add_shift(
            SystematicShift(
                name="jesUncHEMIssueDown",
                shift_config={
                    "global": {
                        "jet_jes_shift": -1,
                        "jet_jes_sources": JEC_sources,
                    }
                },
                producers={"global": jets.JetEnergyCorrection},
            ),
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["data"]
            ],
        )
    #########################
    # Jet energy scale - reduced set
    #########################
    JEC_sources = '{"SinglePionECAL", "SinglePionHCAL", "AbsoluteMPFBias", "AbsoluteScale", "Fragmentation", "PileUpDataMC", "RelativeFSR", "PileUpPtRef"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncAbsoluteUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncAbsoluteDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"AbsoluteStat", "TimePtEta", "RelativeStatFSR"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncAbsoluteYearUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncAbsoluteYearDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"FlavorQCD"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncFlavorQCDUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncFlavorQCDDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"PileUpPtEC1", "PileUpPtBB", "RelativePtBB"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncBBEC1Up",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncBBEC1Down",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"RelativeJEREC1", "RelativePtEC1", "RelativeStatEC"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncBBEC1YearUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncBBEC1YearDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"RelativePtHF", "PileUpPtHF", "RelativeJERHF"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncHFUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncHFDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"RelativeStatHF"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncHFYearUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncHFYearDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"PileUpPtEC2"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncEC2Up",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncEC2Down",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"RelativeJEREC2", "RelativePtEC2"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncEC2YearUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncEC2YearDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"RelativeBal"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncRelativeBalUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncRelativeBalDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    JEC_sources = '{"RelativeSample"}'
    configuration.add_shift(
        SystematicShift(
            name="jesUncRelativeSampleYearUp",
            shift_config={
                "global": {
                    "jet_jes_shift": 1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="jesUncRelativeSampleYearDown",
            shift_config={
                "global": {
                    "jet_jes_shift": -1,
                    "jet_jes_sources": JEC_sources,
                }
            },
            producers={"global": jets.JetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    
    return configuration