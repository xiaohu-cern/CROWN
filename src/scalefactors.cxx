#ifndef GUARD_SCALEFACTORS_H
#define GUARD_SCALEFACTORS_H

#include "../include/basefunctions.hxx"
#include "../include/utility/Logger.hxx"
#include "../include/utility/RooFunctorThreadsafe.hxx"
#include "ROOT/RDataFrame.hxx"
#include "RooFunctor.h"
#include "RooWorkspace.h"
#include "TFile.h"
#include "correction.h"
#include "../include/KIT_Corr.hxx"
#include "../include/RoccoR.hxx"
/// namespace used for scale factor related functions
namespace scalefactor {
namespace muon {
///////KIT Correction/////////
//////////////////muon pt scale////////////////////////////
ROOT::RDF::RNode KIT_MuonPtScale(ROOT::RDF::RNode df, const std::string &pt, const std::string &pt_pre_corr,
                    const std::string &phi, const std::string &eta, 
                    const std::string &charge, const std::string &pt_corrected, 
                    const std::string &sf_file, const std::string &data_type) {
    Logger::get("KIT Muon Momentum Scale")->debug("Setting up functions for KIT muon momentum scale");
    const std::string a_key = "a_" + data_type;
    const std::string m_key = "m_" + data_type;
    auto cset_a = correction::CorrectionSet::from_file(sf_file)->at(a_key);
    auto cset_m = correction::CorrectionSet::from_file(sf_file)->at(m_key);
    auto df1 = df.Define(
        pt_corrected,
        [cset_a, cset_m, data_type](const ROOT::RVec<float> &pt_values,
                                             const ROOT::RVec<float> &pt_pre_corr_values,
                                             const ROOT::RVec<float> &phi_values,
                                             const ROOT::RVec<float> &eta_values,
                                             const ROOT::RVec<int> &q_values) {
            ROOT::RVec<float> corrected_pt_values(pt_values.size());
            for (int i = 0; i < pt_values.size(); i++) {
                if (phi_values.at(i) > -3.14159265 && phi_values.at(i) < 3.14159265 && (pt_values.at(i) <= 200) && eta_values.at(i) > -2.4 && eta_values.at(i) < 2.4) {
                    double a = cset_a->evaluate({eta_values.at(i), phi_values.at(i), "nom"});
                    double m = cset_m->evaluate({eta_values.at(i), phi_values.at(i), "nom"});
                    
                    if (pt_pre_corr_values.at(i) < 26) {
                        corrected_pt_values[i] = pt_pre_corr_values.at(i);
                    }
                    else {
                        corrected_pt_values[i] = 1/(m/pt_pre_corr_values.at(i) + q_values.at(i)*a);
                    }
                }
                else {
                    corrected_pt_values[i] = pt_pre_corr_values.at(i);
                }
                Logger::get("uncorrected pt:")->debug("{}", pt_pre_corr_values.at(i));
                Logger::get("corrected pt:")->debug("{}", corrected_pt_values.at(i));
            }
            return corrected_pt_values;
        },{pt, pt_pre_corr, phi, eta, charge});
    return df1;
}
////////test KIT uncertainty////////////

///////////////////////////////////////////////////////////////////////
ROOT::RDF::RNode KIT_MuonPtRes(ROOT::RDF::RNode df, const std::string &pt, const std::string &pt_pre_corr, 
                    const std::string &phi, const std::string &eta,
                    const std::string &nL, const std::string &evtNumber,
                    const std::string &lumiNumber, const std::string &charge, const std::string &pt_corrected,
                    const std::string &sf_file, const std::string &variation,
                    const std::string &data_type, const std::string &s_variation) {
    Logger::get("KIT Muon Momentum Resolution")->debug("Setting up functions for KIT muon momentum resolution");
    const std::string a_key = "a_" + data_type;
    const std::string m_key = "m_" + data_type;
    auto cset_a = correction::CorrectionSet::from_file(sf_file)->at(a_key);
    auto cset_m = correction::CorrectionSet::from_file(sf_file)->at(m_key);
    auto cset_cb_params = correction::CorrectionSet::from_file(sf_file)->at("cb_params");
    auto cset_poly_params = correction::CorrectionSet::from_file(sf_file)->at("poly_params");
    auto cset_k_data = correction::CorrectionSet::from_file(sf_file)->at("k_data");
    auto cset_k_mc = correction::CorrectionSet::from_file(sf_file)->at("k_mc");
    auto df1 = df.Define(
        pt_corrected,
        [cset_a, cset_m, cset_cb_params, cset_poly_params, cset_k_data, cset_k_mc, variation, data_type, s_variation](
           const ROOT::RVec<float> &pt_values,
           const ROOT::RVec<float> &pt_pre_corr_values,
           const ROOT::RVec<float> &phi_values,
           const ROOT::RVec<float> &eta_values,
           const ROOT::RVec<UChar_t> &nL_values_char,
           ULong64_t evtNumber,
           UInt_t lumiNumber,
           const ROOT::RVec<int> &q_values) {
        ROOT::RVec<float> corrected_pt_values(pt_values.size());
        ROOT::RVec<float> s_pt_values(pt_values.size());
        ROOT::RVec<float> nL_values = ROOT::RVec<float>(nL_values_char.begin(), nL_values_char.end());
        for (int i = 0; i < pt_values.size(); i++) {
            if (phi_values.at(i) > -3.14159265 && phi_values.at(i) < 3.14159265 && eta_values.at(i) > -2.4 && eta_values.at(i) < 2.4){
                if (pt_values.at(i) < 200) {
                    double a = cset_a->evaluate({eta_values.at(i), phi_values.at(i), "nom"});
                    double m = cset_m->evaluate({eta_values.at(i), phi_values.at(i), "nom"});
                    
                    if (pt_pre_corr_values.at(i) < 26) {
                        s_pt_values[i] = pt_pre_corr_values.at(i);
                    }
                    else {
                        s_pt_values[i] = 1/(m/pt_pre_corr_values.at(i) + q_values.at(i)*a);
                    }

                    // auto log = Logger::get("KIT Muon Momentum Resolution");
                    // log->set_level(spdlog::level::debug);
                    // log->info("SCALE!!!!!!!!!!");
                    double stat_a = cset_a->evaluate({eta_values.at(i), phi_values.at(i), "stat"});
                    double stat_m = cset_m->evaluate({eta_values.at(i), phi_values.at(i), "stat"});
                    double stat_rho = cset_m->evaluate({eta_values.at(i), phi_values.at(i), "rho_stat"});

                    double unc = pt_pre_corr_values.at(i)*pt_pre_corr_values.at(i)*sqrt(stat_m*stat_m / (pt_pre_corr_values.at(i)*pt_pre_corr_values.at(i)) + stat_a*stat_a + 2*q_values.at(i)*stat_rho*stat_m/pt_pre_corr_values.at(i)*stat_a);

                    if (s_variation=="Up"){
                        s_pt_values[i] = pt_pre_corr_values.at(i) + unc;
                    }
                    if (s_variation=="Down"){
                        s_pt_values[i] = pt_pre_corr_values.at(i) - unc;
                    }
                }
                else {
                    s_pt_values[i] = pt_pre_corr_values.at(i);
                }

                if (pt_values.at(i) < 200) {
                    double mean = cset_cb_params->evaluate({std::abs(eta_values.at(i)), nL_values.at(i), 0});
                    double sigma = cset_cb_params->evaluate({std::abs(eta_values.at(i)), nL_values.at(i), 1});
                    double n = cset_cb_params->evaluate({std::abs(eta_values.at(i)), nL_values.at(i), 2});
                    double alpha = cset_cb_params->evaluate({std::abs(eta_values.at(i)), nL_values.at(i), 3});

                    double param_0 = cset_poly_params->evaluate({std::abs(eta_values.at(i)), nL_values.at(i), 0});
                    double param_1 = cset_poly_params->evaluate({std::abs(eta_values.at(i)), nL_values.at(i), 1});
                    double param_2 = cset_poly_params->evaluate({std::abs(eta_values.at(i)), nL_values.at(i), 2});

                    double k_data = cset_k_data->evaluate({std::abs(eta_values.at(i)), "nom"});
                    double k_mc = cset_k_mc->evaluate({std::abs(eta_values.at(i)), "nom"});
                    
                    double rndm = (double) KIT::get_rndm(eta_values.at(i), phi_values.at(i), nL_values.at(i), evtNumber, lumiNumber, mean, sigma, n, alpha);
                    double std = (double) KIT::get_std(pt_values.at(i), eta_values.at(i), nL_values.at(i), param_0, param_1, param_2);
                    // double rndm = (double) KIT::get_rndm_gaus(eta_values.at(i), phi_values.at(i), nL_values.at(i), evtNumber, lumiNumber, mean, sigma);
                    // double std = 0.02;
                    double k = (double) KIT::get_k(eta_values.at(i), "nom", k_data, k_mc);
                    
                    // auto log = Logger::get("KIT Muon Momentum Resolution");
                    // log->set_level(spdlog::level::debug);
                    // log->info("std: {}", std);
                    // if (std > 0.05) {std = 0.05;}

                    // double ptc = s_pt_values.at(i) * ( 1 + k*std*rndm);
                    double ptc = s_pt_values.at(i) * ( 1 + k * std *rndm);
                    if (isnan(ptc)) ptc = s_pt_values.at(i);
                    if (ptc / s_pt_values.at(i) > 2 || ptc / s_pt_values.at(i) < 0.1 || s_pt_values.at(i) < 26 || s_pt_values.at(i) > 200) {
                        ptc = s_pt_values.at(i);
                    }
                    corrected_pt_values[i] = ptc;
                    // corrected_pt_values[i] = s_pt_values[i];


                    // auto log = Logger::get("KIT Muon Momentum Resolution");
                    // log->set_level(spdlog::level::debug);
                    // log->info("old pt {}", k, "new pt {}", k);

                    if (k==0) {
                        corrected_pt_values[i] = corrected_pt_values[i];
                    }
                    else{
                        double k_unc = cset_k_mc->evaluate({std::abs(eta_values.at(i)), "stat"});
                        double std_x_rndm = (corrected_pt_values[i] / s_pt_values.at(i) -1 ) / k;
                        if (variation=="Up") {
                            corrected_pt_values[i] = s_pt_values.at(i) * (1 + (k+k_unc) * std_x_rndm);
                            if (corrected_pt_values[i] / s_pt_values.at(i) > 2 || corrected_pt_values[i] / s_pt_values.at(i) < 0.1 || corrected_pt_values[i] < 0) {
                                corrected_pt_values[i] = s_pt_values.at(i);
                            }   
                        }
                        if (variation=="Down") {
                            corrected_pt_values[i] = s_pt_values.at(i) * (1 + (k-k_unc) * std_x_rndm);
                            if (corrected_pt_values[i] / s_pt_values.at(i) > 2 || corrected_pt_values[i] / s_pt_values.at(i) < 0.1 || corrected_pt_values[i] < 0) {
                                corrected_pt_values[i] = s_pt_values.at(i);
                            }
                        }
                    }
                }
                else {
                    corrected_pt_values[i] = s_pt_values.at(i);
                }
            }
            else {
                corrected_pt_values[i] = pt_pre_corr_values.at(i);
            }
        }return corrected_pt_values;
    }, {pt, pt_pre_corr, phi, eta, nL, evtNumber, lumiNumber, charge});
    return df1;  
}
///////////////////////////////// Rochester Correction ///////////////////////////////////////
ROOT::RDF::RNode Rochester_MuonPtRes(ROOT::RDF::RNode df, const std::string &pt, const std::string &pt_pre_corr, const std::string &indextoGen, const std::string &GenPt,
                    const std::string &phi, const std::string &eta,
                    const std::string &charge, const std::string &nL, const std::string &evtNumber,
                    const std::string &lumiNumber, const std::string &pt_corrected,
                    const std::string &sf_file, const std::string &variation,
                    const std::string &data_type) {
    auto df1 = df.Define(
        pt_corrected,
        [sf_file, variation, data_type](
           const ROOT::RVec<float> &pt_values,
           const ROOT::RVec<float> &pt_pre_corr_values,
           const ROOT::RVec<int> &indextoGen_values,
           const ROOT::RVec<float> &GenPt_values,
           const ROOT::RVec<float> &phi_values,
           const ROOT::RVec<float> &eta_values,
           const ROOT::RVec<int> &q_values,
           const ROOT::RVec<UChar_t> &nL_values_char,
           ULong64_t evtNumber,
           UInt_t lumiNumber) {
        ROOT::RVec<float> corrected_pt_values(pt_values.size());
        ROOT::RVec<float> nL_values = ROOT::RVec<float>(nL_values_char.begin(), nL_values_char.end());
        RoccoR rc(sf_file);
        for (int i = 0; i < pt_values.size(); i++) {
            if (phi_values.at(i) > -3.14159265 && phi_values.at(i) < 3.14159265 && eta_values.at(i) > -2.4 && eta_values.at(i) < 2.4){
                if (pt_values.at(i) < 200) {
                    if (data_type == "data") {
                        double dtSF = rc.kScaleDT(q_values.at(i), pt_pre_corr_values.at(i), eta_values.at(i), phi_values.at(i), 0, 0);
                        corrected_pt_values[i] = pt_pre_corr_values.at(i)*dtSF;
                    }
                    if (data_type == "mc") {
                        double mcSF = 1.;
                        double ptuncer = 0.;
                        try {
                            double muon_genpt = GenPt_values.at(indextoGen_values.at(i));
                            mcSF = rc.kSpreadMC(q_values.at(i), pt_pre_corr_values.at(i), eta_values.at(i), phi_values.at(i), muon_genpt, 0, 0);
                            corrected_pt_values[i] = pt_pre_corr_values.at(i)*mcSF;
                            if (variation == "Up") {
                                ptuncer = rc.kEffDifferror2(q_values.at(i), pt_pre_corr_values.at(i), eta_values.at(i), phi_values.at(i), muon_genpt);
                                corrected_pt_values[i] = pt_pre_corr_values.at(i)*(mcSF + ptuncer);
                            }
                            if (variation == "Down") {
                                ptuncer = rc.kEffDifferror2(q_values.at(i), pt_pre_corr_values.at(i), eta_values.at(i), phi_values.at(i), muon_genpt);
                                corrected_pt_values[i] = pt_pre_corr_values.at(i)*(mcSF - ptuncer);
                            }
                        }
                        catch (const std::out_of_range &e) {
                            double rndm = (double) KIT::get_random_nb(phi_values.at(i), evtNumber, lumiNumber);
                            mcSF = rc.kSmearMC(q_values.at(i), pt_pre_corr_values.at(i), eta_values.at(i), phi_values.at(i), nL_values.at(i), rndm, 0, 0);
                            corrected_pt_values[i] = pt_pre_corr_values.at(i)*mcSF;
                            if (variation == "Up") {
                                ptuncer = rc.kEffDifferror1(q_values.at(i), pt_pre_corr_values.at(i), eta_values.at(i), phi_values.at(i), nL_values.at(i), rndm);
                                corrected_pt_values[i] = pt_pre_corr_values.at(i)*(mcSF + ptuncer);
                            }
                            if (variation == "Down") {
                                ptuncer = rc.kEffDifferror1(q_values.at(i), pt_pre_corr_values.at(i), eta_values.at(i), phi_values.at(i), nL_values.at(i), rndm);
                                corrected_pt_values[i] = pt_pre_corr_values.at(i)*(mcSF - ptuncer);
                            }
                        }
                    }
                    
                }
                else {
                    corrected_pt_values[i] = pt_pre_corr_values.at(i);
                }
            }
            else {
                corrected_pt_values[i] = pt_pre_corr_values.at(i);
            }
        }return corrected_pt_values;
    }, {pt, pt_pre_corr, indextoGen, GenPt, phi, eta, charge, nL, evtNumber, lumiNumber});
    return df1;  
}
///////////////////////////////// Rochester Correction End ///////////////////////////////////////
ROOT::RDF::RNode HighPtSmear(ROOT::RDF::RNode df, const std::string &pt, const std::string &eta, const std::string &phi, 
                             const std::string &nL, const std::string &evtNumber, const std::string &lumiNumber, const std::string &pt_smeared, 
                             const double a_barrel, const double b_barrel, const double c_barrel, const double d_barrel,
                             const double a_endcap, const double b_endcap, const double c_endcap, const double d_endcap) {
    auto df1 = df.Define(
        pt_smeared,
        [a_barrel, b_barrel, c_barrel, d_barrel, a_endcap, b_endcap, c_endcap, d_endcap]
        (const ROOT::RVec<float> &pt_values,
        const ROOT::RVec<float> &eta_values,
        const ROOT::RVec<float> &phi_values,
        const ROOT::RVec<UChar_t> &nL_values_char,
        ULong64_t evtNumber,
        UInt_t lumiNumber) {
            ROOT::RVec<float> smeared_pt_values(pt_values.size());
            ROOT::RVec<float> nL_values = ROOT::RVec<float>(nL_values_char.begin(), nL_values_char.end());
            for (int i = 0; i < pt_values.size(); i++) {
                if (phi_values.at(i) > -3.14159265 && phi_values.at(i) < 3.14159265 && pt_values.at(i) >= 200 && eta_values.at(i) > -2.4 && eta_values.at(i) < 2.4){
                    double sigma = 0.;
                    if (std::abs(eta_values.at(i)) < 1.2) {
                        sigma = a_barrel + b_barrel*pt_values.at(i) + c_barrel*pt_values.at(i)*pt_values.at(i) + d_barrel*pt_values.at(i)*pt_values.at(i)*pt_values.at(i);
                    }
                    else {
                        sigma = a_endcap + b_endcap*pt_values.at(i) + c_endcap*pt_values.at(i)*pt_values.at(i) + d_endcap*pt_values.at(i)*pt_values.at(i)*pt_values.at(i);
                    }
                    double rndm = (double) KIT::get_rndm_gaus(eta_values.at(i), phi_values.at(i), nL_values.at(i), evtNumber, lumiNumber, 0, 0.32*sigma);
                    smeared_pt_values[i] = pt_values.at(i) * (1 + rndm);
                }
                else {
                    smeared_pt_values[i] = pt_values.at(i);
                }
            }
            return smeared_pt_values;
        }, {pt, eta, phi, nL, evtNumber, lumiNumber});
    return df1;
}


ROOT::RDF::RNode HighPtScaleData(ROOT::RDF::RNode df, const std::string &pt_raw, const std::string &pt_BSC, const std::string &pt_ReltuneP, const std::string &pt_BSC_Err,
                    const std::string &phi, const std::string &eta, 
                    const std::string &charge, 
                    const std::string &variation_BSC, const std::string &variation_tuneP, const std::string &pt_corrected, 
                    const std::string &sf_file,
                    const std::string &idAlgorithm) {
    Logger::get("HighPtMuon Momentum Scale")->debug("Setting up functions for muon momentum scale");
    Logger::get("HighPtMuon Momentum Scale")->debug("Algorithm - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        pt_corrected,
        [evaluator, variation_BSC, variation_tuneP, sf_file](const ROOT::RVec<float> &pt_values,
                                                             const ROOT::RVec<float> &pt_BSC_values,
                                                             const ROOT::RVec<float> &pt_ReltuneP_values,
                                                             const ROOT::RVec<float> &pt_BSC_Err_values,
                                                             const ROOT::RVec<float> &phi_values,
                                                             const ROOT::RVec<float> &eta_values,
                                                             const ROOT::RVec<int> &q_values) {
            // maybe can input good muon mask also, to speed up the process
            // input is phi and eta
            // https://twiki.cern.ch/twiki/bin/view/CMS/MuonRun32022#Momentum_Scale 
            // https://twiki.cern.ch/twiki/bin/view/CMS/MuonRun3_2023#Momentum_Scale 
            // https://indico.cern.ch/event/1411292/contributions/5932367/attachments/2846614/4977311/GEMethod_22+23_29Apr24.pdf 
            ROOT::RVec<float> corrected_pt_values(pt_values.size());            
            for (int i = 0; i < pt_values.size(); i++) {
                Logger::get("muon momentum scale file:")->debug("{}", sf_file);
                // apply scale for muon pt > 200 using HighPt file
                if (phi_values.at(i) > -3.14159265 && phi_values.at(i) < 3.14159265 && eta_values.at(i) > -2.4 && eta_values.at(i) < 2.4) {
                    if (pt_values.at(i) >= 200) {
                        // q/pt_corr = q/pt + kappa(TeV^-1)
                        float tuneP_pt = pt_values.at(i) * pt_ReltuneP_values.at(i);
                        float kappa = 0;
                        kappa = evaluator->evaluate(
                            {phi_values.at(i), eta_values.at(i), variation_tuneP});
                        corrected_pt_values[i] = (tuneP_pt * q_values.at(i)) / (q_values.at(i) - tuneP_pt * kappa * 0.001);
                    }
                    else {
                        corrected_pt_values[i] = pt_BSC_values.at(i);
                    }
                }
                else {
                    corrected_pt_values[i] = pt_values.at(i);
                } 
            }
            return corrected_pt_values;
        },
        {pt_raw, pt_BSC, pt_ReltuneP, pt_BSC_Err, phi, eta, charge});
    return df1;
}


ROOT::RDF::RNode HighPtScale(ROOT::RDF::RNode df, const std::string &pt_raw, const std::string &pt_BSC, const std::string &pt_ReltuneP, const std::string &pt_BSC_Err,
                    const std::string &phi, const std::string &eta, 
                    const std::string &charge, 
                    const std::string &variation_BSC, const std::string &variation_tuneP, const std::string &pt_corrected, 
                    const std::string &sf_file,
                    const std::string &idAlgorithm) {
    Logger::get("HighPtMuon Momentum Scale")->debug("Setting up functions for muon momentum scale");
    Logger::get("HighPtMuon Momentum Scale")->debug("Algorithm - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        pt_corrected,
        [evaluator, variation_BSC, variation_tuneP, sf_file](const ROOT::RVec<float> &pt_values,
                                                             const ROOT::RVec<float> &pt_BSC_values,
                                                             const ROOT::RVec<float> &pt_ReltuneP_values,
                                                             const ROOT::RVec<float> &pt_BSC_Err_values,
                                                             const ROOT::RVec<float> &phi_values,
                                                             const ROOT::RVec<float> &eta_values,
                                                             const ROOT::RVec<int> &q_values) {
            // maybe can input good muon mask also, to speed up the process
            // input is phi and eta
            // https://twiki.cern.ch/twiki/bin/view/CMS/MuonRun32022#Momentum_Scale 
            // https://twiki.cern.ch/twiki/bin/view/CMS/MuonRun3_2023#Momentum_Scale 
            // https://indico.cern.ch/event/1411292/contributions/5932367/attachments/2846614/4977311/GEMethod_22+23_29Apr24.pdf 
            ROOT::RVec<float> corrected_pt_values(pt_values.size());            
            for (int i = 0; i < pt_values.size(); i++) {
                Logger::get("muon momentum scale file:")->debug("{}", sf_file);
                // apply scale for muon pt > 200 using HighPt file
                if (phi_values.at(i) > -3.14159265 && phi_values.at(i) < 3.14159265 && eta_values.at(i) > -2.4 && eta_values.at(i) < 2.4) {
                    if (pt_values.at(i) >= 200) {
                        // q/pt_corr = q/pt + kappa(TeV^-1)
                        float tuneP_pt = pt_values.at(i) * pt_ReltuneP_values.at(i);
                        float kappa_up = 0;
                        float kappa_down = 0;
                        float kappa = 0;
                        if (variation_tuneP == "systup") {
                            kappa_up = evaluator->evaluate(
                                {phi_values.at(i), eta_values.at(i), variation_tuneP});
                            kappa = evaluator->evaluate(
                                {phi_values.at(i), eta_values.at(i), "nominal"});
                            corrected_pt_values[i] = (tuneP_pt * q_values.at(i)) / (q_values.at(i) + tuneP_pt * (kappa_up - kappa) * 0.001);
                        }
                        else if (variation_tuneP == "systdown") {
                            kappa_down = evaluator->evaluate(
                                {phi_values.at(i), eta_values.at(i), variation_tuneP});
                            kappa = evaluator->evaluate(
                                {phi_values.at(i), eta_values.at(i), "nominal"});
                            corrected_pt_values[i] = (tuneP_pt * q_values.at(i)) / (q_values.at(i) + tuneP_pt * (kappa_down - kappa) * 0.001);
                        }
                        else if (variation_tuneP == "nominal") {
                            corrected_pt_values[i] = tuneP_pt;
                        }
                        else {
                            corrected_pt_values[i] = tuneP_pt;
                        }

                    }
                    else {
                    if (variation_BSC == "Up") {
                        corrected_pt_values[i] = pt_BSC_values.at(i) + pt_BSC_Err_values.at(i);
                    }
                    else if (variation_BSC == "Down") {
                        corrected_pt_values[i] = pt_BSC_values.at(i) - pt_BSC_Err_values.at(i);
                    }
                    else {
                        corrected_pt_values[i] = pt_BSC_values.at(i);
                    }
                    }
                }
                else {
                    corrected_pt_values[i] = pt_values.at(i);
                } 
            }
            return corrected_pt_values;
        },
        {pt_raw, pt_BSC, pt_ReltuneP, pt_BSC_Err, phi, eta, charge});
    return df1;
}

// ROOT::RDF::RNode MuonmomentumBSC(ROOT::RDF::RNode df, const std::string &pt, const std::string &phi, const std::string &eta, 
//                     const std::string &ptErr, const std::string &variation, const std::string &ptBSC) {
//     auto df1 = df.Define(
//         ptBSC,
//         [variation](const ROOT::RVec<float> &pt_values,
//                     const ROOT::RVec<float> &phi_values,
//                     const ROOT::RVec<float> &eta_values,
//                     const ROOT::RVec<float> &ptErr_values) {
//             ROOT::RVec<float> BSC_pt_values(pt_values.size());            
//             for (int i = 0; i < pt_values.size(); i++) {
//                 if (phi_values.at(i) > -3.14159265 && phi_values.at(i) < 3.14159265 && eta_values.at(i) > -2.4 && eta_values.at(i) < 2.4) {
//                     if (variation=="Up") {
//                         BSC_pt_values[i] = pt_values.at(i) + ptErr_values.at(i);
//                     }
//                     if (variation=="Down") {
//                         BSC_pt_values[i] = pt_values.at(i) - ptErr_values.at(i);
//                     }
//                     if (variation=="nominal") {
//                         BSC_pt_values[i] = pt_values.at(i);
//                     }
//                 } 
//                 else {
//                     BSC_pt_values[i] = pt_values.at(i);
//                 }
//             }
//             return BSC_pt_values;
//         },
//         {pt, phi, eta, ptErr});
//     return df1;
// }
///
/**
 * @brief Function used to evaluate id scale factors from muons
 *
 * @param df The input dataframe
 * @param pt muon pt
 * @param eta muon eta
 * @param id_output name of the id scale factor column
 * @param workspace_name path to the Rooworkspace
 * @param id_functor_name name of the function from the workspace
 * @param id_arguments arguments of the function
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode id_rooworkspace(ROOT::RDF::RNode df, const std::string &pt,
                                 const std::string &eta,
                                 const std::string &id_output,
                                 const std::string &workspace_name,
                                 const std::string &id_functor_name,
                                 const std::string &id_arguments) {

    Logger::get("muonsf")->debug("Setting up functions for muon sf");
    Logger::get("muonsf")->debug("ID - Function {} // argset {}",
                                 id_functor_name, id_arguments);

    const std::shared_ptr<RooFunctorThreadsafe> id_function =
        loadFunctor(workspace_name, id_functor_name, id_arguments);
    auto df1 = basefunctions::evaluateWorkspaceFunction(df, id_output,
                                                        id_function, pt, eta);
    return df1;
}
/**
 * @brief Function used to evaluate iso scale factors from muons
 *
 * @param df The input dataframe
 * @param pt muon pt
 * @param eta muon eta
 * @param iso muon iso
 * @param iso_output name of the iso scale factor column
 * @param workspace_name path to the Rooworkspace
 * @param iso_functor_name name of the function from the workspace
 * @param iso_arguments arguments of the function
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode iso_rooworkspace(ROOT::RDF::RNode df, const std::string &pt,
                                  const std::string &eta,
                                  const std::string &iso,
                                  const std::string &iso_output,
                                  const std::string &workspace_name,
                                  const std::string &iso_functor_name,
                                  const std::string &iso_arguments) {

    Logger::get("muonsf")->debug("Setting up functions for muon sf");
    Logger::get("muonsf")->debug("Iso - Function {} // argset {}",
                                 iso_functor_name, iso_arguments);

    const std::shared_ptr<RooFunctorThreadsafe> iso_function =
        loadFunctor(workspace_name, iso_functor_name, iso_arguments);
    auto df1 = basefunctions::evaluateWorkspaceFunction(
        df, iso_output, iso_function, pt, eta, iso);
    return df1;
}
/**
 * @brief Function used to evaluate id scale factors from muons with
 * correctionlib. Configuration:
 * - [UL2018 Muon
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2018_UL.html)
 * - [UL2017 Muon
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2017_UL.html)
 * - [UL2016preVFP Muon
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2016preVFP_UL.html)
 * - [UL2016postVFP Muon
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2016postVFP_UL.html)
 *
 * @param df The input dataframe
 * @param pt muon pt
 * @param eta muon eta
 * @param year_id id for the year of data taking and mc compaign
 * @param variation id for the variation of the scale factor "sf" for nominal
 * and "systup"/"systdown" for up/down variation
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the muon scale factors
 * @param idAlgorithm name of the muon id scale factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode id(ROOT::RDF::RNode df, const std::string &pt,
                    const std::string &eta, const std::string &year_id,
                    const std::string &variation, const std::string &id_output,
                    const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("muonIdSF")->debug("Setting up functions for muon id sf");
    Logger::get("muonIdSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, variation](const float &pt, const float &eta) {
            Logger::get("muonIdSF")->debug("ID - pt {}, eta {}", pt, eta);
            double sf = 1.;
            // preventing muons with default values due to tau energy correction
            // shifts below good tau pt selection
            if (pt >= 0.0 && std::abs(eta) >= 0.0) {
                sf = evaluator->evaluate(
                    {year_id, std::abs(eta), pt, variation});
            }
            return sf;
        },
        {pt, eta});
    return df1;
}
/// sf for vhmm
///
ROOT::RDF::RNode id_vhmm(ROOT::RDF::RNode df, const std::string &p4, 
                    const std::string &year_id,
                    const std::string &variation, const std::string &id_output,
                    const std::string &sf_file,
                    const std::string &idAlgorithm) {

    // Logger::get("muonIdSF")->debug("Setting up functions for muon id sf");
    // Logger::get("muonIdSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, variation, sf_file](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            double sf = 1.;
            
            if (sf_file.find("muon_Z") < sf_file.length()) {
                // Logger::get("muon SF file:")->debug("{}", sf_file);
                // apply sf for muon pt > 15 using Z file
                if (pt < 200.0 && pt > 15.0 && std::abs(eta) >= 0.0) {
                    if (year_id.find("202") < year_id.length()) {
                        sf = evaluator->evaluate(
                            {std::abs(eta), pt, variation});    
                    } else {
                        // only run2 muon_Z file need year_id
                        sf = evaluator->evaluate(
                            {year_id, std::abs(eta), pt, variation});
                    }
                } else if (pt >= 0.0 && pt <= 15.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                } else if (pt >= 200.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                }
            } else if (sf_file.find("muon_JPsi") < sf_file.length()) {
                // Logger::get("muon SF file:")->debug("{}", sf_file);
                // apply sf for muon pt < 15 using JPsi file
                // JPsi has no year_id
                if (pt >= 0.0 && pt <= 15.0 && std::abs(eta) >= 0.0) {
                    sf = evaluator->evaluate(
                        {std::abs(eta), pt, variation});    
                } else if (pt > 15.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                }
            } else if (sf_file.find("muon_HighPt") < sf_file.length()) {
                // Logger::get("muon SF file:")->debug("{}", sf_file);
                // apply sf for muon pt > 200 using HighPt file
                if (pt >= 200.0 && std::abs(eta) >= 0.0) {
                    // for High Pt (>200) muon
                    const float &px = p4.Px();
                    const float &py = p4.Py();
                    const float &pz = p4.Pz();
                    //
                    float p = std::sqrt(px*px + py*py + pz*pz);
                    // Logger::get("muon High pt corr:")->debug("pt: {}, p: {}", pt, p);
                    sf = evaluator->evaluate(
                        {std::abs(eta), p, variation});    
                } else if (pt < 200.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                }
            }
            return sf;
        },
        {p4});
    return df1;
}
//// for mvaTTH SF
ROOT::RDF::RNode mvatth_vhmm(ROOT::RDF::RNode df, const std::string &p4, 
                    const std::string &year_id,
                    const std::string &variation, const std::string &id_output,
                    const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("muonIdSF")->debug("Setting up functions for muon id sf");
    Logger::get("muonIdSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, variation, sf_file](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            double sf = 1.;
            
            Logger::get("muon SF file:")->debug("{}", sf_file);
            // apply sf for muon pt > 5 using mvaTTH
            if (pt >= 5 && std::abs(eta) <= 2.4) {
                sf = evaluator->evaluate(
                    {eta, pt, variation});
            } else {
                sf = 1.;
            }
            return sf;
        },
        {p4});
    return df1;
}
/**
 * @brief Function used to evaluate iso scale factors from muons with
 * correctionlib. Configurations:
 * - [UL2018 Muon
 * Iso](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2018_UL.html)
 * - [UL2017 Muon
 * Iso](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2017_UL.html)
 * - [UL2016preVFP Muon
 * Iso](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2016preVFP_UL.html)
 * - [UL2016postVFP Muon
 * Iso](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/MUO_muon_Z_Run2_UL/MUO_muon_Z_2016postVFP_UL.html)
 *
 * @param df The input dataframe
 * @param pt muon pt
 * @param eta muon eta
 * @param year_id id for the year of data taking and mc compaign
 * @param variation id for the variation of the scale factor "sf" for nominal
 * and "systup"/"systdown" the up/down variation
 * @param iso_output name of the iso scale factor column
 * @param sf_file path to the file with the muon scale factors
 * @param idAlgorithm name of the muon iso scale factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode iso(ROOT::RDF::RNode df, const std::string &pt,
                     const std::string &eta, const std::string &year_id,
                     const std::string &variation,
                     const std::string &iso_output, const std::string &sf_file,
                     const std::string &idAlgorithm) {

    Logger::get("muonIsoSF")->debug("Setting up functions for muon iso sf");
    Logger::get("muonIsoSF")->debug("ISO - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        iso_output,
        [evaluator, year_id, variation](const float &pt, const float &eta) {
            Logger::get("muonIsoSF")->debug("ISO - pt {}, eta {}", pt, eta);
            double sf = 1.;
            // preventing muons with default values due to tau energy correction
            // shifts below good tau pt selection
            if (pt >= 0.0 && std::abs(eta) >= 0.0) {
                sf = evaluator->evaluate(
                    {year_id, std::abs(eta), pt, variation});
            }
            return sf;
        },
        {pt, eta});
    return df1;
}
///
ROOT::RDF::RNode iso_vhmm(ROOT::RDF::RNode df, const std::string &p4, 
                     const std::string &year_id,
                     const std::string &variation,
                     const std::string &iso_output, const std::string &sf_file,
                     const std::string &idAlgorithm) {

    Logger::get("muonIsoSF")->debug("Setting up functions for muon iso sf");
    Logger::get("muonIsoSF")->debug("ISO - Name {}", idAlgorithm);
    // since muon_JPsi has no Iso type for SF
    auto evaluator =
            correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        iso_output,
        [evaluator, year_id, variation, sf_file](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            Logger::get("muonIsoSF")->debug("ISO - pt {}, eta {}", pt, eta);
            double sf = 1.;

            if (sf_file.find("muon_Z") < sf_file.length()) {
                Logger::get("muon SF file:")->debug("{}", sf_file);
                // apply sf for muon pt > 15 using Z file
                if (pt < 200.0 && pt > 15.0 && std::abs(eta) >= 0.0) {
                    if (year_id.find("202") < year_id.length()) {
                        sf = evaluator->evaluate(
                            {std::abs(eta), pt, variation});    
                    } else {
                        sf = evaluator->evaluate(
                            {year_id, std::abs(eta), pt, variation});
                    }
                } else if (pt >= 0.0 && pt <= 15.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                } else if (pt >= 200.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                }
            } else if (sf_file.find("muon_JPsi") < sf_file.length()) {
                // apply sf for muon pt < 15 using JPsi file
                // Since muon_JPsi has no Iso type for SF
                sf = 1.;
            } else if (sf_file.find("muon_HighPt") < sf_file.length()) {
                Logger::get("muon SF file:")->debug("{}", sf_file);
                // apply sf for muon pt > 200 using HighPt file
                if (pt >= 200.0 && std::abs(eta) >= 0.0) {
                    // for High Pt (>200) muon
                    const float &px = p4.Px();
                    const float &py = p4.Py();
                    const float &pz = p4.Pz();
                    //
                    float p = std::sqrt(px*px + py*py + pz*pz);
                    Logger::get("muon High pt corr:")->debug("pt: {}, p: {}", pt, p);
                    sf = evaluator->evaluate(
                        {std::abs(eta), p, variation});    
                } else if (pt < 200.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                }
            }
            return sf;
        },
        {p4});
    return df1;
}
///
/**
 * @brief Function used to readout SFs from the muon scale factor measurements
 *
 * @param df the input dataframe
 * @param pt the pt of the muon
 * @param eta the eta of the muon
 * @param output the name of the output column
 * @param sf_file the path to the correctionlib file containing the scale factor
 * @param correctiontype the type of the correction. Use `emb` for embedding and
 * `mc` for monte carlo
 * @param idAlgorithm the name of the scale factor in the correctionlib
 * file
 * @param extrapolation_factor The extrapolation factor to be used for the scale
 * factor, defaults to 1.
 * @return ROOT::RDF::RNode
 */
ROOT::RDF::RNode muon_sf_vhmm(ROOT::RDF::RNode df, const std::string &p4,
                         const std::string &output,
                         const std::string &sf_file,
                         const std::string correctiontype,
                         const std::string &idAlgorithm,
                         const float &extrapolation_factor = 1.0) {

    Logger::get("MuonTriggerSF")->debug("Correction - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        output,
        [evaluator, correctiontype, extrapolation_factor](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            Logger::get("MuonTriggerSF")
                ->debug(" pt {}, eta {}, correctiontype {}, extrapolation "
                        "factor {}",
                        pt, eta, correctiontype, extrapolation_factor);
            double sf = 1.;
            auto pt_tmp = pt;
            if (pt < 26.0 ) pt_tmp = 26.0;
            sf = extrapolation_factor *
                 evaluator->evaluate({std::abs(eta), pt_tmp, correctiontype});
            Logger::get("MuonTriggerSF")->debug("sf {}", sf);
            return sf;
        },
        {p4});
    return df1;
}
///////////
/// below for reco vhmm High Pt
ROOT::RDF::RNode reco_mu_vhmm(ROOT::RDF::RNode df, const std::string &p4, 
                    const std::string &year_id,
                    const std::string &variation, const std::string &id_output,
                    const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("HighPtMuon RECO SF")->debug("Setting up functions for muon reco sf");
    Logger::get("HighPtMuon RECO SF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, variation, sf_file](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            double sf = 1.;
            
            if (sf_file.find("muon_HighPt") < sf_file.length()) {
                Logger::get("muon SF file:")->debug("{}", sf_file);
                // apply sf for muon pt > 200 using HighPt file
                if (pt >= 200.0 && std::abs(eta) >= 0.0) {
                    // for High Pt (>200) muon
                    const float &px = p4.Px();
                    const float &py = p4.Py();
                    const float &pz = p4.Pz();
                    //
                    float p = std::sqrt(px*px + py*py + pz*pz);
                    Logger::get("muon High pt corr:")->debug("pt: {}, p: {}", pt, p);
                    sf = evaluator->evaluate(
                        {std::abs(eta), p, variation});    
                } else if (pt < 200.0 && std::abs(eta) >= 0.0) {
                    sf = 1.;
                }
            }
            return sf;
        },
        {p4});
    return df1;
}

} // namespace muon
namespace tau {
/**
 * @brief Function used to evaluate vsJets tau id scale factors in the lt
channel with
 * correctionlib

Description of the bit map used to define the tau id working points of the
DeepTau2017v2p1 tagger.
vsJets                              | Value | Bit (value used in the config)
------------------------------------|-------|-------
no ID selection (takes every tau)   |  0    | -
VVVLoose                            |  1    | 1
VVLoose                             |  2    | 2
VLoose                              |  4    | 3
Loose                               |  8    | 4
Medium                              |  16   | 5
Tight                               |  32   | 6
VTight                              |  64   | 7
VVTight                             |  128  | 8
 * @param df The input dataframe
 * @param pt tau pt
 * @param decayMode decay mode of the tau
 * @param genMatch column with genmatch values (from prompt e, prompt mu,
 * tau->e, tau->mu, had. tau)
 * @param selectedDMs list of allowed decay modes for which a scale factor
 * should be calculated
 * @param wp working point of the ID cut
 * @param sf_vsjet_tau30to35 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau35to40 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau40to500 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau500to1000 id for the variation of the scale factor "sf"
for nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau1000toinf id for the variation of the scale factor "sf"
for nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_dependence "pt", "dm" or "eta" based scale factors
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the tau scale factors
 * @param idAlgorithm name of the tau id scale factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode
id_vsJet_lt(ROOT::RDF::RNode df, const std::string &pt,
            const std::string &decayMode, const std::string &genMatch,
            const std::vector<int> &selectedDMs, const std::string &wp,
            const std::string &sf_vsjet_tau30to35,
            const std::string &sf_vsjet_tau35to40,
            const std::string &sf_vsjet_tau40to500,
            const std::string &sf_vsjet_tau500to1000,
            const std::string &sf_vsjet_tau1000toinf,
            const std::string &sf_dependence, const std::string &id_output,
            const std::string &sf_file, const std::string &idAlgorithm) {

    Logger::get("TauIDvsJet_lt_SF")
        ->debug("Setting up function for tau id vsJet sf");
    Logger::get("TauIDvsJet_lt_SF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto idSF_calculator = [evaluator, wp, sf_vsjet_tau30to35,
                            sf_vsjet_tau35to40, sf_vsjet_tau40to500,
                            sf_vsjet_tau500to1000, sf_vsjet_tau1000toinf,
                            sf_dependence, selectedDMs,
                            idAlgorithm](const float &pt, const int &decayMode,
                                         const UChar_t &genMatch) {
        Logger::get("TauIDvsJet_lt_SF")->debug("ID - decayMode {}", decayMode);
        // only calculate SFs for allowed tau decay modes (also excludes default
        // values due to tau energy correction shifts below good tau pt
        // selection)
        double sf = 1.;
        if (std::find(selectedDMs.begin(), selectedDMs.end(), decayMode) !=
            selectedDMs.end()) {
            Logger::get("TauIDvsJet_lt_SF")
                ->debug("ID {} - pt {}, decayMode {}, genMatch {}, wp {}, "
                        "sf_vsjet_tau30to35 {}, sf_vsjet_tau35to40 {}, "
                        "sf_vsjet_tau40to500{}, sf_vsjet_tau500to1000 {}, "
                        "sf_vsjet_tau1000toinf {}, sf_dependence {}",
                        idAlgorithm, pt, decayMode, genMatch, wp,
                        sf_vsjet_tau30to35, sf_vsjet_tau35to40,
                        sf_vsjet_tau40to500, sf_vsjet_tau500to1000,
                        sf_vsjet_tau1000toinf, sf_dependence);
            if (pt >= 30.0 && pt < 35.0) {
                sf = evaluator->evaluate({pt, decayMode,
                                          static_cast<int>(genMatch), wp,
                                          sf_vsjet_tau30to35, sf_dependence});
            } else if (pt >= 35.0 && pt < 40.0) {
                sf = evaluator->evaluate({pt, decayMode,
                                          static_cast<int>(genMatch), wp,
                                          sf_vsjet_tau35to40, sf_dependence});
            } else if (pt >= 40.0 && pt < 500.0) {
                sf = evaluator->evaluate({pt, decayMode,
                                          static_cast<int>(genMatch), wp,
                                          sf_vsjet_tau40to500, sf_dependence});
            } else if (pt >= 500.0 && pt < 1000.0) {
                sf = evaluator->evaluate(
                    {pt, decayMode, static_cast<int>(genMatch), wp,
                     sf_vsjet_tau500to1000, sf_dependence});
            } else if (pt >= 1000.0 && pt < 2000.0) {
                sf = evaluator->evaluate(
                    {pt, decayMode, static_cast<int>(genMatch), wp,
                     sf_vsjet_tau1000toinf, sf_dependence});
            } else {
                sf = 1.;
            }
        }
        Logger::get("TauIDvsJet_lt_SF")->debug("Scale Factor {}", sf);
        return sf;
    };
    auto df1 = df.Define(id_output, idSF_calculator, {pt, decayMode, genMatch});
    return df1;
}
/**
 * @brief Function used to evaluate vsJets tau id scale factors in the lt
channel with the correctionlib for tauembedded samples


 * @param df The input dataframe
 * @param pt tau pt
 * @param wp working point of the ID cut
 * @param sf_vsjet_tau20to25 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau25to30 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau30to35 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau35to40 id for the variation of the scale factor "sf"
for nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tau40toInf id for the variation of the scale factor "sf"
for nominal
 * and "systup"/"systdown" the up/down variation
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the tau scale factors
 * @param correctionset name of the correction set containing the tau id scale
factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode id_vsJet_lt_embedding(
    ROOT::RDF::RNode df, const std::string &pt, const std::string &wp,
    const std::string &sf_vsjet_tau20to25,
    const std::string &sf_vsjet_tau25to30,
    const std::string &sf_vsjet_tau30to35,
    const std::string &sf_vsjet_tau35to40,
    const std::string &sf_vsjet_tau40toInf, const std::string &id_output,
    const std::string &sf_file, const std::string &correctionset) {

    Logger::get("TauIDvsJet_lt_SF_embedding")
        ->debug("Setting up function for tau id vsJet sf");
    Logger::get("TauIDvsJet_lt_SF_embedding")
        ->debug("ID - Name {}", correctionset);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(correctionset);
    auto idSF_calculator = [evaluator, wp, sf_vsjet_tau20to25,
                            sf_vsjet_tau25to30, sf_vsjet_tau30to35,
                            sf_vsjet_tau35to40, sf_vsjet_tau40toInf,
                            correctionset](const float &pt) {
        double sf = 1.;
        Logger::get("TauIDvsJet_lt_SF_embedding")
            ->debug("ID {} - pt {}, wp {} "
                    "sf_vsjet_tau20to25 {}, sf_vsjet_tau25to30 {}, "
                    "sf_vsjet_tau30to35{}, sf_vsjet_tau35to40 {}, "
                    "sf_vsjet_tau40toInf {},",
                    correctionset, pt, wp, sf_vsjet_tau20to25,
                    sf_vsjet_tau25to30, sf_vsjet_tau30to35, sf_vsjet_tau35to40,
                    sf_vsjet_tau40toInf);
        if (pt >= 20.0 && pt < 25.0) {
            sf = evaluator->evaluate({pt, sf_vsjet_tau20to25, wp});
        } else if (pt >= 25.0 && pt < 30.0) {
            sf = evaluator->evaluate({pt, sf_vsjet_tau25to30, wp});
        } else if (pt >= 30.0 && pt < 35.0) {
            sf = evaluator->evaluate({pt, sf_vsjet_tau30to35, wp});
        } else if (pt >= 35.0 && pt < 40.0) {
            sf = evaluator->evaluate({pt, sf_vsjet_tau35to40, wp});
        } else if (pt >= 40.0 && pt < 10000.0) {
            sf = evaluator->evaluate({pt, sf_vsjet_tau40toInf, wp});
        } else {
            sf = 1.;
        }
        Logger::get("TauIDvsJet_lt_SF_embedding")->debug("Scale Factor {}", sf);
        return sf;
    };
    auto df1 = df.Define(id_output, idSF_calculator, {pt});
    return df1;
}
/**
 * @brief Function used to evaluate vsJets tau id scale factors in the tt
channel with the correctionlib for tauembedded samples

 * @param df The input dataframe
 * @param decaymode decay mode of the tau
 * @param wp working point of the ID cut
 * @param sf_vsjet_tauDM0 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tauDM1 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tauDM10 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tauDM11 id for the variation of the scale factor "sf"
for nominal
 * and "systup"/"systdown" the up/down variation
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the tau scale factors
 * @param correctionset name of the correction set containing the tau id scale
factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode id_vsJet_tt_embedding(
    ROOT::RDF::RNode df, const std::string &decaymode, const std::string &wp,
    const std::string &sf_vsjet_tauDM0, const std::string &sf_vsjet_tauDM1,
    const std::string &sf_vsjet_tauDM10, const std::string &sf_vsjet_tauDM11,
    const std::string &id_output, const std::string &sf_file,
    const std::string &correctionset) {

    Logger::get("TauIDvsJet_tt_SF_embedding")
        ->debug("Setting up function for tau id vsJet sf");
    Logger::get("TauIDvsJet_tt_SF_embedding")
        ->debug("ID - Name {}", correctionset);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(correctionset);
    auto idSF_calculator = [evaluator, wp, sf_vsjet_tauDM0, sf_vsjet_tauDM1,
                            sf_vsjet_tauDM10, sf_vsjet_tauDM11,
                            correctionset](const int &decaymode) {
        double sf = 1.;
        Logger::get("TauIDvsJet_tt_SF_embedding")
            ->debug("ID {} - decaymode {}, wp {} "
                    "sf_vsjet_tauDM0 {}, sf_vsjet_tauDM1 {}, "
                    "sf_vsjet_tauDM10{}, sf_vsjet_tauDM11 {}, ",
                    correctionset, decaymode, wp, sf_vsjet_tauDM0,
                    sf_vsjet_tauDM1, sf_vsjet_tauDM10, sf_vsjet_tauDM11);
        if (decaymode == 0) {
            sf = evaluator->evaluate({decaymode, sf_vsjet_tauDM0, wp});
        } else if (decaymode == 1) {
            sf = evaluator->evaluate({decaymode, sf_vsjet_tauDM1, wp});
        } else if (decaymode == 10) {
            sf = evaluator->evaluate({decaymode, sf_vsjet_tauDM10, wp});
        } else if (decaymode == 11) {
            sf = evaluator->evaluate({decaymode, sf_vsjet_tauDM11, wp});
        } else {
            sf = 1.;
        }
        Logger::get("TauIDvsJet_tt_SF_embedding")->debug("Scale Factor {}", sf);
        return sf;
    };
    auto df1 = df.Define(id_output, idSF_calculator, {decaymode});
    return df1;
}
/**
 * @brief Function used to evaluate vsJets tau id scale factors in the tt
channel with
 * correctionlib

Description of the bit map used to define the tau id working points of the
DeepTau2017v2p1 tagger.
vsJets                              | Value | Bit (value used in the config)
------------------------------------|-------|-------
no ID selection (takes every tau)   |  0    | -
VVVLoose                            |  1    | 1
VVLoose                             |  2    | 2
VLoose                              |  4    | 3
Loose                               |  8    | 4
Medium                              |  16   | 5
Tight                               |  32   | 6
VTight                              |  64   | 7
VVTight                             |  128  | 8
 * @param df The input dataframe
 * @param pt tau pt
 * @param decayMode decay mode of the tau
 * @param genMatch column with genmatch values (from prompt e, prompt mu,
 * tau->e, tau->mu, had. tau)
 * @param selectedDMs list of allowed decay modes for which a scale factor
 * should be calculated
 * @param wp working point of the ID cut
 * @param sf_vsjet_tauDM0 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tauDM1 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tauDM10 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsjet_tauDM11 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_dependence "pt", "dm" or "eta" based scale factors
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the tau scale factors
 * @param idAlgorithm name of the tau id scale factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode id_vsJet_tt(
    ROOT::RDF::RNode df, const std::string &pt, const std::string &decayMode,
    const std::string &genMatch, const std::vector<int> &selectedDMs,
    const std::string &wp, const std::string &sf_vsjet_tauDM0,
    const std::string &sf_vsjet_tauDM1, const std::string &sf_vsjet_tauDM10,
    const std::string &sf_vsjet_tauDM11, const std::string &sf_dependence,
    const std::string &id_output, const std::string &sf_file,
    const std::string &idAlgorithm) {

    Logger::get("TauIDvsJet_tt_SF")
        ->debug("Setting up function for tau id vsJet sf");
    Logger::get("TauIDvsJet_tt_SF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto idSF_calculator = [evaluator, wp, sf_vsjet_tauDM0, sf_vsjet_tauDM1,
                            sf_vsjet_tauDM10, sf_vsjet_tauDM11, sf_dependence,
                            selectedDMs,
                            idAlgorithm](const float &pt, const int &decayMode,
                                         const UChar_t &genMatch) {
        Logger::get("TauIDvsJet_tt_SF")->debug("ID - decayMode {}", decayMode);
        // only calculate SFs for allowed tau decay modes (also excludes default
        // values due to tau energy correction shifts below good tau pt
        // selection)
        double sf = 1.;
        if (std::find(selectedDMs.begin(), selectedDMs.end(), decayMode) !=
            selectedDMs.end()) {
            Logger::get("TauIDvsJet_tt_SF")
                ->debug("ID {} - pt {}, decayMode {}, genMatch {}, wp {}, "
                        "sf_vsjet_tauDM0 {}, sf_vsjet_tauDM1 {}, "
                        "sf_vsjet_tauDM1 {}, sf_vsjet_tauDM10{}, "
                        "sf_vsjet_tauDM11 {}, sf_dependence {}",
                        idAlgorithm, pt, decayMode, genMatch, wp,
                        sf_vsjet_tauDM0, sf_vsjet_tauDM1, sf_vsjet_tauDM10,
                        sf_vsjet_tauDM11, sf_dependence);
            if (decayMode == 0) {
                sf = evaluator->evaluate({pt, decayMode,
                                          static_cast<int>(genMatch), wp,
                                          sf_vsjet_tauDM0, sf_dependence});
            } else if (decayMode == 1) {
                sf = evaluator->evaluate({pt, decayMode,
                                          static_cast<int>(genMatch), wp,
                                          sf_vsjet_tauDM1, sf_dependence});
            } else if (decayMode == 10) {
                sf = evaluator->evaluate({pt, decayMode,
                                          static_cast<int>(genMatch), wp,
                                          sf_vsjet_tauDM10, sf_dependence});
            } else if (decayMode == 11) {
                sf = evaluator->evaluate({pt, decayMode,
                                          static_cast<int>(genMatch), wp,
                                          sf_vsjet_tauDM11, sf_dependence});
            } else {
                sf = 1.;
            }
        }
        Logger::get("TauIDvsJet_tt_SF")->debug("Scale Factor {}", sf);
        return sf;
    };
    auto df1 = df.Define(id_output, idSF_calculator, {pt, decayMode, genMatch});
    return df1;
}
/**
 * @brief Function used to evaluate vsEle tau id scale factors with
 * correctionlib

Description of the bit map used to define the tau id working points of the
DeepTau2017v2p1 tagger.
vsElectrons                         | Value | Bit (value used in the config)
------------------------------------|-------|-------
no ID selection (takes every tau)   |  0    | -
VVVLoose                            |  1    | 1
VVLoose                             |  2    | 2
VLoose                              |  4    | 3
Loose                               |  8    | 4
Medium                              |  16   | 5
Tight                               |  32   | 6
VTight                              |  64   | 7
VVTight                             |  128  | 8

vsMuons                             | Value | Bit (value used in the config)
------------------------------------|-------|-------
no ID selection (takes every tau)   |  0    | -
VLoose                              |  1    | 1
Loose                               |  2    | 2
Medium                              |  4    | 3
Tight                               |  8    | 4
 * @param df The input dataframe
 * @param eta tau eta
 * @param decayMode decay mode of the tau
 * @param genMatch column with genmatch values (from prompt e, prompt mu,
 * tau->e, tau->mu, had. tau)
 * @param selectedDMs list of allowed decay modes for which a scale factor
 * should be calculated
 * @param wp working point of the ID cut
 * @param sf_vsele_barrel id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsele_endcap id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the tau scale factors
 * @param idAlgorithm name of the tau id scale factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode
id_vsEle(ROOT::RDF::RNode df, const std::string &eta,
         const std::string &decayMode, const std::string &genMatch,
         const std::vector<int> &selectedDMs, const std::string &wp,
         const std::string &sf_vsele_barrel, const std::string &sf_vsele_endcap,
         const std::string &id_output, const std::string &sf_file,
         const std::string &idAlgorithm) {

    Logger::get("TauIDvsEleSF")
        ->debug("Setting up function for tau id vsEle sf");
    Logger::get("TauIDvsEleSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto idSF_calculator = [evaluator, wp, sf_vsele_barrel, sf_vsele_endcap,
                            selectedDMs,
                            idAlgorithm](const float &eta, const int &decayMode,
                                         const UChar_t &genMatch) {
        double sf = 1.;
        Logger::get("TauIDvsEleSF")->debug("ID - decayMode {}", decayMode);
        // only calculate SFs for allowed tau decay modes (also excludes
        // default values due to tau energy correction shifts below good tau
        // pt selection)
        if (std::find(selectedDMs.begin(), selectedDMs.end(), decayMode) !=
            selectedDMs.end()) {
            Logger::get("TauIDvsEleSF")
                ->debug("ID {} - eta {}, genMatch {}, wp {}, sf_vsele_barrel "
                        "{}, sf_vsele_endcap {}",
                        idAlgorithm, eta, genMatch, wp, sf_vsele_barrel,
                        sf_vsele_endcap);
            if (std::abs(eta) < 1.46) {
                sf = evaluator->evaluate(
                    {eta, static_cast<int>(genMatch), wp, sf_vsele_barrel});
            } else if (std::abs(eta) >= 1.558 && std::abs(eta) < 2.3) {
                sf = evaluator->evaluate(
                    {eta, static_cast<int>(genMatch), wp, sf_vsele_endcap});
            } else {
                sf = 1.;
            }
        }
        Logger::get("TauIDvsEleSF")->debug("Scale Factor {}", sf);
        return sf;
    };
    auto df1 =
        df.Define(id_output, idSF_calculator, {eta, decayMode, genMatch});
    return df1;
}
/**
 * @brief Function used to evaluate vsMu tau id scale factors with
 * correctionlib

Description of the bit map used to define the tau id working points of the
DeepTau2017v2p1 tagger.
vsElectrons                         | Value | Bit (value used in the config)
------------------------------------|-------|-------
no ID selection (takes every tau)   |  0    | -
VVVLoose                            |  1    | 1
VVLoose                             |  2    | 2
VLoose                              |  4    | 3
Loose                               |  8    | 4
Medium                              |  16   | 5
Tight                               |  32   | 6
VTight                              |  64   | 7
VVTight                             |  128  | 8

vsMuons                             | Value | Bit (value used in the config)
------------------------------------|-------|-------
no ID selection (takes every tau)   |  0    | -
VLoose                              |  1    | 1
Loose                               |  2    | 2
Medium                              |  4    | 3
Tight                               |  8    | 4
 * @param df The input dataframe
 * @param eta tau eta
 * @param decayMode decay mode of the tau
 * @param genMatch column with genmatch values (from prompt e, prompt mu,
 * tau->e, tau->mu, had. tau)
 * @param selectedDMs list of allowed decay modes for which a scale factor
 * should be calculated
 * @param wp working point of the ID cut
 * @param sf_vsmu_wheel1 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsmu_wheel2 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsmu_wheel3 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsmu_wheel4 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param sf_vsmu_wheel5 id for the variation of the scale factor "sf" for
nominal
 * and "systup"/"systdown" the up/down variation
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the tau scale factors
 * @param idAlgorithm name of the tau id scale factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode
id_vsMu(ROOT::RDF::RNode df, const std::string &eta,
        const std::string &decayMode, const std::string &genMatch,
        const std::vector<int> &selectedDMs, const std::string &wp,
        const std::string &sf_vsmu_wheel1, const std::string &sf_vsmu_wheel2,
        const std::string &sf_vsmu_wheel3, const std::string &sf_vsmu_wheel4,
        const std::string &sf_vsmu_wheel5, const std::string &id_output,
        const std::string &sf_file, const std::string &idAlgorithm) {

    Logger::get("TauIDvsMuSF")->debug("Setting up function for tau id vsMu sf");
    Logger::get("TauIDvsMuSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto idSF_calculator = [evaluator, wp, sf_vsmu_wheel1, sf_vsmu_wheel2,
                            sf_vsmu_wheel3, sf_vsmu_wheel4, sf_vsmu_wheel5,
                            selectedDMs,
                            idAlgorithm](const float &eta, const int &decayMode,
                                         const UChar_t &genMatch) {
        double sf = 1.;
        Logger::get("TauIDvsMuSF")->debug("ID - decayMode {}", decayMode);
        // only calculate SFs for allowed tau decay modes (also excludes
        // default values due to tau energy correction shifts below good tau
        // pt selection)
        if (std::find(selectedDMs.begin(), selectedDMs.end(), decayMode) !=
            selectedDMs.end()) {
            Logger::get("TauIDvsMuSF")
                ->debug("ID {} - eta {}, genMatch {}, wp {}, sf_vsmu_wheel1 "
                        "{}, sf_vsmu_wheel2 {}, sf_vsmu_wheel3 {}, "
                        "sf_vsmu_wheel4 {}, sf_vsmu_wheel5 {}",
                        idAlgorithm, eta, genMatch, wp, sf_vsmu_wheel1,
                        sf_vsmu_wheel2, sf_vsmu_wheel3, sf_vsmu_wheel4,
                        sf_vsmu_wheel5);
            if (std::abs(eta) < 0.4) {
                sf = evaluator->evaluate(
                    {eta, static_cast<int>(genMatch), wp, sf_vsmu_wheel1});
            } else if (std::abs(eta) >= 0.4 && std::abs(eta) < 0.8) {
                sf = evaluator->evaluate(
                    {eta, static_cast<int>(genMatch), wp, sf_vsmu_wheel2});
            } else if (std::abs(eta) >= 0.8 && std::abs(eta) < 1.2) {
                sf = evaluator->evaluate(
                    {eta, static_cast<int>(genMatch), wp, sf_vsmu_wheel3});
            } else if (std::abs(eta) >= 1.2 && std::abs(eta) < 1.7) {
                sf = evaluator->evaluate(
                    {eta, static_cast<int>(genMatch), wp, sf_vsmu_wheel4});
            } else if (std::abs(eta) >= 1.7 && std::abs(eta) < 2.3) {
                sf = evaluator->evaluate(
                    {eta, static_cast<int>(genMatch), wp, sf_vsmu_wheel5});
            } else {
                sf = 1.0;
            }
        }
        Logger::get("TauIDvsMuSF")->debug("Scale Factor {}", sf);
        return sf;
    };
    auto df1 =
        df.Define(id_output, idSF_calculator, {eta, decayMode, genMatch});
    return df1;
}

/**
 * @brief Function to evaluate the tau trigger scale factor from a xpog file
 *
 * @param df the input dataframe
 * @param decaymode the name of the column containing the tau decay mode
 * variable
 * @param wp the name of the the tau id working point
 * @param type the type of the tau trigger scale factor, available are emb and
 * mc
 * @param pt the name of the column containing the tau pt variable
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the tau scale factors
 * @param correctionset name of the tau trigger scale factor
 * @return ROOT::RDF::RNode a new dataframe containing the new sf column
 */

ROOT::RDF::RNode
tau_trigger_sf(ROOT::RDF::RNode df, const std::string &decaymode,
               const std::string &pt, const std::string &wp,
               const std::string &type, const std::string &id_output,
               const std::string &sf_file, const std::string &correctionset) {

    Logger::get("tau_trigger_sf")
        ->info("Setting up function for tau trigger sf");
    Logger::get("tau_trigger_sf")
        ->info("ID - Name {}, file {}", correctionset, sf_file);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(correctionset);
    Logger::get("tau_trigger_sf")->info("WP {} - type {}", wp, type);
    auto trigger_sf_calculator = [evaluator, wp, type, correctionset](
                                     const int &decaymode, const float &pt) {
        float sf = 1.;
        Logger::get("tau_trigger_sf")
            ->info("ID {} - decaymode {}, wp {} "
                   "pt {}, type {}, ",
                   correctionset, decaymode, wp, pt, type);
        sf = evaluator->evaluate({decaymode, wp, type, pt});
        Logger::get("tau_trigger_sf")->info("Scale Factor {}", sf);
        return sf;
    };
    auto df1 = df.Define(id_output, trigger_sf_calculator, {decaymode, pt});
    return df1;
}
} // namespace tau

