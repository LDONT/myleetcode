#299. Bulls and Cows     数值、位置匹配
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = sum(map(operator.eq, secret,guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')    #所有的相同元素个数和
        return '%dA%dB' % (bulls, both - bulls)
