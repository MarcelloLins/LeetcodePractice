"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
import unittest

class Solution(object):
    def climb_stairs(self, n: int) -> int:
        return self.recursive_climb_stairs(n, dict())

    def recursive_climb_stairs(self, remaining_steps: int, cachedResults: dict) -> int:
        if remaining_steps < 0:
            return 0
        if remaining_steps == 0:
            return 1
        
        if remaining_steps in set(cachedResults.keys()):
            return cachedResults[remaining_steps]

        cachedResults[remaining_steps] = self.recursive_climb_stairs(remaining_steps - 1, cachedResults) + self.recursive_climb_stairs(remaining_steps - 2, cachedResults)
        return cachedResults[remaining_steps]

class SolutionUnitTest(unittest.TestCase):
    def test_climb_stairs(self):
        code = Solution()

        self.assertEqual(code.climb_stairs(2), 2)
        self.assertEqual(code.climb_stairs(3), 3)

if __name__ == "__main__":
    unittest.main()

