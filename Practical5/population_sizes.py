#import sys #确保 Matplotlib 所在的路径在其中
#sys.path.append('C:/Users/Hellen/AppData/Local/Microsoft/WindowsApps/python3.11.exe')#deleted it because found the globle python path
import matplotlib.pyplot as plt
uk_countries=[57.11,3.13,1.91,5.45]#list the population
uk_labels="England","Wales","Northern Ireland","Scotland"#Match population with country
plt.subplot(1,2,1)
plt.title("uk-population")
plt.pie(uk_countries,explode=(0,0,0,0),labels=uk_labels,autopct="%1.1f%%",shadow=False,startangle=0)#draw
zj_province=[65.77,41.88,45.28,61.27,85.15]#list the population
zj_labels="Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"#Match population with the province
plt.subplot(1,2,2)
plt.title("zhejiang-population")
plt.pie(zj_province,explode=(0,0,0,0,0),labels=zj_labels,autopct="%1.1f%%",shadow=False,startangle=0)
plt.show()
uk_countries1=sorted(uk_countries)#sort 
zj_province1=sorted(zj_province)
print(uk_countries1,zj_province1)

#or use: fig,(ax1,ax2)=plt.subplots(1,2)
#set the size of the figure:  fig.set_size_inches(10,5)
#set title: ax1.set_title(...)

