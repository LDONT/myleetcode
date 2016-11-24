#28. Implement strStr()     找字符串中子字符串的位置
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:                #自己写的更好简单
            return haystack.index(needle)
        else:
            return -1
            
#28. Implement strStr() *    找字符串中子字符串的位置
class Solution(object):
	def strStr(self, haystack, needle):
    	"""
    	:type haystack: str
    	:type needle: str
    	:rtype: int
    	"""
    	for i in range(len(haystack) - len(needle)+1):  
        	if haystack[i:i+len(needle)] == needle:
            	return i
    	return -1            