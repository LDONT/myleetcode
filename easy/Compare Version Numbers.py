#165. Compare Version Numbers  比较两个版本数字的大小
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))
        for i in range(max(len(v1),len(v2))):
            temp1 = v1[i] if i<len(v1) else 0
            temp2 = v2[i] if i<len(v2) else 0
            if temp1>temp2:
                return 1
            elif temp1<temp2:
                return -1
        return 0