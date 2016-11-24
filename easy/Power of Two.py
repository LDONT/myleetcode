#231. Power of Two   判断一个数是否为2的多次方
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n!= 1:    #直接判断除2的余数
            m = n%2
            if m!= 0:
                return False
            n /= 2
        return True

#231. Power of Two   判断一个数是否为2的多次方
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n&(n-1)   #按位与，16 = b10000，16 - 1 = b01111，16 & 16 - 1  = 0。但时间貌似更久
