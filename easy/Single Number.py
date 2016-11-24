#136. Single Number  找列表中只出现一次的数
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            ret ^= num    #利用异或，整数先转化为二进制
        return ret
        
#136. Single Number  找列表中只出现一次的数
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y:x^y,nums)

#136. Single Number  找列表中只出现一次的数
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)   #利用set函数