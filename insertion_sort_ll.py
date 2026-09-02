#insertion sort using linked list
# O(n^2) time complexity
# added space complexity of O(n) for linked list
# best case time complexity of O(n) when the list is already sorted
# worst case time complexity of O(n^2) when the list is sorted in reverse order
# average case time complexity of O(n^2) when the list is randomly sorted
# is stable sort algorithm --> values of equal elements not rearranged in the sorted list

class node:
    head = None
    def __init__(self, data):
        self.data = data
        self.next = None


numbers = [10, 9, 8, 7,6, 5, 4, 3, 2, 1]

node.head = node(numbers[0])

for num in numbers[1:]:
    new_node = node(num)

    current = node.head

    if current.data > new_node.data:
        new_node.next = node.head
        node.head = new_node

    elif current.next == None:
        if new_node.data < node.head.data:
            new_node.next = node.head
            node.head = new_node
        else:
            node.head.next = new_node
    else:
        found = False
        while current.next != None:
            if new_node.data < current.next.data:
                new_node.next = current.next
                current.next = new_node
                found = True
                break

            current = current.next

        if current.data < new_node.data and not found:
            current.next = new_node

current = node.head
while current != None:
    print(current.data)
    current = current.next