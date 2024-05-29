
# Definition for singly-linked list. - given
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp = ListNode()
        l = temp

        while list1 and list2:
            if list1.val <= list2.val:
                l.next = list1
                list1 = list1.next
            else:
                l.next = list2
                list2 = list2.next
            l = l.next

        if list1:
            l.next = list1
        elif list2:
            l.next = list2

        return temp.next