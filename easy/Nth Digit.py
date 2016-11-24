#400. Nth Digit    数字位拆分后第n个
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        for digit in range(1,11):
            first = 10**(digit-1)
            if n < 9*first*digit:
                return int(str(first + n//digit)[n%digit])
            n -= 9*digit*first   #-9，-99，-999
