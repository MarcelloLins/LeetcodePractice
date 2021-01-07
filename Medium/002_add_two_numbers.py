"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
import unittest
class ListNode(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Solution(object):
    def sum_two_numbers(self, n1, n2):
        result_head = ListNode(-1)
        result_tail = result_head

        carry_over = 0        
        while n1 or n2:            
            m1 = n1.value if n1 else 0
            m2 = n2.value if n2 else 0            

            # Performing SUM
            resulting_sum = m1 + m2 + carry_over
            
            # Do we need to carry over to the next round ?
            # Carry overs are either 0 or 1
            carry_over = (int)(resulting_sum / 10)

            # If we have a carry over, we need to subtract it from the current sum
            resulting_sum = (int)(resulting_sum % 10)
            
            # Adding value to list
            result_head.next = ListNode(resulting_sum)
            result_head = result_head.next

            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        # Did we have one last carry over ?
        if carry_over > 0:
            result_head.next = ListNode(carry_over)
            result_head = result_head.next

        return result_tail.next

    def _init_stack_from_linked_list(self, listNode):
        stack = list()
        while listNode:        
            stack.append(listNode.value)
            listNode = listNode.next
        return stack

class SolutionUnitTest(unittest.TestCase):
    def test_sum_two_numbers_case_1(self):
        code = Solution()
        n1 = self.build_linked_list_from_list([2,4,3])
        n2 = self.build_linked_list_from_list([5,6,4])
        expected_result = self.build_linked_list_from_list([7,0,8])
        actual_result = code.sum_two_numbers(n1, n2)

        self.compare_lists(expected_result, actual_result)

    def test_sum_two_numbers_case_2(self):
        code = Solution()
        n1 = self.build_linked_list_from_list([0])
        n2 = self.build_linked_list_from_list([0])
        expected_result = self.build_linked_list_from_list([0])
        actual_result = code.sum_two_numbers(n1, n2)

        self.compare_lists(expected_result, actual_result)

    def test_sum_two_numbers_case_3(self):
        code = Solution()
        n1 = self.build_linked_list_from_list([9,9,9,9,9,9,9])
        n2 = self.build_linked_list_from_list([9,9,9,9])
        expected_result = self.build_linked_list_from_list([8,9,9,9,0,0,0,1])
        actual_result = code.sum_two_numbers(n1, n2)

        self.compare_lists(expected_result, actual_result)

    def compare_lists(self, n1, n2):
        while n1 or n2:
            self.assertEqual(n1.value, n2.value)
            n1 = n1.next
            n2 = n2.next

    def build_linked_list_from_list(self, source):
        head = ListNode(-1)
        tail = head

        for x in source:
            head.next = ListNode(x)
            head = head.next

        return tail.next

if __name__ == "__main__":
    unittest.main()