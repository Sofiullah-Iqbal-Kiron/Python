# Accepted in first term.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self, head):
        n = 0
        while head is not None:
            n += 1
            head = head.next
        return n

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = self.length(head) // 2
        for i in range(0, n, 1):
            head = head.next
        return head
