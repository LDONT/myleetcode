#14. Longest Common Prefix  找所有字符串中的最大共有的首字符串部分  
class Solution(object):
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''          #当有一个return后，函数剩下的都不运行
        com = strs[0]
        for i in range(len(com)):
            for j in strs:
                if i >= len(j) or j[i]!=com[i]:
                    return com[0:i]
        return com