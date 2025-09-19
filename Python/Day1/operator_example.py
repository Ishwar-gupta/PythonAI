
# Assignment operator
a=5 
b=6
c=a+b
print(c)

c +=3
print(c)
c -=5
print(c)
c /=3
print(c)
# ----------------comparison operator----------------------------------------
z=5<4
x=5>4
y=5>5
print(z,x,y)
z=5!=4
x=5==5
print(z,x)

# ----------------------------Logical Operators-------------------------------------------

e=True or False  # this is like OR gate which is true if any one is true
print(e) #True

# Truth  Table of 'or'

print("True or True is",True or True)#True
print("True or False is",True or False)#True
print("False or True is",False or True)#True
print("False or False is",False or False)#False

e=True and False  # this is like AND which is only true if both are true otherwise false
print(e)

# Truth  Table of 'and'

print("True and True is",True and True)#True
print("True and False is",True and False)#False
print("False and True is",False and True)#False
print("False and False is",False and False)#False

# Not operator
print(not(False))#True
print(not(True))#False
