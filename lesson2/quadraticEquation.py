!#/usr/bin/env python3

import math

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c:"))
d = b * b -4 * a * c
if d < 0 :
	print("Roots are imaginary")
	
else:
	root1 = (-b + math.sqrt(d))  / (2 * a) 
	root2 = (-b - math.sqrt(d))  / (2 * a)
	print("Root 1 = " , root1)
	print("Root 2 = " , root2)


