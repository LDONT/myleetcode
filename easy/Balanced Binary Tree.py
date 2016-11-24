#110. Balanced Binary Tree    判断一棵树是否是平衡二叉树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return -1 != self.check(root)        
    def check(self,root):      #定义函数计算每个节点的深度
        if root is None:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if left == -1 or right == -1 or abs(left-right)>1:
            return -1
        else:
            return 1+max(left,right)