'''  =============================== Loops  ========================================'''
"""
# 1.Print a multiplication table of a given number up to 10.

def mul(num):
    for i in range(1,11):
         print(f"{num} x {i} ={i*num}")
number=int(input("Enter numbe:"))
mul(number)


# 2.Print all prime numbers between 1 and 50.

for num in range(1,51):
    if num >1: # Prime num are always greater than 1
        for i in range(2,num):
            if num%i ==0:
             break
        else:
                print(f"{num} is prime num.")

# 3.Generate the Fibonacci sequence up to n terms.

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num=int(input("Enter number upto you want to generate fibonacci series:"))
for i in range(num):
    print(fibonacci(i),end="  ")
        
 # Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a, b = 0, 1   # first two terms
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 4.Calculate the factorial of a number using a loop.

def fact(n):
    if n==0  or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter number for factorial finding:"))
print(f"{num}! = {fact(num)}")

# 5.Print the following pattern:
*
* *
* * *
* * * *

def pattern(rows):
    for i in range(1,rows+1):
        print(i*"*")
pattern(4)

def rectangle(row):
    for i in range(1,row+1):
        if i ==1 or i ==row:
            print("*"*row)
        else:
            print("*"+" "*(row-2)+"*")
rectangle(5)
"""