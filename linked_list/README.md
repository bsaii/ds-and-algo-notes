## How to create a linked list
1. Create a Node class with the data and next.
2. Creat a Linked List class with the head and other methods.


```python
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

```python
list = LinkedList()
list.append(2)
list.append(3)
list.append(5)
list.append(9)
```

> **Output**: 2 3 5 9

### How to reverse a linked

**Iteration Method**
1. Initialize three pointers prev as None, curr as head and next as None.
2. Iterate through the linked list. In loop, do following. 

- Before changing next of current, 
   store next node 
`next = curr->next`

- Now change next of current 
- This is where actual reversing happens 
`curr->next = prev` 

- Move prev and curr one step forward 
`prev = curr` 
`curr = next`

![Reverse Linked List GIF](https://media.geeksforgeeks.org/wp-content/cdn-uploads/RGIF2.gif)

```python
 # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
```

> Time Complexity: O(n) 
> 
> Space Complexity: O(1)

**Recursion Method**

1. Divide the list in two parts - first node and rest of the linked list.
2. Call reverse for the rest of the linked list.
3. Link rest to first.
4. Fix head pointer

![Reverse Linked List](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/07/Linked-List-Rverse.gif)

```python
# This function is in the LinkedList class

# Method to reverse the list
    def reverse(self, head):
 
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
 
        # Reverse the rest list
        rest = self.reverse(head.next)
 
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rest
```
> Time Complexity: O(n) 
> 
> Space Complexity: O(1)
