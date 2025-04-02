import re
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAAGTAATTTGTATGAG' 
#find=re.findall(r'GT+(\S)+AG',seq)改成：
find=re.findall(r'GT.*AG',seq)# it requires the greedy#find=re.findall(r'GT.*?AG',seq) is not the one to find the longest!
count=0#initial and storage the place of longest string
#find the longest intron(if to find the not greedy GT...AG)
for i in range(len(find)):
    if len(find[i])>len(find[count]):
        count=i#replace if it is longer(tips:it only contains the first)
#or can use the function:max(最大值函数) or use dictionary
print(find,find[count],len(find[count]))