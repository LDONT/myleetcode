#278. First Bad Version      二分法找最小
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min, max = 1, n
        while min < max:
            mid = (min+max)//2
            if isBadVersion(mid):
                max = mid
            else:
                min = mid + 1
        return min
