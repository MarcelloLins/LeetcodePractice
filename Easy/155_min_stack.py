"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
import unittest
import sys
class Stack(object):
    def __init__(self):
        self.data = list()
        self.min = list()

    def push(self, x):
        if x is not None:
            self.data.append(x)

            # If we are adding a new minimum we need to persist it
            self.update_new_min(x)

    def pop(self) -> int:
        last_element = self.data.pop()
        
        # If we are popping the current min, we need a new minimum
        if last_element == self.min[-1]:
            self.min.pop()
        return last_element

    def top(self) -> int:
        if len(self.data) > 0:
            return self.data[-1]
        return None

    def getMin(self) -> int:
        if len(self.min) > 0:
            return self.min[-1]
        return None

    def update_new_min(self, candidate):
        if len(self.min) == 0 or candidate <= self.min[-1]:
            self.min.append(candidate)
        

class StackUnitTest(unittest.TestCase):
    def test_stack(self):
        stack = Stack()

        testStack = Stack()
        testStack.push(-2)
        testStack.push(0)
        testStack.push(-3)
        
        self.assertEqual(testStack.getMin(), -3)
        self.assertEqual(testStack.pop(), -3)
        self.assertEqual(testStack.top(), 0)        
        self.assertEqual(testStack.getMin(), -2)

        testStack = Stack()
        testStack.push(0)
        testStack.push(1)
        testStack.push(0)
        self.assertEqual(testStack.getMin(), 0)
        self.assertEqual(testStack.pop(), 0)
        self.assertEqual(testStack.getMin(), 0)


if __name__ == "__main__":
    unittest.main()