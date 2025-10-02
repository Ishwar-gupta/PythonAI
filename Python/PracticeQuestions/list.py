"""**************  Mid-Level list problem  ***************************************"""
# 1. Write a Python program to find the second largest number in a list.
"""
lst = [10, 20, 4, 45, 99]
num=set(lst)
print(sorted(num)) # [4,10,20,45,99]
print("The second largest number is: " ,sorted(num)[-2])
"""
# 2. Remove all duplicate elements from a list while preserving the order.
"""
lst = [1, 2, 2, 3, 4, 4, 5]
res=[]
for i in lst:
    if i not in res:
        res.append(i)
print(res)
# Another method using set()
lst = [1, 2, 2, 3, 4, 4, 5]
print(list(set(lst)))
"""
# 3.Rotate a list by k positions to the right.
"""
lst=[1,2,3,4,5,6,7]
k=4
k=k %len(lst)
print(lst[-k:] + lst[:-k])
"""
# 4.Find all pairs of numbers in a list that sum to a target value.
"""
lst=[2,3,4,5,6,7,1,8]
target=9
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if (lst[i] + lst[j]) == target:
            print(lst[i],lst[j])
"""
# 5. Flatten a nested list (e.g., [[1,2],[3,4],[5]] → [1,2,3,4,5]).
"""
nested=[[1,2],[3,4],[5]]
flat=[]
for sub in nested:
    for x in sub:
        flat.append(x)
print(flat)
"""
# Another Method i.e direct method
"""
nested=[[1,2],[3,4],[5]]
flat=[x for sub in nested for x in sub]
print(flat)
"""