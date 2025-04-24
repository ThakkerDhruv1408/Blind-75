'''
Reverse Linked List   	            Blind75 19, LeetCode 206
Merge Two Sorted Lists   	        Blind75 20, LeetCode 21
Linked List Cycle   	            Blind75 21, LeetCode 141
Reorder List   	                    Blind75 22, LeetCode 143
Remove Nth Node From End of List   	Blind75 23, LeetCode 19
Merge K Sorted Lists                Blind75 24, LeetCode 23
middle of list node                 _         , LeetCode 876
'''

# Node class represents each element in the Linked List
class Node:
    def __init__(self, data=0, next=None):
        self.data = data  # Data to store (could be any data type)
        self.next = next  # Pointer to the next node


# LinkedList class encapsulates all linked list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty


    # Add a node at the end of the linked list
    def add_at_end(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return
        
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = newNode


    # Add a node at the beginning of the linked list
    def add_at_beginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    # Insert a node at a specific position
    def add_at_position(self, position, data):

        if position == 0:
            self.add_at_beginning(data)
            return
        
        newNode = Node(data)
        curr = self.head

        for _ in range(position - 1):

            if curr is None:

                raise IndexError("Position out of range")
            
            curr = curr.next

        newNode.next = curr.next
        curr.next = newNode


    # Delete a node by its value
    def delete_by_value(self, value):
        if not self.head:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        curr = self.head
        while curr.next and curr.next.data != value:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

        else:
            raise KeyError("Value not present in linked list")


    # Delete a node by its position (0-based index)
    def delete_by_position(self, position):
        if not self.head:
            return
        
        if position == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        for _ in range(position - 1):

            if curr.next is None:

                raise ValueError("Position out of range")
            
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next


    # Search for a value in the linked list
    def search(self, value):
        curr = self.head
        position = 0
        while curr:
            if curr.data == value:
                return position
            curr = curr.next
            position += 1
        return -1


    # Print the entire linked list
    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next

        print("None")


    # Blind75 - 19  LeetCode 206
    # Reverse the linked list in-place             # Time: O(n), Space: O(1)
    def reverse(self):                     
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev


    # Blind75 - 20  Leetcode 21 - Merge Two Sorted Lists
    # Merge two sorted linked lists
    @staticmethod
    def merge_sorted_list(l1, l2):                      # Time: O(n + m), Space: O(1)
        dummy = Node(0)
        tail = dummy

        while l1 and l2:

            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 or l2
        merged_list = LinkedList()
        merged_list.head = dummy.next

        return merged_list


    # Blind75 - 21 Leetcode 141 - Linked List Cycle
    # Detect if the linked list contains a cycle        # Time: O(n), Space: O(1)
    def has_cycle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    

    # Blind75 - 22  Leetcode 143 - Reorder List
    # Reorder a linked list (L0→Ln→L1→Ln-1→L2→Ln-2→…)       # Time: O(n), Space: O(1)
    def reorderList(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        curr = second
        while curr:

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second = prev

        # Merge two halves
        first = head
        while second:
            tempF, tempS = first.next, second.next
            first.next = second
            second.next = tempF
            first, second = tempF, tempS


    # Blind75 - 23  Leetcode 19 - Remove Nth Node From End of List
    # Remove Nth node from the end of list              # Time: O(n), Space: O(1)
    def removeNthFromEnd(self, head, n):
        dummy = Node(0)
        dummy.next = head
        left, right = dummy, head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


    # Blind75 - 24  Leetcode 23 - Merge k Sorted Lists
    # Merge K sorted linked lists                       # Time: O(N log k), Space: O(1)
    def mergeKSortedLists(self, lists):

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergeList = []

            for i in range(0, len(lists), 2):

                l1 = lists[i].head
                l2 = lists[i + 1].head if (i + 1) < len(lists) else None
                mergeList.append(self.merge_sorted_list(l1, l2))

            lists = mergeList

        return lists[0]


    # Leetcode 876 - Middle of the Linked List
    # Find and return the middle node's value       # Time: O(n), Space: O(1)
    def find_middle(self):
        slow = fast = self.head
        position = 0

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            position += 2

        size = position + 1

        print(f"middle Index is = {(size)//2}")
        print(f"middle element is {slow.data}")

        return slow.data if slow else None


# To test functionality, uncomment test cases below in the main block
if __name__ == "__main__":

# General Testing

    # ll = LinkedList()
    # ll.add_at_end(30)
    # ll.add_at_end(40)
    # ll.add_at_beginning(20)
    # ll.add_at_end(50)
    # ll.add_at_end(60)
    # ll.add_at_beginning(10)
    # ll.add_at_position(2,80)
    # ll.print_list()
    # ll.delete_by_position(6)
    # ll.print_list()
    # x = ll.search(40)
    # print(x)
    # ll.reverse()
    # ll.print_list()
    # ll.find_middle()


# Merge Two Sorted Linked List
    
    # l1 = LinkedList()
    # l2 = LinkedList()

    # for val in [1,3,5]:
    #     l1.add_at_end(val)

    # for val in [2,4,6,7]:
    #     l2.add_at_end(val)

    # l1.print_list()
    # l2.print_list()

    # merged_list = LinkedList.merge_sorted_list(l1.head, l2.head)
    # merged_list.print_list()


# Reorder Linked List

    # ll = LinkedList()
    # for val in [1,2,3,4,5,6,7]:
    #     ll.add_at_end(val)
    
    # ll.print_list()
    # ll.reorderList(ll.head)
    # ll.print_list()


# Remove Nth Element from End of the Linked List 

    # ll = LinkedList()
    # for val in [1,2,3,4,5,6,7]:
    #     ll.add_at_end(val)
    
    # ll.print_list()
    # ll.head = ll.removeNthFromEnd(ll.head, 7)
    # ll.print_list()


# Merge K sorted Linked Lists 

    # l1 = LinkedList()
    # for num in [6,7,8,9,10]:
    #     l1.add_at_end(num)

    # l2 = LinkedList()
    # for num in [1,3,5,13,77]:
    #     l2.add_at_end(num)

    # l3 = LinkedList()
    # for num in [1,3,5,7,9,11]:
    #     l3.add_at_end(num)
    
    # lists = [l1,l2,l3]
    # sol = LinkedList()
    # res = sol.mergeKSortedLists(lists)
    # res.print_list()

    pass
