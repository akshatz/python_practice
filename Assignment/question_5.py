# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

string = input("Enter string:")
count1 = 0
count2 = 0
for i in string:
      if(i.isdigit()):
        count1=count1+1
      elif(i.isupper() or i.islower()):
      	count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)