from typing import List

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            node = Node(cur.val)
            print(node)



    copyRandomList(copyRandomList,[[7,5],[13,0],[11,4],[10,2],[1,0]])