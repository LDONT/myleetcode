#198. House Robber    列表中隔一最大和
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(now, last + num)  #比较上一个最优和当前值加上上个最优的大小
        return now     
