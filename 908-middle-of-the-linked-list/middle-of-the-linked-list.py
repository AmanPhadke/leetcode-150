# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        curr = head
        temp = []

        while curr:
            temp.append(curr.val)
            curr = curr.next

        mid = len(temp) // 2
        curr = head

        for _ in range(mid):
            print(curr.val)
            curr = curr.next

        return curr


        