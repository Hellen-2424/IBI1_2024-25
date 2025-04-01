import re
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 
#find=re.findall(r'GT+(\S)+AG',seq)改成：
find=re.findall(r'GT(.*?)AG',seq)
count=0
for i in range(len(find)):
    if len(find[i])>count:
        count=i
print(find[count])