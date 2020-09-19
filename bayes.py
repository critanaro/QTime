import numpy as np
import scipy.stats as ss; import scipy.special as sp
import csv
import time
import os
from sys import argv

cwd = os.getcwd()

script, dataset, shape, rate, = argv 
SHAPE = float(shape)
RATE = float(rate)
#import matplotlib.pyplot as plt

##The point of the script is to abstract away all of the fucking math 
##And just simply attempt to estimate the true rate at which people 
##Come into coffehouse. The mean and a 95% credible interval are provided;
##The site should display the credible interval as its "guess" of how many
##people are waiting at coffeehouse based on past data

#create empty dictionary that will store values for the next time around
parameter_dict = {}

def convert_time(time_string):
    """
    Input a time in HH:MM:SS form and output 
    a time object representing that
    """
    return time.strptime(time_string, "%H:%M")

#print(convert_time('07:15'))
with open(cwd + '\\' + dataset) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        time = row[0] #Extracting time out of a row of data
        point = int(row[1])
        parameter_dict[time] = [point]
    
def jeffreys_prior(data, a_in = 0.5, b_in = 0):
    """
    input data of chaus lines as an np.array
    and return values of a and b in an uninformative
    gamma prior
    """
    a = sum(data) + a_in
    b = len(data) + b_in
    return a,b


def posterior(y,a,b):
    """
    given data, a, and b from the previous func
    calculate the shape and the rate of the posterior
    """
    shape = a + sum(y)
    rate = b + len(y)
    
    return shape, rate

def credible_interval(shape, rate, alpha):
    """
    given the shape, rate, and alpha, return
    a 1 - alpha% CI for the data
    """
    lb = ss.gamma.ppf(alpha/2, a = shape, scale = 1/rate)
    ub = ss.gamma.ppf(1 - alpha/2, a = shape, scale = 1/rate)
    return lb, ub

def construct_credible_interval(data, alpha = 0.05):
    """
    final function
    """
    a, b = jeffreys_prior(data, a_in = shape, b_in = rate)
    shape, rate = posterior(data, a, b)
    return credible_interval(shape, rate, alpha)

for item in parameter_dict.items():
    a, b = jeffreys_prior(item[1])
    shape, rate = posterior(item[1], a, b)
    item[1].pop()
    item[1].append(shape / rate)
    item[1].append(shape)
    item[1].append(rate)

print(parameter_dict)
    

#np.random.seed(5)
#random_data = np.random.poisson(lam=25, size=100)
#a, b = jeffreys_prior(random_data)
#shape, rate = posterior(random_data, a, b)
#print(credible_interval(shape, rate, 0.05)) 