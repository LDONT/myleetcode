#13. Roman to Integer 
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        temp=0
        r=0
        for i in range(len(s)-1):
            temp+=1
            if dic[s[i]]>dic[s[i+1]]:
                r+=temp*dic[s[i]]
                temp=0
            if dic[s[i]]<dic[s[i+1]]:
                r-=temp*dic[s[i]]
                temp=0
        temp+=1
        r+=temp*dic[s[len(s)-1]]
        return r
#13. Roman to Integer *     
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r = 0
        for i in range(len(s)-1):
            val = table[s[i]]
            if val >= table[s[i+1]]:
                r += val
            else:
                r -= val
        r += table[s[len(s)-1]]
        return r