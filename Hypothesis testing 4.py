# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:30:03 2014

@author: Feng Chen
"""
import scipy.stats
import json
from scipy.stats import norm

def calc_null_parameters(hist):
    count = len(hist[0]) # Total number of measurements per day 
    observations = [item for sublist in hist for item in sublist]
    mu_0 = average(observations)
    sigma_0 = std(observations)
    return mu_0, sigma_0

def calc_alter_parameters(new, S):
    if len(S) == 0:
        return 0, 0
    else:
        alter_observations = [new[i-1] for i in S] # Set of observations from the distribution related to event under alternative hypothesis 
        mu_1 = average(alter_observations)
        sigma_1 = std(alter_observations)
        return mu_1, sigma_1

def calc_likelihood_ratio(new, V_minus_S, S, mu_0, sigma_0, mu_1, sigma_1):
    log_likelihood_alter = 1
    for i in V_minus_S:
        log_likelihood_alter = log_likelihood_alter + math.log(scipy.stats.norm(mu_0, sigma_0).pdf(new[i-1]))
    for i in S:
        log_likelihood_alter = log_likelihood_alter + math.log(scipy.stats.norm(mu_1, sigma_1).pdf(new[i-1]))

    log_likelihood_null = 1
    for i in V_minus_S + S:
        log_likelihood_null = log_likelihood_null + math.log(scipy.stats.norm(mu_0, sigma_0).pdf(new[i-1]))
    likelihood_ratio = log_likelihood_alter - log_likelihood_null
    return likelihood_ratio
    
def day_process(day_observations, mu_0, sigma_0):

    subset_stat = [] # llr: log likelihood ratio
    count = len(day_observations) # Total number of measurements in the current day 
    for C in range(1, count+1):
        V_minus_S = range(1, C+1)
        S = range(C+1, count+1) 
        mu_1, sigma_1 = calc_alter_parameters(day_observations, S)
        if sigma_1 == 0: # We need at least two observations to estimate sigma_1. If there is only one observation, we set sigma_1 = sigma_0
            sigma_1 = sigma_0
        llr = calc_likelihood_ratio(day_observations, V_minus_S, S, mu_0, sigma_0, mu_1, sigma_1)
        subset_stat.append([llr, S])
    [best_llr, best_subset] = max(subset_stat, key = lambda item: item[0])
    return best_llr, best_subset

def anomalous_subset_detection(hist, new_day, alpha):
    
    # Calcualte the mean and standard deviation of normal bload pressure
    mu_0, sigma_0 = calc_null_parameters(hist)
    
    """
    Step 1: Identify the best subset S*
    """
    [best_llr, best_subset] = day_process(new_day, mu_0, sigma_0)
    
    hist_day_max_llrs = []
    """
    Step 2: Caldualte empirical p-value of the best subset S*
    """
    for hist_day in hist:
        [best_hist_day_llr, best_hist_day_subset] = day_process(hist_day, mu_0, sigma_0)
        hist_day_max_llrs.append(best_hist_day_llr)
    
    empirical_p_value = len([item for item in hist_day_max_llrs if item > best_llr]) / (1.0 * len(hist_day_max_llrs))
    
    if empirical_p_value <= alpha:
        return empirical_p_value, best_subset
    else:
        return None, None
    
def anomalous_point_detection(hist, new_day, alpha):

    # Calcualte the mean and standard deviation of normal bload pressure
    mu_0, sigma_0 = calc_null_parameters(hist)

    # Calculate the p-value of individual observations in new_day
    p_values = []
    for idx, observation in enumerate(new_day):
        p_value = 1 - norm.cdf((observation - mu_0)/sigma_0)
        p_values.append([idx, p_value])
        
    signfciant_observations = [item for item in p_values if item[1] <= alpha]

    return signfciant_observations 
    
    
def main(): 
    hist = [[117.0789, 39.8329, 60.7431, 103.4965, 71.9689, 96.6234, 87.0127, 77.3483, 81.4634, 107.7693, 91.5502, 96.2633],
            [86.9670, 129.5889, 86.3238, 85.0010, 108.8420, 41.1513, 101.5214, 97.9736, 42.3581, 35.0623, 98.2947, 87.2719],
            [85.8275, 91.7513, 98.0471, 83.9016, 52.7634, 38.6144, 95.7231, 101.5145, 107.9072, 93.8265, 86.7038, 66.9055],
            [70.3166, 105.0012, 91.5412, 103.2225, 84.5108, 86.5987, 102.9578, 64.7011, 72.4182, 57.0372, 102.6191, 75.6457],
            [84.3837, 51.7167, 106.6527, 96.8917, 46.0231, 66.0304, 82.3612, 75.5786, 60.9230, 79.8989, 91.4643, 82.5022], 
            [89.6469, 73.1993, 105.1215, 92.0040, 105.4100, 93.2298, 82.0560, 87.7405, 79.9211, 88.2881, 69.3171, 114.5792], 
            [93.5278, 79.4387, 71.9818, 110.0050, 102.2343, 98.5396, 105.1555, 79.1627, 56.4271, 99.9547, 48.8925, 67.7837],
            [77.5438, 93.4543, 90.1411, 103.5958, 85.0232, 102.1547, 42.5269, 91.0364, 84.5828, 79.5391, 122.1719, 100.6934], 
            [80.2709, 51.5960, 66.1124, 89.7953, 83.5833, 71.1768, 74.9083, 92.9986, 73.7867, 116.5260, 72.9094, 91.1725],
            [125.4738, 94.4327, 58.5642, 71.1928, 35.2743, 93.9876, 59.5881, 66.4008, 128.5556, 75.3813, 87.0672, 80.3228]
            ]
    new_day = [105.7195, 133.4892, 104.1880, 78.6846, 93.5725, 64.2803, 122.5573, 103.8141, 135.7469, 102.4825, 126.3990, 108.8341]
    
    alpha = 0.05 # confidence interval
    empirical_p_value, best_subset = anomalous_subset_detection(hist, new_day, alpha)
    
    print '\n**************************************'
    print 'Strategy 1: Anomalous Subset Detection at the confidence interval \alpha = 0.05'
    if empirical_p_value != None:
        print 'The signficant subset and empirical p-value are: '
        print best_subset, empirical_p_value
    else:
        print 'No signficant subset is detected'
    print '**************************************\n'

    [empirical_p_value, best_subset] = anomalous_subset_detection(hist, new_day, alpha)    
    signfciant_observations = anomalous_point_detection(hist, new_day, alpha)
    
    print '\n**************************************'
    print 'Strategy 2: Anomalous Points Detection at the confidence interval \alpha = 0.05'
    if len(signfciant_observations) > 0:
        print 'The signficant points and empirical p-values are: '
        for [idx, p_value] in signfciant_observations:
            print idx, p_value
    print '**************************************\n'
    
if __name__ == '__main__':
    main()
    
    pass

#sum_measurements = 0
#for day in range(10):
#    sum_measurements += sum(hist[day])
#mu = sum_measurements / (10.0 * count)

#print hist
    