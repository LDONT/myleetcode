#219. Contains Duplicate II   判断列表中重复数字的坐标差不大于k
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):     #enumerate函数遍历整个列表
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False