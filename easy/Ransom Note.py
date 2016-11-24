#383. Ransom Note   判断字符串是否能用另一个构成
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cou1 = Counter(ransomNote)
        cou2 = Counter(magazine)
        return not cou1-cou2
