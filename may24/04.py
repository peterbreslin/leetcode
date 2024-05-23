"""
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""

class Solution:
	def numRescueBoats(self, people: list[int], limit: int) -> int:
		people.sort()

		# Initialize two pointers and boat counter
		i, j = 0, len(people) - 1  
		boats = 0

		# Loop until pointers intersect
		while i <= j:

			# If the lightest and heaviest person can share a boat, move left pointer inward
			if people[i] + people[j] <= limit:  
				i += 1 

			# If cannot share a boat, the heaviest person will be placed in a boat alone
			j -= 1 

			# Boat counter increments in either case
			boats += 1

		return boats


sol = Solution()
print(sol.numRescueBoats([1, 2], 3))
print(sol.numRescueBoats([3, 2, 2, 1], 3))
print(sol.numRescueBoats([3, 5, 3, 4], 5))
