#350. Intersection of Two Arrays II    两个列表的共有元素，可以重复
class Solution(object):      #时间比较慢
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        dic = {}
        for num in nums1:
            dic[num] = dic.get(num,0) + 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                dic[num] -= 1
                ret += [num]
        return ret
