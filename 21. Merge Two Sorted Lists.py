# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2

        if l2 == None:
            return l1

        l3 = ListNode()
        head = l3
        first = True
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                if first:
                    l3.next = None
                    first = False
                else:
                    l3.next = ListNode()
                    l3 = l3.next
                l3.val = l2.val
                l2 = l2.next
            else:
                if first:
                    l3.next = None
                    first = False
                else:
                    l3.next = ListNode()
                    l3 = l3.next
                l3.val = l1.val
                l1 = l1.next

        while l1 != None:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = l1.val
            l1 = l1.next

        while l2 != None:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = l2.val
            l2 = l2.next

        return head
