# Accepted in first term.
# Taken a messy more help from official solution.
# Official Solution: https://leetcode.com/problems/odd-even-linked-list/solutions/127831/odd-even-linked-list/
# Ubuntu Pastebin: https://pastebin.ubuntu.com/p/SMCWKzwZVB/

from listnode import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        eh = head.next
        o = head
        e = eh
        while o is not None and e is not None and e.next is not None:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = eh
        return head
