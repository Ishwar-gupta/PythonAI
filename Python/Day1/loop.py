
'''
# while loop
# count=1
# while count<=5:
#     print("Sid loves junnu.")
#     count +=1
# print(count)
# i=1
# while i<=1000:
#     print("Trishnaa",i)
#     i+=1

# j=5
# while j>=1:
#     print("Suman",j)
#     j-=1

#-------------- practice time--------------------------------
# print  numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1
# -----------------    2  -----------------------
# print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1
# --------------------------  3---------------------
# print the multiplication table of a number n
# i=1
# n=int(input("Enter number:"))
# while i<=10:
#     print(f"{n } * {i} = {n*i}")
#     i+=1
# --------------------------  4   --------------------
# print the elements of the following list using a loop
# [1,4,9,16,......,81,100]
# traverse:> if it travels of every elements of tuples or array or dictionary are called traverse

# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(nums):
#     # print(idx)
#     print(nums[idx])
#     idx += 1

# --------------------------  5   --------------------
# Search for a number x in the tuple using loop
# [1,4,9,16,......,81,100]
"""
nums=(1,4,9,16,......,81,100)
x=36
i=0
while i < len(nums):
    if(nums[i] == x):
        print("found at index:",i)
    else:
        i +=1
"""
# -------------------------for loop------------------------------------------
# for i in range(1,6):
#     print(i)

#  ---------------------------For loop with lists-------------------------------
# l=[1,4,2,345,45,23,44]
# for i in l:
#     print(i)
#  ---------------------------For loop with tuples-------------------------------
# t=(6,9,8,34,56,2,1)
# for i in t:
#     print(i)
#  ---------------------------For loop with strings-------------------------------
# str="Suman"
# for i in str:
#     print(i)
#  ---------------------------For loops ragne(0,7) similar to range(7)-------------------------------
# for i in range(7):
#     print(i)
# -------for loop with else----------------------
"""
An optional else can be used with a for loop if 
the code is to be executed when the loops exhausts

//e.g 
l=[1,7,8]
for item in l:  
    print(item)
else:
    print("done") # this is printed when the loop exhausts!
# """
# l=[1,7,8]
# for item in l:  
#     print(item)
# else:
#     print("done") # this is printed when the loop exhausts!


# ------------------------for loop with break and continue statement-----------------
# for i in range(30):
#     if(i==20):
#         break #exit the loop instantly
#     print(i)
# for i in range(30):
#     if(i==25):
#         continue # skip only this iteration
#     print(i)
# -------------------for loop with pass statement--------------------------------
"""
pass is a null statement in python
it instructs to "do  nothing"
// e.g
"""
"""
l=[1,7,9,8]
for i in l:
    pass # without pass,the program will throw an error
#  if we donot declare while loop doesn't executed i.e it throws an error
k=0
while(k<20):
    print(k)
    k+=1
"""

# ---------------------------Practice question-----------------------------------
# ******************************Q.N.1********************************************
# WAP to print multiplication table of a given number using for loop
# num=int(input("Enter number:"))
# for i in range(1,11):
#     # print(num ," * " , i , "=",i*num)
#     print(f"{num} * {i} = {num*i}")

# ******************************Q.N.2********************************************
"""
WAP to greet all the person names stored in a list 'l' and which starts with S
l=["harry","Soham","Sachin","Rahul"]
"""
# l=["harry","Soham","Sachin","Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# ******************************Q.N.3********************************************
# Attempt question number1 with while loop
# num=int(input("Enter number:"))
# i=1
# while(i<=10):
#     print(f"{num}*{i}={num*i}")
#     i+=1
'''
"""
WAP to find the sum of first n natural numbers  using while loop
"""
"""
num=int(input("Enter number:"))
sum=0
i=1
while i<=num:
    sum +=i
    i+=1
print(sum)
"""
"""
WAP to find the factorial of given number using for loop
"""
"""
num=int(input("Enter number:"))
product=1
for i in range(1,num+1):
    product *= i
print(f"The factorial of {num} is {product}")
"""

"""
WAP to print the following pyramid pattern
  *
 ***
***** for n=3
# """
# rows=int(input("Enter number of rows:"))
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"*"*(2*i-1))

# *******************   Arko method    *******************************************
# rows=int(input("Enter number of rows:"))
# for i in range(1,rows+1):
#     print(" "*(rows-i),end="")
#     print("*"*(2*i-1),end="")
#     print(" ")
"""
WAP to print the following star pattern
*
**
*** for n=3
 """
"""
rows=int(input("Enter number of rows:"))
for i in range(1,rows+1):
    print("*"*i)
"""
"""
# -----------------Square Pattern printing------------------------------
print this pattern
  * * *
  *   *    for n=3
  * * *
"""
"""
rows=int(input("Enter number of rows:"))
for i in range(1,rows+1):
    if(i == 1 or i == rows):
        print("*"*rows)
    else:
        print("*"+" "*(rows-2)+"*")
"""
"""
WAP to print multiplication table of n using for loops in reverse order.
"""
"""
num=int(input("Enter numbers:"))
for i in range(1,11):
    print(f"{num} X {11-i}= {num*(11-i)}")
"""
