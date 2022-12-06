# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curNode = head
        if curNode == None:
            return None
        elif curNode.next == None:
            if curNode.val == val:
                return None
            else:
                return curNode
        curHead = head
        while curHead.val == val:
            if curHead.next != None:
                curHead = curHead.next
            else:
                return None
        curNode = curHead
        while curNode.next != None:
            if (curNode.next.val == val):
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return curHead
