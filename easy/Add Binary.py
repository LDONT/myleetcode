#67. Add Binary *   二进制数相加  
class Solution(object):
    def addBinary(self, a, b):         #递归的思想self.
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return (a or b)
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1')+'0'
        else :
            return self.addBinary(a[:-1],b[:-1])+str(int(a[-1])+int(b[-1]))  