# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        current = result
        carry = 0
        while l1 is not None and l2 is not None:
            tmp = ListNode((l1.val + l2.val + carry) % 10)
            carry = int((l1.val + l2.val + carry)/10)
            current.next = tmp
            current = current.next
            l1 = l1.next
            l2 = l2.next
        l = l1 if l2 is None else l2
        while l is not None:
            tmp = ListNode((l.val + carry) % 10)
            carry = int((l.val + carry)/10)
            current.next = tmp
            current = current.next
            l = l.next
        if carry == 1: current.next = ListNode(1)
        return result.next
