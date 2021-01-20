from linkedlist import Node, LinkedList

def remove_duplicates(head:Node):
    """
    Remove the duplicates from an unsorted linked list

    using: iteration, dictionary, time O(n) space O(n)

    Args:
        head: head node of linkedlist
    
    Returns:

    """
    unique_map = {}
    previous_node = head
    current_node = head.next

    while current_node is not None:
        if current_node.data in unique_map:
            previous_node.next = current_node.next
            current_node = current_node.next

        else:
            unique_map[current_node.data] = ""
            previous_node = current_node
            current_node = current_node.next


llist = LinkedList([1, 2, 2, 4, 3, 3, 2])
print(llist)
remove_duplicates(llist.head)
print(llist)