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