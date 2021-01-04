import unittest

class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BTreeMethods(object):
    def tree_depth(self, root) -> int:
        if not root:
            return 0
        return self._tree_depth(root)

    def _tree_depth(self, node) -> int:
        if not node:
            return 0
        
        return max(self._tree_depth(node.left), self._tree_depth(node.right)) + 1

    def is_mirror(self, root) -> bool:
        if not root:
            return True

        return self._is_mirror(root.left, root.right)
        
    def _is_mirror(self, subtreeA, subtreeB):
        # structural equality
        if not subtreeA and not subtreeB:
            return True
        if not subtreeA or not subtreeB:
            return False

        # Value difference
        return (subtreeA.val == subtreeB.val) and self._is_mirror(subtreeA.left, subtreeB.right) and self._is_mirror(subtreeA.right, subtreeB.left)

class UnitTests(unittest.TestCase):
    def test_tree_depth(self):
        code = BTreeMethods()

        root_full = TreeNode(
            20,
                TreeNode(10,
                    TreeNode(5),
                    TreeNode(5)),
                TreeNode(30,
                    TreeNode(40),
                    TreeNode(40))
        )

        self.assertEqual(code.tree_depth(root_full), 3)

        root_left_heavy = TreeNode(
            20,
                TreeNode(10,
                    TreeNode(20,
                        TreeNode(30,
                            TreeNode(40))))
        )

        self.assertEqual(code.tree_depth(root_left_heavy), 5)

    def test_is_mirror(self):
        code = BTreeMethods()

        mirrored_tree = TreeNode(
            20,
            TreeNode(10,
                TreeNode(5),
                TreeNode(20)),
            TreeNode(10,
                TreeNode(20),
                TreeNode(5))
        )

        self.assertTrue(code.is_mirror(mirrored_tree))

        structural_mirror_only = TreeNode(
            20,
            TreeNode(10,
                TreeNode(5),
                TreeNode(20)),
            TreeNode(10,
                TreeNode(7),
                TreeNode(5))
        )

        self.assertFalse(code.is_mirror(structural_mirror_only))

        values_mirror_only = TreeNode(
            20,
            TreeNode(10,
                TreeNode(5),
                TreeNode(20)),
            TreeNode(10,
                TreeNode(20))
        )

        self.assertFalse(code.is_mirror(values_mirror_only))

if __name__ == "__main__":
    unittest.main()