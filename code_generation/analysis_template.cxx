#include "ROOT/RDFHelpers.hxx"
#include "ROOT/RDataFrame.hxx"
#include "RooTrace.h"
#include "TStopwatch.h"
#include "src/htxs.hxx"
#include "src/jets.hxx"
#include "src/lorentzvectors.hxx"
#include "src/met.hxx"
#include "src/metfilter.hxx"
#include "src/pairselection.hxx"
#include "src/physicsobjects.hxx"
#include "src/quantities.hxx"
#include "src/reweighting.hxx"
#include "src/scalefactors.hxx"
#include "src/triggers.hxx"
#include "src/utility/Logger.hxx"
#include <ROOT/RLogger.hxx>
#include <TFile.h>
#include <TTree.h>
#include <regex>
#include <string>

static std::vector<std::string> varSet = {"run", "luminosityBlock", "event"};

int main(int argc, char *argv[]) {
    bool verbose = false;
    // ROOT logging
    if (verbose) {
        auto verbosity = ROOT::Experimental::RLogScopedVerbosity(
            ROOT::Detail::RDF::RDFLogChannel(),
            ROOT::Experimental::ELogLevel::kInfo);
        RooTrace::verbose(kTRUE);
        Logger::setLevel(Logger::LogLevel::DEBUG);
    } else {
        RooTrace::verbose(kFALSE);
        Logger::setLevel(Logger::LogLevel::INFO);
        gErrorIgnoreLevel = 6001; // ignore all ROOT errors
    }
    if (argc < 3) {
        Logger::get("main")->critical("Require at least two arguments: N input "
                                      "files and a single output file");
        return 1;
    }
    if (argc > 3) {
        Logger::get("main")->info("Running with {} input files", argc - 2);
    }
    std::vector<std::string> input_files;
    for (int i = 2; i < argc; i++) {
        Logger::get("main")->info("input_file {}: {}", i - 1, argv[i]);
        input_files.push_back(std::string(argv[i]));
    }
    const auto output_path = argv[1];
    Logger::get("main")->info("Output directory: {}", output_path);
    TStopwatch timer;
    timer.Start();

    // file logging
    Logger::enableFileLogging("logs/main.txt");
    // initialize df
    ROOT::RDataFrame df0("Events", input_files);
    Logger::get("main")->info("Starting Setup of Dataframe");

    // auto df_final = df0;

    // {CODE_GENERATION}

    // Logger::get("main")->debug(df_final.Describe()); // <-- starting from
    // ROOT 6.25

    Logger::get("main")->info("Finished Setup");
    Logger::get("main")->info("Runtime for setup (real time: {}, CPU time: {})",
                              timer.RealTime(), timer.CpuTime());
    timer.Continue();

    Logger::get("main")->info("Starting Evaluation");
    ROOT::RDF::RSnapshotOptions dfconfig;
    dfconfig.fLazy = true;
    // {RUN_COMMANDS}
    // Add meta-data
    // clang-format off
    const std::map<std::string, std::vector<std::string>> output_quanties = {OUTPUT_QUANTITIES};
    const std::map<std::string, std::vector<std::string>> variations = {SYSTEMATIC_VARIATIONS};
    // clang-format on
    const std::string analysis = {ANALYSISTAG};
    const std::string era = {ERATAG};
    const std::string sample = {SAMPLETAG};
    const std::string commit_hash = {COMMITHASH};
    bool setup_clean = {CLEANSETUP};
    for (auto const &x : output_quanties) {
        TFile outputfile(x.first.c_str(), "UPDATE");
        TTree quantities_meta = TTree("quantities", "quantities");
        for (auto const &quantity : x.second) {
            quantities_meta.Branch(quantity.c_str(), &setup_clean);
        }
        quantities_meta.Write();
        TTree variations_meta = TTree("variations", "variations");
        for (auto const &variation : variations.at(x.first)) {
            variations_meta.Branch(variation.c_str(), &setup_clean);
        }
        variations_meta.Write();
        TTree conditions_meta = TTree("conditions", "conditions");
        conditions_meta.Branch(analysis.c_str(), &setup_clean);
        conditions_meta.Branch(era.c_str(), &setup_clean);
        conditions_meta.Branch(sample.c_str(), &setup_clean);
        conditions_meta.Write();
        TTree commit_meta = TTree("commit", "commit");
        commit_meta.Branch(commit_hash.c_str(), &setup_clean);
        commit_meta.Fill();
        commit_meta.Write();
        outputfile.Close();
    }

    Logger::get("main")->info("Finished Evaluation");

    const auto nruns = {NRUNS};
    if (nruns != 1) {
        Logger::get("main")->critical(
            "Analysis runs more than one event loop!");
    }

    // as a first testcase, we work on selecting good muons
    Logger::get("main")->info("Overall runtime (real time: {}, CPU time: {})",
                              timer.RealTime(), timer.CpuTime());
}
