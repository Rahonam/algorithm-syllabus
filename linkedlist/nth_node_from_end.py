from linkedlist import Node, LinkedList

def nth_node_from_end(head: Node, reverse_rank:int):
    """
    Find the nth node from the end in the Linked List

    using: iteration, time O(n) space O(1)

    Args:
        head: head node of linkedlist
        reverse_rank: rank from the end
    
    Returns:
        Node.data: data of the nth node from the end
    """
    current_node = head
    while reverse_rank > 0:
        current_node = current_node.next
        reverse_rank -= 1
    
    nth_node = head
    while current_node is not None:
        current_node = current_node.next
        nth_node = nth_node.next
    
    return nth_node.data
    

llist = LinkedList([1, 2, 8, 3, 7, 0, 4])
print(llist)
print(nth_node_from_end(llist.head, 3))
print(nth_node_from_end(llist.head, 5))