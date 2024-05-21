"""
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
"""

class Solution:
	def compareVersion(self, version1: str, version2: str) -> int:

		v1 = version1.split('.')
		v2 = version2.split('.')
		v1 = [int(num) for num in v1]
		v2 = [int(num) for num in v2]

		k = 0
		for i in range(min(len(v1), len(v2))):
			if v1[i] == v2[i]:
				continue
			if v1[i] > v2[i]:
				k = 1
				break
			if v1[i] < v2[i]:
				k = -1
				break

		if k == 0:
			if sum(v1[i:])-v1[i] > 0:
				k = 1
			if sum(v2[i:])-v2[i] > 0:
				k = -1

		return k

sol = Solution()
result = sol.compareVersion('0.10', '1.2.0.1')
print(result)