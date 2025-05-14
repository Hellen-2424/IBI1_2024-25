import re
se=open('D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical13\\se.fa',"r")
seq=[]
for line in se:
    if line[0]==">":
        seq.append("")
    else:
        seq[-1]+=line.replace('\n','')
#print(seq)
seq_human=seq[0]
seq_mouse=seq[1]
seq_ran=seq[2]
H_M=0
for i in range(len(seq_human)):
    if seq_human[i]!=seq_mouse[i]:
        H_M+=1
per1=str(round((len(seq_human)-H_M)/len(seq_human)*100,1))+"%"
print("edit difference between human and mouse: ",H_M)
print("similarity of human and mouse: ",per1)
H_R=0
for i in range(len(seq_human)):
    if seq_human[i]!=seq_ran[i]:
        H_R+=1
per2=str(round((len(seq_human)-H_R)/len(seq_human)*100,1))+"%"
print("edit difference between human and random: ",H_R)
print("similarity of human and random: ",per2)
M_R=0
for i in range(len(seq_mouse)):
    if seq_mouse[i]!=seq_ran[i]:
        M_R+=1
per3=str(round((len(seq_mouse)-M_R)/len(seq_mouse)*100,1))+"%"
print("edit difference between mouse and random: ",M_R)
print("similarity of mouse and random: ",per3)
