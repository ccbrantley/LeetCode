# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, _head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if _head == None:
            return None
        tempList = []
        curNode = _head
        while curNode != None:
            tempList.append(curNode)
            curNode = curNode.next
        returnHead = tempList.pop(-1)
        curHead = returnHead
        for head in tempList[::-1]:
            curHead.next = head
            curHead = head
        curHead.next = None
        return returnHead
