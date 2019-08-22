# Question 3:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

""" Words seperated by comma taken as input from console and sorted words as output """

words = input("Enter words seperated by comma: ").split(", ")
sorted_words = words.sort()
for sorted_words in words:
	print(sorted_words)
