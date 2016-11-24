#404. Sum of Left Leaves     二叉树所有左边叶节点相加
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0
        if not root:
            return ret
        if root.left and not root.left.left and not root.left.right:
            ret += root.left.val
        if root.left:
            ret += self.sumOfLeftLeaves(root.left)
        if root.right:
            ret += self.sumOfLeftLeaves(root.right)
        return ret
