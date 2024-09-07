class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):

        self.head = None

    def append(self, data):
        # check if head is empty or not
        if self.head is None:
            node = Node(data)
            self.head = node

        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def display(self):
        if self.head is None:
            print("list is empty ")

        else:
            result = ""
            current_node = self.head
            while current_node:
                result += f"{current_node.data}=>"
                current_node = current_node.next
            print(result)


ll = LinkedList()
ll.append(10)
ll.append(5)
ll.append(6)
ll.display()

