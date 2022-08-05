from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #-----------------方法一：正常链表---------------------------
    def reverseList1(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


    # -----------------方法二：递归---------------------------

    def reverseList2(self, head:ListNode) -> ListNode:
        def recur(cur,pre):
            cur = head
            while pre:            #重构链表
                pre = cur
                cur = cur.next
                cur.next = pre
                recur(cur,pre)
            return pre

        def test(cur):
            cur = head
            while cur:         #输出重构后的链表结构
                test(cur.next)
                print(cur)
                return cur

    reverseList2(reverseList2, [5, 4, 3, 2, 1])










