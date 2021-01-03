"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

import unittest

class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def merge_two_lists(self, listOne: ListNode, listTwo: ListNode) -> ListNode:
        if not listOne:
            return listTwo

        if not listTwo:
            return listOne

        head = merged = ListNode()
        while not (listOne is None or listTwo is None):
            
            if listOne.value < listTwo.value:
                current = listOne
                listOne = listOne.next
            else:
                current = listTwo
                listTwo = listTwo.next

            merged.next = current
            merged = merged.next
        
        # Links whichever of the two lists has a next element, if any
        merged.next = listOne or listTwo
        return head.next

class SolutionUnitTest(unittest.TestCase):
    def test_merge_two_lists(self):
        code = Solution()

        listOne = ListNode(1, ListNode(2, ListNode(4)))
        listTwo = ListNode(1, ListNode(3, ListNode(4)))

        self.assertIsNotNone(code.merge_two_lists(listOne, listTwo))

        return True

if __name__ == '__main__':
    unittest.main()