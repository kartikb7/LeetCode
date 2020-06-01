# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        reversed_list = None
        while head is not None:
            new_node = ListNode()
            new_node.val = head.val
            new_node.next = reversed_list
            reversed_list = new_node
            head = head.next
        return reversed_list
