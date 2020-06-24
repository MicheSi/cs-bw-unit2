'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        # loop through string
        for i in range(len(s)):
            
            # append characters that are not []
            # if ], loop through characters in brackets to add to decoded
            if s[i] == ']':
                
                # create variable to store decoded characters
                decoded = ''
                
                # loop through stack if it's not [
                while stack[-1] != '[':
                    
                    # pop last char from stack and add to decoded
                    decoded = stack.pop() + decoded
                    
                # pop last char in stack, which should be [
                stack.pop()
                
                # find k
                k = ''
                # while there is a stack and the last item of the stack is a number
                while stack and stack[-1].isdigit():
                    # add that to k
                    k = stack.pop() + k
                
                # multiply k with decoded & add to stack
                decoded = int(k) * decoded
                stack.append(decoded)
                
            # add all characters into stack
            else:
                stack.append(s[i])
                
        # join decoded to make new string
        return ''.join(stack)