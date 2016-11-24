#112. Path Sum     * 计算根节点到叶节点的和是否等于一个数    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val          #sum减去，利用递归
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)    