#257. Binary Tree Paths    返回二叉树的所有路径
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:             #使用递归方法
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        ret = []
        self.add(root,'',ret)
        return ret
    def add(self,root,li,ret):
        if root.left is None and root.right is None:
            ret.append(li+str(root.val))
        if root.left:
            self.add(root.left,li+str(root.val)+'->',ret)
        if root.right:
            self.add(root.right,li+str(root.val)+'->',ret)
