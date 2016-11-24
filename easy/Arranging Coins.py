#441. Arranging Coins    多少行完整阶梯
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        step = 1
        while n >= 0:
            n -= step
            step += 1
            ret += 1
        return ret - 1
