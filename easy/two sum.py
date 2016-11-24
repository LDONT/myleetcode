#1. two sum    5392ms
class Solution(object):  
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            for index2 in range(index+1,len(nums)):
                if nums[index]+nums[index2]==target:
                    return [index,index2]
                    break
#1. two sum*    #65ms
class Solution(object): 
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        process={}
        for index in range(len(nums)):
            if target-nums[index] in process:
                return [process[target-nums[index]],index]
                break
            process[nums[index]]=index 