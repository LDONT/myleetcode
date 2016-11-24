#1. two sum    5392ms
class Solution(object):  
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            for index2 in range(index+1,len(nums)):
                if nums[index]+nums[index2]==target:
                    return [index,index2]
                    break
#1. two sum*    #65ms
class Solution(object): 
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        process={}
        for index in range(len(nums)):
            if target-nums[index] in process:
                return [process[target-nums[index]],index]
                break
            process[nums[index]]=index      
            
#2. add two number*   
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        ret = ListNode(0)  
        cur = ret  
        sum = 0  
        while True:  
            if l1 != None:  
                sum += l1.val  
                l1 = l1.next  
            if l2 != None:  
                sum += l2.val  
                l2 = l2.next  
            cur.val = sum % 10  
            sum /= 10  
            if l1 != None or l2 != None or sum != 0:  #链表
                cur.next = ListNode(0)  
                cur = cur.next  
            else:  
                break  
        return ret     
        
#6. ZigZag Conversion*
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
    		return s
    	length=len(s)
    	wordlist=[""]*numRows
    	charclass=[0]*length               #初始化很赞
    	for i in range(length):
    		charclass[i] = i%(2*numRows-2)
    		if charclass[i] > numRows-1:
    			charclass[i]=2*numRows-2-charclass[i] 
    	for i in range(length):
    		wordlist[charclass[i]]+=(s[i])
    	return "".join(wordlist)
#6. ZigZag Conversion*  更好理解时间也短
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < 2: return s
        rows = ["" for _ in range(numRows)]
        i, right = -1, True
        for ch in s:
            i = i + 1 if right else i - 1
            rows[i] += ch
            right = False if i == numRows-1 else True if i == 0 else right
        return "".join(rows)    	   
        
#7. Reverse Integer  整数反转
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            r=int(str(x)[::-1])   #反向步进切片，每步-1
        if x <= 0:
            x=abs(x)
            r=-int(str(x)[::-1])
        if r>2147483647 or r<-2147483647:   #考虑溢出2^31-1
            r = 0
        return r           
        
# 8. String to Integer (atoi)  
def ov(n):
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31
    return MIN if n < MIN else\
           MAX if n > MAX else n
class Solution(object):
    def myAtoi(self, str):
        import re
        str = str.strip()
        m = re.findall(r'^(?<![\+\-])[\+\-]?[0-9]+', str)
        if not m or not str:
            return 0
        m, d = m[0], lambda x: ord(x) - 48
        sign = 1 if m[0] != '-' else -1
        res = 0
        for e in m:
            if e not in '+-':
                res = res * 10 + d(e)
        return ov(res *sign)                
        
#9. Palindrome Number   判断是否回文
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            return x==int(str(x)[::-1])
            
#13. Roman to Integer 自己写的
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        temp=0
        r=0
        for i in range(len(s)-1):
            temp+=1
            if dic[s[i]]>dic[s[i+1]]:
                r+=temp*dic[s[i]]
                temp=0
            if dic[s[i]]<dic[s[i+1]]:
                r-=temp*dic[s[i]]
                temp=0
        temp+=1
        r+=temp*dic[s[len(s)-1]]
        return r
#13. Roman to Integer *似乎更好理解       
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r = 0
        for i in range(len(s)-1):
            val = table[s[i]]
            if val >= table[s[i+1]]:
                r += val
            else:
                r -= val
        r += table[s[len(s)-1]]
        return r
        
#14. Longest Common Prefix  找所有字符串中的最大共有的首字符串部分  
class Solution(object):
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''          #当有一个return后，函数剩下的都不运行
        com = strs[0]
        for i in range(len(com)):
            for j in strs:
                if i >= len(j) or j[i]!=com[i]:
                    return com[0:i]
        return com

#19. Remove Nth Node From End of List *   删掉一个链表的尾部第n个节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        k1=head                             #链表，指针
        k2=head
        for i in range(n):
            k1= k1.next
            if k1==None:
                return head.next
        while k1.next != None:
            k1=k1.next
            k2=k2.next
        k2.next=k2.next.next
        return head
        
