#171. Excel Sheet Column Number    26进制转10进制
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for char in s[:-1]:
            ret = (ret+(ord(char) - ord('A')+1))*26
        return ret + ord(s[-1])-ord('A')+1

#171. Excel Sheet Column Number    26进制转10进制
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y:26*x+y,map(lambda x:ord(x)-ord('A')+1,s))    #使用reduce函数
