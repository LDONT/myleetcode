#107. Binary Tree Level Order Traversal II      #自底向上得到树的元素组成list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                   #笨方法，先得到自顶向下的再用[::-1]反转
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ret = []
        level = [root]
        while level:
            temp = []
            nextlevel = []
            for node in level:
                temp.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            ret.append(temp)
            level = nextlevel
        return ret[::-1]

#107. Binary Tree Level Order Traversal II      #自底向上得到树的元素组成list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                    # 深度优先+递归	
	def levelOrderBottom1(self, root):
    	res = []
    	self.dfs(root, 0, res)
    	return res
	def dfs(self, root, level, res):
    	if root:
        	if len(res) < level + 1:
            	res.insert(0, [])
        	res[-(level+1)].append(root.val)
        	self.dfs(root.left, level+1, res)
        	self.dfs(root.right, level+1, res)
                  
#107. Binary Tree Level Order Traversal II      #自底向上得到树的元素组成list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                    # 深度优先+栈
	def levelOrderBottom2(self, root):
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))
    return res
    
#107. Binary Tree Level Order Traversal II      #自底向上得到树的元素组成list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                    # 广度优先+队列
	def levelOrderBottom(self, root):
    	queue, res = collections.deque([(root, 0)]), []
    	while queue:
        	node, level = queue.popleft()
        	if node:
            	if len(res) < level+1:
                	res.insert(0, [])
            	res[-(level+1)].append(node.val)
            	queue.append((node.left, level+1))
            	queue.append((node.right, level+1))
    	return res