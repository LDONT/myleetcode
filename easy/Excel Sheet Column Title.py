#168. Excel Sheet Column Title    26进制转换
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if n == 0 else self.convertToTitle((n-1)/26) + chr((n-1)%26 + ord('A'))   #利用递归
