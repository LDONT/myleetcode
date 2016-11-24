#111. Minimum Depth of Binary Tree       计算树的最小深度  
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(1,root)]
        while stack:               #广度优先，栈
            level,node = stack.pop()
            if node.right is None and node.left is None:
                return level
            if node.right is not None:
                stack.insert(0,(level+1,node.right))
            if node.left is not None:
                stack.insert(0,(level+1,node.left))    

#111. Minimum Depth of Binary Tree       计算树的最小深度      
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):              #迭代的方法
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1