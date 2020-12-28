# EASY
from copy import copy

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
        

arr = [1,2,3,4,5]
head = LinkedList(Node())
curr = head.head
for i, el in enumerate(arr):
    if curr is not None:
        curr.val = el
    if i < len(arr)-1:
        curr.next = Node()
        curr = curr.next

head.print_list()
print(head.head)
print("reverse")
head.reverse()
head.print_list()
        


