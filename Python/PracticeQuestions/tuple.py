"""
# 1.Swap two tuples without using a temporary variable.
a=(1,2)
b=(3,4)
a,b=b,a
print(a,b)"""
# *************************************************************************************
"""# 2.Find the element-wise sum of two tuples of the same size.
# tow tuples of same size
t1=(1,2,3,5,6)
t2=(9,8,4,3,5)
# Pair elements together using zip()
pairs=list(zip(t1,t2))
print(pairs)
# Adding each pair using list comprehension
result=[a+b for a,b in pairs]
print("Tuples after adding each pair of list:",tuple(result))"""
# ************************************************************************
"""# 3.Check whether a tuple is a palindrome.
# ========  In Python, slicing with [::-1] means:=======================
=> Start from the end
=> Step backwards
=> Until the beginning

tup=(1,2,3,2,1)
if(tup==tup[::-1]): # [::-1] start from end and step backward until the beginning
    print("palindreome.")
else:
    print('Not palindrome.')

tup=("LEVEL")
tupl=("siddhu")
print(tup==tup[::-1]) # True
print(tupl==tupl[::-1]) #False
"""
"""# 4.Find the maximum and minimum elements in a tuple without using max() or min().

tup=(1,23,4,34,67,90,55,5,43)
maxValue=tup[0]
minValue=tup[0]
for x in tup:
    if(x>maxValue):
        maxValue=x
    if(x<minValue):
        minValue=x
print("maxValue:",maxValue,"\n","MinValue:",minValue)

tup=(1,23,4,34,67,90,55,5,43)
print("MaxValue:",max(tup))
print("MinValue:",min(tup))

# 5.Convert a list of tuples into a dictionary (e.g., [("a",1),("b",2)] → {"a":1,"b":2}).

list=[("name",'Sid'),("age",22),("profession","engineer")]
print(dict(list))
"""