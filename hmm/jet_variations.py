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
    return configuration