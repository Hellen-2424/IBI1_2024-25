import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/浙大海宁学习大一/IBI1/IBI1_2024-25/IBI1_2024-25/Practical10")# change the working directory
df=pd.read_csv("dalys-rate-from-all-causes.csv")

#df.info()#print out the basic information of df
print(df.iloc[2,0:10])


