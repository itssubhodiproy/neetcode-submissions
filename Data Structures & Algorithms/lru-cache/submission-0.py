class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.tail = None
        self.head = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        # If already tail, nothing to move
        if node == self.tail:
            return node.val

        # Remove node from current position
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        # Reassign at tail
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        return node.val

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.map:
            node = self.map[key]
            node.val = value

            # If already tail, nothing to move
            if node == self.tail:
                return

            # Remove node from current position
            if node == self.head:
                self.head = node.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            # Reassign at tail
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

            return

        # Capacity reached - remove LRU
        if self.capacity == len(self.map):
            old_head = self.head

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            del self.map[old_head.key]

        # Add new node
        node = ListNode(key=key, val=value, prev=self.tail)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.map[key] = node