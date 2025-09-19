"""
A file is data stored in storage device.A python program can talk to the file by reading
content from it and writing content to it.
"""
# For reading a existing file 
"""
f=open("File.txt")
data=f.read()
print(data)
f.close()
"""

# ********  for writing into file  *******
"""
str="I am Siddhu as Sid"
f=open("Poem.txt","w")
f.write(str)
f.close()
"""
"""
We can also use f.readline()function to read one full line at a time
e.g 
f.readline() # Read one line from the file
"""
"""
f=open("File.txt","r")
data=f.read()
print(data,type(data)) # class <list>
f.close()
"""
# Appending to existed file i.e append mode
"""
str="I am also a web developer."
f=open("File.txt","a+")
data=f.write(str)
print(data)
f.close()
"""
"""
Reading all the data line by line using loop statement
"""
"""
f=open("File.txt","r")
line=f.readline()
while(line != ""):
    print(line)
    line=f.readline() #if we don't declare this statement then infinite loop will executed
"""
"""
# Different modes in file handling
r-> open for reading
w-> open for writing
a-> open for appending
+-> open for updating
'rb'->will open for read in binary mode
'rt'-> will open for read in text mode
"""
"""
******   With Statement *********
The best way to open and close the file automatically is the "with" statement

# open the file in read mode using 'with' ,which automatically closes the file
# using with statement no needs to close the file explicitly
 
with open("this.txt" , "r") as f:
    # Read the contents of the file
    text=f.read()

# print the contents
print(text)
"""
"""
with open("File.txt","r") as f:
    # print(f.read()) 
    text=f.read()
    print(text)  # no needs to close the file explicitly
"""
"""
***********************   Practice - Set   ****************************
Q.1)WAP to read the text from a given file 'poem.txt' and find out whether it contains
the word 'twinkle' or not
"""
"""
f=open("Poem.txt","r")
content=f.read()
if("Twinkle" in content):
    print("The word twinkle is present in the content.")
else:
    print("The word twinkle isnot present in the content.")
f.close()
"""
"""
# using with statement
with open("Poem.txt","r") as f:
    content=f.read()
    if("Twinkle" in content):
        print("The word twinkle is present in the content.")
    else:
        print("The word twinkle isnot present in the content.")
f.close()
"""
"""
***************** Q.2) ********************************
The game() function in a program lets a user play a game and returns the score as an 
integer.You need to read a file "Hi-score.txt" which is either blank or contains the 
previous Hi-score.You need to write a program to update the High-score whenever the 
game() breaks the Hi-score
"""
"""
import random
def game():
    print("You're playing the game.")
    score= random.randint(1,62)
    # Fetch the high-score
    with open("Hi-score.txt","r") as f:
        highscore=f.read()
        if highscore != "":
            highscore=int(highscore)
        else:
            highscore=0

    print(f"Your score: {score}")
    
    if(score > highscore):
        # write this highscore to the file
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    return score
game()
"""
# -------------------------------   Using exception handling   -----------------------

"""
import random
def game():
    print("You're playing the game.")
    score = random.randint(1,62)
    # Fetch the high-score
    try:
        with open("Hi-score.txt","r") as f:
            highscore = f.read()
            if highscore != "":
                highscore = int(highscore)
            else:
                highscore = 0
    except FileNotFoundError:
        highscore = 0

    print(f"Your score: {score}")
    
    if score > highscore:
        # write this highscore to the file
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    return score

game()
"""
"""
Q.3)WAP to generate multiplication tables from 2 to 20 and write it to the different
files.Place these files in a folder for f13 year old.
"""
"""
def generateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)
for i in range(2,21):
    generateTable(i)
"""
""" 
************************   Q.4)   ********************************************************
A file contains a word "Donkey" multiple times.You need to write a program which replace
this word with ### by updating the same file.
word="Donkey"
with open("File.txt","r") as f:
    content=f.read()
newContent=content.replace(word,"######")
with open("File.txt","w") as f:
    f.write(newContent)
    print(newContent,"written successfully")
"""
"""
Q.5)  *****************************************************
 Repeat program 4 for a list of such words to be censored.
words=["Donkey","bad","nice","developer","studying"]
with open("File.txt","r") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#"*len(word))
with open("File.txt","w") as f:
    f.write(content)
    print(f"{content} is replaced successfully.")
"""
"""*********************************************************************
Q.6) WAP to mine a log file and find out whether it contains 'python'
with open("File.txt","r") as f:
    content = f.read()
if("python" in content):
    print("yes python is present.")# if there python word is present then it print
else:
    print("No python isnot present!! ")# if not present then not  print 
"""
"""***********************************************************
Q.7) WAP to find out the line number where python is present from Q.6)

with open("File.txt","r") as f:
    lines=f.readlines()

lineN0=1
for line in lines:
    if("python" in line):
        print(f"Yes Python is present in lineNum:{lineN0}")
        break
    lineN0 += 1
else:
    print("no python isnot present!!")
"""
"""*********************   Q.N.8)   ************************************
WAP to make a copy of a text file "this.txt"
with open("File.txt","r") as f:
    content=f.read()
with open("Poem.txt","w") as f:
    f.write(content)
"""
"""********************  Q.N.9)   ************************************
WAP to find out whether a file is indentical & matches the content of another file.

with open("File.txt","r") as f:
    content1=f.read()
with open("Poem.txt","r") as f:
    content2=f.read()
if(content1 == content2):
    print("Yes these two files are identical.")
else:
    print("No these files are not identical.!!")
"""
"""******************   Q.N.10)   ***************************
WAPto wipe out the content of a file using python.(wipe means removing content from file)

with open("Poem.txt","w") as f:
    f.write("")
"""
"""*****************   Q.N.11)    ***************************
WAP to rename a file to "rename_by_python.txt"
with open("old.txt","r") as f:
    content=f.read()
with open("renamed_by_python.txt","w") as f:
    f.write(content)
"""




























































