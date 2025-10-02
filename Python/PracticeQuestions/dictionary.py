"""
🔹###### Dictionary (5)  ########

# 1.Count the frequency of each character in a string using a dictionary.
----------------------------------------------------------------------------------------------
# Program to count frequency of each character
str="banana" # initializing string for count
freq={} # empty dict 
for ch in str:   # checking one by one using loop
    freq[ch]=freq.get(ch,0)+1 
print(freq)
===========================================================================================
# 2.Merge two dictionaries, summing values for common keys.

d1,d2={"a":1,"b":4,"c":5},{"a":5,"c":6}
res=d1.copy()
for k,v in d2.items():
    res[k]=res.get(k,0)+v
print(res)
# ==========================================================================
# 3.Find the key with the maximum value in a dictionary.

dic={"a":5,"b":15,"c":23,"d":2}
print(max(dic,key=dic.get))
# ======================================================================
# 4.Create a dictionary from two lists: one for keys, one for values.

keys=["a","b","c","d"]
val=[4,5,6,10]
dic=dict(zip(keys,val))
print(dic)
print(max(dic,key=dic.get))
# ==========================================================================
# 5.Invert a dictionary (swap keys and values).
d = {"a": 1, "b": 2}
print({v: k for k, v in d.items()})
"""