#20. Valid Parentheses * 判断输入的括号是否有效
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {'}':'{',']':'[',')':'('}
        for char in s:								# for char in s
            if char in table.values():									
                stack.append(char)                 #使用栈
            if char in table.keys():
                if stack==[] or stack.pop() != table[char]:
                    return False
        return stack==[]
                
#21. Merge Two Sorted Lists* 两个有序的链表整合到一个有序链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):                      #迭代思想
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
       
#21. Merge Two Sorted Lists* 两个有序的链表整合到一个有序链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):                      #递归思想
	def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2 

#23. Merge k Sorted Lists *多个有序链表合并
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):           #堆排序，不是很懂
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next
        return dummy.next   
        
#24. Swap Nodes in Pairs *链表交换节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre,pre.next = self,head          #self代替dummy
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            a.next = pre.next.next.next
            b.next = a
            pre.next = b
            pre = a
        return self.next
        
#26. Remove Duplicates from Sorted Array*  找有序list中不同整数的个数n，且前n个元素为这n个不同的数。不能用其他的物理资源
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if not nums:
            return 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i = i+1
                nums[i] = nums[j]      #对自己修改
        return i+1   

#27. Remove Element 和上题类似，移除列表中的指定数字
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i 
                
#28. Implement strStr()     找字符串中子字符串的位置
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:                #自己写的更好简单
            return haystack.index(needle)
        else:
            return -1
            
#28. Implement strStr() *    找字符串中子字符串的位置
class Solution(object):
	def strStr(self, haystack, needle):
    	"""
    	:type haystack: str
    	:type needle: str
    	:rtype: int
    	"""
    	for i in range(len(haystack) - len(needle)+1):  
        	if haystack[i:i+len(needle)] == needle:
            	return i
    	return -1            

#38. Count and Say  *
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)           #不是很懂
        return s

#38. Count and Say  *
class Solution(object):     #更好理解，时间更短
     def countAndSay(self, n):
         s = '1'
         for _ in range(n-1):
             r = ''
             pre = s[0]
             count = 0
             for l in s:
                 if l == pre:
                     count += 1 
                 else:
                     r+=str(count)+pre
                     pre = l
                     count = 1
             r+=str(count)+pre
             s = r
         return s
         
#58. Length of Last Word*  最后一个单词的长度
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])  #strip去掉首尾空格，split拆分字符串
        
#66. Plus One*  数组数字加一
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x,y:x*10+y,digits)+1   #lambda reduce全局函数
        return [int(i) for i in str(num)]
        
#66. Plus One*  数组数字加一
class Solution(object):      #非lambda方法
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
            num += digits[i]*pow(10,len(digits)-i-1)
        return [int(j) for j in str(num+1)]
        
#67. Add Binary *   二进制数相加  
class Solution(object):
    def addBinary(self, a, b):         #递归的思想self.
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return (a or b)
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1')+'0'
        else :
            return self.addBinary(a[:-1],b[:-1])+str(int(a[-1])+int(b[-1]))  
            
#70. Climbing Stairs  爬梯子问题，每次一步或者两步
class Solution(object):
    def climbStairs(self, n):        #把梯子的阶数当作对象，每次储存当前和下一阶
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        a,b = 1,2
        for _ in range(1,n):
            a,b = b,a+b
        return a

#70. Climbing Stairs  爬梯子问题，每次一步或者两步
class Solution(object):                 #递归方法，时间复杂度太大
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
		return self.climbStairs(n-1)+self.climbStairs(n-2)

#83. Remove Duplicates from Sorted List   链表中删除相同的元素
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre,pre.next = self,head
        var = []
        if head == None:
            return head
        while pre.next != None:
            if pre.next.val in var:
                pre.next = pre.next.next 
            else :
                var += [pre.next.val]
                pre = pre.next
        return head

#88. Merge Sorted Array *  两个有序数组合并
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m and n:             #从后往前赋值，省去推移
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n:
            nums1[:n] = nums2[:n]

