#7. Reverse Integer  整数反转
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            r=int(str(x)[::-1])   #反向步进切片，每步-1
        if x <= 0:
            x=abs(x)
            r=-int(str(x)[::-1])
        if r>2147483647 or r<-2147483647:   #考虑溢出2^31-1
            r = 0
        return r    