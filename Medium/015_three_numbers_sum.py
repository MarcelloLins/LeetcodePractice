"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
"""
import unittest

class Solution(object):
    def three_number_sum(self, nums):
        results = []       

        # Sorting the array allows us to reduce this problem to a "two sum" problem, where the target is not zero, but the complement of the two numbers being summed.
        nums = sorted(nums)
        for a in range(0, len(nums) - 2):

            # If we have already calculated the three sum with this value fixed for a, we can skip it to avoid duplicated results
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            # For the inner iteration, we will use two pointers
            b = a + 1
            c = len(nums) - 1
            while b < c:                
                sum = nums[a] + nums[b] + nums[c]

                # If the sum is > 0, our upper pointer is too high
                if sum > 0:
                    c = c - 1
                elif sum < 0:
                    b = b + 1
                else:
                    # We found a possible solution
                    results.append([nums[a], nums[b], nums[c]])
                    b = b + 1
                    while b < c and nums[b] == nums[b - 1]:
                        continue
        return results

class SolutionUnitTest(unittest.TestCase):
    def test_three_number_sum(self):

        code = Solution()

        test_case_1 = [-1,0,1,2,-1,-4]
        response_1 = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(code.three_number_sum(test_case_1), response_1)

if __name__ == "__main__":
    unittest.main()