import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/浙大海宁学习大一/IBI1/IBI1_2024-25/IBI1_2024-25/Practical10")# change the working directory
df=pd.read_csv("dalys-rate-from-all-causes.csv")

uk=df.loc[df.Entity=="United Kingdom",["DALYs", "Year"]]
Ice=df.loc[df.Entity=="Iceland",["DALYs", "Year"]]
plt.title("DALYs of UK and Iceland")
plt.plot(Ice.Year,Ice.DALYs,"b.")
plt.plot(uk.Year,uk.DALYs,"r+")
plt.grid(True)
plt.show()


