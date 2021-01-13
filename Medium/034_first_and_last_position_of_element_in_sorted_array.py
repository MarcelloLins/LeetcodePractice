"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

[1,2,3,4,4,5,6,6]
"""
import unittest

class Solution(object):
    def expand_search_range(self, nums, target, starting_idx):
        left = right = starting_idx
        searching_left = searching_right = True
        while searching_left or searching_right:
            # Lower array boundary and stop condition
            if left - 1 < 0 or nums[left - 1] != target:
                searching_left = False
            else:
                left = left - 1
            
            # Upper array boundary and stop condition
            if right + 1 > len(nums) - 1 or nums[right + 1] != target:
                searching_right = False
            else:
                right = right + 1

        return [left, right]

    def search_range(self, nums, target):
        # Binary search to find one instance of the target
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle_point = (int)(left + (right - left) / 2)

            if nums[middle_point] == target:
                # Expand around the middle
                return self.expand_search_range(nums, target, middle_point)
            elif nums[middle_point] > target:
                right = middle_point - 1
            else:
                left = middle_point + 1

        return [-1, -1]


class SolutionUnitTest(unittest.TestCase):
    def test_search_range(self):
        code = Solution()

        self.assertEqual(code.search_range([5,7,7,8,8,10], 8), [3,4])
        self.assertEqual(code.search_range([5,7,7,8,8,10], 6), [-1,-1])
        self.assertEqual(code.search_range([], 1), [-1,-1])
        self.assertEqual(code.search_range([2], 2), [0, 0])

if __name__ == "__main__":
    unittest.main()