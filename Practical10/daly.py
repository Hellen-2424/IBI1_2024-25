import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/浙大海宁学习大一/IBI1/IBI1_2024-25/IBI1_2024-25/Practical10")# change the working directory
df=pd.read_csv("dalys-rate-from-all-causes.csv")

#task 4
df.info()#print out the basic information of df
#print(df.head(5))#when in 静默模式
#print(df.describe())
print(df.iloc[2,0:2])
#print(df.iloc[0:2,:])
#print(df.iloc[0:10:2,0:5])
print(df["Year"].head(10))#comment:10th data:1999
print(df.loc[df.Year==1990,"DALYs"])

#task 5_1
F=df[df["Entity"]=="France"]["DALYs"].mean()
U=df[df["Entity"]=="England"]["DALYs"].mean()
print("DALYS of France: "+str(F))


print("DALYS of UK: "+str(U))
if F==U:
    print("the mean DALYs in the UK was equal to France")
elif F<U:
    print("the mean DALYs in the UK was greater than France")
else:
    print("the mean DALYs in the UK was smaller than France")

#task 5_2
uk=df.loc[df.Entity=="United Kingdom",["DALYs", "Year"]]
plt.title("DALYs of UK")
plt.plot(uk.Year, uk.DALYs, 'b.')
plt.xticks(uk.Year,rotation=-90)
plt.grid(True)
plt.show()

#task 6
uk=df.loc[df.Entity=="United Kingdom",["DALYs", "Year"]]
Ice=df.loc[df.Entity=="Iceland",["DALYs", "Year"]]
plt.title("DALYs of UK and Iceland")
plt.plot(Ice.Year,Ice.DALYs,"b.")
plt.plot(uk.Year,uk.DALYs,"r+")
plt.grid(True)
plt.show()


Ch=df.loc[df.Entity=="China",["DALYs", "Year"]]
Ja=df.loc[df.Entity=="Japan",["DALYs", "Year"]]
plt.title("DALYs of China and Japan")
plt.plot(Ch.Year,Ch.DALYs,"r.")
plt.plot(Ja.Year,Ja.DALYs,"b.")
plt.grid(True)
plt.show()

print(df[df["DALYs"]>650000]["Entity"])#可以用tolist()仅取一个entity

plt.title("DALYs in 1990")
y=df.loc[df.Year==1990,["Entity","DALYs"]]#find data of 1990
plt.bar(y.Entity,y.DALYs)
plt.xticks(y.Entity,rotation=-90,fontsize=4)
plt.grid(True)
plt.show()



