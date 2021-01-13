"""
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
"""
import unittest

class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums) == 0:
            return -1

        # Finding the pivot point using a modified binary search
        left = 0
        right = len(nums) - 1

        while left < right:
            middle_point = (int) (left + (right - left) / 2)
            if nums[middle_point] > nums[right]:
                left = middle_point + 1
            else:
                right = middle_point

        # Found the pivot point
        pivot = left
        # Defining boundaries of our new search domain 
        if target >= nums[pivot] and target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            right = pivot
            left = 0

        # Regular binary search
        # [4,5,6,7,0,1,2]
        while left <= right:
            middle_point = (int) (left + (right - left) / 2)

            if nums[middle_point] == target:
                return middle_point
            elif nums[middle_point] > target:
                right = middle_point - 1
            else:
                left = middle_point + 1
        return -1

class SolutionUnitTest(unittest.TestCase):
    def test_search(self):
        code = Solution()

        self.assertEqual(code.search([4,5,6,7,0,1,2], 0), 4)
        self.assertEqual(code.search([4,5,6,7,0,1,2], 6), 2)
        self.assertEqual(code.search([4,5,6,7,0,1,2], 3), -1)        
        self.assertEqual(code.search([1], 1), 0)
        self.assertEqual(code.search([], 1), -1)

if __name__ == "__main__":
    unittest.main()