#415. Add Strings    两个字符串相加
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(reduce(lambda x,y: x*10 + ord(y)-48, num1, 0) + reduce(lambda x,y: x*10 + ord(y)-48, num2, 0))    #reduce函数最后一个初始值可省略
