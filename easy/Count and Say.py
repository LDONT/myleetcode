#38. Count and Say  *
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)           #不是很懂
        return s

#38. Count and Say  *
class Solution(object):     #更好理解，时间更短
     def countAndSay(self, n):
         s = '1'
         for _ in range(n-1):
             r = ''
             pre = s[0]
             count = 0
             for l in s:
                 if l == pre:
                     count += 1 
                 else:
                     r+=str(count)+pre
                     pre = l
                     count = 1
             r+=str(count)+pre
             s = r
         return s