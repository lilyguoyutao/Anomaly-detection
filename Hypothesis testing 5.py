import math
def kl(a, b):
    if a == 0:
        return (1 - a) * math.log((1 - a) / (1 - b))
    elif a == 1:
        return a * math.log(a / b)
    else:
        return a * math.log(a / b) + (1 - a) * math.log((1 - a) / (1 - b))
def phi(data, S):
    ns = len(S) * 1.0
    nalphas = len([data[i] for i in S if data[i]==1]) * 1.0
    return ns * kl(nalphas / ns, 0.05)



def phi2(data, S):
    ns = len(S) * 1.0
    nalphas = len([data[i] for i in S if data[i]==1]) * 1.0
    return nalphas*math.log(nalphas)-ns*math.log(ns)




item=[0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1]

S1=[0,1,2,3,4]
S3=[0,1,2,3,4,5,6]
K=[9]


print phi(item,S1+K)-phi(item,S1)-(phi(item,S3+K)-phi(item,S3))

print phi2(item,S1+K)-phi2(item,S1)-(phi2(item,S3+K)-phi2(item,S3))
