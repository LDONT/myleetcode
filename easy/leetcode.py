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
            if l1 != None or l2 != None or sum != 0:  #����
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
    	charclass=[0]*length               #��ʼ������
    	for i in range(length):
    		charclass[i] = i%(2*numRows-2)
    		if charclass[i] > numRows-1:
    			charclass[i]=2*numRows-2-charclass[i] 
    	for i in range(length):
    		wordlist[charclass[i]]+=(s[i])
    	return "".join(wordlist)
#6. ZigZag Conversion*  �������ʱ��Ҳ��
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
        
#7. Reverse Integer  ������ת
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            r=int(str(x)[::-1])   #���򲽽���Ƭ��ÿ��-1
        if x <= 0:
            x=abs(x)
            r=-int(str(x)[::-1])
        if r>2147483647 or r<-2147483647:   #�������2^31-1
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
        
#9. Palindrome Number   �ж��Ƿ����
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
            
#13. Roman to Integer �Լ�д��
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
#13. Roman to Integer *�ƺ��������       
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
        
#14. Longest Common Prefix  �������ַ����е�����е����ַ�������  
class Solution(object):
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''          #����һ��return�󣬺���ʣ�µĶ�������
        com = strs[0]
        for i in range(len(com)):
            for j in strs:
                if i >= len(j) or j[i]!=com[i]:
                    return com[0:i]
        return com

#19. Remove Nth Node From End of List *   ɾ��һ�������β����n���ڵ�
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
        k1=head                             #����ָ��
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
        
#20. Valid Parentheses * �ж�����������Ƿ���Ч
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
                stack.append(char)                 #ʹ��ջ
            if char in table.keys():
                if stack==[] or stack.pop() != table[char]:
                    return False
        return stack==[]
                
#21. Merge Two Sorted Lists* ����������������ϵ�һ����������
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):                      #����˼��
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
       
#21. Merge Two Sorted Lists* ����������������ϵ�һ����������
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):                      #�ݹ�˼��
	def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2 

#23. Merge k Sorted Lists *�����������ϲ�
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):           #�����򣬲��Ǻܶ�
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
        
#24. Swap Nodes in Pairs *�������ڵ�
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
        pre,pre.next = self,head          #self����dummy
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            a.next = pre.next.next.next
            b.next = a
            pre.next = b
            pre = a
        return self.next
        
#26. Remove Duplicates from Sorted Array*  ������list�в�ͬ�����ĸ���n����ǰn��Ԫ��Ϊ��n����ͬ������������������������Դ
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
                nums[i] = nums[j]      #���Լ��޸�
        return i+1   

#27. Remove Element ���������ƣ��Ƴ��б��е�ָ������
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
                
#28. Implement strStr()     ���ַ��������ַ�����λ��
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:                #�Լ�д�ĸ��ü�
            return haystack.index(needle)
        else:
            return -1
            
#28. Implement strStr() *    ���ַ��������ַ�����λ��
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
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)           #���Ǻܶ�
        return s

#38. Count and Say  *
class Solution(object):     #������⣬ʱ�����
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
         
#58. Length of Last Word*  ���һ�����ʵĳ���
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])  #stripȥ����β�ո�split����ַ���
        
#66. Plus One*  �������ּ�һ
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x,y:x*10+y,digits)+1   #lambda reduceȫ�ֺ���
        return [int(i) for i in str(num)]
        
#66. Plus One*  �������ּ�һ
class Solution(object):      #��lambda����
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
            num += digits[i]*pow(10,len(digits)-i-1)
        return [int(j) for j in str(num+1)]
        
#67. Add Binary *   �����������  
class Solution(object):
    def addBinary(self, a, b):         #�ݹ��˼��self.
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
            
#70. Climbing Stairs  ���������⣬ÿ��һ����������
class Solution(object):
    def climbStairs(self, n):        #�����ӵĽ�����������ÿ�δ��浱ǰ����һ��
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

