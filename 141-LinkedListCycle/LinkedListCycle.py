# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return False
        degree = 2
        degreeNode = head
        while degreeNode.next != None:
            curNode = degreeNode.next
            steps = degree
            while steps != 0:
                curNode = curNode.next
                if curNode == None:
                    return False
                if curNode == degreeNode:
                    return True
                steps -= 1
            degree **= 2
            degreeNode = curNode
        return False
