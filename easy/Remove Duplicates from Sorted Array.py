#26. Remove Duplicates from Sorted Array*  找有序list中不同整数的个数n，且前n个元素为这n个不同的数。不能用其他的物理资源
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if not nums:
            return 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i = i+1
                nums[i] = nums[j]      #对自己修改
        return i+1  