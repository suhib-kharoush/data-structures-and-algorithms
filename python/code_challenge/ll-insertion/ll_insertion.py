from typing import Counter


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, value):
        new_value = Node(value)
        new_value.next = self.head
        self.head = new_value

    def includes(self, x):
        current = self.head
        try:
            while current != None:
                if current.value == x:
                    return True
                current = current.next
            return False
        except:
            print("something went wrong")

    def __str__(self):
        output = ''
        current = self.head
        try:
            while current:
                output += f"{ {current.value} } --->"
                current = current.next
            output += f"{None}"
            return output
        except:
            print("wrong insertion")

    def append(self, value):
        new_value = Node(value)
        current = self.head
        if not self.head:
            self.head = new_value
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_value

    def __repr__(self):
        pass

    def kthFromEnd(self, k):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        value = None
        if length < k:
            current = self.head
            for i in range(0, length-k-1):
                value = current.data
                current = current.next
        return value


    def insertAfter(self, value, new_value):
        if value is None:
            return "wrong insertion"
        else:
            current = self.head
            new_node = Node(new_value)
            while current:
                if current.value == value:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next

    def insertBefore(self, value, new_value):
        newInsertion = Node(new_value)
        current = self.head
        if current == None:
            return "empty list"
        else:
            if current.value == value:
                newInsertion.next = self.head
                self.head = newInsertion
            
            while current.next:
                if current.next.value == value:
                    newInsertion.next = current.next
                    current.next = newInsertion
                    return
                else:
                    current = current.next
            return "value not in the node"
    
    def empty_link_list(self):
        self.head = None
        return

             
    
    



if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)
    ll1.insert(4)

    
    print(ll1)
