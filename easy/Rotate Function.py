#396. Rotate Function      列表旋转乘积找最大值
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        l = range(len(A))
        length = len(A)
        ret = sum(list(map(lambda x,y:x*y,l,A)))
        vi = ret
        sa = sum(A)
        for i in range(len(A)-1,0,-1):       #规律
            vi = vi+sa-length*A[i]
            ret = max(ret,vi)
        return ret
