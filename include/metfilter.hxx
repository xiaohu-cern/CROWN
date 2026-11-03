#ifndef GUARDMETFILTER_H
#define GUARDMETFILTER_H

namespace metfilter {

ROOT::RDF::RNode ApplyMetFilter(ROOT::RDF::RNode df,
                                const std::string &flagname,
                                const std::string &filtername);
} // namespace metfilter

namespace eventsplit {
///////split the Summer24 MC to 2 parts, one for 2024 and the other for 2025.
ROOT::RDF::RNode ApplyEventSplit(ROOT::RDF::RNode df,
                                 const std::string &year,
                                 const std::string &filtername);
}

#endif /* GUARDMETFILTER_H */