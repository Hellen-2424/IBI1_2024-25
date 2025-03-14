# What does this piece of code do?
# Answer: how many numbers ("progress" ) of trying until the two random numbers become equal for the first time( What is the first time two random numbers are equal)
#在第几次时两个随机数第一次相等
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil  #？

progress=0
while progress>=0:
	progress+=1#as a counter
	first_n = randint(1,6)
	second_n = randint(1,6)
	print(first_n,second_n)
	if first_n == second_n:
		print(progress)
		break

