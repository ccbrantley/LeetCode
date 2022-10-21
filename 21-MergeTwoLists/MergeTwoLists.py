# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        solutionTail = ListNode()
        tempTail = solutionTail
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tempTail.val = list1.val
                list1 = list1.next
            else:
                tempTail.val = list2.val
                list2 = list2.next
            tempTail.next = ListNode()
            tempTail = tempTail.next
        while list1 != None:
            tempTail.val = list1.val
            if list1.next != None:
                tempTail.next = ListNode()
                tempTail = tempTail.next
            list1 = list1.next
        while list2 != None:
            tempTail.val = list2.val
            if list2.next != None:
                tempTail.next = ListNode()
                tempTail = tempTail.next
            list2 = list2.next
        return solutionTail
