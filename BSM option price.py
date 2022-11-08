import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()

def euro_vanilla_call(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    print(d1)
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    print(d2)
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call

euro_vanilla_call(100, 120, 1, 0.05, 0.20)


def euro_vanilla_put(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    print(d1)
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    print(d2)
    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    
    return put
euro_vanilla_put(100, 120, 1, 0.05, 0.20)


def call_gap(S, K1, K2, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K2) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    print(d1)
    d2 = (np.log(S / K2) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    print(d2)
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K1 * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call

call_gap(60, 65, 70, 1, 0.10, 0.25)






