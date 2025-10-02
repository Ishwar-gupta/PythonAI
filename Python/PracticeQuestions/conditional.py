"""
🔹====================== Conditional Operator (if-else) (5)    ====================================

# 1.Find the largest of three numbers using conditional statements.

def greater(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            print(f"{n1} is greatest number.")
        else:
            print(f"{n3} is greatest number.")
    elif n2>n1:
        if n2>n3:
            print(f"{n2} is greatest number.")
        else:
            print(f"{n3} is greatest number.")
    else:
        print(f"{n3} is greatest number.")

num1=int(input("Enter first num:"))
num2=int(input("Enter second num:"))
num3=int(input("Enter third num:"))
greater(num1,num2,num3)

# 2.Check if a year is a leap year or not.

def leapYearChecker(yrs):
    if (yrs%400 == 0) or (yrs%4==0 and yrs%100 !=0):
        print(f"{yrs} is leap year.")
    else:
        print(f"{years} isnot leap year.")
years=int(input("Enter years:"))
leapYearChecker(years)

# 3.Classify a number as positive, negative, or zero.

def postiveNegative(num):
    if num>0:
        print("Postive")
    elif num<0:
        print("Negative")
    else:
        print("Zero")
number=int(input("Enter number:"))
postiveNegative(number)

# 4.Check if a number is even or odd without using %.

def evenOddChecker(num):
    if num  & 1==0:
        print(num,"is Even.")
    else:
        print(num,"is Odd.")
num=int(input("Enter number:"))
for i in range(1,num):
    evenOddChecker(i)

"""

'''==========================   Problem  ====================================
6. Conditional Operators (10 Questions)

Write a program to classify a triangle as scalene, isosceles, or equilateral.

Determine if a given year is a leap year (using only conditionals).

Implement a simple calculator using conditional operators only.

Check if a number is an Armstrong number.

Write a grading system using nested conditionals.

Implement min() and max() functions without using built-ins.

Check if three numbers can form a valid Pythagorean triplet.

Write a conditional-based program for FizzBuzz (multiples of 3 and 5).

Given two dates, check which one comes first.

Determine if a number can be expressed as the sum of two primes.
'''

