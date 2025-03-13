from typing import Optional

class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        ans = ListNode()
        current = ans
        
        while list1 and list2:
            if list1.val  <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2 
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return ans.next
