'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        # find shortest and longest word of array
        shortest = min(strs)
        longest = max(strs)
        
        # if no shortest, return empty string
        if not shortest:
            return ''
        
        for i in range(len(shortest)):
            # if letters of words are not the same
            if longest[i] != shortest[i]:
                # return the letters up until this index - this is the prefix
                return longest[:i]
        # return copy of shortest
        return shortest[:]