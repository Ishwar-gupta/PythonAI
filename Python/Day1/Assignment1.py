"""
--------------------------Quiz Time:------------------------------ 
************Problem based on the loops**********************************
----------------------Q.N.1---------------------------
what is the output of the following program
for i in range(2,10,2):
    print(i,end="")
"""
"""
for i in range(2,10,2):
    print(i,end=" ")# it print from 2 to 10 but not 10 itself with jump-size of 2 numbers
    # i.e 2 4 6 8
"""
"""----------------------Q.N.2---------------------------
WAP to print all even numbers between 1 and 50.
"""
"""
for i in range(1,51):
    if(i%2==0):
        print(i,end=" ")
"""
# using while loop
"""
i=2
while(i<51):
    print(i,end=" ")
    i +=2
"""
"""----------------------Q.N.3---------------------------
# What is the difference between break and continue in loops?
Ans: break statement terminates the entire loop when encountered but
     continue statement skip the specific iteration when encountered
"""
"""

************Problem based on the tuples**********************************

Q.N.1   which of the following is true about tuples?
a.)Tuples are immutable
b.)Tuples allow duplicate values
c.)Tuples are defined using ()
d.)All of the above
Ans: option d 
"""

# Q.N.2 convert the list[10,20,30] into tuple in python
"""
list=[10,20,30]
print(tuple(list))  # (10,20,30)
"""
"""
Q.N.3 What happens if you try to change a value in a tuple? show with code

a=(10,20,"Siddhu","Python",100,"Hours")
# What if i want to change the python course with Java in tuple
# a[2]="Java"#it throws an TypeError:'tuple' object doesn't support item assignment
a(2)="Java"# cannot assign to function call here
print(a)

"""
"""
************Problem based on the lists**********************************
----------------------------------------------------------
Q.N.1.) What is the output of the following code?
lst=[1,2,3]
lst.append([4,5])
print(len(lst))
a.)3   b.)4    c.)5     d.)Error
Ans: option b i.e 4 becoz append values takes as 1 element not 2 element
output:[1,2,3,[4,5]]
--------------------------------------------------------
Q.N.2.)WAP to remove duplicates from a lists.
We can remove duplicates using set()(order not preserved)
lst=[1,2,4,2,5,6,2,1,6,7,3]
print(list(set(lst)))
# uniqueList=list(set(lst))
# print(uniqueList)
-----------------------------------------------
Q.N.2.) Explain the difference between append() and extend() with examples
*******************   append()  ***********************
append(): 
-> add a single element(obj) at the end of the list
->even if we pass a list,it will add the whole list as one element
for e.g
list1=[1,2,3]
list1.append([4,5])
print(list1)#[1,2,3,[4,5]] here [4,5] is added as a single element
print(len(list1)) #output:4

*******************   extend()  ***********************
extend():
-> Adds multiple elements(iterable) to the list
-> If we pass a list ,it will add each item individually
for e.g
list2=[1,2,3]
list2.extend([4,5])
print(list2)#[1,2,3,4,5] here [4,5] is added separately
print(len(list2)) #output:5

"""
"""
************Problem based on the dictionaries    **********************************
----------------------------------------------------
Q.N.1) What will be the output ?
d={
    "a":1,
    "b":2
}
print(d.get("c",5))

a.)1    b.)2   c.)5    d.)None
Ans: option c(5)
--------------------------------------------------------------
Q.N.2) Write a python dictionary for storing student names as keys and marks as values.
Then print the student with highest marks.
students={
    "Rajiv":75,
    "Rohit":85,
    "Shittal":95,
    "Sid":84
}
topStudents=max(students,key=students.get)
print(f"Students with highest marks is: {topStudents} with {students[topStudents]} marks")
------------------------------------------------------------------
Q.N.3) What is the difference between dict.get(key) and dict[key]
********    dict.get(key):  ******************
->if key exists,it returns the value
->if key doesn't exist,it simply return None or default value if provided
->safer when we aren't sure if the key exists
********     dict[key]:   *************
->if key exists,it returns the value
->if key doesn't exist,it raises a KeyError
->Use when we are sure the key exists
students={
    "Siddhu":85,
    "Suman":75
}
print(students.get("Siddhu"))# 85
print(students.get("Hari"))# None
print(students.get("Junnu",90))#90(default value)
print(students["Siddhu"])#85
print(students["junnu"])#KeyError
"""
"""
************   Problem based on the Strings    **********************************
-----------------------------------------------------------
Q.N.1) What is the output of:
s="Python"
print(s[::-1])
a.)Python   b.)nohtyP   c.)Error    d.)  Pyt
Ans:option b(nohtyP)
---------------------------------------------------
Q.N.2) WAP to count vowels in a given string.
str=input("Enter any string:")
vowel=0
for i in range(0,len(str)):
    if str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u":
        vowel +=1
    else:
        False
print(f"Sting contains: {vowel} vowels count")
---------------------------------------------------------
Q.N.3) Explain the difference between isalpha() and isdigit() methods of Strings
************************   isalpha()   *******************************
-> Checks if all characters in a string are alphabetic(A-Z ,a-z) not even numeric values
->Return type:Boolean i.e true or false
->It'll return False if the string contains spaces,numbers or symbols
# print("Hello".isalpha())# True(only alphabet)
# print("Hello123".isalpha())#False(contains number)
# print("Hii!!".isalpha())#False(contains symbols '!')
************************   isdigit()   *******************************
->Checks if all characters in a string are digits(0-9). not even alphabetic symbol
->ReturnType:Boolean i.e Ture or False
->Works only for Numeric characters,not for alphabets or symbols

# print("1234".isdigit())#True (only numeric)
# print("12a456".isdigit())#False(contains alphabets)
# print("123!@456".isdigit())#False(contains symbol)
"""
"""
************   Problem based on the Sets    **********************************
Q.1) Which of the following statements is false about sets?
a.)Sets are unordered            b.)Sets allow duplicate values
c.)Sets are mutable              d.)Sets are defined using {}
Ans: option b 
--------------------------------------------------------------------
Q.2) Write a python program to find the union and intersection of two sets
set1={1,2,3,4}
set2={2,3,5,6,7}
print("Set1 =",set1)
print("Set2 =",set2)
print("\nUnion =",set1.union(set2))
print("Intersection =",set1.intersection(set2))
------------------------------------------------------------------------------
Q.3) What is the ouput ?
s={1,2,3}
s.add(2)
print(s) # 2 is already exists in the set s so output :s={1,2,3} is same
"""




