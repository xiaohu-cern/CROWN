#include <boost/math/special_functions/erf.hpp>
#include <cstdint>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include "TRandom3.h"

namespace KIT{
class SeedSequence {
public:
    explicit SeedSequence(std::initializer_list<uint32_t> seeds)
        : m_seeds(seeds) {}

    template <typename Iter>
    void generate(Iter begin, Iter end) const {
        const size_t n = std::distance(begin, end);
	if (n == 0) return;

	const uint32_t mult = 0x9e3779b9;
	const uint32_t mix_const = 0x85ebca6b;

	std::vector<uint32_t> buffer(n, 0x8b8b8b8b);

	size_t s = m_seeds.size();
	size_t t = (n >= s) ? n - s : 0;

        size_t i = 0;

	for(; i < std::min(n, s); ++i) {
            buffer[i] = buffer[i] ^ (m_seeds[i] + mult * i);
	}
	for(; i < n; ++i) {
            buffer[i] = buffer[i] ^ (mult * i);
        }

	for (size_t k = 0; k < n; ++k) {
            uint32_t z = buffer[(k + n - 1) % n] ^ (buffer[k] >> 27);
	    buffer[k] = (z * mix_const) ^ (buffer[k] << 13);
        }

	std::copy(buffer.begin(), buffer.end(), begin);
    }

private:
    std::vector<uint32_t> m_seeds;
};

struct CrystalBall{
    double pi=3.14159;
    double sqrtPiOver2=sqrt(pi/2.0);
    double sqrt2=sqrt(2.0);
    double m;
    double s;
    double a;
    double n;
    double B;
    double C;
    double D;
    double N;
    double NA;
    double Ns;
    double NC;
    double F;
    double G;
    double k;
    double cdfMa;
    double cdfPa;
CrystalBall():m(0),s(1),a(10),n(10){
    init();
}
CrystalBall(double mean, double sigma, double alpha, double n)
    :m(mean),s(sigma),a(alpha),n(n){
    init();
}
void init(){
    double fa = fabs(a);
    double ex = exp(-fa*fa/2);
    double A  = pow(n/fa, n) * ex;
    double C1 = n/fa/(n-1) * ex; 
    double D1 = 2 * sqrtPiOver2 * erf(fa/sqrt2);
    B = n/fa-fa;
    C = (D1+2*C1)/C1;   
    D = (D1+2*C1)/2;   
    N = 1.0/s/(D1+2*C1); 
    k = 1.0/(n-1);  
    NA = N*A;       
    Ns = N*s;       
    NC = Ns*C1;     
    F = 1-fa*fa/n; 
    G = s*n/fa;    
    cdfMa = cdf(m-a*s);
    cdfPa = cdf(m+a*s);
}
double pdf(double x) const{ 
    double d=(x-m)/s;
    if(d<-a) return NA*pow(B-d, -n);
    if(d>a) return NA*pow(B+d, -n);
    return N*exp(-d*d/2);
}
double pdf(double x, double ks, double dm) const{ 
    double d=(x-m-dm)/(s*ks);
    if(d<-a) return NA/ks*pow(B-d, -n);
    if(d>a) return NA/ks*pow(B+d, -n);
    return N/ks*exp(-d*d/2);

}
double cdf(double x) const{
    double d = (x-m)/s;
    if(d<-a) return NC / pow(F-s*d/G, n-1);
    if(d>a) return NC * (C - pow(F+s*d/G, 1-n) );
    return Ns * (D - sqrtPiOver2 * erf(-d/sqrt2));
}
double invcdf(double u) const{
    if(u<cdfMa) return m + G*(F - pow(NC/u, k));
    if(u>cdfPa) return m - G*(F - pow(C-u/NC, -k) );
    return m - sqrt2 * s * boost::math::erf_inv((D - u/Ns )/sqrtPiOver2);
}
};

struct Gaussian {
    double pi = 3.141592653589793;
    double sqrt2 = std::sqrt(2.0);
    double sqrtPiOver2 = std::sqrt(pi / 2.0);

    double m;   // mean
    double s;   // sigma
    double N;   // normalization

    Gaussian(): m(0.0), s(1.0) {
        init();
    }

    Gaussian(double mean, double sigma): m(mean), s(sigma) {
        init();
    }

    void init() {
        N = 1.0 / (s * std::sqrt(2.0 * pi));
    }

    // PDF
    double pdf(double x) const {
        double d = (x - m) / s;
        return N * std::exp(-0.5 * d * d);
    }

    // CDF
    double cdf(double x) const {
        double d = (x - m) / (s * sqrt2);
        return 0.5 * (1.0 + std::erf(d));
    }

    // inverse CDF
    double invcdf(double u) const {
        return m + s * sqrt2 * boost::math::erf_inv(2.0 * u - 1.0);
    }
};

double get_random_nb(double phi, int evtNumber, int lumiNumber) {
    int64_t phi_seed = static_cast<int64_t>((phi / M_PI) * ((1LL << 31) - 1)) & 0xFFF;
    SeedSequence seq{static_cast<uint32_t>(evtNumber), static_cast<uint32_t>(lumiNumber), static_cast<uint32_t>(phi_seed)};
    uint32_t seed;
    seq.generate(&seed, &seed + 1);
    TRandom3 rnd(seed);
    double rndm = rnd.Rndm();
    return rndm;
}

double get_rndm_gaus(double eta, double phi, float nL, int evtNumber, int lumiNumber, double mean, double sigma) {
    // instantiate CB and get random number following the CB
    Gaussian gaus(mean, sigma);
    int64_t phi_seed = static_cast<int64_t>((phi / M_PI) * ((1LL << 31) - 1)) & 0xFFF;
    SeedSequence seq{static_cast<uint32_t>(evtNumber), static_cast<uint32_t>(lumiNumber), static_cast<uint32_t>(phi_seed)};
    uint32_t seed;
    seq.generate(&seed, &seed + 1);

    TRandom3 rnd(seed);
    double rndm = rnd.Rndm();
    return gaus.invcdf(rndm);
}

double get_rndm(double eta, double phi, float nL, int evtNumber, int lumiNumber, double mean, double sigma, double n, double alpha) {
    // instantiate CB and get random number following the CB
    CrystalBall cb(mean, sigma, alpha, n);
    int64_t phi_seed = static_cast<int64_t>((phi / M_PI) * ((1LL << 31) - 1)) & 0xFFF;
    SeedSequence seq{static_cast<uint32_t>(evtNumber), static_cast<uint32_t>(lumiNumber), static_cast<uint32_t>(phi_seed)};
    uint32_t seed;
    seq.generate(&seed, &seed + 1);

    TRandom3 rnd(seed);
    double rndm = rnd.Rndm();
    return cb.invcdf(rndm);
}


double get_std(double pt, double eta, float nL, double param_0, double param_1, double param_2) {

    // calculate value and return max(0, val)
    double sigma = param_0 + param_1 * pt + param_2 * pt*pt;
    if (sigma < 0) sigma = 0;
    return sigma; 
}


double get_k(double eta, std::string var, double k_data, double k_mc) {
    // calculate residual smearing factor
    // return 0 if smearing in MC already larger than in data
    double k = 0;
    if (k_mc < k_data) k = sqrt(k_data*k_data - k_mc*k_mc);
    return k;
}
}