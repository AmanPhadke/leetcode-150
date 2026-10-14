# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        current = head
        seen = set()

        while current is not None:
            if current in seen:
                return current
            seen.add(current)
            current = current.next

    

            
        