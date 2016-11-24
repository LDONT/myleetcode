#172. Factorial Trailing Zeroes    判断n阶乘末尾0的个数
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n ==0 else n//5 + self.trailingZeroes(n//5)    #数5的个数，递归

#172. Factorial Trailing Zeroes    判断n阶乘末尾0的个数
class Solution(object):
    def trailingZeroes(self, n):        
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n>0:
            n /=5    #被5整除，被5*5整除。。。
            ret += n
        return ret