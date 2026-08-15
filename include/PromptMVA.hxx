#include <TMVA/Reader.h>
struct ElePromptReader {

    TMVA::Reader reader;

    float pt;
    float eta;
    float pfRelIso03_all;
    float miniPFRelIso_chg;
    float miniRelIsoNeutral;
    float jetNDauCharged;
    float jetPtRelv2;
    float jetBTagDeepFlavB;
    float jetPtRatio;
    float sip3d;
    float log_dxy;
    float log_dz;
    float mvaIso;


    ElePromptReader(const std::string &xml)
        : reader("Silent")
    {
        reader.AddVariable("Electron_pt", &pt);
        reader.AddVariable("Electron_eta", &eta);
        reader.AddVariable("Electron_pfRelIso03_all", &pfRelIso03_all);
        reader.AddVariable("Electron_miniPFRelIso_chg", &miniPFRelIso_chg);
        reader.AddVariable("Electron_miniRelIsoNeutral := Electron_miniPFRelIso_all - Electron_miniPFRelIso_chg", &miniRelIsoNeutral);
        reader.AddVariable("Electron_jetNDauCharged", &jetNDauCharged);
        reader.AddVariable("Electron_jetPtRelv2", &jetPtRelv2);
        reader.AddVariable("Electron_jetBTagDeepFlavB := Electron_jetIdx > -1 ? Jet_btagDeepFlavB[Electron_jetIdx] : 0", &jetBTagDeepFlavB);
        reader.AddVariable("Electron_jetPtRatio := min(1 / (1 + Electron_jetRelIso), 1.5)", &jetPtRatio);
        reader.AddVariable("Electron_sip3d", &sip3d);
        reader.AddVariable("Electron_log_dxy := log(abs(Electron_dxy))", &log_dxy);
        reader.AddVariable("Electron_log_dz  := log(abs(Electron_dz))", &log_dz);
        reader.AddVariable("Electron_mvaIso", &mvaIso);
        
        reader.BookMVA("BDTG",xml);
    }
};


struct MuonPromptReader {

    TMVA::Reader reader;

    float pt;
    float eta;
    float pfRelIso03_all;
    float miniPFRelIso_chg;
    float miniRelIsoNeutral;
    float jetNDauCharged;
    float jetPtRelv2;
    float jetBTagDeepFlavB;
    float jetPtRatio;
    float sip3d;
    float log_dxy;
    float log_dz;
    float segmentComp;



    MuonPromptReader(const std::string &xml)
        : reader("Silent")
    {
        reader.AddVariable("Muon_pt", &pt);
        reader.AddVariable("Muon_eta", &eta);
        reader.AddVariable("Muon_pfRelIso03_all", &pfRelIso03_all);
        reader.AddVariable("Muon_miniPFRelIso_chg", &miniPFRelIso_chg);
        reader.AddVariable("Muon_miniRelIsoNeutral := Muon_miniPFRelIso_all - Muon_miniPFRelIso_chg", &miniRelIsoNeutral);
        reader.AddVariable("Muon_jetNDauCharged", &jetNDauCharged);
        reader.AddVariable("Muon_jetPtRelv2", &jetPtRelv2);
        reader.AddVariable("Muon_jetBTagDeepFlavB := Muon_jetIdx > -1 ? Jet_btagDeepFlavB[Muon_jetIdx] : 0", &jetBTagDeepFlavB);
        reader.AddVariable("Muon_jetPtRatio := min(1 / (1 + Muon_jetRelIso), 1.5)", &jetPtRatio);
        reader.AddVariable("Muon_sip3d", &sip3d);
        reader.AddVariable("Muon_log_dxy := log(abs(Muon_dxy))", &log_dxy);
        reader.AddVariable("Muon_log_dz  := log(abs(Muon_dz))", &log_dz);
        reader.AddVariable("Muon_segmentComp", &segmentComp);
        
        reader.BookMVA("BDTG",xml);
    }
};