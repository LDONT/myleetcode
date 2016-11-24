#447. Number of Boomerangs      距离相等的组合点
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        num = 0
        for p in points:
            dic = {}
            for q in points:
                v = (p[0] - q[0])**2 + (p[1] - q[1])**2
                dic[v] = dic.get(v,0) + 1
            for v in dic:
                num += dic[v] * (dic[v] - 1)
        return num