#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : is_palindrome.py
@Datetime   : 2021/10/8
@Site       :
@Software   : PyCharm

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast_node = head
        slow_node = head
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        slow = self.reserve(slow_node)  # 后半部分反转链表
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True

    def reserve(self, head: ListNode):
        """
            链表反转
        :param head:
        :return:
        """
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre


def testIsPalindrome():
    head = ListNode(val=1)
    next = ListNode(val=2)
    head.next = next
    assert False == Solution().isPalindrome(head)
