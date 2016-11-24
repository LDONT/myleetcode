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