#100. Same Tree*   判断是否为相同的树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):     #树用递归的方法
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

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
    
#118. Pascal's Triangle   杨辉三角    
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        ret = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = [1]
            for j in range(len(ret[i-2])-1):
                temp += [ret[i-2][j]+ret[i-2][j+1]] 
            temp += [1]
            ret += [temp]
        return ret    
    
#118. Pascal's Triangle   杨辉三角  
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1]]
        for i in range(1,numRows):   #利用杨辉三角的性质，0121+1210
            ret += [map(lambda x,y:x+y, ret[-1]+[0],[0]+ret[-1])]
        return ret[:numRows]    

#119. Pascal's Triangle II  杨辉三角返回某个index的行
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in range(0,rowIndex):
            ret = list(map(lambda x,y:x+y,[0]+ret,ret+[0]))
        return ret

#121. Best Time to Buy and Sell Stock  列表后减前最大值
class Solution(object):     
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:             #动态规划
            min_price = min(min_price,price)
            if price != min_price:
                max_profit = max(max_profit,price - min_price)
        return max_profit

#122. Best Time to Buy and Sell Stock II   可多次买卖股票
class Solution(object):            #贪心算法，想得太复杂，对比前后两天
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        profit = 0
        min_price = prices[0]
        L = len(prices)
        prices += [0]
        for i in range(1,L):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] == prices[i+1]:
                prices[i] = prices[i-1]
            if prices[i] > prices[i-1] and prices[i] > prices[i+1]:
                profit += (prices[i]-min_price)
                min_price = prices[i+1]
        return profit

#122. Best Time to Buy and Sell Stock II   可多次买卖股票
class Solution(object):   #直接当后一天比前一天贵就前一天买后一天卖
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices)-1))
        
#125. Valid Palindrome  判断回文
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0,len(s)-1    #两端夹逼
        while l<r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

#136. Single Number  找列表中只出现一次的数
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            ret ^= num    #利用异或，整数先转化为二进制
        return ret
        
#136. Single Number  找列表中只出现一次的数
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y:x^y,nums)

#136. Single Number  找列表中只出现一次的数
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)   #利用set函数

#141. Linked List Cycle   判断链表是否循环
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):   #利用异常，若能到达链尾则没有循环
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while fast is not slow:    #两个指针的差距1,2,3...
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False

#141. Linked List Cycle   判断链表是否循环
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):          #不使用异常
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#155. Min Stack  构建一个栈
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []       
    def push(self, x):    #在push过程中就存储好最小的数
        """
        :type x: int
        :rtype: void
        """
        if self.getMin() is None:
            self.stack.append((x,x))
        else:
            self.stack.append((x,min(self.getMin(),x)))
    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()      
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        else:
            return None
    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]  
        else:
            return None
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#160. Intersection of Two Linked Lists    #找两个链表的交叉点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import gc
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        curA,curB = headA,headB
        while curA is not curB:        #总路径等于两段单独加上共有
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        gc.collect()
        return curA

#165. Compare Version Numbers  比较两个版本数字的大小
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))
        for i in range(max(len(v1),len(v2))):
            temp1 = v1[i] if i<len(v1) else 0
            temp2 = v2[i] if i<len(v2) else 0
            if temp1>temp2:
                return 1
            elif temp1<temp2:
                return -1
        return 0

#168. Excel Sheet Column Title    26进制转换
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if n == 0 else self.convertToTitle((n-1)/26) + chr((n-1)%26 + ord('A'))   #利用递归

#169. Majority Element   找出现最多的数
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}       
        t = len(nums)//2
        for num in nums:
            dic[num] = dic.get(num,0) + 1          #使用字典，第一次出现赋值为0
            if dic[num] > t:
                return num

#171. Excel Sheet Column Number    26进制转10进制
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for char in s[:-1]:
            ret = (ret+(ord(char) - ord('A')+1))*26
        return ret + ord(s[-1])-ord('A')+1

#171. Excel Sheet Column Number    26进制转10进制
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y:26*x+y,map(lambda x:ord(x)-ord('A')+1,s))    #使用reduce函数

