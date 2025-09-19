""" ---------      simple operation on function  --------------------"""
"""
def greet(name,ending):# functin definition
    print(f"Hello {name} Good Morning!")
    print(ending)
greet('Siddhu','Thank you')#function call
"""
"""
# default argument------------------
def greet(name,ending="Thank you"):
    print(f"Hello {name},Good Morning!! ")
    print(ending)

greet("Siddhu","Thanks")
"""
"""
*****************************   Recursion  ******************************
Recursion is a fucntion which calls itself.
It is used to directly use a mathematical formula as function.
Example:
factorial(n)=n x factorial(n-1)
def factorial(n):
    if n==0 or n==1: #base condition which doesn't call the function any further
        return 1
    else:
        return n*factorial(n-1) #fucntion calling itself
n=int(input("Enter number:"))
print(f"Factorial of {n} : {factorial(n)}")
"""
"""  *******************************   Practice -Set   ******************************"""
"""
**************************************    Q.1)     ********************************
Q.1) WAP using functions to find greatest of three numbers.
def greatest(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            print(f"{n1} is greatest number.")
        else:
            print(f"{n3} is greatest number.")
    elif n2 > n3:
        if n2 > n1:
            print(f"{n2} is greatest number.")
        else:
            print(f"{n1} is greatest number.")
    else:
        print(f"{n3} is greatest number.")

greatest(1110,30,10901)
"""
"""
**************************************    Q.2)     ********************************
WAP using function to convert Celsius to Fahrenheit---------------------
def tempConverter(Celsius):
    return (Celsius * 9/5)+32
celsius=float(input("Enter degree Celsius:"))
print(f"Fahrenheit : {round(tempConverter(celsius),2)}")
"""
"""
**************************************    Q.3)     ********************************
How do we prevent a python print() function  to print a new line at the  end.
Ans:we can use end="" to prevent a new line at the end
print("a")            Output:   a
print("b")                      b                  
print("c",end="")               cd   
print("d",end="")                i.e end="" prevent a new line 
"""
"""
**************************************    Q.4)     ********************************
Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n
n=int(input("Enter number:"))
print(f"Sum from 1 to {n} : {sum(n)}")
"""
"""
**************************************    Q.5)     ********************************
WAP using function to print n lines of the following pattern:
***
**
*
def reversePattern(rows):
    # for i in range(1,rows+1):
    #     print(" "*(rows-i)+"*"*(2*i-1))# it print pyramid
    for i in range(0,rows+1):
        print((rows-i)*"*")
rows=int(input("Enter number of rows:"))
reversePattern(rows)
"""
"""
# Using recursion
def pattern(n):
    if(n==0):
        return ""
    print("*"*n)
    pattern(n-1)

pattern(5)
"""
# --------------------------------------------------------------------------
"""
**************************************    Q.6)     ********************************
WAP using function which converts inches to cms.

def inchToCm(inch):
    return inch*2.54
n=float(input("Enter value in inches:"))
print(f"The corresponding value in cm is : {inchToCm(n)}")
"""
"""
**************************************    Q.7)     ********************************
WAP using function to remove a given word from a list and strip it at the same time.

def remove(l,word):
    n=[]
    for item in l:
        # l.remove(word)
        # return l
        if not(item == word):
            n.append(item.strip(word))
    return n

lst=["Siddhu","Trishna","Junnu","kiran","Suman","an"]
print(remove(lst,"an"))
"""
"""
**************************************    Q.8)     ********************************
WAP using function to print multiplication table of a given number.

def mul(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
n=int(input("Enter number:"))
mul(n)
"""