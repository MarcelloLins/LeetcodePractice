"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

import unittest

class TreeNode(object):
    def __init__(self, val: int, lchild, rchild):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

class Solution(object):
    def maximum_depth(self, root_node: TreeNode) -> int:
        if not root_node:
            return 0

        left_depth = self.maximum_depth(root_node.lchild)
        right_depth = self.maximum_depth(root_node.rchild)

        return max(left_depth, right_depth) + 1

class SolutionUnitTest(unittest.TestCase):
    def test_maximum_depth(self):
        code = Solution()

        rchild = TreeNode(14, None, None)
        lower_child = TreeNode(5, None, None)
        lchild = TreeNode(4, None, lower_child)        
        bTree = TreeNode(10, lchild, rchild)

        self.assertEqual(code.maximum_depth(bTree), 3)

if __name__ == "__main__":
    unittest.main()