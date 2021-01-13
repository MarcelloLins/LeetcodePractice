"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

2, 3, 6, 7

2 + 2
2 + 3
2 + 6
2 + 7

2 + 2 + 2
2 + 

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
import unittest

class Solution(object):
    def combination_backtrack(self, candidates, index, current_sequence, results, target):
        # Base case of the backtracking
        if target == 0:
            results.append(current_sequence.copy())
            return

        # We overshot it
        if target < 0:
            return

        local_index = index
        while local_index < len(candidates):
            current_candidate = candidates[local_index]
            current_sequence.append(current_candidate)
            self.combination_backtrack(candidates, local_index, current_sequence, results, target - current_candidate)
            current_sequence.pop()
            local_index = local_index + 1

    def combination_sum(self, candidates, target):
        results = []

        if not candidates or len(candidates) == 0:
            return results

        self.combination_backtrack(candidates, 0, [], results, target)
        return results        

class SolutionUnitTest(unittest.TestCase):
    def test_combination_sum(self):
        code = Solution()
        response = code.combination_sum([2,3,6,7], 7)
        self.assertEqual(response,[[2,2,3],[7]])

if __name__ == "__main__":
    unittest.main()