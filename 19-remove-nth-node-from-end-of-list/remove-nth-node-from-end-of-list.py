# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        def get_length_recursive(head):
            if not head:
                return 0
                
            return 1 + get_length_recursive(head.next)

        length = get_length_recursive(head)
        
        position = length - n

        dummy = ListNode(-1)
        dummy.next = head

        current = dummy
        count = 0

        while count < position:
                current = current.next
                count += 1    

        current.next = current.next.next

        return dummy.next


            
            
        