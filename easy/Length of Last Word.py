#58. Length of Last Word*  最后一个单词的长度
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])  #strip去掉首尾空格，split拆分字符串