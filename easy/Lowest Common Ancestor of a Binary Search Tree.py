#235. Lowest Common Ancestor of a Binary Search Tree     二叉搜索树的最低公共节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):    #迭代方法
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while (root.val-p.val)*(root.val-q.val)>0:     #二叉搜索树的性质，按大小排列
            root = (root.left,root.right)[p.val > root.val]    #满足条件时取root.right，否则root.left
        return root

#235. Lowest Common Ancestor of a Binary Search Tree     二叉搜索树的最低公共节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):      #递归方法
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if q.val<root.val>p.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if q.val>root.val<p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root