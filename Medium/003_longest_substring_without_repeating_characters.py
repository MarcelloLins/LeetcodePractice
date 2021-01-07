"""
Given a string s, find the length of the longest substring without repeating characters.
"""
import unittest
class Solution(object):
    def longest_substring(self, s):
        max_length, start, end = 0, 0, 0
        
        seen = set()        
        while start < len(s) and end < len(s):
            end_character = s[end]
            starting_character = s[start]
            if end_character not in seen:
                seen.add(end_character)
                
                end = end + 1
                max_length = max(max_length, end - start)
            else:
                seen.remove(starting_character)
                start = start + 1
            
        return max_length

class SolutionUnitTest(unittest.TestCase):
    def test_longest_substring(self):
        code = Solution()
        self.assertEqual(code.longest_substring("abcabcbb"), 3)
        self.assertEqual(code.longest_substring("cabcdea"), 5)
        self.assertEqual(code.longest_substring("bbbbb"), 1)
        self.assertEqual(code.longest_substring("pwwkew"), 3)
        self.assertEqual(code.longest_substring(""), 0)

if __name__ == "__main__":
    unittest.main()