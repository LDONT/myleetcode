#412. Fizz Buzz       3,5倍数
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz'*(not m % 3) + 'Buzz'*(not m % 5) or str(m) for m in range(1,n+1)]       # *True/False   or命令
