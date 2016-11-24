#155. Min Stack  构建一个栈
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []       
    def push(self, x):    #在push过程中就存储好最小的数
        """
        :type x: int
        :rtype: void
        """
        if self.getMin() is None:
            self.stack.append((x,x))
        else:
            self.stack.append((x,min(self.getMin(),x)))
    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()      
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        else:
            return None
    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]  
        else:
            return None
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
