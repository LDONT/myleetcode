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
