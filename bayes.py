import numpy as np
import scipy.stats as ss; import scipy.special as sp
import matplotlib.pyplot as plt

##The point of the script is to abstract away all of the fucking math 
##And just simply attempt to estimate the true rate at which people 
##Come into coffehouse. The mean and a 95% credible interval are provided;
##The site should display the credible interval as its "guess" of how many
##people are waiting at coffeehouse based on past data

def jeffreys_prior(data):
    """
    input data of chaus lines as an np.array
    and return values of a and b in an uninformative
    gamma prior
    """
    a = sum(data) + 0.5
    b = len(data)
    return a,b


def posterior(y,a,b):
    """
    given data, a, and b from the previous func
    calculate the shape and the rate of the posterior
    """
    shape = a + y.sum()
    rate = b + y.size
    
    return shape, rate

def credible_interval(shape, rate, alpha):
    """
    given the shape, rate, and alpha, return
    a 1 - alpha% CI for the data
    """
    lb = ss.gamma.ppf(alpha/2, a = shape, scale = 1/rate)
    ub = ss.gamma.ppf(1 - alpha/2, a = shape, scale = 1/rate)
    return (lb, ub)


np.random.seed(5)
random_data = np.random.poisson(lam=25, size=100)
a, b = jeffreys_prior(random_data)
shape, rate = posterior(random_data, a, b)
print(credible_interval(shape, rate, 0.05))