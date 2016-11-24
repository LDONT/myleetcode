#258. Add Digits    整数各位相加
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num%10
                num /= 10
            num = temp
        return num
