# a=(1,45.5,"Apple",45.5,2,1,'A',"Siddhu","Harry",'C','A', False,True,"Cherry")
# print(type(a))  # class <tuple>
# print(a)
# num=a.count(45.5)# it count how many times the given value exists in tuples
# print(num)
# print(a.count('A'))
# # var.index(value)// it returns the first occurence index in tuples
# print(a.index(False))#11
# print(a.index("Apple"))#2

# ----------------------------------------------------------------
'''
📌 Other Useful Built-in Functions for Tuples

(Not methods, but often used with tuples):

len(t) → Returns number of elements.

max(t) → Returns maximum element.

min(t) → Returns minimum element.

sum(t) → Returns sum of all elements (if numeric).

sorted(t) → Returns a sorted list (not tuple).
'''
# t = (5, 1, 8, 3)

# print(len(t))      # 4
# print(max(t))      # 8
# print(min(t))      # 1
# print(sum(t))      # 17
# print(sorted(t))   # [1, 3, 5, 8]
# ---------------------------------------------------------------------
'''
🔹 7. tuple() Constructor

Convert other iterables (list, set, string) into a tuple.
'''
# print(tuple([1, 2, 3]))    # (1, 2, 3)
# print(tuple("hello"))      # ('h', 'e', 'l', 'l', 'o')
# --------------------------------------------------------------------
''' Slicing and  Concatenation '''
'''
t = (10, 20, 30, 40, 50)
print(t[1:4])     # (20, 30, 40)

t2 = t + (60, 70)
print(t2)         # (10, 20, 30, 40, 50, 60, 70)

'''
# -------------------------------------------------------------------
'''    Membership test (true or false)   '''

"""
colors = ("red", "green", "blue")
print("green" in colors)   # True
print("yellow" not in colors)  # True

"""
# --------------------------------------------------------
"""
🔹 1. Tuple Unpacking

Unpacking lets you assign multiple values at once.
"""
"""
# Example 1: Unpacking tuple into variables
person = ("Alice", 25, "Engineer")
name, age, profession = person
print(name)      # Alice
print(age)        # 25
print(profession) # Engineer

# Example 2: Swapping values using unpacking
a, b = 10, 20
a, b = b, a
print(a, b)   # 20 10

"""
"""
def get_user():
    return ("Alice", 25, "Engineer")
, age, role = get_user()   # tuple unpacking
print, age, role)
# Output: Alice 25 Engineer

"""
# ----------------------------------------------------------------------------
"""
🔹 2. zip() with Tuples

Pairs elements from multiple iterables — often used for combining data.
"""
#=("Siddhu","Shittal","Rohit","Rajiv")
# marks=(88,90,89,82)
# combined=list(zip,marks))
# print(combined)
#,marks=zip(*combined)
# print)
# print(marks)
"""s = ("Alice", "Bob", "Charlie")
marks = (85, 90, 78)

# Pairs with marks
combined = list(zips, marks))
print(combined)
# Output: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

# Convert back to separate lists
n, m = zip(*combined)
print(n)  # ('Alice', 'Bob', 'Charlie')
print(m)  # (85, 90, 78)
"""

"""
3. enumerate()

Gives index along with the element while looping
"""
# marks = ("apple", "banana", "cherry")

# for index, fruit in enumerate(marks):
#     print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry
# marks=("apple","banan","cherry","berry")
# for index, fruit in enumerate(marks):
#     print(index,fruit)

"""
🔹 4. map()

Applies a function to each element in a sequence.
"""
# numbers=(1,2,3,4,5,6)
# squares=tuple(map(lambda x:x**2,numbers))
# print(squares)

# strings=list(map(str,numbers))
# print(strings)

"""
filter():
filter out elements based on condition
"""
# numbers=(1,2,3,4,5,6)
# even=tuple(filter(lambda x:x%2==0,numbers))
# print(even)
# greaterNum=list(filter(lambda x:x>3,numbers))
# print(greaterNum)

# -------------------------- Practice Time  -1   -------------------------------
#  WAP to store seven marks in a list  entered by the user
'''
marks=[]
f1=int(input("Enter marks:"))
marks.append(f1)
f2=int(input("Enter marks:"))
marks.append(f2)
f3=int(input("Enter marks:"))
marks.append(f3)
f4=int(input("Enter marks:"))
marks.append(f4)
f5=int(input("Enter marks:"))
marks.append(f5)
f6=int(input("Enter marks:"))
marks.append(f6)
f7=int(input("Enter marks:"))
marks.append(f7)
print(marks)
'''

# -------------------------- Practice Time  --2  -------------------------------
# WAP to accept marks of 6 students and display  them in a sorted manner
"""
marks=[]
f1=int(input("Enter marks:"))
marks.append(f1)
f2=int(input("Enter marks:"))
marks.append(f2)
f3=int(input("Enter marks:"))
marks.append(f3)
f4=int(input("Enter marks:"))
marks.append(f4)
f5=int(input("Enter marks:"))
marks.append(f5)
f6=int(input("Enter marks:"))
marks.append(f6)
marks.sort()
print(marks)
"""
# -------------------------- Practice Time   -3   -------------------------------
# Check that tuple cannot be  changed in python
# a=(934,,234,"sid")
# a[2]="Siddhu"
# print(a)# hence this type can't be changed

# -------------------------- Practice Time    -4-------------------------------
# WAP to sum a list with 4 numbers
# list=[1,4,5,2,3]
# print(sum(list))

# -------------------------- Practice Time    -5-------------------------------
# WAP to count the number of zeros in the following tuple:
# a=(7,0,8,0,0,9)
# a=(7,0,8,0,0,9)
# print(a.count(0))#3

