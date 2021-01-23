class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                new_node = Node(data=elem)
                node.next = new_node
                new_node.previous = node
                node = new_node
            self.tail = new_node

    def __repr__(self):
        node = self.head
        nodes = ["None"]
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " <=> ".join(str(x) for x in nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, node):
        if self.head is None:
            self.head = node
            if self.tail is not None:
                self.head.next = self.tail
                self.tail.previous = self.head
            else:
                self.tail = node
            return
        self.head.previous = node
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.tail is None:
            self.tail = node
            if self.head is not None:
                self.tail.previous = self.head
                self.head.next = self.tail
            else:
                self.head = node
            return
        self.tail.next = node
        node.previous = self.tail
        self.tail = node
    
    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.tail.data == target_node_data:
            return self.add_last(new_node)

        for node in self:
            if node.data == target_node_data:
                next_node = node.next
                new_node.next = next_node
                next_node.previous = new_node
                node.next = new_node
                new_node.previous = node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.previous = prev_node
                new_node.next = node
                node.previous = new_node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            self.head.previous = None
            return
        
        if self.tail.data == target_node_data:
            self.tail = self.tail.previous
            self.tail.next = None
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                next_node = node.next
                previous_node.next = next_node
                next_node.previous = previous_node
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

