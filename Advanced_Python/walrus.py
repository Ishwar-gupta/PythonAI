'''
The walrus operator (:=),introduced in python 3.8 allows you to assign values to variables
as part of an expression.This operator ,named for its resembelance to the eyes and tusks of
a walrus,is officially called the "assignment expression."

'''
# Using walrus opertor
if(n:= len([1,2,3,4,5,6]))>3:
    print(f"List is too long({n} elements,expected <=3)")

'''
# Types definitions in python
Type hints are added using the colon(:) syntax for variables and the -> syntax for function
return types.

e.g
n:int=5
name:str="Sid"
#Variable type hint:
age:int=25
# function type hint:
def greet(name:str)-> str:
    return f"Hello,{name}!!"
# usage
print(greet("Sid")) # output: Hello,Sid!!
'''
def sum(a:int,b:int) -> int:
    return a+b
print(sum(5,8))


'''
# ***************  Advanced TYPE Hints   ********************************
Python's typing module provides more advanced type hints,such as List,Tuple,Dict & Union
We can import List,Tuple,Dict & Union from typing module like this:
syntax: from typing import List,Tuple,Dict,Union
'''
from typing import List,Tuple,Dict,Union
# List of Integers
numbers:List[int]=[1,2,3,4,5]
# Tuples of a string & integer
person:Tuple[str,int]=("Sid",22)
# Dictionary with string keys & integer value
scores:Dict[str,int]={"Alice":90,"Sid":95}
# Union type for variables that can hold multiple type
identifier:Union[int,str]="ID123"
identifier=12345 #also valid

"""These annotations help in making the code self-documenting and allow developers to 
understand the data structures used at a glance."""