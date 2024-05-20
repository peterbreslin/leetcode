"""
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
Return the positive integer k. If there is no such integer, return -1.
"""

class Solution:
	def findMaxK(self, nums: list[int]) -> int:
		if len(nums) < 1 or len(nums) > 1000 or any(num == 0 or num < -1000 or num > 1000 for num in nums):
			return -1

		nums_set = set(nums)
		max_k = -1
		for num in nums:
			if -num in nums_set:
				max_k = max(max_k, abs(num))
		return max_k


z = [-4, 3, 5, -1, 7, 8, 9, -7, -11]
sol = Solution()
result = sol.findMaxK(nums=z)
print(result)