""" ************  Dictionary Merge & update operators
New operators |and| =allow for merging and updating dictionaries
"""
dict1:dict[str,int]={'a':1,'b':5,'c':3}
dict2:dict[str,int]={'b':3,'c':4}
merged=dict1 | dict2
print(merged)

"""
We can now use multiple context managers in a single with statement more cleanly using
the parenthesised context maanager
with(
    open('file1.txt','r') as f1,
    open('file2.txt','r') as f2
):

"""