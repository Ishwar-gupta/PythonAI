# Strings are immutable which means that :-
# we can't change them bu running functions on them

# str="sid"
# # str2='junnu'
# # str3='''trishna'''
# # print(str,str2,str3)

# # Indexing of the string
# str="junnu"
# # printing particular string index
# print(str[4])
# # printing string from starting index to final index 
# # using colon but final index is neglected and also run after final index is not found
# res=str[0:6]
# print(res)
# # it also takes negative index and counted as reversed but output is in forward order
# print(str[-4:-1])# it is same as str[1:4]
# print(str[2:4])
# print(str[:4])#it is same as str[0:4]
# print(str[2:])#it is same as str[2:5]


# # slicing with skip value
# #it first slice from starting to second one index then from result
# #  it jumps to that times where 3rd index is given
# word="amazing"
# print(word[1:6:2])# output:mzn
# """
# how does it works:
# firstly it slice from 1 to 6th index as 
# --word[1:6]  #i.e mazin
# secondly it jumps after every 2 character which is specified as 2 i.e word[1:6:2]
# --we get mzn as output
# """

# checking length:  len(str) or endswith() or startswith() function
"""
str="trishnna"
print(len(str))# 8
print(str.startswith("tri"))#True
print(str.endswith("nna"))#True
print(str.startswith("shn"))#False
print(str.endswith("ish"))#False
# capitalize the first word only
print(str.capitalize())#trishnna is capitalize as Trishnna
"""

# --------------------Practice-Time------------------------------------
# 1.) WAP to display a user entered name followed by Good Afternoon using input() function
# name=input("Enter your name:")
# print(f"Good Afternoon {name}")# f"{var}" is fstring without f it doesnot work 

# 2.) WAP to fill in a letter template given below with name and date
'''
letter="""
    Dear <|Name|>,
    You are selected
    <|Date|>
    """
'''

# letter="""
#     Dear <|Name|>,
#     You are selected
#     <|Date|>
#     """
# print(letter.replace("<|Name|>","Siddheshwar").replace("<|Date|>","8 sep,2025"))

# 3.) WAP to detect double space in a  string.
# name="hello this is  siddhu gupta   "
# print(name.find("  "))# 13 if double space not found it return -1 as output
# print(name.find("dhu"))

# 4.) WAP to replace the double space from problem 3 with single spaces.
# name="hello this is  siddhu gupta   "
# print(name.replace("  "," "))

# 5.) WAP to format the following letter using escape characters
"""
letter = "Dear Harry , this python course is nice."
"""
letter = "Dear Harry,\n This python course is nice.\n Thanks!!"
print(letter)












