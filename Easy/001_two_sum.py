"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List
import unittest

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()

        for index, current_number in enumerate(nums):
            # Persisting searchable element
            mapping[current_number] = index
            
            # Do we already have its complement on the map ?
            complement = (target - current_number)
            # The second check prevents a case where the complement * 2 = the target
            if complement in mapping.keys() and mapping[complement] != index:
                return [mapping[complement], index]
        return None

class TwoSumUnitTest(unittest.TestCase):
    def testsingleNumber(self):
        code = TwoSum()

        self.assertEqual(code.twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(code.twoSum([2,7,11,15], 22), [1,3])
        self.assertEqual(code.twoSum([-3,8,10,-5], 5), [0,1])
        self.assertEqual(code.twoSum([-3,8,10,-5], -8), [0,3])
        
#if __name__ == '__main__':
#    unittest.main()

