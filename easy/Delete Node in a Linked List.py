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
