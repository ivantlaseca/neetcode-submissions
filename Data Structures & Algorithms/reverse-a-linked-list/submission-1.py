"""
1 -> 2 -> null

while curr not null

tmp: 2
curr.next: null
prev: 1
curr: 2

<- 1 <- 2

tmp = curr.next
curr.next = prev
prev = curr
curr = tmp

null <- 1 <- 2 

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
