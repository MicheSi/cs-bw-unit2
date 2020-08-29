
#
# Complete the 'reverseInParentheses' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# need to loop through all characters
# when you get to a (, all the letters that follow until the ) need to be reversed
# can return letters in parens from last index forward
# store them in a string in order and reverse that string or store them in reverse order - from ) forward
# add those letters back into the main string

def reverseInParentheses(s):
    # Write your code here
    # track letters in parentheses
    # if the letters are in parens, reverse the letters
    # add back to other letters and return string

    # we'll be storing all characters in a stack
    stack = []

    # loop through characters in the string
    for char in s:
        # if character is a closing paren
        if char == ')':
            # this is where we'll store letters in the parentheses
            letters = ''
            # this allows us to loop through all the characters in the stack between parens
            while stack[-1] is not '(':
                # remove those characters from the stack and add them to the letters string
                letters += stack.pop()
            # now remove the closing paren
            stack.pop()
            # for each letter in our new letters string
            for l in letters:
                # add it to the stack
                stack.append(l)

        else:
            # these are the letters that are not in parens
            stack.append(char)
    
    # join the characters in the stack back into a string
    return ''.join(stack)

'''
Time complexity is O(n^2) - looping through lists twice, exponentially increasing run time
Space complexity is O(n) - only takes up as much as number of characters in string
'''

# use recursion
# loop through characters in string
# When you get to a (, print all of the letters after that index starting from the last letter so it prints them in reverse order
# when you get to a ), that's the end of what you want to print
# recurse through until you have no more letters to loop through

# def reverseParentheses(s):
#     for i in range(len(s)):
#         if s[i] == "(":
#             start = i
#             print (s[:start])
#         if s[i] == ")":
#             end = i
#             print (end)
#             return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
#     return s