"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
import unittest
from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.t9_dict = defaultdict()
        self.t9_dict["2"] = ["a", "b", "c"]
        self.t9_dict["3"] = ["d", "e", "f"]
        self.t9_dict["4"] = ["g", "h", "i"]
        self.t9_dict["5"] = ["j", "k", "l"]
        self.t9_dict["6"] = ["m", "n", "o"]
        self.t9_dict["7"] = ["p", "q", "r", "s"]
        self.t9_dict["8"] = ["t", "u", "v"]
        self.t9_dict["9"] =  ["w", "x", "y", "z"]

    def _letter_combination(self, result, digits, current_combination, index):
        # If we reached the end of the string, return the current combination
        if index == len(digits):
            result.append(current_combination)
            return result

        # If not, we need to get the characters that correspond to the current index
        t9_chars = self.t9_dict[digits[index]]
        
        # Call the function recursively for each character, making sure we add it to the current_combinaton string first
        for character in t9_chars:
            combination = current_combination + character
            self._letter_combination(result, digits, combination, index + 1)

    def letter_combinations(self, digits):
        result = []
        if not digits or len(digits) == 0:
            return result
        
        self._letter_combination(result, digits, "", 0)
        return result

class SolutionUnitTest(unittest.TestCase):
    def test_letter_combinations(self):
        code = Solution()
        
        results = code.letter_combinations("23")
        self.assertEqual(len(results), 9)

        results = code.letter_combinations("")
        self.assertEqual(len(results), 0)

        results = code.letter_combinations("2")
        self.assertEqual(len(results), 3)

if __name__ == "__main__":
    unittest.main() 