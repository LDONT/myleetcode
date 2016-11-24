#118. Pascal's Triangle   杨辉三角    
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        ret = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = [1]
            for j in range(len(ret[i-2])-1):
                temp += [ret[i-2][j]+ret[i-2][j+1]] 
            temp += [1]
            ret += [temp]
        return ret    
    
#118. Pascal's Triangle   杨辉三角  
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1]]
        for i in range(1,numRows):   #利用杨辉三角的性质，0121+1210
            ret += [map(lambda x,y:x+y, ret[-1]+[0],[0]+ret[-1])]
        return ret[:numRows]    
