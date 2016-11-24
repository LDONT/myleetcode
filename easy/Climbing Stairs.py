#70. Climbing Stairs  爬梯子问题，每次一步或者两步
class Solution(object):
    def climbStairs(self, n):        #把梯子的阶数当作对象，每次储存当前和下一阶
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        a,b = 1,2
        for _ in range(1,n):
            a,b = b,a+b
        return a

#70. Climbing Stairs  爬梯子问题，每次一步或者两步
class Solution(object):                 #递归方法，时间复杂度太大
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
		return self.climbStairs(n-1)+self.climbStairs(n-2)