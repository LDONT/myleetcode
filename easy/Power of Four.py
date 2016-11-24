#342. Power of Four     判断是否为4的多次方
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num     #先判断是否为2的多次方，进一步确定1的位置