#70. Climbing Stairs  ���������⣬ÿ��һ����������
class Solution(object):                 #�ݹ鷽����ʱ�临�Ӷ�̫��
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

#83. Remove Duplicates from Sorted List   ������ɾ����ͬ��Ԫ��
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

#88. Merge Sorted Array *  ������������ϲ�
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m and n:             #�Ӻ���ǰ��ֵ��ʡȥ����
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n:
            nums1[:n] = nums2[:n]

#100. Same Tree*   �ж��Ƿ�Ϊ��ͬ����
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):     #���õݹ�ķ���
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

#101. Symmetric Tree  *     �ж��������Ƿ�Գ�
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):         #ʹ�õݹ�ķ���
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
        if left.val == right.val:                      #ÿ���ж������������ĸ���
            outpair = self.isSame(left.left,right.right)
            inpair = self.isSame(left.right,right.left)
            if outpair and inpair:
                return True
            else:
                return False
        else:
            return False

#101. Symmetric Tree  *     �ж��������Ƿ�Գ�
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
        stack = [(root.left,root.right)]      #ʹ��ջ����������ò����ʱ����
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
        
#102. Binary Tree Level Order Traversal   ����������������������
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):                 #�����������bfs
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
                    nextlevel.append(node.left)           #ֱ�Ӱѽڵ���뵽list��
                if node.right:
                    nextlevel.append(node.right)
                temp.append(node.val)
            ret.append(temp)
            level = nextlevel
        return ret

#104. Maximum Depth of Binary Tree  *������������
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        #�����õݹ�ķ���
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

#107. Binary Tree Level Order Traversal II      #�Ե����ϵõ�����Ԫ�����list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                   #���������ȵõ��Զ����µ�����[::-1]��ת
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

#107. Binary Tree Level Order Traversal II      #�Ե����ϵõ�����Ԫ�����list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                    # �������+�ݹ�	
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
                  
#107. Binary Tree Level Order Traversal II      #�Ե����ϵõ�����Ԫ�����list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                    # �������+ջ
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
    
#107. Binary Tree Level Order Traversal II      #�Ե����ϵõ�����Ԫ�����list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):                    # �������+����
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
    
#110. Balanced Binary Tree    �ж�һ�����Ƿ���ƽ�������
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
    def check(self,root):      #���庯������ÿ���ڵ�����
        if root is None:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if left == -1 or right == -1 or abs(left-right)>1:
            return -1
        else:
            return 1+max(left,right)
    
#111. Minimum Depth of Binary Tree       ����������С���  
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
        while stack:               #������ȣ�ջ
            level,node = stack.pop()
            if node.right is None and node.left is None:
                return level
            if node.right is not None:
                stack.insert(0,(level+1,node.right))
            if node.left is not None:
                stack.insert(0,(level+1,node.left))    

#111. Minimum Depth of Binary Tree       ����������С���      
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):              #�����ķ���
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
    
#112. Path Sum     * ������ڵ㵽Ҷ�ڵ�ĺ��Ƿ����һ����    
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
        sum -= root.val          #sum��ȥ�����õݹ�
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)    
    
#118. Pascal's Triangle   �������    
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
    
#118. Pascal's Triangle   �������  
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1]]
        for i in range(1,numRows):   #����������ǵ����ʣ�0121+1210
            ret += [map(lambda x,y:x+y, ret[-1]+[0],[0]+ret[-1])]
        return ret[:numRows]    

#119. Pascal's Triangle II  ������Ƿ���ĳ��index����
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

#121. Best Time to Buy and Sell Stock  �б���ǰ���ֵ
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
        for price in prices:             #��̬�滮
            min_price = min(min_price,price)
            if price != min_price:
                max_profit = max(max_profit,price - min_price)
        return max_profit

