#189. Rotate Array   列表若干位翻转
class Solution(object):   #三步翻转
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k % len(nums)
        end = len(nums)-1
        self.reverse(nums,0,end-k)
        self.reverse(nums,end-k+1,end)
        self.reverse(nums,0,end)
    def reverse(self,nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1

#189. Rotate Array     列表若干位翻转
class Solution(object):   #自制简单粗暴
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k%len(nums)
        k = len(nums)-k
        for i in range(k):
            nums.append(nums[i])
        del nums[:k]
