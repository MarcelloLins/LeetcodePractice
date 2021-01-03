"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

import unittest

class Solution:
    def are_parenthesis_valid(self, input: str) -> bool:
        # Short circuit: Od number of characters can be a valid sequence
        if (len(input) % 2 != 0) or not input:
            return False

        symbols_map = {")":"(", "}":"{", "]":"["}
        closing_symbols = set(symbols_map.keys())

        symbols_stack = []
        for i in range(0, len(input)):
            current_charater = input[i]

            if current_charater not in closing_symbols:
                symbols_stack.append(current_charater)
                continue

            # closing symbols            
            # if we reach a closing symbol and the stack is empty, we can short circuit
            if len(symbols_stack) == 0:
                return False

            # Was the last symbol the complement of the current one ?
            if symbols_stack.pop() != symbols_map[current_charater]:
                return False

        return len(symbols_stack) == 0


class SolutionUnitTest(unittest.TestCase):
    def test_are_parenthesis_valid(self):
        solution = Solution()
        
        self.assertEqual(solution.are_parenthesis_valid("()"), True)
        self.assertEqual(solution.are_parenthesis_valid("()[]{}"), True)        
        self.assertEqual(solution.are_parenthesis_valid("{[]}"), True)        
        self.assertEqual(solution.are_parenthesis_valid("{}{{}}"), True)
        self.assertEqual(solution.are_parenthesis_valid("((()(())))"), True)        

        self.assertEqual(solution.are_parenthesis_valid("(]"), False)
        self.assertEqual(solution.are_parenthesis_valid("{}{}}"), False)
        self.assertEqual(solution.are_parenthesis_valid("(((((((()"), False)
        self.assertEqual(solution.are_parenthesis_valid("([)]"), False)

if __name__ == '__main__':
     unittest.main()