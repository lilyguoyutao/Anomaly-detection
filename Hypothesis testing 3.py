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
    total=[[0,1,3,4],[1,2,4,5],[3,4,6,7],[4,5,7,8],[0,1,2,3,4,5],[3,4,5,6,7,8],[0,1,3,4,6,7],[1,2,4,5,7,8],[0,1,2,3,4,5,6,7,8]]
    for i in range(len(total)):
        S=total[i]
        llr = phi(data, S)
        llrs.append([S, llr])
    best_S, best_llr = max(llrs, key = lambda item: item[1])
    return best_llr, best_S, llrs
histdata=[[64, 62, 45, 77, 42, 61, 78, 61, 68],
         [57, 63, 46, 79, 42, 53, 77, 57, 69],
         [73, 67, 56, 75, 42, 57, 78, 59, 73],
         [70, 64, 47, 73, 48, 61, 82, 55, 73],
         [67, 61, 43, 77, 43, 60, 75, 65, 72],
[72, 62, 43, 78, 40, 60, 83, 57, 69],
[75, 68, 54, 72, 47, 62, 82, 63, 68],
[67, 65, 53, 74, 46, 60, 79, 58, 69],
[61, 68, 50, 77, 44, 55, 77, 58, 75],
[71, 62, 45, 73, 48, 56, 80, 58, 64],
[68, 67, 51, 80, 45, 62, 78, 62, 66],
[66, 66, 55, 72, 45, 60, 80, 60, 69],
[67, 64, 48, 71, 45, 65, 82, 57, 73],
[69, 66, 49, 76, 53, 57, 75, 58, 68],
[65, 66, 51, 77, 45, 54, 78, 61, 65],
[67, 64, 51, 75, 44, 63, 84, 59, 69],
[69, 68, 47, 78, 46, 59, 79, 57, 68],
[67, 64, 55, 77, 45, 61, 82, 56, 73],
[69, 67, 50, 71, 45, 60, 86, 63, 72],
[72, 69, 52, 66, 40, 64, 82, 57, 68],
[73, 68, 51, 76, 50, 57, 83, 64, 66],
[74, 65, 43, 75, 45, 53, 84, 60, 70],
[70, 61, 45, 70, 49, 63, 79, 53, 68],
[71, 68, 51, 74, 39, 55, 83, 62, 62],
[69, 64, 50, 76, 44, 59, 77, 62, 68],
[69, 66, 47, 69, 46, 57, 79, 58, 72],
[76, 55, 50, 77, 45, 61, 81, 64, 69],
[74, 59, 52, 80, 46, 61, 80, 59, 69],
[69, 59, 49, 75, 43, 58, 81, 54, 73],
[74, 67, 45, 74, 45, 67, 81, 62, 70],
[69, 59, 49, 70, 46, 61, 84, 56, 73],
[71, 61, 49, 69, 44, 56, 79, 61, 69],
[68, 59, 49, 73, 45, 57, 82, 60, 76],
[62, 65, 49, 74, 41, 61, 80, 62, 68],
[70, 67, 49, 74, 48, 62, 75, 60, 76],
[69, 64, 46, 74, 46, 64, 77, 63, 66],
[70, 68, 45, 74, 45, 59, 76, 57, 66],
[65, 63, 45, 75, 48, 60, 76, 62, 69],
[69, 65, 57, 68, 46, 59, 81, 59, 73],
[69, 58, 51, 77, 44, 57, 80, 56, 66],
[64, 62, 54, 78, 48, 61, 78, 61, 72],
[72, 62, 46, 76, 38, 63, 89, 59, 66],
[70, 68, 51, 73, 45, 60, 78, 58, 68],
[69, 61, 45, 73, 46, 54, 80, 58, 65],
[73, 65, 45, 74, 44, 66, 82, 60, 68],
[69, 67, 54, 73, 41, 59, 86, 63, 70],
[73, 62, 45, 73, 46, 55, 78, 61, 69],
[67, 64, 49, 81, 45, 63, 76, 59, 75],
[69, 69, 50, 75, 47, 61, 78, 61, 71],
[72, 60, 54, 76, 44, 56, 72, 61, 73],
[69, 65, 47, 74, 48, 63, 78, 57, 68],
[70, 67, 48, 69, 46, 57, 80, 57, 67],
[71, 66, 48, 81, 50, 55, 80, 58, 68],
[71, 69, 52, 69, 45, 61, 80, 57, 74],
[74, 69, 50, 75, 43, 57, 86, 58, 70],
[70, 63, 52, 77, 43, 59, 77, 63, 71],
[76, 61, 52, 79, 44, 59, 81, 62, 73],
[73, 67, 47, 70, 44, 61, 87, 63, 73],
[74, 67, 55, 76, 49, 64, 75, 61, 71],
[71, 65, 41, 74, 41, 57, 81, 63, 68],
[73, 66, 51, 75, 46, 60, 81, 62, 69],
[69, 63, 53, 73, 45, 61, 80, 60, 75],
[67, 66, 47, 73, 48, 59, 82, 64, 73],
[67, 66, 47, 73, 47, 58, 79, 56, 73],
[74, 64, 46, 66, 47, 64, 85, 60, 73],
[68, 64, 50, 77, 44, 61, 81, 63, 68],
[68, 64, 54, 77, 47, 59, 77, 59, 71],
[67, 66, 47, 68, 41, 59, 81, 60, 67],
[67, 66, 48, 76, 45, 62, 78, 59, 67],
[71, 64, 50, 71, 46, 60, 74, 54, 76],
[65, 65, 48, 78, 45, 62, 78, 61, 66],
[69, 65, 49, 77, 45, 65, 84, 62, 67],
[73, 66, 54, 79, 47, 64, 77, 68, 65],
[67, 69, 45, 78, 46, 59, 76, 69, 69],
[66, 68, 47, 75, 45, 59, 77, 61, 65],
[77, 69, 49, 75, 39, 58, 79, 64, 71],
[77, 59, 51, 77, 45, 62, 85, 63, 73],
[69, 59, 48, 76, 45, 55, 77, 61, 69],
[67, 62, 49, 76, 39, 60, 82, 58, 69],
[69, 68, 49, 70, 51, 59, 78, 61, 73],
[74, 63, 54, 76, 36, 59, 81, 64, 75],
[67, 67, 51, 75, 41, 60, 80, 58, 73],
[73, 66, 46, 74, 46, 60, 76, 56, 61],
[67, 66, 50, 74, 44, 62, 78, 55, 66],
[73, 66, 52, 70, 45, 57, 80, 58, 70],
[64, 60, 50, 81, 42, 58, 81, 63, 67],
[73, 62, 51, 77, 40, 58, 75, 59, 63],
[72, 69, 52, 72, 42, 58, 82, 56, 74],
[66, 62, 49, 70, 46, 53, 83, 67, 74],
[70, 62, 50, 76, 48, 62, 79, 57, 69],
[67, 69, 50, 75, 45, 61, 80, 57, 69],
[71, 60, 52, 70, 44, 60, 81, 59, 70],
[74, 68, 46, 74, 40, 55, 75, 60, 74],
[69, 64, 51, 73, 48, 59, 81, 65, 72],
[71, 66, 47, 74, 43, 56, 81, 61, 70],
[70, 66, 48, 75, 43, 53, 80, 61, 66],
[67, 63, 48, 78, 50, 55, 82, 57, 65],
[75, 64, 52, 75, 42, 56, 77, 64, 64],
[70, 61, 50, 74, 43, 60, 83, 62, 70],
[69, 64, 52, 75, 47, 58, 80, 56, 70]]
newdata=[71, 67, 52, 77, 47, 53, 82, 59,73]
allhistdata = [item for sublist in histdata for item in sublist]

print 'Y='
print newdata
print 'X='
for data in histdata:
    print data

n = len(allhistdata) * 1.0
y = [len([item1 for item1 in allhistdata if item1 <= item]) / n for item in newdata]

x = [len([item1 for j, item1 in enumerate(allhistdata) if item1 <= item and i != j]) / n for i, item in enumerate(allhistdata)]

n = 9
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







