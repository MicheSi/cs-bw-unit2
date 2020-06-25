'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        # initialize indexes we'll be comparing
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            # assign middle number
            mid = (start + end) // 2
            
            # if the middle num is the target, return it
            if nums[mid] == target:
                return mid
            
            # go through 1st half of numbers
            if nums[start] <= nums[mid]:
                # if index is <= target and target is <= to the middle number
                if nums[start] <= target and target <= nums[mid]:
                    # reset last index to middle - 1
                    end = mid - 1
                # else reset first index to 2nd half of array
                else:
                    start = mid + 1
            # go through 2nd half of numbers
            else:
                if nums[mid] <= target and target <= nums[end]:
                    # reset 1st index to num after mid
                    start = mid + 1
                else:
                    end = mid -1
                    
        return -1