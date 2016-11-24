# 8. String to Integer (atoi)  
def ov(n):
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31
    return MIN if n < MIN else\
           MAX if n > MAX else n
class Solution(object):
    def myAtoi(self, str):
        import re
        str = str.strip()
        m = re.findall(r'^(?<![\+\-])[\+\-]?[0-9]+', str)
        if not m or not str:
            return 0
        m, d = m[0], lambda x: ord(x) - 48
        sign = 1 if m[0] != '-' else -1
        res = 0
        for e in m:
            if e not in '+-':
                res = res * 10 + d(e)
        return ov(res *sign)                