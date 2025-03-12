from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        ans = ListNode()
        current = ans
        count = 0

        while head and head.next:
            if head.val == head.next.val:
                count += 1
            else:
                if count == 0:
                    current.next = head
                    current = current.next
                count = 0 
            head = head.next

        if count == 0:
            current.next = head
        else:
            current.next = None

        return ans.next