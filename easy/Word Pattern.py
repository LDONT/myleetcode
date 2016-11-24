#290. Word Pattern     字符比配，类似205
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return list(map(pattern.find,pattern)) == list(map(str.split(' ').index, str.split(' ')))     #使用map函数
