#import sys #确保 Matplotlib 所在的路径在其中
#sys.path.append('C:/Users/Hellen/AppData/Local/Microsoft/WindowsApps/python3.11.exe')#deleted it because found the globle python path
import matplotlib.pyplot as plt
dic={"JavaScript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}#make and match the dictionary
n="HTML"#create the valuable which should have been inputed (highlight it)
print(dic[n])#
plt.xlabel("language")#define the label
#plt.xticks(dic.keys())
plt.ylabel("Usrs(percentage)")
plt.title("programming language popularity")#make sure the title
plt.bar(dic.keys(),dic.values())#draw

plt.show()


#####a little bit problem:solved