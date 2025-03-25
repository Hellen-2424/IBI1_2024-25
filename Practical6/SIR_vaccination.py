# import
# point and define the variables
# vaccination loop:
#     time loop
#     draw

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
N=10000#population
sus=[N]
inf=[0]
rec=[0]
vac=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
b=0.3#storage beta
r=0.05#storage gamma
#into time loop: random the people to get infected(n) and to get recovered(m)
x=1000
colors=cm.viridis(np.linspace(0,10,100))#define the colors
for j in range(len(vac)):
    for i in range(x):
        if int(sus[-1]-N*vac[j])<=0:
            inf.append(inf[-1])
        else:
            n_pre=np.random.choice(range(2),int(sus[-1]-N*vac[j]),p=[1-b,b])#individuals get infected
            n=sum(n_pre)#sum of the infected 
            m_pre=np.random.choice(range(2),inf[-1],p=[1-r,r])#individuals get recovered
            m=sum(m_pre)#sum of the recovered
            sus.append(sus[-1]-n)
            inf.append(inf[-1]+n-m)
            rec.append(rec[-1]+m)
    #draw
    time=[p for p in range(x+1)]#add the initial "1"
    plt.plot(time,inf,color=colors[j],label=f"Vaccination Rate: {vac[j]}")#important and remember!!!!!
    plt.title("SIR model with different vaccination rates")        
    plt.xlabel("time")
    plt.ylabel("number of peaple")
    plt.legend()
    sus=[N]#initialize!!!!!!!!!!!!!
    inf=[0]
    rec=[0]
plt.show()
