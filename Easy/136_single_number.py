"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""

import unittest
class Solution(object):

    def single_number_brute_force(self, numbers):
        found_numbers = list()
        for i in numbers:
            if i not in found_numbers:
                found_numbers.append(i)
            else:
                found_numbers.remove(i)
        
        return found_numbers[0]

    def single_number_hashmap(self, numbers):
        found_numbers = dict()
        for i in numbers:
            if i not in found_numbers.keys():
                found_numbers[i] = 1
            else:
                found_numbers[i] += 1

        for i in numbers:
            if found_numbers[i] == 1:
                return i
        return None

class SolutionUnitTest(unittest.TestCase):

    def test_single_number(self):
        code = Solution()

        test_case_a = [4,1,2,1,2]
        self.assertEqual(code.single_number_brute_force(test_case_a), 4)
        self.assertEqual(code.single_number_hashmap(test_case_a), 4)

        test_case_b = [2,2,1]
        self.assertEqual(code.single_number_brute_force(test_case_b), 1)
        self.assertEqual(code.single_number_hashmap(test_case_b), 1)

        test_case_c = [2]
        self.assertEqual(code.single_number_brute_force(test_case_c), 2)
        self.assertEqual(code.single_number_hashmap(test_case_c), 2)

if __name__ == "__main__":
    unittest.main()