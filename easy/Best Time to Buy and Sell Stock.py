#121. Best Time to Buy and Sell Stock  列表后减前最大值
class Solution(object):     
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:             #动态规划
            min_price = min(min_price,price)
            if price != min_price:
                max_profit = max(max_profit,price - min_price)
        return max_profit