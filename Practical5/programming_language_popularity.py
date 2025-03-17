import sys #确保 Matplotlib 所在的路径在其中
sys.path.append('C:/Users/Hellen/AppData/Local/Microsoft/WindowsApps/python3.11.exe')
import matplotlib.pyplot as plt
dic={"JavaScript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}
n="HTML"#highlight
print(dic[n])
plt.xlabel("language")
#plt.xticks(dic.keys)
plt.ylabel("Usrs(percentage)")
plt.title("programming language popularity")
plt.bar(dic.keys(),dic.values())
plt.show()


#####a little bit problem