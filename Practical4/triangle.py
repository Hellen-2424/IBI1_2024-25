#define the first number
a=1
#use for loops to find each numbers 
for i in range(2,11):
    print(a)
    a+=i
#print the lost last number(since when i==10, the for loop will break and would not print the last number)
print(a)
a=0
for i in range(1,11):
    print(a+i)#a would not be replaced!!Remember...
    a+=i