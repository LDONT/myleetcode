#453. Minimum Moves to Equal Array Elements      每次n-1个元素加一，使最终相等
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)    #转化为每次一个元素减一
