"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

import unittest
import math

class Solution(object):
    def maximum_sub_array(self, array: [int]) -> int:
        global_max = current_max = array[0]
        
        for index in range(1, len(array)):
            current_max = max(current_max + array[index], array[index])

            if current_max > global_max:
                global_max = current_max

        return global_max

class SolutionUnitTest(unittest.TestCase):
    def test_maximum_sub_array(self):
        code = Solution()

        self.assertEqual(code.maximum_sub_array([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(code.maximum_sub_array([-2147483647]), -2147483647)

if __name__ == '__main__':
    unittest.main()