#172. Factorial Trailing Zeroes    判断n阶乘末尾0的个数
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n ==0 else n//5 + self.trailingZeroes(n//5)    #数5的个数，递归

#172. Factorial Trailing Zeroes    判断n阶乘末尾0的个数
class Solution(object):
    def trailingZeroes(self, n):        
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n>0:
            n /=5    #被5整除，被5*5整除。。。
            ret += n
        return ret

#189. Rotate Array   列表若干位翻转
class Solution(object):   #三步翻转
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k % len(nums)
        end = len(nums)-1
        self.reverse(nums,0,end-k)
        self.reverse(nums,end-k+1,end)
        self.reverse(nums,0,end)
    def reverse(self,nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1

#189. Rotate Array     列表若干位翻转
class Solution(object):   #自制简单粗暴
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k%len(nums)
        k = len(nums)-k
        for i in range(k):
            nums.append(nums[i])
        del nums[:k]

#190. Reverse Bits    二进制翻转
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = bin(n)[2:]    #转化为2进制
        return int(num.zfill(32)[::-1],2)   

#191. Number of 1 Bits   找二进制数1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2:]
        return num.count('1') 

#198. House Robber    列表中隔一最大和
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(now, last + num)  #比较上一个最优和当前值加上上个最优的大小
        return now     

#202. Happy Number    开心数字
class Solution(object):    #速度有点慢
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while n != 1:
            l += [n] 
            n = self.add(n)
            if n in l:
                return False
        return True
    def add(self,n):
        num = 0
        for char in str(n):
            num += int(char)**2
        return num 

#202. Happy Number    开心数字
class Solution(object):
    def isHappy(self, n):    #利用循环
        """
        :type n: int
        :rtype: bool
        """
        fast = self.next(n)
        slow = n
        while fast != slow:
            fast = self.next(self.next(fast))
            slow = self.next(slow)
        return fast == 1
    def next(self,n):
        num = 0
        while n>0:
            num += (n%10)**2
            n /=10
        return num  

#203. Remove Linked List Elements   移除链表中的指定数值
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next != None:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next

#204. Count Primes    数小于n的质数个数
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        for i in range(2,int((n-1)**0.5)+1):   #因子只可能是2到根号（n-1）中取值
            if primes[i]:
                primes[i*i:n:i] = [False]*len(primes[i*i:n:i])   #i*i,i*(i+1)...非质数
        return sum(primes)

#205. Isomorphic Strings   两个字符串一一对应
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.find,s)) == list(map(t.find,t))
        
#205. Isomorphic Strings   两个字符串一一对应
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) and len(set(zip(t,s))) == len(set(t))   #zip函数
        
#206. Reverse Linked List   翻转一个链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):         #迭代方法，使用两个指针
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre

#206. Reverse Linked List   翻转一个链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):         #递归方法
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head,None)               
    def reverse(self,node,pre):
        if node:
            n = node.next
            node.next = pre
            pre = node
        else :
            return pre
        return self.reverse(n,pre)
        
#217. Contains Duplicate      判断列表中是否存在相同元素
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
            if dic[num] >1:
                return True
        return False

#217. Contains Duplicate      判断列表中是否存在相同元素
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) 

#219. Contains Duplicate II   判断列表中重复数字的坐标差不大于k
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):     #enumerate函数遍历整个列表
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False

#223. Rectangle Area   两个长方形的面积
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x = [A,C,E,G]
        y = [F,H,B,D]
        x.sort()
        y.sort()
        if x[1] in [A,E] and y[1] in [F,B]:
            return (C-A)*(D-B)+(G-E)*(H-F) - (x[2] - x[1])*(y[2] - y[1])
        else:
            return (C-A)*(D-B)+(G-E)*(H-F)

#223. Rectangle Area   两个长方形的面积
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = max(min(C,G)-max(A,E),0)*max(min(D,H)-max(B,F),0)   #先计算重叠部分
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap

#226. Invert Binary Tree   翻转一个二叉树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

