# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        current = head
        
        while temp != None:
            if(temp.val == current.val):
                temp = temp.next
                continue
            current.next = temp
            temp = temp.next
            current = current.next
        
        if current != None:
            current.next = None
            
        return head
