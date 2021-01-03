"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

import unittest
import sys

class Solution(object):
    def best_time_buy_stock_brute_force(self, values):
        best_profit = 0

        for i in range(0, len(values)):
            for j in range(i + 1, len(values)):
                buy_value = values[i]
                sell_value = values[j]

                if (sell_value - buy_value > best_profit):
                    best_profit = sell_value - buy_value
        
        return best_profit

    def best_time_buy_stock_elegant(self, values):
        best_profit = 0
        min_price = sys.maxsize

        for i in range(0, len(values)):
            current_price = values[i]
            if current_price < min_price:
                min_price = current_price

            if current_price - min_price > best_profit:
                best_profit = current_price - min_price

        return best_profit



class SolutionUnitTest(unittest.TestCase):
    def test_best_time_buy_stock(self):
        code = Solution()

        test_case_a = [7,1,5,3,6,4]
        self.assertEqual(code.best_time_buy_stock_brute_force(test_case_a), 5)
        self.assertEqual(code.best_time_buy_stock_elegant(test_case_a), 5)

        test_case_b = [7,6,4,3,1]
        self.assertEqual(code.best_time_buy_stock_brute_force(test_case_b), 0)
        self.assertEqual(code.best_time_buy_stock_elegant(test_case_b), 0)

if __name__ == '__main__':
    unittest.main()