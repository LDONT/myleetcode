#389. Find the Difference      找字符串的不同
from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cou1, cou2 = Counter(s), Counter(t)
        return list(cou2-cou1)[0]        #先转化为list
