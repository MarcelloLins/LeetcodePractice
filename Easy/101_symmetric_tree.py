"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2 
   \   \
   3    3
"""
import unittest

class TreeNode(object):
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution(object):
    def is_symetrical(self, node):
        if not node:
            return True

        return self.are_subtrees_symmetrical(node.right, node.left)

    def are_subtrees_symmetrical(self, nodeOne, nodeTwo):
        if not nodeOne and not nodeTwo:
            return True

        if not nodeOne or not nodeTwo:
            return False

        return (nodeOne.val == nodeTwo.val) and self.are_subtrees_symmetrical(nodeOne.left, nodeTwo.right) and self.are_subtrees_symmetrical(nodeOne.right, nodeTwo.left)


class SolutionUnitTest(unittest.TestCase):
    def test_is_symetrical(self):
        
        right_subtree = TreeNode(
            2,
            TreeNode(3),
            TreeNode(4)
        )

        left_subtree = TreeNode(
            2,
            TreeNode(4),
            TreeNode(3)
        )

        root = TreeNode(1, right_subtree, left_subtree)

        code = Solution()
        self.assertTrue(code.is_symetrical(root))


if __name__ == "__main__":
    unittest.main()

