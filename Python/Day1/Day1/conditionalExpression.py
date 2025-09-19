# # Some basic problem based on if/else statement
# # a=int(input("Enter your age:"))
# # if(a>=18):
# #     print("You are the above the 18.")
# #     print("Good fand you!!.")
# # else:
# #     print("You are the below the 18.")

# # print("End of program.")

# # multiple conditional statement

# a=int(input("Enter your age:"))
# if(a>=18):
#     print("You are above the 18")
#     print("Good  fand You !!")
# elif(a<0):
#     print("Invalid Input(negative age isnot valid) !!")
# elif(a==0):
#     print("you are entering negative age.")
# else:
#     print("You are below  18")

# -------Practice Question------------------------------------
# -----------------------Q.N.1-----------------------------
# WAP to find the greatest of four numbers entered  by the user
"""
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))

# checking greatest numbers among 4 numbers
if(a>b and a>c and a>d ):
    print(a,"is greatest")
elif(b>a and b>c and b>d):
    print(b,"is greatest.")
elif(c>a and c>b and c>d):
    print(c,"is greatest.")
else:
    print(d,"is greatest.")

"""
# -----------------------Q.N.2-----------------------------
# WAP to find out whether a student has passed or failed if it  requires a total of 40%
#  and at least 33% in each subject to pass.Assume 3 subjects and take marks as userInput
"""
marks1=int(input("Enter marks1:"))
marks2=int(input("Enter marsk2:"))
marks3=int(input("Enter marks3:"))
total_percentage=(100*(marks1+marks2+marks3))/300
if(total_percentage >= 40 and marks1 >= 33 and marks2>=33 and marks3>=33):
    print("You are passed with ",total_percentage)
else:
    print("You are failed with ",total_percentage)

"""
"""
# -----------------------Q.N.3-----------------------------
A spam comment is defined as a text containing following keywords.
"make a lot of money","buy now","subscribe this","click this".
WAP  to detect these spams
"""
"""
p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("Enter your comments:")
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is a spam")
else:
    print("This comment is not spam.")    
    """
"""
# -----------------------Q.N.4-----------------------------
WAP to find whether a given username contains less than 10 characters or not
"""
"""
userName=input("Enter your username:")
if(len(userName)<=10):
    print("Your username contains less than 10 characters.")
else:
    print("Your username contains more than 10 characters.")
    """
"""
# -----------------------Q.N.5-----------------------------
WAP which finds out whether a given name is present ina list or not.
"""
"""
l=["harry","rohan","divya","trishna","junnu"]
name=input("Enter your name:")
if(name.lower() in l):
    print("Your name is in the list")
else:
    print("Your name isnot in the list")
   """
"""
# -----------------------Q.N.6-----------------------------
WAP to calculate  the grade of a student from his marks from the following scheme:
90-100=> Ex  , 80-90 => A , 70-80=> B , 60-70=> C , 50-60=> D , <50 -> F
"""
"""
marks=int(input("Enter your marks:"))
if(marks <=100 and marks >=90):
    grade="Ex"
elif(marks <90 and marks >= 80):
    grade="A"
elif(marks <80 and marks >= 70):
    grade="B"
elif(marks <70 and marks >= 60):
    grade="C"
elif(marks <60 and marks >= 50):
    grade="D"
elif(marks <50 and marks >=0):
    grade="F"
else:
    grade="Invalid Input"

print(grade)
"""
"""
# -----------------------Q.N.6-----------------------------
WAP to find out  whether a given post is taking  about "Harry" or not
"""
"""
post=input("Enter the post:")
if("Harry".lower() in post.lower()):
    print("This post is talking about Harry:")
else:
    print("This post isnot talking about Harry:")
"""