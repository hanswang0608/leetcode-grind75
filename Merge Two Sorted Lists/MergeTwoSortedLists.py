from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newListCur = newHead = ListNode()
        list1Cur = list1
        list2Cur = list2

        while list1Cur and list2Cur:
            if list1Cur.val < list2Cur.val:
                newListCur.next = list1Cur
                list1Cur = list1Cur.next
            else:
                newListCur.next = list2Cur
                list2Cur = list2Cur.next
            newListCur = newListCur.next
        
        if list1Cur:
            newListCur.next = list1Cur
        elif list2Cur:
            newListCur.next = list2Cur
        
        return newHead.next