#303. Range Sum Query - Immutable    列表指定位置的和
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.li = nums
        for i in range(1,len(nums)):
            self.li[i] += self.li[i-1]    #下面的函数会多次调用，所以先储存起来
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.li[j] - (self.li[i-1] if i >0 else 0)
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
