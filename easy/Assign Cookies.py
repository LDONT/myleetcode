#455. Assign Cookies      两个列表组合
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        ret = 0
        init = 0
        for cookies in s:
            if init < len(g) and g[init] <= cookies:
                ret += 1
                init += 1
        return ret
