import numpy as np
import matplotlib.pyplot as plt
#from script.? import odeint
from matplotlib.colors import ListedColormap
population=np.zeros((100, 100))#set a two-dimensional array filled with all zeros
b=0.3#beta
r=0.05#gamma
#vaccination_rate=0.2
outbreak=np.random.choice(range(100),2)#initialize the first get infected
population[outbreak[0],outbreak[1]]=1#initialize the first get infected
cmap =ListedColormap(['darkviolet', 'turquoise', 'gold', 'lightgreen'])#define the color
#num_vaccinated=int(100*100*vaccination_rate)
#vaccinated_indices=np.random.choice(100*100,num_vaccinated,replace=False)
#for index in vaccinated_indices:
 #   x,y=index//100,index%100
  #  population[x,y]=3
plt.figure(figsize=(6,4),dpi=150)#fig:the whole figure;axes:a list comtains all the sub figures!!!
x=100#times
for i in range(x): 
    position=np.where(population==1)#for the structure of np.where is [a,b]
    for j in range(len(position[0])):#!!!
        for dx in[-1,0,1]:#run through the surrounding of the "infected" ones
            for dy in[-1,0,1]:
                if dx==0 and dy==0:#skip the original place
                    continue
                new_x,new_y=position[0][j]+dx,position[1][j]+dy#find the new position
                if 0<=new_x<100 and 0<=new_y<100:#make sure the position is not at the corner
                    if population[new_x,new_y]==0:  #邻居为易感者
                        population[new_x,new_y]=np.random.choice(range(2),p=[1-b,b])
                        #if np.random.rand()<b:  #以beta概率感染邻居#np.random.rand():randomize all the numbers between[0,1]
                       #     population[new_x,new_y]=1
        if np.random.rand()<r:#find the recovered one
            population[position[0][j],position[1][j]]=2

        #all of behind: delete!!!!!!!!
        #population(position[j])
        # 0 1 3 
        #2 p 5#p=[position[0][j],position[1][j]:
        #4 6 7
        #if position[0][j]==0 and position[1][j]==0 or position[0][j]==0 and position[1][j]==99 or position[0][j]==99 and position[1][j]==0 or position[0][j]==99 and position[1][j]==99:
         #   n=np.random.choice(range(2),3,p=[1-b,b])
          #  population[[position[0][j]-1,position[1][j]]-1,]=n
        #elif position[0][j]==0 or position[0][j]==99 or position[1][j]==0 or position[1][j]==99:   
        #    n=np.random.choice(range(2),5,p=[1-b,b])
         #   population[[position[0][j]-1,position[1][j]]-1,]=n
        #else:    
         #   n=np.random.choice(range(2),8,p=[1-b,b])
          #  population[[position[0][j]-1,position[1][j]]-1,]=n
    #plt.figure(figsize=(6, 4),dpi=150)
    #plt.imshow(population,cmap=cmap,interpolation='nearest')
    #plt.title(f'Time step:{i}')
    #plt.axis('off')
    #plt.show()
    #change it into subplot:!!!!!!!
    plt.imshow(population,cmap=cmap,interpolation='nearest')
    plt.title(f'Time step:{i}',fontsize=6)
    plt.pause(0.1)
    plt.axis('on')
    #set the fonsize of axis:
    #ax.tick_params(axis='both', which='major', labelsize=4)
    #ax.tick_params(axis='both', which='minor', labelsize=2)
plt.show()