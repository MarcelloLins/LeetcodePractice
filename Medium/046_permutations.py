"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
import unittest

class Solution(object):
    def permute_backtrack(self, nums, current_sequence, results):
        # Are we on the last element of the list ?
        # Backtracking base case
        if len(current_sequence) == len(nums):
            results.append(current_sequence.copy())
            return

        for i in nums:
            if i in set(current_sequence):
                continue
            current_sequence.append(i)
            self.permute_backtrack(nums, current_sequence, results)
            current_sequence.pop()
        

    
    def permute(self, nums):
        results = []

        if not nums or len(nums) == 0:
            return results

        # Backtrack !
        self.permute_backtrack(nums, [], results)
        return results

class SolutionUnitTest(unittest.TestCase):
    def test_permute(self):
        code = Solution()

        response = code.permute([1,2,3])
        self.assertEqual(len(response), 6)

if __name__ == "__main__":
    unittest.main()