'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set hash table of numbers visited
        visited = {}
        # loop through nums list
        for i, num in enumerate(nums):
            # difference is target - num
            diff = target - num
            # if difference has not been visited
            if diff not in visited:
                # add to visited and assign as index
                visited[num] = i
            # return index of difference in visited table and index of num
            else:
                return [visited[diff], i]