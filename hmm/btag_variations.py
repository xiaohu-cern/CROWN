from code_generation.systematics import SystematicShift
from .producers import scalefactors as scalefactors


def add_btagVariations(configuration, available_sample_types):
    #########################
    # btagging shape uncertainties
    #########################
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFUp",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_hf"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFDown",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_hf"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats1Up",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_hfstats1"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats1Down",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_hfstats1"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats2Up",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_hfstats2"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncHFstats2Down",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_hfstats2"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncLFUp",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_lf"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncLFDown",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_lf"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats1Up",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_lfstats1"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats1Down",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_lfstats1"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats2Up",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_lfstats2"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncLFstats2Down",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_lfstats2"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr1Up",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_cferr1"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr1Down",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_cferr1"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr2Up",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "up_cferr2"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="btagUncCFerr2Down",
            shift_config={
                ("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): {"btag_sf_variation": "down_cferr2"},
            },
            producers={("e2m","m2m", "eemm","mmmm","nnmm","fjmm","fjmm_cr",
                 "m2m_dyfakeingmu_regionb","m2m_dyfakeingmu_regionc","m2m_dyfakeingmu_regiond",
                 "e2m_dyfakeinge_regionb","e2m_dyfakeinge_regionc","e2m_dyfakeinge_regiond"): scalefactors.btaggingloose_SF},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data"]
        ],
    )