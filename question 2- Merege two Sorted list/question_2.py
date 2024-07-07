# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point of the merged list
        cur = dummy = ListNode()

        # Iterate as long as both list1 and list2 have nodes
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            if list1.val < list2.val:
                # If list1's value is smaller, append list1's node to the merged list
                cur.next = list1
                # Move to the next node in list1 and update cur to the newly added node
                list1, cur = list1.next, list1
            else:
                # If list2's value is smaller or equal, append list2's node to the merged list
                cur.next = list2
                # Move to the next node in list2 and update cur to the newly added node
                list2, cur = list2.next, list2
            
        # If either list1 or list2 still has nodes left, append the remaining nodes to the merged list
        if list1 or list2:
            cur.next = list1 if list1 else list2

        # Return the merged list, which starts at dummy.next (skipping the dummy node)
        return dummy.next


#https://leetcode.com/problems/merge-two-sorted-lists/


'''

:-: Initialization: dummy and cur are initialized to a new ListNode(). The dummy node acts as a placeholder to simplify 
edge cases (like when the input lists are empty), and cur is used to track the current position in the merged list.



:-: Merging Process:
The while loop continues as long as both list1 and list2 are not None.
Inside the loop, the values of the current nodes of list1 and list2 are compared.
If list1.val is less than list2.val, cur.next is set to list1, and both list1 and cur are moved to their next nodes.
If list2.val is less than or equal to list1.val, cur.next is set to list2, and both list2 and cur are moved to their next nodes.


:-: Appending Remaining Nodes: After the loop, there might still be remaining nodes in either list1 or list2. The if statement checks 
which list is not empty and appends the remaining nodes to the merged list by setting cur.next to the non-empty list.


:-: Returning the Result: The merged list starts from dummy.next, skipping the dummy node itself, and this is returned as the result.
'''
