"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

import unittest

class Solution(object):

    def _generate_backtrack(self, results, current_string, opens, closes, n):
        # Have we reached the maximum string size ? 
        # Because we need PAIRS of parenthesis, strings can't be bigger than n * 2 (or twice the number of pairs we are targetting)
        if len(current_string) == n * 2:
            results.append(current_string)
            return
        
        # We can't open more than N pairs
        if opens < n:
            new_current = current_string + "("
            self._generate_backtrack(results, new_current, opens + 1, closes, n)
        
        # We can't close more than open
        if closes < opens:
            new_current = current_string + ")"
            self._generate_backtrack(results, new_current, opens, closes + 1, n)
        
    def generate_parenthesis(self, n):
        results = []
        if n == 0:
            return results
        if n == 1:
            results.append("()")
            return results

        self._generate_backtrack(results, "", 0, 0, n)
        return results

class SolutionUnitTest(unittest.TestCase):
    def test_generate_parenthesis(self):
        code = Solution()
        response = code.generate_parenthesis(3)
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        self._compare_results(response, expected)

        response = code.generate_parenthesis(1)
        expected =  ["()"]
        self._compare_results(response, expected)

        
    def _compare_results(self, response, expected):
        r1 = set(response)
        r2 = set(expected)
        
        for resp in r1:
            self.assertTrue(resp in r2)

if __name__ == "__main__":
    unittest.main()