#242. Valid Anagram   两个字符串的字母是否相同
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)    #sorted函数
