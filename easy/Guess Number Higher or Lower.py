#374. Guess Number Higher or Lower     二分法查找
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min, max = 1, n
        while min < max:
            mid = (min + max)//2
            if guess(mid) == -1:
                max = mid
            elif guess(mid) == 1:
                min = mid+1
            elif guess(mid) == 0:
                return mid
        return min
