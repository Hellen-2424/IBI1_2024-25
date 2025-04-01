import re
import sys

tata_box=open('D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',"r")
tata_genes=[]
gene_name=[]
gene=''#let "gene" be string instead of list
for line in tata_box:
    if line[0]==">":
        if re.search(r"TATA[AT][AT][AT]",gene):
            tata_genes.append(gene)
            gene_name.append(">"+re.search(r'gene:(\S+)',line).group(1)+'\n')#to change to strings
        gene=''
    else:
        gene+=line
if re.search(r'TATA[AT][AT][AT]',gene):
   tata_genes.append(gene)  
#write into tata_genes
f=open("D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\tata_genes.fa",'w')
for i in range(len(gene_name)):
    f.write(gene_name[i])
    f.write(tata_genes[i])
f.close()
tata_box.close()