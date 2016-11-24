#122. Best Time to Buy and Sell Stock II   可多次买卖股票
class Solution(object):            #贪心算法，想得太复杂，对比前后两天
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        profit = 0
        min_price = prices[0]
        L = len(prices)
        prices += [0]
        for i in range(1,L):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] == prices[i+1]:
                prices[i] = prices[i-1]
            if prices[i] > prices[i-1] and prices[i] > prices[i+1]:
                profit += (prices[i]-min_price)
                min_price = prices[i+1]
        return profit

#122. Best Time to Buy and Sell Stock II   可多次买卖股票
class Solution(object):   #直接当后一天比前一天贵就前一天买后一天卖
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices)-1))