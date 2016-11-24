#102. Binary Tree Level Order Traversal   二叉树遍历按级返回数组
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):                 #广度优先搜索bfs
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level = [root]
        if root is None:
            return []
        while level:
            nextlevel = []
            temp = []
            for node in level:
                if node.left:
                    nextlevel.append(node.left)           #直接把节点存入到list中
                if node.right:
                    nextlevel.append(node.right)
                temp.append(node.val)
            ret.append(temp)
            level = nextlevel
        return ret