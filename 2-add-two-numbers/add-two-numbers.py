# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst_node = ListNode()
        carry = 0
        cur_node = lst_node
      
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total_sum = digit1 + digit2 + carry
            carry, digit_value = divmod(total_sum, 10)
            cur_node.next = ListNode(digit_value)
            cur_node = cur_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return lst_node.next
        