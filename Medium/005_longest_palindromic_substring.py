"""
Given a string s, return the longest palindromic substring in s.

public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}

""" 

import unittest

class Solution(object):

    def _expand_window_around_center(self, s, left, right):
        l = left
        r = right

        # While these characters are still mirrors, within the limits of the string, expand the window
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l = l -1
            r = r + 1
        
        # Window Length
        return r - l - 1

    def longest_palindrome(self, s):
        if not s or len(s) < 1:
            return ""

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return ""

        start, end = 0, 0        
        for center in range(0, len(s)):
            # Locating characters around the center
            length_starting_from_current = self._expand_window_around_center(s, center, center)
            length_starting_from_next = self._expand_window_around_center(s, center, center + 1)
            best_candidate = max(length_starting_from_current, length_starting_from_next)
            
            if best_candidate > (end - start):
                start = (int) (center - (best_candidate - 1) / 2)
                end = (int) (center + best_candidate / 2)

        return s[start : end + 1]

class SolutionUnitTest(unittest.TestCase):
    def test_longest_palindrome(self):
        code = Solution()

        self.assertEqual(code.longest_palindrome("babad"), "aba")

if __name__ == "__main__":
    unittest.main()