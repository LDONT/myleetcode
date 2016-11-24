#119. Pascal's Triangle II  杨辉三角返回某个index的行
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in range(0,rowIndex):
            ret = list(map(lambda x,y:x+y,[0]+ret,ret+[0]))
        return ret