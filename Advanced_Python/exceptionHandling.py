'''try:
    age=int(input("Enter your age:"))
    print(age)
except Exception as e:
    print("Exception caught ,",e)
print("Program Continues.....")'''

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if b==0:
    raise ZeroDivisionError("Our program is not meant to divide numbers by zero.")
else:
    print(f"The division a/b is {a/b}")
