"""
Instance attributes state preference over class attributes during assignment and retrival
->first check instance attribute if present then it print instance attr 
->otherwise it check class attr if yes then it print class attr else print error
"""
# for example
"""
class Employee:
    language="Python" # this is  a class attribute
    salary=1200000
sid =Employee()
sid.language="JavaScript" # this is an instance attribute
print(sid.language,sid.salary) # here Instance attributes printed ignoring class attributes
"""

"""
Self parameter:
self refer to the instance of the class.It automatically passed with a function call from
an object.
sid.getSalary() #here self is sid
# The equivalent to Employee.getSalary(sid)
for exmaple:
"""
class Employee:
    language="python"
    salary=1200000

    def getInfo(self):
        print(f"Name:{self.name} \nLanguage:{self.language} \nSalary:{self.salary}")
    def greet(self): 
        #if self isn't given.Employee.greet() takes 0 positional arguments but 1 was given
        print("Good Salary bro !!") # so it is essential to pass self 
    def purpose(self):
        print("I love Python.")
 #  if i don't want to pass self para so it should be declared static
# for eg.  @staticmethod before the function the function begins
#  It doesno't require class & instance attributes
    @staticmethod
    def Greet():
        print("Hello Python AI engineer.")

sid=Employee()
sid.name="Sid-Gupta" # this is instace attribute
Employee.getInfo(sid)
sid.greet()
sid.purpose()
sid.Greet()

