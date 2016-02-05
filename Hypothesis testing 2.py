# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:01:02 2015

@author: Feng Chen
"""

import numpy as np
import math
class prettyfloat(float):
    def __repr__(self):
        return "%0.2f" % self

def kl(a, b):
    if a == 0:
        return (1 - a) * math.log((1 - a) / (1 - b))
    elif a == 1:
        return a * math.log(a / b)
    else:
        return a * math.log(a / b) + (1 - a) * math.log((1 - a) / (1 - b))
    
def phi(data, S):
    ns = len(S) * 1.0
    nalphas = len([data[i] for i in S if data[i] <= 0.05]) * 1.0
    return ns * kl(nalphas / ns, 0.05)

def find_best_llr(data):
    llrs = []
    for i in range(len(data)):
        S = range(i, len(data))
        llr = phi(data, S)
        llrs.append([S, llr])
    best_S, best_llr = max(llrs, key = lambda item: item[1])
    return best_llr, best_S, llrs

histdata=[[88, 94, 91, 89, 86, 93, 89, 81, 86, 86, 92, 91],
              
              [88, 89, 92, 87, 85, 91, 88, 85, 92, 91, 87, 89],
              
              [89, 89, 89, 85, 90, 94, 92, 90, 82, 89, 91, 92],
              
              [91, 92, 90, 89, 91, 87, 91, 90, 83, 87, 91, 93],
              
              [89, 91, 92, 88, 91, 92, 92, 90, 87, 91, 93, 87],
              
              [93, 91, 89, 95, 89, 86, 90, 93, 90, 87, 91, 91],
              
              [94, 92, 88, 94, 92, 95, 91, 91, 89, 95, 91, 86],
              
              [90, 89, 93, 88, 86, 87, 89, 91, 93, 89, 87, 87],
              
              [90, 90, 88, 87, 91, 88, 89, 86, 86, 90, 93, 92],
              
              [93, 89, 95, 93, 90, 86, 93, 91, 91, 92, 90, 91],
              
              [84, 89, 86, 90, 88, 88, 88, 90, 89, 92, 92, 97],
              
              [88, 91, 88, 91, 88, 91, 85, 86, 92, 84, 85, 91],
              
              [92, 88, 89, 92, 93, 88, 93, 93, 89, 89, 91, 85],
              
              [87, 90 ,85, 92 ,90, 87, 92, 91, 87, 87, 88 ,89]]
newdata =  [89, 102, 88, 93, 92, 94, 88, 86, 91, 99, 100, 89]

allhistdata = [item for sublist in histdata for item in sublist]

print 'Y='
print newdata
print 'X='
for data in histdata:
    print data

n = len(allhistdata) * 1.0
y = [len([item1 for item1 in allhistdata if item1 < item]) / n for item in newdata]

x = [len([item1 for j, item1 in enumerate(allhistdata) if item1 < item and i != j]) / n for i, item in enumerate(allhistdata)]

n = 12
x = [x[i:i+n] for i in range(0, len(x), n)] 


print 'Y='
print map(prettyfloat, y)

print 'X='
for data in x:
    print map(prettyfloat, data)


print 'new data LLRnew'
best_llr, best_S, llrs = find_best_llr(y)
for S, llr in llrs:
    print S, map(prettyfloat, [llr])

hist_llrs = []
for t in range(len(x)):
    t_best_llr, _, _ = find_best_llr(x[t])
    hist_llrs.append(t_best_llr)

print '\nhistory data_LLR', map(prettyfloat, hist_llrs)
pvalue = len([llr for llr in hist_llrs if llr >= best_llr]) / (len(hist_llrs) * 1.0)

print '\nbest subset=',best_S
print 'Best_LLRnew=', best_llr
print 'p-value=',pvalue







