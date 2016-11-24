#292. Nim Game   仍石子游戏，脑筋急转弯
class Solution(object):     #只要是4的倍数就输了
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n %4 == 0:
            return False
        else:
            return True
