#Program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re
string=input("Enter the String:")
a=re.compile("[A-Za-z0-9]+")
if a.fullmatch(string):
    print("Valid String")
else:
    print("Invalid String")

#Python program that matches a word containing 'ab'
string1=input("Enter the word:")
if re.search('ab',string1):
    print(" matches a word 'ab' ")
else:
    print("Invalid")

#Python program to check for a number at the end of a word/sentence
string2=input("Enter the Sentence:")
if re.search(r'\d$',string2):
    print("Number at the end of a word/sentence")
else:
    print("Invalid sentence/word")

#Python program to search the numbers (0-9) of length between 1 to 3 in a given string
string3=input("Enter the String:")
if re.search('\d',string3) and len(string3)<=3:
    print("Found")
else:
    print("Not found")

#Python program to match a string that contains only uppercase letters
string4=input("Enter the String:")
if re.match("^[A-Z]+$",string4):
    print("Valid")
else:
    print("Invalid")
