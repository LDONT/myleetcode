#202. Happy Number    开心数字
class Solution(object):    #速度有点慢
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while n != 1:
            l += [n] 
            n = self.add(n)
            if n in l:
                return False
        return True
    def add(self,n):
        num = 0
        for char in str(n):
            num += int(char)**2
        return num 

#202. Happy Number    开心数字
class Solution(object):
    def isHappy(self, n):    #利用循环
        """
        :type n: int
        :rtype: bool
        """
        fast = self.next(n)
        slow = n
        while fast != slow:
            fast = self.next(self.next(fast))
            slow = self.next(slow)
        return fast == 1
    def next(self,n):
        num = 0
        while n>0:
            num += (n%10)**2
            n /=10
        return num  