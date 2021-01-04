"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

import unittest

class ListNode(object):
    def __init__(self, val, next = None):
        self.value = val
        self.next = next

class Solution(object):
    def find_intersection(self, headA, headB):
        seen_nodes = set()
        while headA or headB:
            if headA:
                if headA in seen_nodes:
                    return headA
                seen_nodes.add(headA)
                headA = headA.next
            if headB:
                if headB in seen_nodes:
                    return headB
                seen_nodes.add(headB)            
                headB = headB.next

        return None

class SolutionUnitTest(unittest.TestCase):
    def test_find_intersection(self):
        code = Solution()

        node_a1 = ListNode(10)
        node_a2 = ListNode(11)
        node_a3 = ListNode(12)
        node_a1.next = node_a2
        node_a2.next = node_a3        

        node_b1 = ListNode(20)
        node_b2 = ListNode(21)
        node_b3 = ListNode(22)
        node_b4 = ListNode(23)
        node_b1.next = node_b2
        node_b2.next = node_b3
        node_b3.next = node_b4

        intersection_a1 = ListNode(30)
        intersection_a2 = ListNode(31)
        intersection_a3 = ListNode(32)
        intersection_a1.next = intersection_a2
        intersection_a2.next = intersection_a3
        
        node_a3.next = intersection_a1
        node_b4.next = intersection_a1

        self.assertEqual(code.find_intersection(node_a1, node_b1), intersection_a1)
        self.assertEqual(code.find_intersection(node_a1, None), None)

if __name__ == "__main__":
    unittest.main()