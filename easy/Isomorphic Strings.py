#205. Isomorphic Strings   两个字符串一一对应
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.find,s)) == list(map(t.find,t))
        
#205. Isomorphic Strings   两个字符串一一对应
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) and len(set(zip(t,s))) == len(set(t))   #zip函数