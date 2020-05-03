# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        result = ListNode(0)
        it = result
        t1 = l1
        t2 = l2
        if t1.val > t2.val:
            it.val = t2.val
            t2 = t2.next
        else:
            it.val = t1.val
            t1 = t1.next
        while t1 is not None and t2 is not None:
            if t1.val > t2.val:
                it.next = ListNode(t2.val)
                it = it.next
                t2 = t2.next
            else:
                it.next = ListNode(t1.val)
                it = it.next
                t1 = t1.next
        l = [t1, t2][t1 is None]
        while l is not None:
            it.next = ListNode(l.val)
            it = it.next
            l = l.next
        return result
