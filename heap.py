class Heap(object):

    def __init__(self):
        self.heaplist = [0]
        self.current_size = 0


    def perc_up(self, i):
        # until we get to the root
        while i // 2 > 0:
            # if current item at heap is less than parent node
            if self.heaplist[i] < self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i//2] = self.heaplist[i//2], self.heaplist[i]

            # update current node to parent
            i = i // 2


    def insert(self, k):
        # add new item to end of list
        self.heaplist.append(k)

        # update size of list
        self.current_size += 1

        # perc up new item
        self.perc_up(self.current_size)


    def perc_down(self, i):
        # while we're not at a leaf node
        while i * 2 <= self.current_size:

            # find index of smallest child
            min_child_idx = self.min_child(i)
            if  self.heaplist[i] < self.heaplist[min_child]:
                self.heaplist[min_child], self.heaplist[i] = self.heaplist[i], self.heaplist[min_child]
            i = min_child_idx


    def min_child(self, i):

        # if there is no right child return the idx of the left child
        if i * 2 + 1 > self.current_size
            return i * 2

        # otherwise, find the smaller child of the two
        if self.heaplist[i * 2 + 1] < self.heaplist[i * 2]:
            return i * 2 + 1
        else:
            return i * 2


    def del_min(self):

        # swap first item with last item
        return_val = self.heaplist[1]
        self.heaplist[current_size] = self.heaplist[1]
        # remove last item
        self.heaplist.pop()
        self.current_size -= 1
        # perc down previous last item
        self.perc_down(1)

        return return_val


    def build_heap(self, alist):

        i = len(alist) // 2
        self.current_size = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1




