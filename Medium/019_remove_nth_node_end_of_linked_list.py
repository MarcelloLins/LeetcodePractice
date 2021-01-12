"""
Given the head of a linked list, remove the nth node from the end of the list and return its head

1 -> 2
n = 2

"""
import unittest

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Solution(object):
    def remove_nth_from_end(self, listNode, n):
        if not listNode:
            return None

        head = listNode
        
        # First Phase - Discovery
        stack = []
        while listNode:
            stack.append(listNode)
            listNode = listNode.next

        reverse_index = 1
        while len(stack) > 0:
            current_node = stack.pop()

            # Is this the element we want to remove ?
            if reverse_index == n:
                if len(stack) == 0:                    
                    head = head.next                                
                else:                    
                    previous_node = stack.pop()
                    previous_node.next = current_node.next
                return head

            reverse_index = reverse_index + 1

        return None
            
class SolutionUnitTest(unittest.TestCase):
    def test_remove_nth_from_end(self):
        code = Solution()
        
        test_case_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        response = code.remove_nth_from_end(test_case_1, 2)
        self._compare_lists(response, expected_1)

        test_case_2 = ListNode(1, ListNode(2))
        expected_2 = ListNode(2)
        response = code.remove_nth_from_end(test_case_2, 2)
        self._compare_lists(response, expected_2)

    def _compare_lists(self, response, expected):
        while response and expected:
            self.assertEqual(response.value, expected.value)
            response = response.next
            expected = expected.next

if __name__ == "__main__":
    unittest.main()