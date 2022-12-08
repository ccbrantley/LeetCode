# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None):
            return None
        sb = str(head.val)
        curHead = head.next
        while curHead != None:
            sb += str(curHead.val)
            curHead = curHead.next
        while len(sb) > 1:
            if sb[0] != sb[-1]:
                return False
            sb = sb[1:-1:]
        return True
