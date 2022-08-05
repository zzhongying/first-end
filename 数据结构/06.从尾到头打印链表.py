from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        resver=[]
        while head:
            resver.append( head.val )
            head = head.next
        return resver[::-1]


    reversePrint(reversePrint,[1,2,3])