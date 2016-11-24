#66. Plus One*  数组数字加一
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x,y:x*10+y,digits)+1   #lambda reduce全局函数
        return [int(i) for i in str(num)]
        
#66. Plus One*  数组数字加一
class Solution(object):      #非lambda方法
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
            num += digits[i]*pow(10,len(digits)-i-1)
        return [int(j) for j in str(num+1)]