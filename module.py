#Q.1-What is TimeTuple?

#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

#Index	Field	Values
#0	4-digit year	2008
#1	Month	1 to 12
#2	Day	1 to 31
#3	Hour	0 to 23
#4	Minute	0 to 59
#5	Second	0 to 61 (60 or 61 are leap-seconds)
#6	Day of Week	0 to 6 (0 is Monday)
#7	Day of year	1 to 366 (Julian day)
#8	Daylight savings	-1, 0, 1, -1 means library determines DST
    

#Q.2- Write a program to get formatted time.

import datetime
current = datetime.datetime.now()
print ("current date and time are:",current)
print ("YEAR: ",current.strftime("%Y"))
print ("MONTH: ",current.strftime("%B"))
print ("DATE: ",current.strftime("%d"))
print ("DAY: ",current.strftime("%A"))

print("\n\n",10*"*")



#Q.3- Extract month from the time

import datetime
current = datetime.datetime.now()
print ("MONTH: ",current.strftime("%B"))

print("\n\n",10*"*")




#Q.4- Extract day from the time.

import datetime
current = datetime.datetime.now()
print ("DAY: ",current.strftime("%A"))

print("\n\n",10*"*")




#Q.5- Extract date (ex : 11 in 11/01/2021) from the time.

import datetime
specific = datetime.datetime(2021,1,11,14,15)
print(specific.day)

print("\n\n",10*"*")



#Q.6- Write a program to print time using localtime method.
import time
print("Local time is ",time.localtime(time.time()))

print("\n\n",10*"*")




#Q.7- Find the factorial of a number input by user using math package functions.

import math
num = int(input("enter the number:"))
print("factorial of %d is "%(num),math.factorial(num))

print("\n\n",10*"*")





#Q.8- Find the GCD of a number input by user using math package functions.

import math
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print("gcd of %d,%d is "%(num1,num2),math.gcd(num1,num2))

print("\n\n",10*"*")




#Q.9- Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.

import os
print("current working directory is ",os.getcwd())
print("user environment is ",os.name)

print("\n\n",10*"*")
