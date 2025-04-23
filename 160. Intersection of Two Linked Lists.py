# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        def getLength(head):
            length = 0
            curr = head
            while curr:
                length += 1
                curr = curr.next
            return length

        len1 = getLength(headA)        
        len2 = getLength(headB)    

        if len2 > len1:
            headA, headB = headB, headA 
            len1, len2 = len2, len1
       
        for i in range(len1 - len2 ):
            headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None             

        
