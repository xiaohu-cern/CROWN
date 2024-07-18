from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from code_generation.configuration import Configuration
from code_generation.systematics import SystematicShift
from .producers import fatjets as fatjets
from .producers import scalefactors as scalefactors

def add_fatjetVariations(
    configuration: Configuration, available_sample_types: List[str], era: str
):
    #########################
    # Jet energy resolution
    #########################
    configuration.add_shift(
        SystematicShift(
            name="fatjerUncUp",
            shift_config={
                "global": {"fatjet_jer_shift": '"up"'},
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjerUncDown",
            shift_config={
                "global": {"fatjet_jer_shift": '"down"'},
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncTotalUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                },
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_jes"},
            },
            producers={
                "global": {
                    fatjets.FatJetEnergyCorrection,
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
            name="fatjesUncTotalDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                },
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_jes"},
            },
            producers={
                "global": {
                    fatjets.FatJetEnergyCorrection,
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
                name="fatjesUncHEMIssueUp",
                shift_config={
                    "global": {
                        "fatjet_jes_shift": 1,
                        "fatjet_jes_sources": JEC_sources,
                    }
                },
                producers={"global": fatjets.FatJetEnergyCorrection},
            ),
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["data"]
            ],
        )
        configuration.add_shift(
            SystematicShift(
                name="fatjesUncHEMIssueDown",
                shift_config={
                    "global": {
                        "fatjet_jes_shift": -1,
                        "fatjet_jes_sources": JEC_sources,
                    }
                },
                producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncAbsoluteUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncAbsoluteDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncAbsoluteYearUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncAbsoluteYearDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncFlavorQCDUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncFlavorQCDDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncBBEC1Up",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncBBEC1Down",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncBBEC1YearUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncBBEC1YearDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncHFUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncHFDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncHFYearUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncHFYearDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncEC2Up",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncEC2Down",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncEC2YearUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncEC2YearDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncRelativeBalUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncRelativeBalDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
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
            name="fatjesUncRelativeSampleYearUp",
            shift_config={
                "global": {
                    "fatjet_jes_shift": 1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="fatjesUncRelativeSampleYearDown",
            shift_config={
                "global": {
                    "fatjet_jes_shift": -1,
                    "fatjet_jes_sources": JEC_sources,
                }
            },
            producers={"global": fatjets.FatJetEnergyCorrection},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    
    return configuration