# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge(self, A, B, lists, idx):
        if not A:
            lists[idx] = B
            return
        if not B:
            return
        
        prevA = None
        while A and B:
            if A.val <= B.val:
                prevA = A
                A = A.next
            else:
                BNext = B.next
                B.next = A
                if prevA:
                    prevA.next = B
                else:
                    lists[idx] = B
                prevA = B
                B = BNext

        if not A:
            prevA.next = B
        


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None
        if n == 1:
            return lists[0]
        
        step = 1
        while step < n:
            for i in range(0, n, 2*step):
                if i + step < n:
                    self.merge(lists[i], lists[i+step], lists, i)
                else:
                    break
            step *= 2
        
        return lists[0]



        