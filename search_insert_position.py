'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # use binary search to loop through array
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            # if middle num is target, return it's index
            if nums[mid] == target:
                return mid
            # if middle num < target, move to 2nd half of array
            if nums[mid] < target:
                start = mid + 1
            # target doesn't exit, add it to end of array  
            else:
                end = mid - 1
        
        return start