# ******************************Q.N.1********************************************
# ------------Write a program to find the given number is prime or not-----------------------
"""
num=int(input("Enter number:"))
if num <= 1:
    print(f"{num} isnot prime.")
else:
    for i in range(2,num):
        if num % i ==0:
            print(f"{num} isnot prime.")
            break
        else:
            print(f"{num} is prime.")
            break
"""

"""
# ---------------------Q.N.2--------------------
Build a simple temperature converter(Celsius to Fahrenheit).Without using function
"""
"""
celsius=int(input("Enter degree celsius:"))# userInput of Celsius
fahrenheit=(celsius*9/5)+32 # conversion formula of C to F
print(f"Temperature in Fahrenheit:{fahrenheit} F")
"""

"""
# -----------------------------Q.N.3------------------------------
Print a multiplication table for any given number.
"""
"""
# taking input
num=int(input("Enter number:"))
for i in range(1,11):  # this loop execute from 1 to 10 only
    print(f"{num} * {i} = {num*i}")# multiplication table using userInput
"""
"""
# -----------------------Q.N.4----------------
Find all numbers divisible by 7 but not a multiple of 5 between 1000-3000
"""
"""
for i in range(1000,3001):
    if i%7==0 and i%5 != 0:
        print(f"{i} is divisible by but not multiple of 5.")
        # print(i,end=" ")
"""
"""
# --------------------Q.N.5----------------------------------------
Pattern printing  a.) pyramid  b.)diamond   c.)Pascal's triangle
"""
"""
rows=int(input("Enter number of rows:"))
for i in range(1,rows+1):
    print(" " * (rows - i) + "*" * (2*i-1))
"""
"""********************** Diamond Problem  ***********************
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
"""
"""
rows = int(input("Enter number of rows: "))
for i in range(rows):
    print(" " * (rows - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
"""
"""
*************  Challenge Project: Create a mini student grading system (input marks, 
    calculate average, assign grades).***********************************************
n = int(input("Enter number of students: "))

for s in range(1, n + 1):
    print("\nStudent", s)
    marks = []
    subjects = int(input("Enter number of subjects: "))
    
    total = 0
    for i in range(subjects):
        m = float(input("Enter marks of subject " + str(i + 1) + ": "))
        marks.append(m)
        total += m
    
    avg = total / subjects
    print("Average Marks:", avg)
    
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print("Grade:", grade)

"""
