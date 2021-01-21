
from linkedlist import Node, LinkedList
import heapq

def merge_sorted_linkedlists(head_list:list):
    """
    Merge k given sorted linked lists into one sorted linked list

    using: iteration, min heap, time O(nlog(k)) space O(n), n is length of longest linkedlist

    Args:
        head_list: array of head nodes of linkedlists
    
    Returns:
        Linkedlist: the merged linkedlist

    """
    heapq.heapify(head_list)
    
    current_node = heapq.heappop(head_list)
    sorted_linkedlist = LinkedList([current_node]) 
    if current_node.next is not None:
        heapq.heappush(head_list, current_node.next)

    while len(head_list):
        node = heapq.heappop(head_list)
        sorted_linkedlist.add_last(Node(node))
        if node.next is not None:
            heapq.heappush(head_list, node.next)

    return sorted_linkedlist


llist1 = LinkedList([1, 5])
llist2 = LinkedList([4, 8])
llist3 = LinkedList([4, 6, 9])
llist4 = LinkedList([2, 7, 10])
print(llist1,llist2,llist3,llist4)

print(merge_sorted_linkedlists([llist1.head,llist2.head,llist3.head,llist4.head]))