namespace electron {
/**
 * @brief Function used to evaluate id scale factors of electrons with
 * correctionlib, configurations:
 * - [UL2018 Electron
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/EGM_electron_Run2_UL/EGM_electron_2018_UL.html)
 * - [UL2017 Electron
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/EGM_electron_Run2_UL/EGM_electron_2017_UL.html)
 * - [UL2016preVFP Electron
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/EGM_electron_Run2_UL/EGM_electron_2016preVFP_UL.html)
 * - [UL2016postVFP Electron
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/EGM_electron_Run2_UL/EGM_electron_2016postVFP_UL.html)
 * @param df The input dataframe
 * @param pt electron pt
 * @param eta electron eta
 * @param year_id id for the year of data taking and mc compaign
 * @param wp wp of the electron id
 * @param variation id for the variation of the scale factor. Available Values:
 * sf, sfdown, sfup
 * @param id_output name of the id scale factor column
 * @param sf_file path to the file with the electron scale factors
 * @param idAlgorithm name of the electron id scale factor
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode id(ROOT::RDF::RNode df, const std::string &pt,
                    const std::string &eta, const std::string &year_id,
                    const std::string &wp, const std::string &variation,
                    const std::string &id_output, const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("electronIDSF")
        ->debug("Setting up functions for electron id sf with correctionlib");
    Logger::get("electronIDSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, idAlgorithm, wp, variation](const float &pt,
                                                         const float &eta) {
            Logger::get("electronIDSF")
                ->debug("Year {}, Name {}, WP {}", year_id, idAlgorithm, wp);
            Logger::get("electronIDSF")->debug("ID - pt {}, eta {}", pt, eta);
            double sf = 1.;
            if (pt >= 0.0) {
                sf = evaluator->evaluate({year_id, variation, wp, eta, pt});
            }
            Logger::get("electronIDSF")->debug("Scale Factor {}", sf);
            return sf;
        },
        {pt, eta});
    return df1;
}
///
ROOT::RDF::RNode id_e_vhmm(ROOT::RDF::RNode df,
                    const std::string &p4, const std::string &year_id,
                    const std::string &wp, const std::string &variation,
                    const std::string &id_output, const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("electronIDSF")
        ->debug("Setting up functions for electron id sf with correctionlib");
    Logger::get("electronIDSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, idAlgorithm, wp, variation](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            const float &phi = p4.Phi();
            Logger::get("electronIDSF")
                ->debug("Year {}, Name {}, WP {}", year_id, idAlgorithm, wp);
            Logger::get("electronIDSF")->debug("ID - pt {}, eta {}, phi {}", pt, eta, phi);
            double sf = 1.;
            if (pt >= 10.0) {
                if (year_id.find("2023") < year_id.length()) {
                    sf = evaluator->evaluate({year_id, variation, wp, eta, pt, phi});
                } else {
                    sf = evaluator->evaluate({year_id, variation, wp, eta, pt});
                }
            } else if (pt < 10) {
                sf = 1.;
            }
            Logger::get("electronIDSF")->debug("Scale Factor {}", sf);
            return sf;
        },
        {p4});
    return df1;
}

ROOT::RDF::RNode custom_e_vhmm(ROOT::RDF::RNode df,
                    const std::string &p4, const std::string &year_id,
                    const std::string &wp, const std::string &variation,
                    const std::string &id_output, const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("electronIDSF")
        ->debug("Setting up functions for electron id sf with correctionlib");
    Logger::get("electronIDSF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, idAlgorithm, wp, variation](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            Logger::get("electronIDSF")
                ->debug("Year {}, Name {}, WP {}", year_id, idAlgorithm, wp);
            Logger::get("electronID-customSF")->debug("ID - pt {}, eta {}", pt, eta);
            double sf = 1.;
            if (pt >= 7.0 && pt < 10.0) {
                sf = evaluator->evaluate({year_id, variation, wp, eta, pt});
            } else if (pt < 200 && pt >= 10 && wp == "mvaTTH") {
                sf = evaluator->evaluate({year_id, variation, wp, eta, pt});
            } else {
                sf = 1.;
            }
            Logger::get("electronIDSF")->debug("Scale Factor {}", sf);
            return sf;
        },
        {p4});
    return df1;
}

ROOT::RDF::RNode reco_e_vhmm(ROOT::RDF::RNode df,
                    const std::string &p4, const std::string &year_id,
                    const std::string &variation,
                    const std::string &id_output, const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("electronRecoSF")
        ->debug("Setting up functions for electron reco sf with correctionlib");
    Logger::get("electronRecoSF")->debug("Reco - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, year_id, idAlgorithm, variation](ROOT::Math::PtEtaPhiMVector &p4) {
            const float &pt = p4.Pt();
            const float &eta = p4.Eta();
            const float &phi = p4.Phi();
            Logger::get("electronRecoSF")
                ->debug("Year {}, Name {}", year_id, idAlgorithm);
            // wp -> RecoBelow20, Reco20to75, RecoAbove75
            double sf = 1.;
            if (pt >= 10.0 && pt < 20) {
                if (year_id.find("2023") < year_id.length()) {
                    Logger::get("electronRecoSF")->debug("RecoBelow20 - pt {}, eta {}, phi {}", pt, eta, phi);
                    sf = evaluator->evaluate({year_id, variation, "RecoBelow20", eta, pt, phi});
                } else {
                    Logger::get("electronRecoSF")->debug("RecoBelow20 - pt {}, eta {}", pt, eta);
                    sf = evaluator->evaluate({year_id, variation, "RecoBelow20", eta, pt});
                }
            } else if (pt >= 20 && pt < 75) {
                if (year_id.find("2023") < year_id.length()) {
                    Logger::get("electronRecoSF")->debug("Reco20to75 - pt {}, eta {}, phi {}", pt, eta, phi);
                    sf = evaluator->evaluate({year_id, variation, "Reco20to75", eta, pt, phi});
                } else {
                    Logger::get("electronRecoSF")->debug("Reco20to75 - pt {}, eta {}", pt, eta);
                    sf = evaluator->evaluate({year_id, variation, "Reco20to75", eta, pt});
                }
            } else if (pt >= 75) {
                if (year_id.find("2023") < year_id.length()) {
                    Logger::get("electronRecoSF")->debug("RecoAbove75 - pt {}, eta {}, phi {}", pt, eta, phi);
                    sf = evaluator->evaluate({year_id, variation, "RecoAbove75", eta, pt, phi});
                } else {
                    Logger::get("electronRecoSF")->debug("RecoAbove75 - pt {}, eta {}", pt, eta);
                    sf = evaluator->evaluate({year_id, variation, "RecoAbove75", eta, pt});
                }
            } else if (pt < 10) {
                sf = 1.;
            }
            Logger::get("electronRecoSF")->debug("Scale Factor {}", sf);
            return sf;
        },
        {p4});
    return df1;
}

} // namespace electron
namespace jet {
/**
 * @brief Function used to evaluate b-tagging scale factors of jets with
 * correctionlib, configurations:
 * - [UL2018 b-tagging
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/BTV_btagging_Run2_UL/BTV_btagging_2018_UL.html)
 * - [UL2017 b-tagging
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/BTV_btagging_Run2_UL/BTV_btagging_2017_UL.html)
 * - [UL2016preVFP b-tagging
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/BTV_btagging_Run2_UL/BTV_btagging_2016preVFP_UL.html)
 * - [UL2016postVFP b-tagging
 * ID](https://cms-nanoaod-integration.web.cern.ch/commonJSONSFs/BTV_btagging_Run2_UL/BTV_btagging_2016postVFP_UL.html)
 * @param df The input dataframe
 * @param pt jet pt
 * @param eta jet eta
 * @param btag_discr btag value of a jet based on a b-jet tagger (e.g. DeepJet)
 * @param flavor flavor of the jet
 * @param jet_mask mask for good/selected jets
 * @param bjet_mask mask for good/selected b jets
 * @param jet_veto_mask veto mask for overlapping jets
 * @param variation id for the variation of the scale factor. Available Values:
 * central, down_*, up_* (* name of variation)
 * @param sf_output name of the scale factor column
 * @param sf_file path to the file with the btagging scale factors
 * @param corr_algorithm name of the btagging correction algorithm
 * @return a new dataframe containing the new column
 */
ROOT::RDF::RNode
btagSF_2WPs(ROOT::RDF::RNode df, const std::string &pt, const std::string &eta,
            const std::string &btag_discr, const std::string &flavor,
            const std::string &jet_mask, const std::string &bjet_mask,
            const std::string &jet_veto_mask, const std::string &variation,
            const std::string &sf_output, const std::string &sf_file,
            const std::string &loose_eff_file, const std::string &medium_eff_file,
            const std::string &year, const std::string &channel, 
            const float &loose_cut, const float &medium_cut, const std::string &btag_label) {
    auto evaluator_bc = correction::CorrectionSet::from_file(sf_file)->at(btag_label + "_comb");
    auto evaluator_light = correction::CorrectionSet::from_file(sf_file)->at(btag_label + "_light");
    auto loose_btag_eff = correction::CorrectionSet::from_file(loose_eff_file)->at("Btagging efficiency[pt,eta,flavor]");
    auto medium_btag_eff = correction::CorrectionSet::from_file(medium_eff_file)->at("Btagging efficiency[pt,eta,flavor]");

    auto btagSF_lambda = [evaluator_bc, evaluator_light, loose_btag_eff, medium_btag_eff, variation, year, channel, loose_cut, medium_cut](
            const ROOT::RVec<float> &pt_values,
            const ROOT::RVec<float> &eta_values,
            const ROOT::RVec<float> &btag_values,
            const ROOT::RVec<UChar_t> &flavors,
            const ROOT::RVec<int> &jet_mask,
            const ROOT::RVec<int> &bjet_mask,
            const ROOT::RVec<int> &jet_veto_mask) {
        Logger::get("btagSF")->debug("Vatiation - Name {}", variation);
        float sf = 1.;
        int m_bjets_nb = 0;
        int l_bjets_nb = 0;
        for (int i = 0; i < pt_values.size(); i++) {
             Logger::get("btagSF")->debug(
                 "jet masks - jet {}, bjet {}, jet veto {}", jet_mask.at(i),
                 bjet_mask.at(i), jet_veto_mask.at(i));
             // considering only good jets/bjets, this is needed since jets and
             // bjets might have different cuts depending on the analysis
             if ((jet_mask.at(i) || bjet_mask.at(i)) && jet_veto_mask.at(i) && pt_values.at(i) >= 20.0 && pt_values.at(i) < 10000.0 && std::abs(eta_values.at(i)) < 2.5 &&  btag_values.at(i) > 0 ) {
                if (btag_values.at(i) >= medium_cut) { 
                    m_bjets_nb += 1;
                }
                else if (btag_values.at(i) >= loose_cut && btag_values.at(i) < medium_cut) {
                    l_bjets_nb += 1;    
                }
            }
        };

        if (l_bjets_nb == 0 ){
            sf = 1;
        }
        else if (l_bjets_nb > 0 && m_bjets_nb ==0){
            for (int i = 0; i < pt_values.size(); i++) {
                if ((jet_mask.at(i) || bjet_mask.at(i)) && jet_veto_mask.at(i) && pt_values.at(i) >= 20.0 && pt_values.at(i) < 10000.0 && std::abs(eta_values.at(i)) < 2.5 &&  btag_values.at(i) > 0 ) {
                auto loose_bjet_sf = 1.0;
                auto medium_bjet_sf = 1.0;
                auto pt_tmp = 0.0;
                if ( pt_values.at(i) >= 200) {pt_tmp = 199.99; } else pt_tmp=  pt_values.at(i) ;

                // for difference case: if evaluate light variation, use light SF and light flavor, vice versa. 
                if (variation.find("light") != std::string::npos) {
                    if ( flavors.at(i) == 0) {
                        loose_bjet_sf = evaluator_light->evaluate({variation, "L", flavors.at(i), std::abs(eta_values.at(i)), pt_values.at(i)  });}
                    else {
                        loose_bjet_sf = evaluator_bc->evaluate({"central", "L", flavors.at(i), std::abs(eta_values.at(i)), pt_values.at(i)  });}
                    }   
                else {
                    if ( flavors.at(i) == 0) {
                        loose_bjet_sf = evaluator_light->evaluate({"central", "L", flavors.at(i), std::abs(eta_values.at(i)), pt_values.at(i)  });}
                    else {
                        loose_bjet_sf = evaluator_bc->evaluate({variation, "L", flavors.at(i), std::abs(eta_values.at(i)), pt_values.at(i)  });}
                    }

                auto  loose_bjet_eff =  loose_btag_eff->evaluate({year, "btagging-eff", channel, pt_tmp, eta_values.at(i), flavors.at(i)  });
                if (btag_values.at(i) >= loose_cut) {
                    if (loose_bjet_sf * loose_bjet_eff >= 1) {
                        sf *= 1;
                    }
                    else {
                    sf *= loose_bjet_sf;
                        }
                    }
                else {
                    if (loose_bjet_sf * loose_bjet_eff >= 1) {
                        sf *= 1;
                    }
                    else {
                    sf *= (1 - loose_bjet_sf * loose_bjet_eff) / (1 - loose_bjet_eff);
                        }
                    }
                }
            };
        }
        else {
            sf = 1;
        }
        
        if (sf < 0.96 || sf > 1.04) {
            sf = 1;
        }
        return sf;
    };
    auto df1 = df.Define(
         sf_output, btagSF_lambda,
         {pt, eta, btag_discr, flavor, jet_mask, bjet_mask, jet_veto_mask});
     return df1;
}

ROOT::RDF::RNode
btagSF(ROOT::RDF::RNode df, const std::string &pt, const std::string &eta,
       const std::string &btag_discr, const std::string &flavor,
       const std::string &jet_mask, const std::string &bjet_mask,
       const std::string &jet_veto_mask, const std::string &variation,
       const std::string &sf_output, const std::string &sf_file,
       const std::string &corr_algorithm) {
    Logger::get("btagSF")->debug(
        "Setting up functions for b-tag sf with correctionlib");
    Logger::get("btagSF")->debug("Correction algorithm - Name {}",
                                 corr_algorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(corr_algorithm);

    auto btagSF_lambda = [evaluator,
                          variation](const ROOT::RVec<float> &pt_values,
                                     const ROOT::RVec<float> &eta_values,
                                     const ROOT::RVec<float> &btag_values,
                                     const ROOT::RVec<unsigned char> &flavors,
                                     const ROOT::RVec<int> &jet_mask,
                                     const ROOT::RVec<int> &bjet_mask,
                                     const ROOT::RVec<int> &jet_veto_mask) {
        Logger::get("btagSF")->debug("Vatiation - Name {}", variation);
        float sf = 1.;
        for (int i = 0; i < pt_values.size(); i++) {
            Logger::get("btagSF")->debug(
                "jet masks - jet {}, bjet {}, jet veto {}", jet_mask.at(i),
                bjet_mask.at(i), jet_veto_mask.at(i));
            // considering only good jets/bjets, this is needed since jets and
            // bjets might have different cuts depending on the analysis
            if ((jet_mask.at(i) || bjet_mask.at(i)) && jet_veto_mask.at(i)) {
                Logger::get("btagSF")->debug(
                    "SF - pt {}, eta {}, btag value {}, flavor {}",
                    pt_values.at(i), eta_values.at(i), btag_values.at(i),
                    flavors.at(i));
                float jet_sf = 1.;
                // considering only phase space where the scale factors are
                // defined
                float btag_tmp_values = btag_values.at(i);
                if (btag_values.at(i) < 0){
                    btag_tmp_values = 0;
                }
                Logger::get("btagSF")->debug("btag_tmp_values {}", btag_tmp_values);
                if (pt_values.at(i) >= 20.0 && pt_values.at(i) < 10000.0 &&
                    std::abs(eta_values.at(i)) < 2.5) {
                    // for c jet related uncertainties only scale factors of
                    // c-jets are varied, the rest is nominal/central
                    if (variation.find("cferr") != std::string::npos) {
                        // flavor=4 means c-flavor
                        if (flavors.at(i) == 4) {
                            jet_sf = evaluator->evaluate(
                                {variation, flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        } else if (flavors.at(i) == 0 || flavors.at(i) == 5) {
                            // above line change else with else if (flavors.at(i) == 0 || flavors.at(i) == 5)
                            jet_sf = evaluator->evaluate(
                                {"central", flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        }
                    }
                    // for nominal/central and all other uncertainties c-jets
                    // have a scale factor of 1 (only for central defined in
                    // json file from BTV)
                    else {
                        // change flavors.at(i) != 4 with flavors.at(i) == 0 || flavors.at(i) == 5
                        if (flavors.at(i) == 0 || flavors.at(i) == 5) {
                            jet_sf = evaluator->evaluate(
                                {variation, flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        } else if (flavors.at(i) == 4) {
                            // above line change else with else if (flavors.at(i) == 4)
                            jet_sf = evaluator->evaluate(
                                {"central", flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        }
                    }
                }
                Logger::get("btagSF")->debug("Jet Scale Factor {}", jet_sf);
                sf *= jet_sf;
            }
        };
        Logger::get("btagSF")->debug("Event Scale Factor {}", sf);
        return sf;
    };
    auto df1 = df.Define(
        sf_output, btagSF_lambda,
        {pt, eta, btag_discr, flavor, jet_mask, bjet_mask, jet_veto_mask});
    return df1;
}
ROOT::RDF::RNode
btagSF_run2(ROOT::RDF::RNode df, const std::string &pt, const std::string &eta,
       const std::string &btag_discr, const std::string &flavor,
       const std::string &jet_mask, const std::string &bjet_mask,
       const std::string &jet_veto_mask, const std::string &variation,
       const std::string &sf_output, const std::string &sf_file,
       const std::string &corr_algorithm) {
    Logger::get("btagSF")->debug(
        "Setting up functions for b-tag sf with correctionlib");
    Logger::get("btagSF")->debug("Correction algorithm - Name {}",
                                 corr_algorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(corr_algorithm);

    auto btagSF_lambda = [evaluator,
                          variation](const ROOT::RVec<float> &pt_values,
                                     const ROOT::RVec<float> &eta_values,
                                     const ROOT::RVec<float> &btag_values,
                                     const ROOT::RVec<int> &flavors,
                                     const ROOT::RVec<int> &jet_mask,
                                     const ROOT::RVec<int> &bjet_mask,
                                     const ROOT::RVec<int> &jet_veto_mask) {
        Logger::get("btagSF")->debug("Vatiation - Name {}", variation);
        float sf = 1.;
        for (int i = 0; i < pt_values.size(); i++) {
            Logger::get("btagSF")->debug(
                "jet masks - jet {}, bjet {}, jet veto {}", jet_mask.at(i),
                bjet_mask.at(i), jet_veto_mask.at(i));
            // considering only good jets/bjets, this is needed since jets and
            // bjets might have different cuts depending on the analysis
            if ((jet_mask.at(i) || bjet_mask.at(i)) && jet_veto_mask.at(i)) {
                Logger::get("btagSF")->debug(
                    "SF - pt {}, eta {}, btag value {}, flavor {}",
                    pt_values.at(i), eta_values.at(i), btag_values.at(i),
                    flavors.at(i));
                float jet_sf = 1.;
                // considering only phase space where the scale factors are
                // defined
                float btag_tmp_values = btag_values.at(i);
                if (btag_values.at(i) < 0){
                    btag_tmp_values = 0;
                }
                Logger::get("btagSF")->debug("btag_tmp_values {}", btag_tmp_values);
                if (pt_values.at(i) >= 20.0 && pt_values.at(i) < 10000.0 &&
                    std::abs(eta_values.at(i)) < 2.5) {
                    // for c jet related uncertainties only scale factors of
                    // c-jets are varied, the rest is nominal/central
                    if (variation.find("cferr") != std::string::npos) {
                        // flavor=4 means c-flavor
                        if (flavors.at(i) == 4) {
                            jet_sf = evaluator->evaluate(
                                {variation, flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        } else if (flavors.at(i) == 0 || flavors.at(i) == 5) {
                            // above line change else with else if (flavors.at(i) == 0 || flavors.at(i) == 5)
                            jet_sf = evaluator->evaluate(
                                {"central", flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        }
                    }
                    // for nominal/central and all other uncertainties c-jets
                    // have a scale factor of 1 (only for central defined in
                    // json file from BTV)
                    else {
                        // change flavors.at(i) != 4 with flavors.at(i) == 0 || flavors.at(i) == 5
                        if (flavors.at(i) == 0 || flavors.at(i) == 5) {
                            jet_sf = evaluator->evaluate(
                                {variation, flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        } else if (flavors.at(i) == 4) {
                            // above line change else with else if (flavors.at(i) == 4)
                            jet_sf = evaluator->evaluate(
                                {"central", flavors.at(i),
                                 std::abs(eta_values.at(i)), pt_values.at(i),
                                 btag_tmp_values});
                        }
                    }
                }
                Logger::get("btagSF")->debug("Jet Scale Factor {}", jet_sf);
                sf *= jet_sf;
            }
        };
        Logger::get("btagSF")->debug("Event Scale Factor {}", sf);
        return sf;
    };
    auto df1 = df.Define(
        sf_output, btagSF_lambda,
        {pt, eta, btag_discr, flavor, jet_mask, bjet_mask, jet_veto_mask});
    return df1;
}
/// for PNet WvsQCD SF
ROOT::RDF::RNode pnet_wqcd_sf(ROOT::RDF::RNode df, const std::string &p4, 
                    const std::string &variation, const std::string &id_output,
                    const std::string &sf_file,
                    const std::string &idAlgorithm) {

    Logger::get("PNet WQCD SF")->debug("Setting up functions for pnet sf");
    Logger::get("PNet WQCD SF")->debug("ID - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        id_output,
        [evaluator, variation, sf_file](ROOT::Math::PtEtaPhiMVector &p4) {
            double sf = 1.;
            Logger::get("PNet SF file:")->debug("{}", sf_file);
            // apply sf for fatjet channel    
            const float &fatjet_pt = p4.Pt();
            if (fatjet_pt < 200) {
                // Logger::get("muon High pt corr:")->debug("pt: {}, p: {}", pt, p);
                sf = 1.;
            } else if (fatjet_pt >= 800) {
                sf = 1.;
            } else {
                // for fatjet_pt from 200 to 800
                sf = evaluator->evaluate(
                    {fatjet_pt, variation});
            }
            return sf;
        },
        {p4});
    return df1;
}
///
} // namespace jet

namespace embedding {
/**
 * @brief Function used to readout the embedding selection trigger scalefactors
 *
 * @param df the input dataframe
 * @param pt_1 the pt of the leading generator particle in the event. This
 * corresponds to the leading muon selected by the embedding selection
 * @param eta_1 the eta of the leading generator particle in the event. This
 * corresponds to the leading muon selected by the embedding selection
 * @param pt_2 the pt of the subleading generator particle in the event. This
 * corresponds to the subleading muon selected by the embedding selection
 * @param eta_2 the eta of the subleading generator particle in the event. This
 * corresponds to the subleading muon selected by the embedding selection
 * @param output name of the output column
 * @param sf_file path to the correctionlib file containing the scale factor
 * @param idAlgorithm name of the scale factor in the correctionlib file
 * @return ROOT::RDF::RNode
 */
ROOT::RDF::RNode
selection_trigger(ROOT::RDF::RNode df, const std::string &pt_1,
                  const std::string &eta_1, const std::string &pt_2,
                  const std::string &eta_2, const std::string &output,
                  const std::string &sf_file, const std::string &idAlgorithm) {

    Logger::get("EmbeddingSelectionTriggerSF")
        ->debug("Correction - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        output,
        [evaluator](const float &pt_1, const float &eta_1, const float &pt_2,
                    const float &eta_2) {
            Logger::get("EmbeddingSelectionTriggerSF")
                ->debug(" pt_1 {}, eta_1 {}, pt_2 {}, eta_2 {}", pt_1, eta_1,
                        pt_2, eta_2);
            double sf = 1.;
            sf = evaluator->evaluate(
                {pt_1, std::abs(eta_1), pt_2, std::abs(eta_2)});
            Logger::get("EmbeddingSelectionTriggerSF")->debug("sf {}", sf);
            return sf;
        },
        {pt_1, eta_1, pt_2, eta_2});
    return df1;
}
/**
 * @brief Function used to readout the embedding selection trigger scalefactors.
 *
 * @param df the input dataframe
 * @param pt the pt of the generator particle in the event. This corresponds to
 * one of the muons selected by the embedding selection
 * @param eta the eta of the generator particle in the event. This corresponds
 * to one of the muons selected by the embedding selection
 * @param output the name of the output column
 * @param sf_file the path to the correctionlib file containing the scale factor
 * @param idAlgorithm the name of the scale factor in the correctionlib
 * file
 * @return ROOT::RDF::RNode
 */
ROOT::RDF::RNode selection_id(ROOT::RDF::RNode df, const std::string &pt,
                              const std::string &eta, const std::string &output,
                              const std::string &sf_file,
                              const std::string &idAlgorithm) {

    Logger::get("EmbeddingSelectionIDSF")
        ->debug("Correction - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 =
        df.Define(output,
                  [evaluator](const float &pt, const float &eta) {
                      Logger::get("EmbeddingSelectionIDSF")
                          ->debug(" pt {}, eta {},", pt, eta);
                      double sf = 1.;
                      sf = evaluator->evaluate({pt, std::abs(eta)});
                      Logger::get("EmbeddingSelectionIDSF")->debug("sf {}", sf);
                      return sf;
                  },
                  {pt, eta});
    return df1;
}
/**
 * @brief Function used to readout SFs from the muon scale factor measurements
 *
 * @param df the input dataframe
 * @param pt the pt of the muon
 * @param eta the eta of the muon
 * @param output the name of the output column
 * @param sf_file the path to the correctionlib file containing the scale factor
 * @param correctiontype the type of the correction. Use `emb` for embedding and
 * `mc` for monte carlo
 * @param idAlgorithm the name of the scale factor in the correctionlib
 * file
 * @param extrapolation_factor The extrapolation factor to be used for the scale
 * factor, defaults to 1.
 * @return ROOT::RDF::RNode
 */
ROOT::RDF::RNode muon_sf(ROOT::RDF::RNode df, const std::string &pt,
                         const std::string &eta, const std::string &output,
                         const std::string &sf_file,
                         const std::string correctiontype,
                         const std::string &idAlgorithm,
                         const float &extrapolation_factor = 1.0) {

    Logger::get("EmbeddingMuonSF")->debug("Correction - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        output,
        [evaluator, correctiontype, extrapolation_factor](const float &pt,
                                                          const float &eta) {
            Logger::get("EmbeddingMuonSF")
                ->debug(" pt {}, eta {}, correctiontype {}, extrapolation "
                        "factor {}",
                        pt, eta, correctiontype, extrapolation_factor);
            double sf = 1.;
            sf = extrapolation_factor *
                 evaluator->evaluate({pt, std::abs(eta), correctiontype});
            Logger::get("EmbeddingMuonSF")->debug("sf {}", sf);
            return sf;
        },
        {pt, eta});
    return df1;
}
/**
 * @brief Function used to readout SFs from the electron scale factor
 * measurements
 *
 * @param df the input dataframe
 * @param pt the pt of the electron
 * @param eta the eta of the electron
 * @param output the name of the output column
 * @param sf_file the path to the correctionlib file containing the scale factor
 * @param correctiontype the type of the correction. Use `emb` for embedding and
 * `mc` for monte carlo
 * @param idAlgorithm the name of the scale factor in the correctionlib
 * file
 * @param extrapolation_factor The extrapolation factor to be used for the scale
 * factor, defaults to 1.
 * @return ROOT::RDF::RNode
 */
ROOT::RDF::RNode electron_sf(ROOT::RDF::RNode df, const std::string &pt,
                             const std::string &eta, const std::string &output,
                             const std::string &sf_file,
                             const std::string correctiontype,
                             const std::string &idAlgorithm,
                             const float &extrapolation_factor = 1.0) {

    Logger::get("EmbeddingElectronSF")
        ->debug("Correction - Name {}", idAlgorithm);
    auto evaluator =
        correction::CorrectionSet::from_file(sf_file)->at(idAlgorithm);
    auto df1 = df.Define(
        output,
        [evaluator, correctiontype, extrapolation_factor](const float &pt,
                                                          const float &eta) {
            Logger::get("EmbeddingElectronSF")
                ->debug(" pt {}, eta {}, correctiontype {}, extrapolation "
                        "factor {}",
                        pt, eta, correctiontype, extrapolation_factor);
            double sf = 1.;
            sf = extrapolation_factor *
                 evaluator->evaluate({pt, eta, correctiontype});
            Logger::get("EmbeddingElectronSF")->debug("sf {}", sf);
            return sf;
        },
        {pt, eta});
    return df1;
}
} // namespace embedding
} // namespace scalefactor
#endif /* GUARD_SCALEFACTORS_H */