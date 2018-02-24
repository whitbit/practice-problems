class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return 'Val {}'.format(self.val)


class LinkedList(object):

    def __init__(self):
        self.head = None

    def __repr__(self):
        return '<Head {}>'.format(self.head)

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node
   

    def reverse_list_in_place(self):
        current = self.head
        prev = None

        while current:
            # current.next, current, prev = prev, current.next, current
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next

        self.head = prev
        return prev

    def build_new_reversed_list(self):
        current = self.head
        new_list = LinkedList()
        
        while current:
            new_node = Node(current.val)
            new_list.push(new_node)
            current = current.next

        return new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurence of key in linked list
    def deleteNode(self, key):
         
        # Store head node
        current = self.head
 
        # If head node itself holds the key to be deleted
        if (current is not None):
            if (current.data == key):
                self.head = current.next
                current = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(current is not None):
            if current.data == key:
                break
            prev = current
            current = current.next
 
        # if key was not present in linked list
        if(current == None):
            return
 
        # Unlink the node from linked list
        prev.next = current.next
 
        current = None

    def contains_cycle(first_node):

        slow_runner = first_node
        fast_runner = first_node

        while fast_runner is not None and fast_runner.next is not None:
            slow_runner = slow_runner.next
            fast_runner = slow_runner.next.next

        if fast_runner is slow_runner:
            return True

        return False

    def contains_cycle(self):

        current = self.head
        nodes = set()
        print 'hello'

        while current is not None:
            if current in nodes:
                return True
            nodes.add(current)
            current = current.next
        return False





a = Node(5)
print a
b = Node(6)
c = Node(7)
d = Node(8)
e = Node(5)
print e
LL = LinkedList()

LL.push(a)
LL.push(b)
LL.push(c)
LL.push(d)
LL.push(e)
print LL.contains_cycle()
