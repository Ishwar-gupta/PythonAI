"""
🔹 String (5)

# 1.Check if a string is a palindrome.

string=input("Enter String to check palindrome :")
def palin(str):
    palin=str[::-1]  # reversing given string and store in palin 
    if(str == palin):
        print(str,"is palindrome.")
    else:
        print(str,"isnot palindrome")
palin(string.lower())

# 2.Count vowels and consonants in a string.

def count(text):
    vowels,consonant=0,0
    for ch in text.lower():
        if ch in "aeiou":
            vowels+=1
        else:
            consonant+=1
    print(f"vowels count:{vowels} \nConsonant count:{consonant}")
string=input("Enter string to count vowels & consonant:")
count(string)

# 3.Find the first non-repeating character in a string.

def non_repeating_char(str):
    # 1. counting frequency of each character
    freq={}
    for ch in str:
        freq[ch]=freq.get(ch,0)+1
    # 2. finding first character with frequency 1
    for ch in str:
        if freq[ch]==1: #
         return ch
    return None # i.e if characters are all repeating 
string=input("Enter string to find first non-repeating character:")
final=non_repeating_char(string.lower())
if final:
   print("First non-repeating character:",final)
else:
   print("No repeating character.")

# 4.Reverse the order of words in a string.

def reversOrder(words):
    print(words.split()) # split into list of strings
    print(words.split()[::-1]) # reverse the list of strings
    print(''.join(words.split()[::-1])) # print in reverse order without space
    print(" ".join(words.split()[::-1]))# print in reverse order with space
word=input("Enter string:")
reversOrder(word)

# 5.Replace every vowel in a string with *.
def replaceString(vowel):
    result=''
    for ch in vowel:
        if ch.lower() in "aeiou":
            result+="*"
        else:
            result+=ch
    return result
string=input("Enter string:")
print("Replaced String:",replaceString(string))


s = "Siddhu"
print("".join("*" if ch.lower() in "aeiou" else ch for ch in s))
"""