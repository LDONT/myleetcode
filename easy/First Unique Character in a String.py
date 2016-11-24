#387. First Unique Character in a String     寻找字符串中第一个不重复字符
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cou = Counter(s)
        for i in range(len(s)):
            if cou[s[i]] == 1:
                return i
        return -1
