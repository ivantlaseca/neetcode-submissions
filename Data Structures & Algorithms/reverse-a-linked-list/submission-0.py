# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
null <- 0 <- 1 -> 2 -> null
                  p1   n
             p

null <- 0

prev = null

while head
    nxt = p1.next
    p1.next = prev
    prev = p1
    p1 = nxt


null <- 0 <- 1 <- 2 <- null



"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
        