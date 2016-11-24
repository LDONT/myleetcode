#9. Palindrome Number   判断是否回文
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            return x==int(str(x)[::-1])