class Node():
    def __init__(self, a_number) -> int:
        self.data = a_number
        self.next = None


# Linked List
class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_element(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head

        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head

        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None

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


list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

list2.reverse(list2)

# print(list2.show_element())


# print('list2.length:', list2.length())

# print('list2.get_element(0): ', list2.get_element(0))
# print('list2.get_element(2): ', list2.get_element(2))
# print('list2.get_element(1): ', list2.get_element(1))
