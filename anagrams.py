# Complete the 'makeAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagrams(a, b):
    # Write your code here
    # compare letters in each string
    # if letters are same, increment count
    # remove any letters that are not in both strings

    # loop through characters in 1st string
    for char in a:
        # if the character is also in 2nd string
        if char in b:
            # replace the character with an empty space
            a = a.replace(char, '', 1)
            b = b.replace(char, '', 1)

    # this is how many characters remain
    return len(a) + len(b)