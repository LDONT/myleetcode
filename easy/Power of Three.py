#326. Power of Three   判断是否为3的多次方
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19%n == 0    #32位最大19次方
