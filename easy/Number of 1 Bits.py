#191. Number of 1 Bits   找二进制数1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2:]
        return num.count('1') 
