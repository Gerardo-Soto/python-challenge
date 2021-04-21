"""
Dificult: Easy

Merge two sorted lists.

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

"""

"""
Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Don't use len() 
"""

class Solution(object):
    def mergeTwoList(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        
        ptr1 = ListNode(l1)
        l1_head = ptr1

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                ptr1.next = l1
                l1 = l1.next

            else:
                ptr1.next = l2
                l2 = l2.next
        
        # case base
        if l1 is not None:
            ptr1.next = l1
        if l2 is not None:
            ptr1.next = l2

        return l1_head.next
        """
        if not l1 and not l2:
            return ListNode(0).next

        if not l1:
            return l2

        if not l2:
            return l1


        result = list()
        while l1 and l2:
            if l1.val <= l2.val:
                result.append(l1)
                l1 = l1.next_val

            else:
                result.append(l2)
                l2 = l2.next_val


        while l1:
            result.append(l1)
            l1 = l1.next_val


        while l2:
            result.append(l2)
            l2 = l2.next_val

        for i in range(len(result)-1):
            result[i].next_val = result[i+1]

        result[-1].next = None

        print(result)
        print(result[1].next_val.val)

        return result[0]
        """


class ListNode(object):
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

    def next_list(self, next):
        self.next = next

    def __str__(self):
        return str(self.val)


if __name__ == '__main__':

    list_shorted_1 = ListNode(1)
    list_shorted_1.next = ListNode(1,2)
    list_shorted_1.next = ListNode(2,3)

    list_shorted_2 = ListNode(1)
    list_shorted_2.next = ListNode(1,2)
    list_shorted_2.next = ListNode(2,4)
    merge = Solution()
    print('Solution:::')
    print(merge.mergeTwoList(list_shorted_1, list_shorted_2))


