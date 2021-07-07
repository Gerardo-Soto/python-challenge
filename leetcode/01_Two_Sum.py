"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums, target):
        solution = []
        for num in range(len(nums) - 1):
            print(target, nums[num], nums[num + 1:])
            if (target - nums[num]) in nums[num + 1:]:
            	solution.append(num)
            	solution.append(nums[num + 1:].index(target - nums[num])+ 1 + num)
            	return solution
           

s = Solution()
v = [2,7,11,15]
print(s.twoSum(v, 9))


"""
Runtime: 656 ms, faster than 28.12% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 63.31% of Python3 online submissions for Two Sum.
"""
