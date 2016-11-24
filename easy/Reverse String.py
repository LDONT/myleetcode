#344. Reverse String   翻转字符串
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]    #简单

#344. Reverse String   翻转字符串
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if len(s)  < 2:
            return s
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])     #递归方法，时间更长
        
#344. Reverse String   翻转字符串
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = list(s)
        i, j = 0, len(s) -1
        while i < j:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
        return ''.join(li)       #借用列表
