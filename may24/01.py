""" 
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.
"""

class Solution:
	def reversePrefix(self, word: str, ch: str) -> str:

		if not (1 <= len(word) <= 250):
			return word
		if not word.islower():
			return word
		if not ch.islower() or len(ch) != 1:
			return word

		if ch not in word:
			return word
		else:
			i = word.find(ch)
			subset = word[:i+1]
			return subset[::-1] + word[i+1:]

sol = Solution()
result = sol.reversePrefix("abcdefd", 'd')
print(result) 