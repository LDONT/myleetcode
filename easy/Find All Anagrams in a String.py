#438. Find All Anagrams in a String    找字符串中子字符串所有可能位置
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l = len(p)
        cou = Counter(p)
        cous = Counter(s[:l])
        ret = []
        for i in range(len(s)-l+1):
            if cous == cou:
                ret += [i]
            if i < len(s)-l:
                cous[s[i+l]] = cous.get(s[i+l],0) + 1
                if cous[s[i]] == 1:
                    del cous[s[i]]
                if cous[s[i]] > 1:
                    cous[s[i]] -= 1
        return ret
