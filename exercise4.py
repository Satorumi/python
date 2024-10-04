# # 1. Factor Counting Program

# # assume num >= 1

# num = int(input("Enter your number: "))

# if num == 1:
#     print("Number 1 has 1 factor")
# else:
#     n_factor = 2
#     for i in range(2, (num//2)+1):
#         if num % i == 0:
#             n_factor += 1

#     print(f"Number {num} has {n_factor} factors")


# # 2. String Cleaning Program
# import re # regex library in python

# def cleaner(string):
#     string = string.strip()
#     s = re.sub('[^a-zA-Z]+', '', string) # use regex pattern for non-alphabetical characters
#     return string

# # 3. Palindrome Program

# def isPalindrom():
#     ''' returns True if the given string argument is a palindrome
    
#     Args:
#         string: represent a series of alphabetical characters, string
    
#     Returns:
#         a boolean describe if the given string is a palindrome
#     '''

#     from math import floor

#     string = input("Enter string: ")

#     mid = floor(len(string)/2)

#     str1 = string[:mid]
#     str2 = string[-1:-mid-1:-1]

#     if str1 == str2:
#         return True
#     else:
#         return False

# # end of isPalindrome()


# # 4. String Consonant Counter

# def consonantCounter(string):
#     ''' counts the number of consonants in the given string argument
    
#     Args:
#         string: a given string, string
    
#     Returns:
#         an integer represent the number of consonants
#     '''

#     vowels = "aeiou"
#     count = 0

#     for char in string:
#         if char in vowels:
#             count += 1

#     return len(string) - count
# # end of consonantCounter()

# def patternCreator(n):
#     ''' create a pattern base on integer input
    
#     Args:
#         n: an integer greater than 0
    
#     Returns:
#         None
#     '''

#     prevPattern = ''

#     for i in range(1,n+1):
#         prevPattern += str(i%2)
#         print(prevPattern)

# # end of patternCreator()

# # 6. Anagram Checker

# def anagramChecker(str1, str2):

#     ''' determine whether two strings are anagram
    
#     Args:
#         str1: a string
#         str2: a string

#     Returns:
#         a boolean that describe whether the two strings are anagram
#     '''

#     if len(str1) != len(str2):
#         return False
#     else:
#         str1 = list(str1)
#         str2 = list(str2)

#         str1 = {x: str1.count(x) for x in set(str1)}
#         str2 = {x: str2.count(x) for x in set(str2)}

#         for (key, value) in str1.items():
#             for (key2, value2) in str2.items():
#                 if key == key2 and value != value2: # not anagrams
#                     return False
        
#         return True

# # end of anagramChecker()

# 7. Duplicates between Two Strings

def returnDuplicates(str1, str2):

    ''' return a single sorted list of characters that are found in each string.
    
    Args:
        str1: a string
        str2: a string

    Returns:
        a list containing duplicated characters in two strings
    '''

    str1 = set(str1)
    str2 = set(str3)

    duplicates = []

    for char in str1:
        if char in str2:
            duplicates.append(char)

    return duplicates
    
# end of returnDuplicates()
