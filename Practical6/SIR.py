# import
# point and define the variables
# time loop

import numpy as np
import matplotlib.pyplot as plt
N=10000#population
##SIR=[9999,1,0]#create a list contains the Susceptible(SIR[0]), Infected(SIR[1]) and Recovered(SIR[2])
sus=[9999]
inf=[1]
rec=[0]
b=0.3#storage beta
r=0.05#storage gamma
#arrays=[]#track and storage the changes over time
##arrays.append(SIR)
#into time loop: random the people to get infected(n) and to get recovered(m)
x=1000
for i in range(x):
    n_pre=np.random.choice(range(2),sus[-1],p=[1-b,b])#individuals get infected
    n=sum(n_pre)#sum of the infected 
    m_pre=np.random.choice(range(2),inf[-1],p=[1-r,r])#individuals get recovered
    m=sum(m_pre)#sum of the recovered
    ##arrays.append([SIR[0]-n,SIR[1]+n-m,SIR[2]+m])#record. however, this form is not good to draw, so a changed the storage type
    sus.append(sus[-1]-n)
    inf.append(inf[-1]+n-m)
    rec.append(rec[-1]+m)
#draw
time=[i for i in range(x+1)]#add the initial "1"
plt.title("SIR model")
plt.xlabel("time")
plt.ylabel("number of peaple")
plt.plot(time,sus,"y",label="susceptible")#define the color:'b'代表蓝色（blue）、'g'代表绿色（green） 、'r'代表红色（red）、'c'代表青色（cyan）、'm'代表品红色（magenta）、'y'代表黄色（yellow）、'k'代表黑色（black）、'w'代表白色（white）
plt.plot(time,inf,"r",label="infected")
plt.plot(time,rec,"g",label="recovered")
plt.legend()
plt.show()




    