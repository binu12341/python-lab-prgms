'''
print("Hello Friends")

a = 3
b = 5
print("Addition = ", a+b)
print("Subtraction = ", a-b)
print("Multiplication = ", a*b)
print("Division = ", a/b)

def reverse(s):
    str = " "
    for i in s:
        str = i+str
    return str
s="binu"
print(s)
print(reverse(s))
'''

'''
#Program to add two numbers entered by the user?

num1=input('Enter first number:')
num2=input('Enter second number:')
sum=float(num1)+float(num2)
print(num1,"+",num2,"=",sum)

#Change this value and test your self?
num=6.25
num_sqrt=num**0.5
print('The square root of',num,'is:',num_sqrt)


#Find the square root of real or complex numbers?

import cmath
num=64-64j
num_sqrt=cmath.sqrt(num)
print('The square root of',num,'is',num_sqrt)

#Area of a triangle?
a=3
b=4
c=5
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of a triangle is',area)

#swap two vales?
x=5.0
y=10
temp=x
x=y
y=temp
print('After swapping,')
print('x=',x)
print('y=',y)

#Multiplication table?
num=10
for i in range(1,11):
    print(num,'*',i,'=',num*i)

'''
'''
#To find the largest number among the 3 numbers?

num1=float(input('Enter first number:'))
num2=float(input('Enter second number:'))
num3=float(input('Enter third number:'))

num1=10
num2=14
num3=12

if(num1>=num2) and (num1>=num3):
    largest=num1
elif(num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
print("The largest number between",num1,",",num2,"and",num3,"is",largest)

#Quadratic quation
import cmath
a=1
b=5
c=6
d=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print('The roots are :')
print(root1)
print(root2)


#Calculate miles?
#kilometers=5.5
kilometers=float(input('Enter value in kilometers:'))
conv_fac=0.621371
miles=kilometers*conv_fac
print('%0.3f kilometers is equal to %0.3f miles',(kilometers,miles))

#To convert temperature in celsius to fahrenheit?
celsius=37.5
fahrenheit=(celsius*1.8)+32
print('%0.1f degree celsius is equal to %0.1f degree fahrenheit',(celsius,fahrenheit))

num=float(input('Enter a number:'))
if num>0:
    print('positive number')
elif num==0:
    print('zero')
else:
    print('negative number')
    

num=float(input('Enter a number:'))
if num>=0:
    if num==0:
        print('zero')
    else:
        print('positive number')
else:
    print('negative number')

#program to check if the input number is odd or even ?
num=int(input('Enter a number:'))
if (num%2)==0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))

#program to check if the input year is a leap year or not?
#year=2000
year=int(input('Enter a year:'))
if(year%4)==0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
    
#program to check if the input number is a prime or not?
#num=407
num=int(input('Enter a number:'))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")

#program to check if the input number is a prime or not and check for factors?
import math
#num=617
num=int(input('Enter a number:'))
if num>1:
    for i in range(2,math.ceil(num/2)):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num,"is not a prime number")

#program to display all the prome numbers within an interval?
#lower=900
#upper=1000

lower=int(input('Enter a lower limit:'))
upper=int(input('Enter a upper limit:'))
print("prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
'''

