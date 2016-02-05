
import random

def F(S):
    result=-1
    if S==set([1]):
        return 4
    elif S==set([2]):
        return 1
    elif S==set([3]):
        return 1.5
    elif S==set([1,2]):
        return  4.6
    elif S==set([1,3]):
        return 5.1
    elif S==set([2,3]):
        return 2.1
    elif S==set([1,2,3]):
        return 5.6
    else:
        return 0;

def H(d,Sigma):
    if d==1:
        return F(set([Sigma[0]]))-F(set([]))
    if d==2:
        return F(set([Sigma[0],Sigma[1]]))-F(set([Sigma[0]]))
    if d==3:
        return F(set([Sigma[0],Sigma[1],Sigma[2]]))-F(set([Sigma[0],Sigma[1]]))
Sold=set([])

def Max(W):
    return [item for item in [1,2,3] if W[item-1]>0]

while True:
    Sigma=[1,2,3]
    random.shuffle(Sigma)
    W=[H(1,Sigma),H(2,Sigma),H(3,Sigma)]
    print W
    Snew=Max(W)
    Sn=set(Snew)
    if(Sn==Sold):
        print Sn
        break
    else:
        Sold=Sn
