import re
def split(ori,rec):#create the function called split to find the place of the first sequence in "ori" match "rec"
    a=len(rec)
    if re.search(r'[^ACGT]',ori)!="None" or re.search(r'[ACGT]',rec)!="None":
        return("incorrect necleotide sequence")
    for i in range(len(ori)-a):
        #if ori[i] not in ["A","C",'G','T']:
            #return("incorrect necleotide sequence")NOOOOOO!!!!!!!!!!: if the last letter is out of range, it wouldn't be tested!!!
        if ori[i:i+a]==rec:
            return i
    return("Can't found")
#example
a="ACGTAGCTACGATCPATCAGCATACGCAT"
b="CATGATAGTGAC" 
print(split(a,b))
