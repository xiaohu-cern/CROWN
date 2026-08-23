#ifndef GUARDJETS_H
#define GUARDJETS_H

namespace jet {
ROOT::RDF::RNode
VetoOverlappingJets(ROOT::RDF::RNode df, const std::string &output_col,
                    const std::string &jet_eta, const std::string &jet_phi,
                    const std::string &muon_eta, const std::string &muon_phi, const std::string &muon_mask,
                    const float &deltaRmin);
ROOT::RDF::RNode
VetoOverlappingJets(ROOT::RDF::RNode df, const std::string &output_col,
                    const std::string &jet_eta, const std::string &jet_phi,
                    const std::string &p4_1, const std::string &p4_2,
                    const float &deltaRmin);
ROOT::RDF::RNode
VetoOverlappingJets(ROOT::RDF::RNode df, const std::string &output_col,
                    const std::string &jet_eta, const std::string &jet_phi,
                    const std::string &p4_1, const float &deltaRmin);
ROOT::RDF::RNode VetoOverlappingJetsIsoLepOnly(ROOT::RDF::RNode df,
                                               const std::string &output_col,
                                               const std::string &jet_eta,
                                               const std::string &jet_phi,
                                               const std::string &p4_1,
                                               const std::string &lep_is_iso,
                                               const float &deltaRmin);
ROOT::RDF::RNode OrderJetsByPt(ROOT::RDF::RNode df,
                               const std::string &output_col,
                               const std::string &jet_pt,
                               const std::string &jetmask_name);
} // end namespace jet

