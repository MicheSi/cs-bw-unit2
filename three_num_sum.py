'''
Write function that takes non-empty array of integer and a target integer
Find all triplets in array that sum up to target sum and return 2 dimensional array of all triplets
sort in ascending order by 1st triplet element
'''

# class Solution(object):
# 	def threeSum(self, nums):
# 		res = []
# 		nums.sort()
# 		length = len(nums)
# 		for i in xrange(length-2): #[8]
# 			if nums[i]>0: break #[7]
# 			if i>0 and nums[i]==nums[i-1]: continue #[1]

# 			l, r = i+1, length-1 #[2]
# 			while l<r:
# 				total = nums[i]+nums[l]+nums[r]

# 				if total<0: #[3]
# 					l+=1
# 				elif total>0: #[4]
# 					r-=1
# 				else: #[5]
# 					res.append([nums[i], nums[l], nums[r]])
# 					while l<r and nums[l]==nums[l+1]: #[6]
# 						l+=1
# 					while l<r and nums[r]==nums[r-1]: #[6]
# 						r-=1
# 					l+=1
# 					r-=1
# 		return res


# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         result = []
#         n = len(nums)
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             head = i + 1
#             end = n - 1
#             while head < end:
#                 if nums[i] + nums[head] + nums[end] == 0:
#                     result.append([nums[i], nums[head], nums[end]])
#                     head += 1
#                     while head < end and nums[head] == nums[head-1]:
#                         head += 1
#                     end -= 1
#                     while head < end and nums[end] == nums[end+1]:
#                         end -= 1
#                 elif nums[i] + nums[head] + nums[end] < 0:
#                     head += 1
#                     while head < end and nums[head] == nums[head-1]:
#                         head += 1
#                 else:
#                     end -= 1
#                     while head < end and nums[end] == nums[end+1]:
#                         end -= 1
#         return result


class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res     