# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        freq={}
        current=head
        while current is not None :
            if current.val in freq:
                freq[current.val]+=1

            else:
                freq[current.val]=1 
            current=current.next           


        arr=[]
        for value in freq:
            if freq[value] == 1:
                arr.append(value)

        dummy=ListNode(0)
        current=dummy

        for value in arr:
            current.next=ListNode(value) 
            current=current.next
        return dummy.next       