namespace physicsobject {
namespace jet {

ROOT::RDF::RNode CutID(ROOT::RDF::RNode df, const std::string &maskname,
                       const std::string &nameID, const int &idxID);
ROOT::RDF::RNode CutUCharID(ROOT::RDF::RNode df, const std::string &maskname,
                       const std::string &nameID, const unsigned char &idxID);
ROOT::RDF::RNode CutBoolID(ROOT::RDF::RNode df, const std::string &maskname, const std::string &nameID);

ROOT::RDF::RNode CutPUID(ROOT::RDF::RNode df, const std::string &maskname,
                         const std::string &nameID, const std::string &jet_pt,
                         const int &idxID, const float &jet_pt_cut);
ROOT::RDF::RNode
JetVetoMap(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi,
                const std::string &jet_ID,
                const std::string &jet_chEmEF, const std::string &jet_neEmEF,
                const std::string &jet_neHEF,
                const std::string &jet_veto_map, const std::string &jet_veto_tag);
ROOT::RDF::RNode
JetVetoMap_v15(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi,
                const std::string &jetTightLepVetoID,
                const std::string &jet_chEmEF, const std::string &jet_neEmEF,
                const std::string &jet_veto_map, const std::string &jet_veto_tag);
ROOT::RDF::RNode
FatJetVetoMap(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi,
                const std::string &jet_veto_map, const std::string &jet_veto_tag);
ROOT::RDF::RNode 
Cal_JetTightID_v12(ROOT::RDF::RNode df, const std::string passJetIdTight, const std::string jet_eta,
              const std::string jet_neEmEF, const std::string jet_neHEF, const std::string jet_ID);
ROOT::RDF::RNode 
Cal_JetTightID_v15(ROOT::RDF::RNode df, const std::string passJetIdTight, const std::string jet_eta,
              const std::string jet_neEmEF, const std::string jet_neHEF, const std::string jet_chEmEF, const std::string jet_chHEF,
              const std::string jet_chMultiplicity, const std::string jet_neMultiplicity);
ROOT::RDF::RNode 
Cal_JetTightLepVetoID(ROOT::RDF::RNode df, const std::string passJetIdTightLepVeto, const std::string jet_eta,
              const std::string passJetIdTight, const std::string jet_muEF, const std::string jet_chEmEF);
ROOT::RDF::RNode
JetPtCorrection(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi, const std::string &jet_area,
                const std::string &jet_rawFactor, const std::string &jet_ID,
                const std::string &gen_jet_pt, const std::string &gen_jet_eta,
                const std::string &gen_jet_phi, const std::string &rho,
                const std::string &jet_chEmEF, const std::string &jet_neEmEF,
                const std::string &jet_neHEF, const std::string &jet_muEF,
                bool reapplyJES,
                const std::vector<std::string> &jes_shift_sources,
                const int &jes_shift, const std::string &jer_shift,
                const std::string &jec_file, const std::string &jer_tag,
                const std::string &jes_tag, const std::string &jec_algo,
                const std::string &jet_veto_map, const std::string &jet_veto_tag);
ROOT::RDF::RNode
JetPtCorrection_v15(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi, const std::string &jet_area,
                const std::string &jet_rawFactor, const std::string &jetTightLepVetoID,
                const std::string &gen_jet_pt, const std::string &gen_jet_eta,
                const std::string &gen_jet_phi, const std::string &rho,
                const std::string &jet_chEmEF, const std::string &jet_neEmEF, const std::string &lumi, const std::string &event,
                bool reapplyJES,
                const std::vector<std::string> &jes_shift_sources,
                const int &jes_shift, const std::string &jer_shift,
                const std::string &jec_file1, const std::string &jer_tag,
                const std::string &jes_tag, const std::string &jec_algo,
                const std::string &jet_veto_map, const std::string &jet_veto_tag, const std::string &year_id, bool include_phi);
ROOT::RDF::RNode
JetPtCorrection_v15_data(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi, const std::string &jet_area,
                const std::string &jet_rawFactor, const std::string &jetTightLepVetoID,
                const std::string &jet_chEmEF, const std::string &jet_neEmEF, const std::string &rho, const std::string &data_run,
                bool reapplyJES,
                const std::string &jec_file1,
                const std::string &jes_tag, const std::string &jec_algo,
                const std::string &jet_veto_map, const std::string &jet_veto_tag, const std::string &year_id, bool include_phi);
ROOT::RDF::RNode
FatJetPtCorrection(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi, const std::string &jet_area,
                const std::string &jet_rawFactor, const std::string &jet_ID,
                const std::string &gen_jet_pt, const std::string &gen_jet_eta,
                const std::string &gen_jet_phi, const std::string &rho,
                bool reapplyJES,
                const std::vector<std::string> &jes_shift_sources,
                const int &jes_shift, const std::string &jer_shift,
                const std::string &jec_file, const std::string &jer_tag,
                const std::string &jes_tag, const std::string &jec_algo,
                const std::string &jet_veto_map, const std::string &jet_veto_tag);
ROOT::RDF::RNode
FatJetPtCorrection_v15(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi, const std::string &jet_area,
                const std::string &jet_rawFactor,
                const std::string &gen_jet_pt, const std::string &gen_jet_eta,
                const std::string &gen_jet_phi, const std::string &rho, const std::string &lumi, const std::string &event,
                bool reapplyJES,
                const std::vector<std::string> &jes_shift_sources,
                const int &jes_shift, const std::string &jer_shift,
                const std::string &jec_file1, const std::string &jer_tag,
                const std::string &jes_tag, const std::string &jec_algo,
                const std::string &jet_veto_map, const std::string &jet_veto_tag, const std::string &year_id, bool include_phi);
ROOT::RDF::RNode
FatJetPtCorrection_v15_data(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi, const std::string &jet_area,
                const std::string &jet_rawFactor, const std::string &rho, const std::string &data_run,
                bool reapplyJES,
                const std::string &jec_file1,
                const std::string &jes_tag, const std::string &jec_algo,
                const std::string &jet_veto_map, const std::string &jet_veto_tag, const std::string &year_id, bool include_phi);
ROOT::RDF::RNode
JetPtCorrection_run2(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                const std::string &jet_pt, const std::string &jet_eta,
                const std::string &jet_phi, const std::string &jet_area,
                const std::string &jet_rawFactor, const std::string &jet_ID,
                const std::string &gen_jet_pt, const std::string &gen_jet_eta,
                const std::string &gen_jet_phi, const std::string &rho,
                bool reapplyJES,
                const std::vector<std::string> &jes_shift_sources,
                const int &jes_shift, const std::string &jer_shift,
                const std::string &jec_file, const std::string &jer_tag,
                const std::string &jes_tag, const std::string &jec_algo,
                const std::string &jet_veto_map, const std::string &jet_veto_tag);
ROOT::RDF::RNode
JetPtCorrection_data(ROOT::RDF::RNode df, const std::string &corrected_jet_pt,
                     const std::string &jet_pt, const std::string &jet_eta,
                     const std::string &jet_area,
                     const std::string &jet_rawFactor, const std::string &rho,
                     const std::string &jec_file, const std::string &jes_tag,
                     const std::string &jec_algo);
ROOT::RDF::RNode CutRawID(ROOT::RDF::RNode df, const std::string &quantity,
                          const std::string &maskname,
                          const float &idThreshold);
ROOT::RDF::RNode AntiCutRawID(ROOT::RDF::RNode df, const std::string &quantity,
                              const std::string &maskname,
                              const float &idThreshold);
} // end namespace jet
} // end namespace physicsobject

namespace quantities {
namespace jet {
ROOT::RDF::RNode NumberOfJets(ROOT::RDF::RNode df,
                              const std::string &outputname,
                              const std::string &jetcollection);
ROOT::RDF::RNode btagValue(ROOT::RDF::RNode df, const std::string &outputname,
                           const std::string &btagcolumn,
                           const std::string &jetcollection,
                           const int &position);
ROOT::RDF::RNode flavor(ROOT::RDF::RNode df, const std::string &outputname,
                        const std::string &flavorcolumn,
                        const std::string &jetcollection, const int &position);
ROOT::RDF::RNode buildSubJet(ROOT::RDF::RNode df, const std::string &subjet_pt,
                             const std::string &subjet_eta, const std::string &subjet_phi,
                             const std::string &subjet_mass, const std::string &fatjet_collection,
                             const std::string &fatjet_subjetId, const int &position, 
                             const std::string &subjet_p4);
} // end namespace jet
} // end namespace quantities
#endif /* GUARDJETS_H */
