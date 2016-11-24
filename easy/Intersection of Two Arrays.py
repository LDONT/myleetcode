#349. Intersection of Two Arrays      两个列表的共有元素
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for num in nums1:
            if num in nums2:
                ret += [num]
        return ret
