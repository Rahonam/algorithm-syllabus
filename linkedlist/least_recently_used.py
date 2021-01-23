from doubly_linkedlist import Node, LinkedList

class LeastRecentlyUsed:
    """
    A data structure which implements Least Recently Used (LRU) Cache
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.item_list = LinkedList()
        self.item_map = {}
    
    def __repr__(self):
        return self.item_list
    
    def look(self, item):
        if item in self.item_map:
            self.item_list.remove_node(item)
            self.item_list.add_first(Node(item))
        elif self.capacity > 0:
            self.item_list.add_first(Node(item))
            self.item_map[item] = Node(item)
            self.capacity -= 1
        else:
            self.item_map.pop(self.item_list.tail.data)
            self.item_map[item] = Node(item)
            self.item_list.remove_node(self.item_list.tail.data)
            self.item_list.add_first(Node(item))
        print(self.item_list)


lru = LeastRecentlyUsed(4)
lru.look(1)
lru.look(2)
lru.look(1)
lru.look(3)
lru.look(4)
lru.look(3)
lru.look(5)
lru.look(4)
lru.look(6)