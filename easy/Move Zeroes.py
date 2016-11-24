#283. Move Zeroes    列表中的0往后挪
class Solution(object):          #两两比较
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[point] = nums[point], nums[i]
                point += 1 
