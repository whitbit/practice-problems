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
   

    def reverse_list(self):
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