#122. Best Time to Buy and Sell Stock II   �ɶ��������Ʊ
class Solution(object):            #̰���㷨�����̫���ӣ��Ա�ǰ������
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

#122. Best Time to Buy and Sell Stock II   �ɶ��������Ʊ
class Solution(object):   #ֱ�ӵ���һ���ǰһ����ǰһ�����һ����
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices)-1))
        
#125. Valid Palindrome  �жϻ���
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0,len(s)-1    #���˼б�
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

#136. Single Number  ���б���ֻ����һ�ε���
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            ret ^= num    #�������������ת��Ϊ������
        return ret
        
#136. Single Number  ���б���ֻ����һ�ε���
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y:x^y,nums)

#136. Single Number  ���б���ֻ����һ�ε���
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)   #����set����

#141. Linked List Cycle   �ж������Ƿ�ѭ��
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):   #�����쳣�����ܵ�����β��û��ѭ��
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while fast is not slow:    #����ָ��Ĳ��1,2,3...
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False

#141. Linked List Cycle   �ж������Ƿ�ѭ��
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):          #��ʹ���쳣
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

#155. Min Stack  ����һ��ջ
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []       
    def push(self, x):    #��push�����оʹ洢����С����
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

#160. Intersection of Two Linked Lists    #����������Ľ����
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
        while curA is not curB:        #��·���������ε������Ϲ���
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        gc.collect()
        return curA

#165. Compare Version Numbers  �Ƚ������汾���ֵĴ�С
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

#168. Excel Sheet Column Title    26����ת��
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if n == 0 else self.convertToTitle((n-1)/26) + chr((n-1)%26 + ord('A'))   #���õݹ�

#169. Majority Element   �ҳ���������
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}       
        t = len(nums)//2
        for num in nums:
            dic[num] = dic.get(num,0) + 1          #ʹ���ֵ䣬��һ�γ��ָ�ֵΪ0
            if dic[num] > t:
                return num

#171. Excel Sheet Column Number    26����ת10����
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

#171. Excel Sheet Column Number    26����ת10����
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y:26*x+y,map(lambda x:ord(x)-ord('A')+1,s))    #ʹ��reduce����

#172. Factorial Trailing Zeroes    �ж�n�׳�ĩβ0�ĸ���
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n ==0 else n//5 + self.trailingZeroes(n//5)    #��5�ĸ������ݹ�

#172. Factorial Trailing Zeroes    �ж�n�׳�ĩβ0�ĸ���
class Solution(object):
    def trailingZeroes(self, n):        
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n>0:
            n /=5    #��5��������5*5����������
            ret += n
        return ret

#189. Rotate Array   �б�����λ��ת
class Solution(object):   #������ת
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

#189. Rotate Array     �б�����λ��ת
class Solution(object):   #���Ƽ򵥴ֱ�
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

#190. Reverse Bits    �����Ʒ�ת
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = bin(n)[2:]    #ת��Ϊ2����
        return int(num.zfill(32)[::-1],2)   

#191. Number of 1 Bits   �Ҷ�������1�ĸ���
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2:]
        return num.count('1') 

#198. House Robber    �б��и�һ����
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(now, last + num)  #�Ƚ���һ�����ź͵�ǰֵ�����ϸ����ŵĴ�С
        return now     

#202. Happy Number    ��������
class Solution(object):    #�ٶ��е���
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

#202. Happy Number    ��������
class Solution(object):
    def isHappy(self, n):    #����ѭ��
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

#203. Remove Linked List Elements   �Ƴ������е�ָ����ֵ
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

#204. Count Primes    ��С��n����������
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
        for i in range(2,int((n-1)**0.5)+1):   #����ֻ������2�����ţ�n-1����ȡֵ
            if primes[i]:
                primes[i*i:n:i] = [False]*len(primes[i*i:n:i])   #i*i,i*(i+1)...������
        return sum(primes)

