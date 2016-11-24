#414. Third Maximum Number       找第三大的数
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        return nums[-3] if len(nums) >= 3 else nums[-1] 
