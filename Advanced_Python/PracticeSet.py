"""====================   Problm-1   ======================
WAP to  open three files if any these files arenot present ,a message without exiting the
program must be printed prompting the same.

try:
    with open("file1.txt","r") as f:
        print(f.read())
except Exception  as e:
    print(e)
        
try:
   with open("file2.txt","r") as f:
        print(f.read())
except Exception  as e:
    print(e)

try:
    with open("file3.txt","r") as f:
        print(f.read())
except Exception  as e:
    print(e)  

print("Program continues....")     
# ======================  Prblm -2  =====================
WAP to print third, fifth and seventh element from a list using enumerate function

list=[1,4,6,55,23,45,67,45,46,24,12]
for i,item in enumerate(list):
    if i==2 or i==4 or i==6:
        print(item)

# ====================== Prblm -3   =====================
Write a list comprehension to print a list which contains  the multiplication table of
a user entered number.


n=int(input("Enter a number:"))
table=[n*i for i in range(1,11)]
print(table)

# ====================== Prblm -4   ===========================
WAP to display a/b where a and b are integers.If b=0 ,display infinite by handlig the
'ZeroDivisionError'
try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")

# ====================== Prblm -5   ===========================
 Store the multiplication tables generated in prblm-3 in a file named Tables,txt
"""
n=int(input("Enter a number:"))
table=[n*i for i in range(1,11)]
with open("file1.txt","a") as f:
    f.write(f"Table of {n}: {str(table)}\n")