#231. Power of Two   判断一个数是否为2的多次方
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n!= 1:    #直接判断除2的余数
            m = n%2
            if m!= 0:
                return False
            n /= 2
        return True

#231. Power of Two   判断一个数是否为2的多次方
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n&(n-1)   #按位与，16 = b10000，16 - 1 = b01111，16 & 16 - 1  = 0。但时间貌似更久

#234. Palindrome Linked List   判断列表是否回文
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):           #先把列表全部翻转，再进行比较
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre = None
        li = []
        i = 0
        while head:
            li += [head.val]
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        while pre:
            if li[i] != pre.val:
                return False
            i = i+1
            pre = pre.next
        return True

#234. Palindrome Linked List   判断列表是否回文
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):         #只翻转一半
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next     #对应slow走了一半链表
            cur, cur.next, slow = slow, cur, slow.next   #利用逗号两边不同步，翻转简洁
        slow = slow.next if fast else slow
        while cur and cur.val == slow.val:
            cur = cur.next
            slow = slow.next
        return not cur

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

#237. Delete Node in a Linked List   #删除链表指定位置，不给根节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val        #把下个节点的值赋给当前节点，删除下个节点
        node.next = node.next.next

#242. Valid Anagram   两个字符串的字母是否相同
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)    #sorted函数

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

#258. Add Digits    整数各位相加
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num%10
                num /= 10
            num = temp
        return num

#263. Ugly Number    判断质因子只有2, 3, 5
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        for p in (2,3,5):
            while num %p == 0:
                num /= p
        return num == 1

#278. First Bad Version      二分法找最小
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min, max = 1, n
        while min < max:
            mid = (min+max)//2
            if isBadVersion(mid):
                max = mid
            else:
                min = mid + 1
        return min

#283. Move Zeroes    列表中的0往后挪
class Solution(object):          #两两比较
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[point] = nums[point], nums[i]
                point += 1 

#290. Word Pattern     字符比配，类似205
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return list(map(pattern.find,pattern)) == list(map(str.split(' ').index, str.split(' ')))     #使用map函数

#292. Nim Game   仍石子游戏，脑筋急转弯
class Solution(object):     #只要是4的倍数就输了
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n %4 == 0:
            return False
        else:
            return True

#299. Bulls and Cows     数值、位置匹配
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = sum(map(operator.eq, secret,guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')    #所有的相同元素个数和
        return '%dA%dB' % (bulls, both - bulls)

#303. Range Sum Query - Immutable    列表指定位置的和
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.li = nums
        for i in range(1,len(nums)):
            self.li[i] += self.li[i-1]    #下面的函数会多次调用，所以先储存起来
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.li[j] - (self.li[i-1] if i >0 else 0)
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

#326. Power of Three   判断是否为3的多次方
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19%n == 0    #32位最大19次方

#342. Power of Four     判断是否为4的多次方
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num     #先判断是否为2的多次方，进一步确定1的位置

#344. Reverse String   翻转字符串
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]    #简单

#344. Reverse String   翻转字符串
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if len(s)  < 2:
            return s
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])     #递归方法，时间更长
        
#344. Reverse String   翻转字符串
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = list(s)
        i, j = 0, len(s) -1
        while i < j:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
        return ''.join(li)       #借用列表

#345. Reverse Vowels of a String    翻转字符串中的元音字母
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                li += [i]       #先找出元音字母的位置
        j, k = 0, len(li)-1
        sli = list(s)
        while j < k:
            sli[li[j]], sli[li[k]] = sli[li[k]], sli[li[j]]
            j += 1
            k -= 1
        return ''.join(sli)

#349. Intersection of Two Arrays      两个列表的共有元素
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for num in nums1:
            if num in nums2:
                ret += [num]
        return ret

#350. Intersection of Two Arrays II    两个列表的共有元素，可以重复
class Solution(object):      #时间比较慢
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        dic = {}
        for num in nums1:
            dic[num] = dic.get(num,0) + 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                dic[num] -= 1
                ret += [num]
        return ret

