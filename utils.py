#Utils
from functools import reduce
import random
from numpy import cumsum

def sample(w,x):
    r=random.random()
    nw=list(map((lambda y:y**x),w)) #eleva ao expoente x todos os elemntos de w
    sum=reduce((lambda x,y:x+y),nw,0) #soma todos os elemntos da lista nw
    nw=list(map((lambda y:y/sum),nw)) #divide todos os elemntos da lista por sum
    nw= list(cumsum(nw)) #corre a lista acumulando em uma posiçao a
    #print(nw)
    #print(r)
    #retorna o indice da lista associado ao primeiro elemnto que seja maior que r
    #a lista começa pelo elemento 0
    return nw.index(next(x for x in nw if x>r))
#index : searches for a given element from the start of the list and returns the lowest index where the element appears
#next faz percorrer a lista toda


def generate_and_return_original_and_fragments(n,c,dmin,dmax):
    r=[]
    for i in range(n):
        r+=[random.randint(0,3)]
    w=[]
    print(r) # original DNA string
    cov=[]
    for i in range(n):
        cov+=[False]
    for i in range(c):
        pos=random.randint(0,n-dmin-1)
        dim=random.randint(dmin,dmax)
        w+=[r[pos:min(pos+dim,n)]]
        for j in range(pos,min(pos+dim,n)):
            cov[j]=True
    while not all(cov):
        pos=random.randint(0,n-dmin-1)
        dim=random.randint(dmin,dmax)
        w+=[r[pos:min(pos+dim,n)]]
        for j in range(pos,min(pos+dim,n)):
            cov[j]=True
    return [r,w]



def generate(n,c,dmin,dmax):
    r=[]
    for i in range(n):
        r+=[random.randint(0,3)]
    w=[]
    print(r) # original DNA string
    cov=[]
    for i in range(n):
        cov+=[False]
    for i in range(c):
        pos=random.randint(0,n-dmin-1)
        dim=random.randint(dmin,dmax)
        w+=[r[pos:min(pos+dim,n)]]
        for j in range(pos,min(pos+dim,n)):
            cov[j]=True
    while not all(cov):
        pos=random.randint(0,n-dmin-1)
        dim=random.randint(dmin,dmax)
        w+=[r[pos:min(pos+dim,n)]]
        for j in range(pos,min(pos+dim,n)):
            cov[j]=True
    return w

