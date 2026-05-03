import math
import scipy.integrate

class BayesFactor:
    def __init__(self, n, k):
        if not isinstance(n, int) or not isinstance(k, int):
            raise TypeError("n and k must be integers!")
        if n < 0 or k < 0:
            raise ValueError("n and k cannot be negative!")
        if k > n:
            raise ValueError("k cannot be greater than n!")        
        self.n = n
        self.k = k

    def likelihood(self, theta):
        if not isinstance(theta, (int, float)):
            raise TypeError("theta must be numeric!")
        if theta < 0 or theta > 1:
            raise ValueError("theta must be between 0 and 1!")
        return math.comb(self.n, self.k) * (theta ** self.k) * ((1 - theta) ** (self.n - self.k))
    
    def evidence_slab(self):
        result, error = scipy.integrate.quad(self.likelihood, 0, 1)
        return result
    
    def evidence_spike(self):
        a = 0.4999
        b = 0.5001
        c = b - a
        def integrand(theta):
            return (1 / c) * self.likelihood(theta)
        result, error = scipy.integrate.quad(integrand, a, b)
        return result
    
    def bayes_factor(self):
        slab = self.evidence_slab()
        spike = self.evidence_spike()
        if slab == 0:
            raise ZeroDivisionError("slab evidence cannot be zero!")
        return spike / slab
    