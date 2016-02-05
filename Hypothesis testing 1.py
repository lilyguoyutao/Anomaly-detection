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
        return 0
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
hist1=[[3,12,16,2,7,8,7,11,7,8,7,10],
          [10,13,7,4,7,11,11,11,9,5,3,8],
          [10,4 ,9 ,3,5,9,7,10,8,9,10,12],
          [11,6 ,11 ,4,7,6,4,3,7,10,8,6],
          [4, 8 ,10,10,8,5,9,2,9,7,11,8],
          [8, 8 ,9,8,12,9,8,5,5,8,14,6],
          [11,6 ,4,10,9,7,7,6,12,9,14,6],
          [13,9,5,6,8,5,12,7,5,9,8,8],
          [6 ,7 ,6,6,4,5,7,5,6,5,10,6],
          [6 ,8 ,10,7,5,12,12,9,13,12,7,10],
          [7 ,10,10,12,16,11,3,6,7,8,7,10],
          [8 ,18,11,7,6,9,6,7,14,8,10,6],
          [2 ,6 ,6,4,4,13,7,10,7,10,10,6],
          [9 ,6 ,6,9,6,12,13,4,10,10,7,9]]
hist2=[[15,27,25,10,18,18,17,24,18,22,21,19],

          [20,16,12,17,12,19,23,25,17,18,24,22],

          [30,14,20,19,15,18,14,19,19,17,20,25],

          [21,16,23,14,17,14,18,20,21,22,16,23],

          [13,25,27,24,15,20,19,16,29,19,21,21],

          [23,23,19,27,20,20,18,20,18,19,26,21],

          [26,18,13,18,23,14,21,12,22,25,29,16],

          [24,22,12,17,13,15,23,19,18,21,17,21],

          [15,22,14,21,15,19,19,18,16,20,28,19],

          [25,16,22,18,19,18,24,24,22,20,21,15],

          [18,20,23,26,28,21,14,15,17,20,17,23],

          [23,33,28,21,21,18,15,19,29,15,23,16],

          [13,24,22,14,16,26,15,27,19,22,17,14],

          [20,25,17,26,20,23,23,16,19,18,25,22]]
for i in range(len(hist1)):
    for j in range(len(hist1[0])):
        hist1[i][j]=hist1[i][j]*1.0/hist2[i][j]

histdata=hist1
newdata =[0.5555555555555556, 0.3888888888888889, 0.7, 0.35, 0.4166666666666667, 0.4, 0.5652173913043478, 0.5384615384615384, 0.6470588235294118, 0.5714285714285714, 0.55, 0.5151515151515151]

allhistdata = [item for sublist in histdata for item in sublist]

print 'Y='
print newdata
print 'X='
for data in histdata:
    print data

n = len(allhistdata) * 1.0
y = [len([item1 for item1 in allhistdata if item1 > item]) / n for item in newdata]

x = [len([item1 for j, item1 in enumerate(allhistdata) if item1 > item and i != j]) / n for i, item in enumerate(allhistdata)]

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







