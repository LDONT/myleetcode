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