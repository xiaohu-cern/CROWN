#ifndef GUARDMETFILTER_H
#define GUARDMETFILTER_H
/// The namespace that contains the metfilter function.
#include "ROOT/RDFHelpers.hxx"
#include "ROOT/RDataFrame.hxx"
#include "../include/basefunctions.hxx"
#include <regex>
#include <string>

namespace metfilter {

/// Function to apply a metfilter to the dataframe
///
/// \param df the dataframe to add the quantity to
/// \param flagname Name of the Filterflag in NanoAOD
/// \param filtername Name of the Filter to be shown in the dataframe report
///
/// \returns a dataframe with the filter applied
ROOT::RDF::RNode ApplyMetFilter(ROOT::RDF::RNode df,
                                const std::string &flagname,
                                const std::string &filtername) {
    return df.Filter([](const bool flag) { return flag; }, {flagname},
                     filtername);
}

} // namespace metfilter

namespace eventsplit {
///////split the Summer24 MC to 2 parts, one for 2024 and the other for 2025.
ROOT::RDF::RNode ApplyEventSplit(ROOT::RDF::RNode df,
                                 const std::string &year,
                                 const std::string &filtername) {
    return df.Filter(
        [year](ULong64_t entry) {
            return (entry % 2) == (year == "2024" ? 0 : 1);
        },
        {"rdfentry_"},
        filtername
    );
}

}
#endif /* GUARDMETFILTER_H */