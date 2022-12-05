'''Purpose:Reverse words in a given string

Author:Suryansh Sharma
'''
def reverse_words(string):  
    words = string.split(' ') 
    rev = ' '.join(reversed(words)) 
    return rev
 
s= input("Enter the string :")
print (reverse_words(s))