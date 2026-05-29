# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(node):
            curr = node
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        if not head or not head.next:
            return

        # find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split
        second = slow.next
        slow.next = None

        # reverse second half
        rev = reverseList(second)

        # merge
        first = head

        while rev:
            tmp1 = first.next
            tmp2 = rev.next

            first.next = rev
            rev.next = tmp1

            first = tmp1
            rev = tmp2


        
