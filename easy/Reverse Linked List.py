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
