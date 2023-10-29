# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        current = head
        next = head.next
        current.next = None
        while next != None:
            temp = next.next
            next.next = current
            current = next
            next = temp
        return current