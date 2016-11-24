#223. Rectangle Area   两个长方形的面积
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x = [A,C,E,G]
        y = [F,H,B,D]
        x.sort()
        y.sort()
        if x[1] in [A,E] and y[1] in [F,B]:
            return (C-A)*(D-B)+(G-E)*(H-F) - (x[2] - x[1])*(y[2] - y[1])
        else:
            return (C-A)*(D-B)+(G-E)*(H-F)

#223. Rectangle Area   两个长方形的面积
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = max(min(C,G)-max(A,E),0)*max(min(D,H)-max(B,F),0)   #先计算重叠部分
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap
