#217. Contains Duplicate      判断列表中是否存在相同元素
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
            if dic[num] >1:
                return True
        return False

#217. Contains Duplicate      判断列表中是否存在相同元素
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) 
