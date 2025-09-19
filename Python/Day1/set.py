# # set()
# #  e=set() # empty set not a empty dionary which is defined by e={}
# #  simeple example of set  in python
# # e=set()
# # print(e ,type(e))
# # repetition is not allowed in  set
# # s={ 1,5,2,34,55,23,11,56}
# # print(s,type(s))
# # s.add(0)
# # s.add(100)
# # print(s)
# # s.pop()
# # s.clear()# it clear all the element of the set

# # print(s)


# """
# 🔹 Basic Operations

# add(elem) → Adds an element to the set.

# remove(elem) → Removes an element; raises KeyError if not found.

# discard(elem) → Removes an element if present (no error if absent).

# pop() → Removes and returns an arbitrary element.

# clear() → Removes all elements from the set.

# copy() → Returns a shallow copy of the set.
# """
# """
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A.union(B))                # {1, 2, 3, 4, 5}
# print(A.intersection(B))         # {3}
# print(A.difference(B))           # {1, 2}
# print(A.symmetric_difference(B)) # {1, 2, 4, 5}

# A.add(6)
# A.remove(2)
# print(A)  # {1, 3, 6}
# """
# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A.union(B))
# print(A.intersection(B))
# print(B.intersection(A))
# print(A.difference(B))
# print(B.difference(A))
# print(A.symmetric_difference(B))# it removes the common element from both sets
# print(A.symmetric_difference_update(B))

#  -----------   Practice Time -----------------------------------------------
#   ------------------------Q.N.1-----------------------------
# # WAP to create dionary hindi words with values as their English translation user input
# words ={
#     "kursi":"Chair",
#     "billi":"Cat",
#     "Sep":"Apple"
# }
# addedInput=input("Enter words you want meaning of :")
# print(words[addedInput])

#   ------------------------Q.N.2-----------------------------
# wap to input eight numbers from the user and display all the unique numbers(once)
# s=set()
# n=input("Enter number:")
# s.add(int(n))
# n=input("Enter number:")
# s.add(int(n))
# n=input("Enter number:")
# s.add(int(n))
# n=input("Enter number:")
# s.add(int(n))
# n=input("Enter number:")
# s.add(int(n))
# n=input("Enter number:")
# s.add(int(n))
# n=input("Enter number:")
# s.add(int(n))
# n=input("Enter number:")
# s.add(int(n))
# print(s)
#   ------------------------Q.N.3-----------------------------
# Can we have a set with 18(int) and '18'(str) as a value in it ?
# s=set()
# s.add(18)
# s.add(18.0)
# s.add('18')
# print(s,len(s)) # yes len: 2
#   ------------------------Q.N.3-----------------------------
# create a empty dionary.Allow 4 friends to enter their favourite language as 
# value and use keys as their name:.Assume that name: are unique.
"""
d={}
name=input("Enter friends name:")
lang=input("Enter language name:")

d.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language name:")

d.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language name:")

d.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language name:")

d.update({name:lang})
print(d)
"""
# can we change the value inside a list which is contained in set S?
# s={ 8,7,12,"sid",[1,2]}
# s={ 8,7,12,"sid",[1,2]}
# we cannot change the value inside a list becoz it is immutable and not hashable



















