#Create Linked List
# Display

class Node:
    def __init__(self,data=None):
        self.data =data
        self.next =None

class SingleLinkedList:
    def __init__(self):
        self.head =None # Address next Node/Object

    def appened_data(self,data):
        new_node = Node(data)
        print("Head : : ",not self.head)
        while self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_at_begning(self):
        temp = self.head
        self.head= temp.next

    def delte_at_last(self):
        temp = self.head
        last_but_next = None
        while temp.next:
            last_but_next =temp
            temp = temp.next
        last_but_next.next =None

    def display(self):
        """Print all the elements of the list."""
        if self.head is None:
            print("Single Linked List is Empty")
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str,elements)) + " -> None", "   ::  ", elements)

l = SingleLinkedList()

for i in range(3):
    n = input("Enter number: ")
    l.appened_data(n)
    l.display()
input("Press enter to delete at the begning...: ")
l.delete_at_begning()
#l.delte_at_last()

l.display()
print(l.head)