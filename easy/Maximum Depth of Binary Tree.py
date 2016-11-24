#104. Maximum Depth of Binary Tree  *找树的最大深度
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        #还是用递归的方法
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))