# 122. Best Time to Buy and Sell Stock II

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > left:
                res += prices[i] - left
            left  =  prices[i]
        return res

'''
time: o(n)
spsce: o(1)
'''