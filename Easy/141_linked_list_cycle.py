"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

import unittest

class ListNode(object):
    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode

class Solution(object):
    def has_cycle(self, node):
        previously_visited_nodes = set()

        head = node
        while head:
            # Have we seen this node before ?
            if head in previously_visited_nodes:
                return True

            # if not, store it and move on.
            previously_visited_nodes.add(head)
            head = head.next

        return False


class SolutionUnitTest(unittest.TestCase):
    def test_has_cycle(self):
        code = Solution()

        head_a = ListNode(3)
        node_1 = ListNode(2)
        node_2 = ListNode(0)
        node_3 = ListNode(-4)

        head_a.next = node_1
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = head_a

        self.assertTrue(code.has_cycle(head_a))

        # Undoing cycle
        node_3.next = None
        self.assertFalse(code.has_cycle(head_a))

        # single node 
        self.assertFalse(code.has_cycle(ListNode(2)))

        # No nodes
        self.assertFalse(code.has_cycle(None))


if __name__ == '__main__':
    unittest.main()