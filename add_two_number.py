
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list = ListNode()
        current =list
        new =0
        while True:
            if(l1==None and l2==None ):
                if new ==1:
                    current.next =ListNode(new)
                    current = current.next
                break

            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            if new ==1:
                sum = l1_value + l2_value +1
                new = 0
            else:
                sum = l1_value + l2_value
            
            if sum>=10:
                new =1
                sum =sum -10
            
            current.next =ListNode(sum)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return list.next