#374. Guess Number Higher or Lower     二分法查找
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min, max = 1, n
        while min < max:
            mid = (min + max)//2
            if guess(mid) == -1:
                max = mid
            elif guess(mid) == 1:
                min = mid+1
            elif guess(mid) == 0:
                return mid
        return min

#383. Ransom Note   判断字符串是否能用另一个构成
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cou1 = Counter(ransomNote)
        cou2 = Counter(magazine)
        return not cou1-cou2

#387. First Unique Character in a String     寻找字符串中第一个不重复字符
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cou = Counter(s)
        for i in range(len(s)):
            if cou[s[i]] == 1:
                return i
        return -1

#389. Find the Difference      找字符串的不同
from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cou1, cou2 = Counter(s), Counter(t)
        return list(cou2-cou1)[0]        #先转化为list

#396. Rotate Function      列表旋转乘积找最大值
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        l = range(len(A))
        length = len(A)
        ret = sum(list(map(lambda x,y:x*y,l,A)))
        vi = ret
        sa = sum(A)
        for i in range(len(A)-1,0,-1):       #规律
            vi = vi+sa-length*A[i]
            ret = max(ret,vi)
        return ret

#400. Nth Digit    数字位拆分后第n个
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        for digit in range(1,11):
            first = 10**(digit-1)
            if n < 9*first*digit:
                return int(str(first + n//digit)[n%digit])
            n -= 9*digit*first   #-9，-99，-999

#401. Binary Watch      二进制手表n个1可能的情况
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' %(m, n) for m in range(12) for n in range(60) if (bin(m).count('1')+bin(n).count('1')) == num]

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

#409. Longest Palindrome       找字符串能构成的最长回文
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(v & 1 for v in Counter(s).values())     #v&1判断是否为奇数，总数为奇数的不能构成回文
        return len(s) - odd + bool(odd)

#412. Fizz Buzz       3,5倍数
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz'*(not m % 3) + 'Buzz'*(not m % 5) or str(m) for m in range(1,n+1)]       # *True/False   or命令

#414. Third Maximum Number       找第三大的数
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        return nums[-3] if len(nums) >= 3 else nums[-1] 

#415. Add Strings    两个字符串相加
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(reduce(lambda x,y: x*10 + ord(y)-48, num1, 0) + reduce(lambda x,y: x*10 + ord(y)-48, num2, 0))    #reduce函数最后一个初始值可省略

#438. Find All Anagrams in a String    找字符串中子字符串所有可能位置
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l = len(p)
        cou = Counter(p)
        cous = Counter(s[:l])
        ret = []
        for i in range(len(s)-l+1):
            if cous == cou:
                ret += [i]
            if i < len(s)-l:
                cous[s[i+l]] = cous.get(s[i+l],0) + 1
                if cous[s[i]] == 1:
                    del cous[s[i]]
                if cous[s[i]] > 1:
                    cous[s[i]] -= 1
        return ret

#441. Arranging Coins    多少行完整阶梯
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        step = 1
        while n >= 0:
            n -= step
            step += 1
            ret += 1
        return ret - 1
            
#447. Number of Boomerangs      距离相等的组合点
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        num = 0
        for p in points:
            dic = {}
            for q in points:
                v = (p[0] - q[0])**2 + (p[1] - q[1])**2
                dic[v] = dic.get(v,0) + 1
            for v in dic:
                num += dic[v] * (dic[v] - 1)
        return num

#453. Minimum Moves to Equal Array Elements      每次n-1个元素加一，使最终相等
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)    #转化为每次一个元素减一
            
#455. Assign Cookies      两个列表组合
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        ret = 0
        init = 0
        for cookies in s:
            if init < len(g) and g[init] <= cookies:
                ret += 1
                init += 1
        return ret

#459. Repeated Substring Pattern    字符串是否能由子字符串重复构成
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        l = len(str)
        for i in range(1,l//2+1):
            if l % i != 0:
                continue
            li = str.split(str[:i])
            if len(set(li)) == 1:
                return True
        return False
