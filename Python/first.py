import math

#Display program
print("Hello world")
print("Python is fun")

#to perform mathematical operations
a = eval(input("Enter first value: "))
b = eval(input("Enter second value: "))
c = a + b

print("the answer is:", c)

#calculate time
seconds = eval(input("Enter time in seconds: "))

#how to calculate
minutes = seconds // 60 #gets time in minutes
remainingSeconds = seconds % 60 #remaining seconds left

print( seconds, " can be converted to ", minutes, "and", remainingSeconds, "seconds")

#using maths functions
print("The square-root of 4 is: ", math.sqrt(4))

sum = '3' + '2'
print(sum)