class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


head, tail = None, None
N, MAX = 0, 0
mMap = {}


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        global head, tail, MAX, N, mMap
        head = None
        tail = None
        MAX = capacity
        N = 0
        mMap = {}

    def updateAccessList(self, node):
        global head
        temp = node.prev
        temp.next = node.next
        temp = node.next
        if (temp != None):
            temp.prev = node.prev

        node.next = head
        head.prev = node
        node.prev = None
        head = node

    # @return an integer
    def get(self, key):
        global head, tail, MAX, N, mMap
        if (N == 0):
            return -1

        if (key in mMap):
            node = mMap[key]
            if (key == head.key):
                return node.val
            if (tail.key == key):
                tail = tail.prev

            self.updateAccessList(node)
            return node.val

        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        global head, tail, MAX, N, mMap
        if (key in mMap):
            node = mMap[key]
            if (node.key == head.key):
                node.val = value
                return
            if (tail.key == key):
                tail = tail.prev
            self.updateAccessList(node)
            node.val = value
            return

        if (N == MAX):
            if (tail != None):
                del mMap[tail.key]
                tail = tail.prev
                if (tail != None):
                    tail.next.prev = None
                    tail.next = None
                N -= 1

        node = Node(key, value)
        node.next = head
        if (head != None):
            head.prev = node

        head = node
        N += 1

        if (N == 1):
            tail = head

        mMap[key] = node