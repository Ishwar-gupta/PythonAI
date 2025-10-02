'''
# 1.Find the intersection of two sets without using &.

s1,s2={1,2,3,4},{3,4,5,6}
print({x for x in s1 if x in s2})
# or
s1,s2={1,2,3,4},{3,4,5,6}
print(s1.intersection(s2))

# 2.Check if one set is a subset of another.

s1,s2={1,2},{1,2,3,4,5}
print(s1.issubset(s2)) #True

# 3.Remove elements from a set that are divisible by 3.

s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
print({x for x in s if x % 3 !=0})

# 4.Find the symmetric difference between two sets.
s1,s2={1,2,3},{3,4,5}
print((s1-s2) | (s2-s1)) # it removes the common element between two or more sets

# 5.Convert a list with duplicates into a set and back into a sorted list.

s={1,8,3,6,2,3,8,4,6,8,10,3,45,98}
print(sorted(set(s)))
'''