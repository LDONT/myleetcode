#20. Valid Parentheses * 判断输入的括号是否有效
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {'}':'{',']':'[',')':'('}
        for char in s:								# for char in s
            if char in table.values():									
                stack.append(char)                 #使用栈
            if char in table.keys():
                if stack==[] or stack.pop() != table[char]:
                    return False
        return stack==[]