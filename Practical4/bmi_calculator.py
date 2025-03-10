#input the wanted numbers
w=float(input("weight(kg)="))
h=float(input("height(m)="))
#calculate BMI
bmi=w/h**2
#find where this specific BMI is and print
if 18.5<=bmi<=30:
    print("your BMI is"+str(bmi)+". Congradulations! It's normal weight.")
elif bmi>30:
    print("your BMI is"+str(bmi)+". Sorry, you are considered obese.")
else:
    print("your BMI is"+str(bmi)+". Sorry, you are considered underweight.")