#205. Isomorphic Strings   �����ַ���һһ��Ӧ
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.find,s)) == list(map(t.find,t))
        
#205. Isomorphic Strings   �����ַ���һһ��Ӧ
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) and len(set(zip(t,s))) == len(set(t))   #zip����
        
#206. Reverse Linked List   ��תһ������
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):         #����������ʹ������ָ��
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

#206. Reverse Linked List   ��תһ������
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):         #�ݹ鷽��
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
        
#217. Contains Duplicate      �ж��б����Ƿ������ͬԪ��
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

#217. Contains Duplicate      �ж��б����Ƿ������ͬԪ��
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) 

#219. Contains Duplicate II   �ж��б����ظ����ֵ���������k
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):     #enumerate�������������б�
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False

#223. Rectangle Area   ���������ε����
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

#223. Rectangle Area   ���������ε����
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
        overlap = max(min(C,G)-max(A,E),0)*max(min(D,H)-max(B,F),0)   #�ȼ����ص�����
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap

#226. Invert Binary Tree   ��תһ��������
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

#231. Power of Two   �ж�һ�����Ƿ�Ϊ2�Ķ�η�
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n!= 1:    #ֱ���жϳ�2������
            m = n%2
            if m!= 0:
                return False
            n /= 2
        return True

#231. Power of Two   �ж�һ�����Ƿ�Ϊ2�Ķ�η�
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n&(n-1)   #��λ�룬16 = b10000��16 - 1 = b01111��16 & 16 - 1  = 0����ʱ��ò�Ƹ���

#234. Palindrome Linked List   �ж��б��Ƿ����
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):           #�Ȱ��б�ȫ����ת���ٽ��бȽ�
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

#234. Palindrome Linked List   �ж��б��Ƿ����
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):         #ֻ��תһ��
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next     #��Ӧslow����һ������
            cur, cur.next, slow = slow, cur, slow.next   #���ö������߲�ͬ������ת���
        slow = slow.next if fast else slow
        while cur and cur.val == slow.val:
            cur = cur.next
            slow = slow.next
        return not cur

#235. Lowest Common Ancestor of a Binary Search Tree     ��������������͹����ڵ�
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):    #��������
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while (root.val-p.val)*(root.val-q.val)>0:     #���������������ʣ�����С����
            root = (root.left,root.right)[p.val > root.val]    #��������ʱȡroot.right������root.left
        return root

#235. Lowest Common Ancestor of a Binary Search Tree     ��������������͹����ڵ�
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):      #�ݹ鷽��
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

#237. Delete Node in a Linked List   #ɾ������ָ��λ�ã��������ڵ�
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
        node.val = node.next.val        #���¸��ڵ��ֵ������ǰ�ڵ㣬ɾ���¸��ڵ�
        node.next = node.next.next

#242. Valid Anagram   �����ַ�������ĸ�Ƿ���ͬ
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)    #sorted����

#257. Binary Tree Paths    ���ض�����������·��
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:             #ʹ�õݹ鷽��
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

#258. Add Digits    ������λ���
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

#263. Ugly Number    �ж�������ֻ��2, 3, 5
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

#278. First Bad Version      ���ַ�����С
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

#283. Move Zeroes    �б��е�0����Ų
class Solution(object):          #�����Ƚ�
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

#290. Word Pattern     �ַ����䣬����205
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return list(map(pattern.find,pattern)) == list(map(str.split(' ').index, str.split(' ')))     #ʹ��map����

#292. Nim Game   ��ʯ����Ϸ���Խת��
class Solution(object):     #ֻҪ��4�ı���������
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n %4 == 0:
            return False
        else:
            return True

