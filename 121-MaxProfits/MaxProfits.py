class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        interestPrice = prices[0]
        maxDifference = 0
        for price in prices:
            if price - interestPrice > maxDifference:
                maxDifference = price - interestPrice
            if price < interestPrice:
                interestPrice = price
        return maxDifference
