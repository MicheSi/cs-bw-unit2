# Complete the 'makeAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

# Consider comparing indices of strings
# Add same letters to a list
# Compare string lengths to list, then subtract to get difference
# len(a) - list + len(b) - list = len of different letters

# loop through both strings
# if letter is not in both, add that letter to a list
# return length of the list containing different letters

# compare letters in each string
# if letters are same, increment count
# remove any letters that are not in both strings

# compare letters in strings
# replace same letters with '' (null), removing them from the string
# add lengths of new strings - this is the # of letters not in both strings

def makeAnagrams(a, b):
    # Write your code here
    

    # loop through characters in 1st string
    for char in a:
        # if the character is also in 2nd string
        if char in b:
            # replace the character with an empty space - make null
            a = a.replace(char, '', 1)
            b = b.replace(char, '', 1)

    # this is how many characters remain
    return len(a) + len(b)

'''
Time complexity is O(n) - only takes up as much time as n # of characters
Space complexity is O(n) - will only take up as much space as n # of characters
'''

# def remAnagram(a, b): 
  
#     # make hash array for both string  
#     # and calculate 
#     # frequency of each character 
#     count1 = [0]*CHARS 
#     count2 = [0]*CHARS 
  
#     # count frequency of each character  
#     # in first string 
#     i = 0
#     while i < len(a): 
#         count1[ord(a[i])-ord('a')] += 1
#         i += 1
  
#     # count frequency of each character  
#     # in second string 
#     i =0
#     while i < len(b): 
#         count2[ord(b[i])-ord('a')] += 1
#         i += 1
  
#     # traverse count arrays to find  
#     # number of characters 
#     # to be removed 
#     result = 0
#     for i in range(26): 
#         result += abs(count1[i] - count2[i]) 
#     return result 