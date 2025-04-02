import re
splice=input("splice donor/acceptor combinations:")
tata_box=open("D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
tata_genename=[]#to store gene name
genes=[]#to store gene_sequence
gene=''#to store current gene_sequence
current=""#to store current gene_name
# to find the gene that has the splice
for line in tata_box:
    if line[0]==">":#start with the new gene 
        a=re.findall(splice,gene)#the number of the splice in the gene
        if len(a)!=0:#it has
            tata_genename.append(f">{current} {len(a)}\n")#to instead ">"+current+str(len(a))+'\n'
            genes.append(gene+'\n')#update the gene_sequence storage
        current=line[1:8].strip()#write() argument must be str, not int
        gene=''#update current gene_sequence
    else:
        gene+=line.strip()#update and add to current gene_sequence and delete\n
#if the last matches the type, then add it
a=re.findall(splice,gene)
if len(a)!=0:
   tata_genename.append(f">{current} {len(a)}\n")
   genes.append(gene+'\n')
 #write into matched spllice genes.fa 
f=open(f"D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\{splice}_splice_genes.fa","w")
for i in range(len(tata_genename)):
     f.write(tata_genename[i])
     f.write(genes[i])
tata_box.close()
f.close()