#299. Bulls and Cows     ��ֵ��λ��ƥ��
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = sum(map(operator.eq, secret,guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')    #���е���ͬԪ�ظ�����
        return '%dA%dB' % (bulls, both - bulls)

#303. Range Sum Query - Immutable    �б�ָ��λ�õĺ�
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.li = nums
        for i in range(1,len(nums)):
            self.li[i] += self.li[i-1]    #����ĺ������ε��ã������ȴ�������
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

#326. Power of Three   �ж��Ƿ�Ϊ3�Ķ�η�
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19%n == 0    #32λ���19�η�

#342. Power of Four     �ж��Ƿ�Ϊ4�Ķ�η�
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num     #���ж��Ƿ�Ϊ2�Ķ�η�����һ��ȷ��1��λ��

#344. Reverse String   ��ת�ַ���
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]    #��

#344. Reverse String   ��ת�ַ���
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if len(s)  < 2:
            return s
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])     #�ݹ鷽����ʱ�����
        
#344. Reverse String   ��ת�ַ���
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
        return ''.join(li)       #�����б�

#345. Reverse Vowels of a String    ��ת�ַ����е�Ԫ����ĸ
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                li += [i]       #���ҳ�Ԫ����ĸ��λ��
        j, k = 0, len(li)-1
        sli = list(s)
        while j < k:
            sli[li[j]], sli[li[k]] = sli[li[k]], sli[li[j]]
            j += 1
            k -= 1
        return ''.join(sli)

#349. Intersection of Two Arrays      �����б�Ĺ���Ԫ��
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

#350. Intersection of Two Arrays II    �����б�Ĺ���Ԫ�أ������ظ�
class Solution(object):      #ʱ��Ƚ���
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

#374. Guess Number Higher or Lower     ���ַ�����
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

#383. Ransom Note   �ж��ַ����Ƿ�������һ������
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

#387. First Unique Character in a String     Ѱ���ַ����е�һ�����ظ��ַ�
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

#389. Find the Difference      ���ַ����Ĳ�ͬ
from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cou1, cou2 = Counter(s), Counter(t)
        return list(cou2-cou1)[0]        #��ת��Ϊlist

#396. Rotate Function      �б���ת�˻������ֵ
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
        for i in range(len(A)-1,0,-1):       #����
            vi = vi+sa-length*A[i]
            ret = max(ret,vi)
        return ret

#400. Nth Digit    ����λ��ֺ��n��
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
            n -= 9*digit*first   #-9��-99��-999

#401. Binary Watch      �������ֱ�n��1���ܵ����
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' %(m, n) for m in range(12) for n in range(60) if (bin(m).count('1')+bin(n).count('1')) == num]

#404. Sum of Left Leaves     �������������Ҷ�ڵ����
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

#409. Longest Palindrome       ���ַ����ܹ��ɵ������
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(v & 1 for v in Counter(s).values())     #v&1�ж��Ƿ�Ϊ����������Ϊ�����Ĳ��ܹ��ɻ���
        return len(s) - odd + bool(odd)

#412. Fizz Buzz       3,5����
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz'*(not m % 3) + 'Buzz'*(not m % 5) or str(m) for m in range(1,n+1)]       # *True/False   or����

#414. Third Maximum Number       �ҵ��������
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        return nums[-3] if len(nums) >= 3 else nums[-1] 

#415. Add Strings    �����ַ������
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(reduce(lambda x,y: x*10 + ord(y)-48, num1, 0) + reduce(lambda x,y: x*10 + ord(y)-48, num2, 0))    #reduce�������һ����ʼֵ��ʡ��

#438. Find All Anagrams in a String    ���ַ��������ַ������п���λ��
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

#441. Arranging Coins    ��������������
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
            
#447. Number of Boomerangs      ������ȵ���ϵ�
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

#453. Minimum Moves to Equal Array Elements      ÿ��n-1��Ԫ�ؼ�һ��ʹ�������
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)    #ת��Ϊÿ��һ��Ԫ�ؼ�һ
            
#455. Assign Cookies      �����б����
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

#459. Repeated Substring Pattern    �ַ����Ƿ��������ַ����ظ�����
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
