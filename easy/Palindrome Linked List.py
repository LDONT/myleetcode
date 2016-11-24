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
