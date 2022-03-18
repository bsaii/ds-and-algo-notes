## How to create a linked list
1. Create a Node class with the data and next.
2. Creat a Linked List class with the head and other methods.


```
# create a node
class Node():
    def __init__(self, a_number) -> int:
        self.data = a_number
        self.next = None
        
# Linked List
class LinkedList():
    def __init__(self):
        self.head = None
    
    # add a node at the end
    def append(self, value):
        if self.head is None:
            self.head = Node(value)

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

```

An example:

```
list = LinkedList()
list.append(2)
list.append(3)
list.append(5)
list.append(9)
```

> **Output**: 2 3 5 9

### How to reverse a linked list

```
# This function is in the LinkedList class

def reverse(self, list):
        if list.head is None:
            return

        current_node = list.head
        prev_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node
        list.head = prev_node
```
