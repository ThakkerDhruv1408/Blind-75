'''
LeetCode 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:          # Time - O(n), Space - O(1)
        profit, l = 0, 0

        for r in range(1, len(prices)):

            profit = max(profit, prices[r] - prices[l])
            
            if prices[r] < prices[l]:
                l = r

        return profit

        
# Testing

test = Solution()
nums = [7,1,5,3,6,4]
w = test.maxProfit(nums)
print(w)
