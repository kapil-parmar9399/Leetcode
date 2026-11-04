# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        current =head
        small=[]
        greater=[]
        while current is not None :
            if current.val < x :
                small.append(current.val)

                

            else:
                greater.append(current.val) 

            current =current.next

        arr=small+greater
        

        dummy = ListNode(0)
        current = dummy

        for value in arr:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

