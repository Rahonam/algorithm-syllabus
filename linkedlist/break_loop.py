from linkedlist import Node, LinkedList

def break_loop(head:Node):
    """
    Find the loop in given linkedlist, its length and break the loop.

    using: iteration, Floyd’s Cycle detection algorithm, time O(log(n)), space O(1)
    Floyd’s Cycle detection algorithm terminates when fast and slow pointers meet at a common point.

    Args:
        head: head node of linkedlist
    
    Returns:
        integer: the length of loop in given linkedlist

    """
    first_pointer = head
    second_pointer = first_pointer.next.next
    has_loop = False

    while second_pointer is not None and second_pointer.next is not None:
        if first_pointer == second_pointer:
            has_loop = True
            break
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next.next

    loop_length = 0
    if has_loop:
        second_pointer = second_pointer.next
        loop_length = 1
        while first_pointer != second_pointer:
            second_pointer = second_pointer.next
            loop_length += 1
        
        first_pointer = head
        second_pointer = head
        i = 1
        while i < loop_length:
            second_pointer = second_pointer.next
            i += 1
        
        while second_pointer.next != first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        
        second_pointer.next = None
    
    return loop_length


llist1 = LinkedList([10, 20, 30, 40, 50, 60])
print(llist1)
print(break_loop(llist1.head))

# create a loop
last_node = llist1.head
loop_node = llist1.head
for node in llist1:
    last_node = node
    if node.data == 30:
        loop_node = node

last_node.next = loop_node
print(break_loop(llist1.head))
print(llist1)