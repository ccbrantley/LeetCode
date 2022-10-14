# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curNode = head
        while curNode != None and curNode.next != None:
            while curNode.val == curNode.next.val:
                if curNode.next.next != None:
                    curNode.next = curNode.next.next
                else:
                    curNode.next = None
                    break
            curNode = curNode.next
        return head
