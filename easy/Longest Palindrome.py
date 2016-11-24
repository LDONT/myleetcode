#409. Longest Palindrome       找字符串能构成的最长回文
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(v & 1 for v in Counter(s).values())     #v&1判断是否为奇数，总数为奇数的不能构成回文
        return len(s) - odd + bool(odd)
