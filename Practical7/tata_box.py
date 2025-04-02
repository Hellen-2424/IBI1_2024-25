import re
tata_box=open('D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',"r")#use D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\ if can't find the route
tata_genes=[]#store gene sequences
gene_name=[]#store gene name
current=''#store current gene name
gene=''#let "gene" be string instead of list and store full of current gene line 
#find genes with TATA[AT]A[AT] and store them to gene_sequences and gene_name
for line in tata_box:
    if line[0]==">":#find the beginning
        if re.search(r"TATA[AT]A[AT]",gene):#if it has
            tata_genes.append(gene)#add to gene_sequence
            gene_name.append(">"+current+'\n')#add to gene name
        current=re.search(r'gene:(\S+)',line).group(1)#to change to strings, update current gene name
        gene=''#update current gene line
    else:
        gene+=line#update and add to gene_sequence
#if the last matches the type, then add it
if re.search(r'TATA[AT]A[AT]',gene):
   gene_name.append(">"+current+'\n')
   tata_genes.append(gene)  
#write into tata_genes
print(tata_genes[1])
f=open("D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\tata_genes.fa",'w')
for i in range(len(gene_name)):
    f.write(gene_name[i])
    f.write(tata_genes[i])
f.close()
tata_box.close()