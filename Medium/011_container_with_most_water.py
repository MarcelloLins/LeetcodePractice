"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""
import unittest

class Solution(object):
    def _calculate_area(self, left, right, left_idx, right_idx):
        if left_idx >= right_idx:
            return 0
        height = min(left, right)
        width = (right_idx - left_idx)
        return height * width
    
    def container_most_water_brute_force(self, coords):
        max_area = 0
        if not coords or len(coords) <= 1:
            return 0

        for left_idx in range(0, len(coords)):
            for right_idx in range(left_idx + 1, len(coords)):
                area = self._calculate_area(coords[left_idx], coords[right_idx], left_idx, right_idx)
                max_area = max(area, max_area)
        return max_area

    def container_most_area_moving_pointers(self, coords):
        max_area = 0
        if not coords or len(coords) <= 1:
            return 0

        left_idx, right_idx = 0, len(coords) - 1

        while left_idx < right_idx:
            left_height, right_height = coords[left_idx], coords[right_idx]

            # Calculate the current area
            local_area = (min(left_height, right_height) * (right_idx - left_idx))
            max_area = max(local_area, max_area)

            # Which pointer do we move ?
            if left_height < right_height:
                left_idx = left_idx + 1
            else:
                right_idx = right_idx - 1

        return max_area

class SolutionUnitTest(unittest.TestCase):
    def test_container_most_water(self):
        code = Solution()

        test_case_1 = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(code.container_most_water_brute_force(test_case_1), 49)
        self.assertEqual(code.container_most_area_moving_pointers(test_case_1), 49)

        test_case_2 = [4,3,2,1,4]
        self.assertEqual(code.container_most_water_brute_force(test_case_2), 16)
        self.assertEqual(code.container_most_area_moving_pointers(test_case_2), 16)

        test_case_3 = [1, 1]
        self.assertEqual(code.container_most_water_brute_force(test_case_3), 1)
        self.assertEqual(code.container_most_area_moving_pointers(test_case_3), 1)

        test_case_4 = [1, 2, 1]
        self.assertEqual(code.container_most_water_brute_force(test_case_4), 2)
        self.assertEqual(code.container_most_area_moving_pointers(test_case_4), 2)

        test_case_5 = [2,3,4,5,18,17,6]
        self.assertEqual(code.container_most_water_brute_force(test_case_5), 17)
        self.assertEqual(code.container_most_area_moving_pointers(test_case_5), 17)

if __name__ == "__main__":
    unittest.main()