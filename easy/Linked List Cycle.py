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