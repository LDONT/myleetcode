#101. Symmetric Tree  *     判断两棵树是否对称
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):         #使用递归的方法
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isSame(root.left,root.right)
    def isSame(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:                      #每次判断两颗子树的四个点
            outpair = self.isSame(left.left,right.right)
            inpair = self.isSame(left.right,right.left)
            if outpair and inpair:
                return True
            else:
                return False
        else:
            return False

#101. Symmetric Tree  *     判断两棵树是否对称
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = [(root.left,root.right)]      #使用栈，迭代方法貌似用时更少
        while stack:
            left,right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left,right.right))
                stack.append((left.right,right.left))
            else:
                return False
        return True   