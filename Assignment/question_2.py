# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


""" No of both row elements and column elements to be taken as input """

import sys
import re

while True:
	try:
		X, Y= int(input("Enter number of rows and columns: ")).split(", ")
		for i in range(len(X)):
			if (re.search("\D", X[i])):
				raise ValueError(X)
			else:
				continue
		for i in range(len(Y)):
			if (re.search("\D", Y[i])):
				raise ValueError(Y)
			else:
				continue
	except ValueError as NumberException:
	        print("Invalid Input:'{}' is not a number".format(NumberException))
	        sys.exit(0)
	else:
		multi_list = [[0 for col in range(Y)] for row in range(X)]
		for row in range(X):
			for col in range(Y):
				multi_list[row][col]= row*col

		print("List generated: ",multi_list)
		sys.exit(0)
	