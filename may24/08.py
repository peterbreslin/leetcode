"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. 
All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, 
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
"""

class Solution:
    def findRelativeRanks(self, score: list[int]) ->list[str]:
        
        a = "Gold Medal"
        b = "Silver Medal"
        c = "Bronze Medal"

        # Add indices to scores
        idx_list = list(enumerate(score))

        # Sort scores whilst retaining indices
        sorted_idx_list = sorted(idx_list, key=lambda x: x[1], reverse=True)

        # Creating list for the final result
        medals = [a,b,c] + list(range(4, 4 + len(score)-3))

        # Need to assign to a tuple: convert to list then back to tuple
        for i, isolated_tuple in enumerate(sorted_idx_list):
            tuple_to_list = list(isolated_tuple)
            tuple_to_list[1] = medals[i]
            isolated_tuple = tuple(tuple_to_list)
            sorted_idx_list[i] = isolated_tuple

        # Order according to original indices
        result = ['']*len(sorted_idx_list)
        for i,j in enumerate(sorted_idx_list):
            result[j[0]] = str(j[1])
        
        return result


# score = ['5']
score = [3,4,7,1,2,10]
sol = Solution()
result = sol.findRelativeRanks(score)
print(result)