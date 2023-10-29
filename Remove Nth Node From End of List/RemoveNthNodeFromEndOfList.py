# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        listSize = 0
        while cur:
            cur = cur.next
            listSize += 1
        i = 1
        cur = head
        toBeRemoved = listSize - n
        if toBeRemoved == 0:
            head = head.next
        while i < toBeRemoved:
            cur = cur.next
            i += 1
        print(listSize, toBeRemoved, cur.val, i)
        if cur.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        return head
        

solution = Solution()
head, n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n = 2
solution.removeNthFromEnd(head, n)