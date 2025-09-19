"""
***********************    _INIT_CONSTRUCTOR    *****************************************
->  _init_() is a special method which is first run as soon as the object is created
-> _init_()method is also known as constructor
-> it takes self-argument and can also take further arguments
for example:
class Employee:
    def _init_(self,name):
        self.name=name
    def getSalary(self):
        .....
sid = Employee("Trishnaa")
"""
"""
class Employee:
    language="Python"
    salary=1200000
    
    def __init__(self): # _init_ is an dunder method that gets automatic called on object creation
        # self.name=name
        # self.salary=salary
        # self.language=language
        print("Constructor is called.")

sid=Employee()
sid.name="Siddhu"
print(sid.name,sid.language,sid.salary)
junnu=Employee()
"""
"""
class Employee:
    language="Python"
    salary=1200000
    
    def __init__(self,name,language,salary): # _init_ is an dunder method that gets automatic called on object creation
        self.name=name
        self.language=language
        self.salary=salary
        print("Constructor is called.")

sid=Employee("Siddhu","JavaScript",1300000)
# sid.name="Siddhu"
print(sid.name,sid.language,sid.salary)
"""

"""*********************   Practice -set -chapter-10  *************************
Q.1) Create a class "Programmer" for storing information of few programmers working
class Employee:
    company="Microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e1=Employee("Ishwar-Gupta",5000000)
print(e1.name,e1.salary,e1.company)
e2=Employee("Rajeev",3000000)
print(e2.name,e2.salary,e2.company)
at Microsoft."""
# ------------------------------------------------------------------
""" Q.2) Write a class "calculator" capable fo finding square ,cube and
 square root of a number:

 class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square of {self.n} : {self.n**2}")  # (self.n * self.n)
    def cube(self):
        print(f"The cube of {self.n} : {self.n * self.n * self.n}")
    def squareRoot(self):
        print(f"The squareRoot of {self.n} : {self.n**0.5}")
a=Calculator(16)
a.square()
a.cube()
a.squareRoot()"""
# ----------------------------------------------------------------------------------------
""" Q.3) Create a class with a class attribute a; create an object from it & set 'a' directly
using object.a=o.Does the change the class attribute? 

class Demo:
    a=5
obj=Demo()
print(obj.a) # 5 it print class attribute
obj.a=0
print(obj.a) # 0 it print assigned instance attribute

print(Demo.a) # 5 that's why class attribute doesnot change throughout it's life
# --------------------------------------------------------------------------------------
"""
"""
Q.4) Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square of {self.n} : {self.n**2}")  # (self.n * self.n)
    def cube(self):
        print(f"The cube of {self.n} : {self.n * self.n * self.n}")
    def squareRoot(self):
        print(f"The squareRoot of {self.n} : {self.n**0.5}")
    # Adding static method to greet the user with hello
    @staticmethod
    def greet():
        print("Hello there !!")
a=Calculator(16)
a.square()
a.cube()
a.squareRoot()
a.greet()
# ----------------------------------------------------
"""
"""
Q.5) Write a class Train which has methods to book a ticket ,get status(no of seats) and
get fare information of train running under Indian Railways.
Q.6)Can you change the self-parameter inside a class to something else(say "sid").Try
changing self to "slf" or "sid" and see the effects.

"""