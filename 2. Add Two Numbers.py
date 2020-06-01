# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2

        if l2 == None:
            return l1

        l3 = ListNode(0)
        head = l3
        over10 = 0

        while (l1 != None) & (l2 != None):

            l3.next = ListNode()
            l3 = l3.next
            l3.val = (l1.val + l2.val + over10) % 10
            if (l1.val + l2.val + over10) >= 10:
                over10 = 1
            else:
                over10 = 0

            l1 = l1.next
            l2 = l2.next

        if l1 == None:
            while l2 != None:
                l3.next = ListNode()
                l3 = l3.next
                l3.val = (l2.val + over10) % 10
                if (l2.val + over10) >= 10:
                    over10 = 1
                else:
                    over10 = 0
                l2 = l2.next
        if l2 == None:
            while l1 != None:
                l3.next = ListNode()
                l3 = l3.next
                l3.val = (l1.val + over10) % 10
                if (l1.val + over10) >= 10:
                    over10 = 1
                else:
                    over10 = 0
                l1 = l1.next
        if over10 == 1:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = over10
        return head.next