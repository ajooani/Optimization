import random,math
import numpy as np

def generate(n, m, l, u):   #Generated solution
    data = []
    for i in range(n):
        tem = []
        for j in range(m):
            tem.append(random.uniform(l, u))
        data.append(tem)
    return data

N, M, lb, ub = 10, 5, 1, 5
g, max = 0, 100

soln = generate(N, M, lb, ub)

def fitness(soln):
    F = []
    for i in range(len(soln)):
        F.append(random.random())
    return F
def selected_stage(P,Pbest,pmean):
    Alpha=0.3
    Pnew=[]
    r=random.uniform(0,1)
    for i in range(len(P)):
        for j in range(len(P[i])):
            Pnew.append(Pbest[j]+Alpha*r*(pmean-P[i][j]))
    return Pnew

def search_stage(Pi,pmean):
    Pinew=[]
    a=random.uniform(5,10)
    R=random.uniform(0.5,2)
    pi=3.14
    Teta=a*pi*random.random()
    ri=Teta+R*random.random()
    Xr=ri*np.sin(Teta)
    yr=ri*np.cos(Teta)
    for i in range(len(Pi)):

        Pinew.append(Pi[i]+yr*(Pi[i]-Pi[i-1])+Xr*(Pi[i]-pmean))
    return Pinew

def swooping_stage(pbest,Pi):
    Pos_New=[]
    R = random.uniform(0.5, 2)
    pi = 3.14
    a = random.uniform(5, 10)
    Teta = a * pi * random.random()
    ri = Teta + R * random.random()
    xr=ri*np.sinh(Teta)
    yr=ri*np.cosh(Teta)
    c1=random.uniform(1,2)
    c2=random.uniform(1,2)
    for i in range(len(pbest)):
        Pos_New.append(random.random()*pbest[i]+xr*(Pi[i]-c1*pmean)+yr*Pi[i]-c2*pbest[i])
    return Pos_New

while g<max:
    Fit=fitness(soln)
    bst=np.argmax(Fit)
    pbest=soln[bst]
    pmean=np.mean(soln)
    Pnew=selected_stage(soln,pbest,pmean)
    Ss=search_stage(Pnew,pmean)
    Sw_S=swooping_stage(pbest,Ss)
    f_Pbest=np.argmax(Sw_S)
    best_soln=soln[f_Pbest]


    g+=1

print(best_soln)
