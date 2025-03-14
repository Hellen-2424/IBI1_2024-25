a=15#bus walk time
b=1*60+15#bus journal time
c=a+b#bus whole time
d=1*60+30#drive
e=5#car park
f=d+e#car whole time
if c>f:#compare
    print("car is faster")
else:
    print("bus is faster")
#
X=True
Y=False
W=X and Y#False
print(W)
#table:
#X      Y       Z
#True  True   True
#True  False  False
#False True   False
#False False  False
