# class p:
# 	x = 3
# ia = p()
# ia.x = ia.x + 1
# print(ia.x)
# def outer():
#     a = 0
#     b = 1

#     def inner():
#         print (a)
#         print( b)
#         b = 4

#     inner()

# outer()

# def myfunc1():
#   x = "John"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2() 
#   return x

# print(myfunc1())
#create a function:
def myfunction():
  global x
  x = "hello"

#execute the function:
myfunction()

#x should now be global, and accessible in the global scope.
print(x)
x = 2
print(x)