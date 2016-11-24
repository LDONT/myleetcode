#169. Majority Element   找出现最多的数
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}       
        t = len(nums)//2
        for num in nums:
            dic[num] = dic.get(num,0) + 1          #使用字典，第一次出现赋值为0
            if dic[num] > t:
                return num