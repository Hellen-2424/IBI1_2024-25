import re
splice=input("splice donor/acceptor combinations:")
tata_box=open("D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\tata_genes.fa","r")
tata_genename=[]
genes=[]
gene=''
current=""
for line in tata_box:
    if line[0]==">":
        a=re.findall(splice,gene)
        if len(a)!=0:
            tata_genename.append(f">{current} {len(a)}\n")#to instead ">"+current+str(len(a))+'\n'
            genes.append(gene+'\n')
        current=line[1:].strip()#write() argument must be str, not int
        gene=''
    else:
        gene+=line.strip()
a=re.findall(splice,gene)
if len(a)!=0:
   tata_genename.append(f">{current} {len(a)}\n")
   genes.append(gene+'\n')
f=open(f"D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\{splice}_splice_genes.fa","w")
for i in range(len(tata_genename)):
     f.write(tata_genename[i])
     f.write(genes[i])
tata_box.close()
f.close()

