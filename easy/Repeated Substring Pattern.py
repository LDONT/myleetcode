#459. Repeated Substring Pattern    字符串是否能由子字符串重复构成
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        l = len(str)
        for i in range(1,l//2+1):
            if l % i != 0:
                continue
            li = str.split(str[:i])
            if len(set(li)) == 1:
                return True
        return False
