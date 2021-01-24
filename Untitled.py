
# Python3 program to implement sorting a
# queue data structure
from queue import Queue

# Queue elements after sortedIndex are
# already sorted. This function returns
# index of minimum element from front to
# sortedIndex
def minIndex(q, sortedIndex):
    min_index = -1
    min_val = 999999999999
    n = q.qsize()
    for i in range(n):
        curr = q.queue[0]
        q.get() # This is dequeue() in C++ STL

        # we add the condition i <= sortedIndex
        # because we don't want to traverse
        # on the sorted part of the queue,
        # which is the right part.
        if (curr <= min_val and i <= sortedIndex):
            min_index = i
            min_val = curr
        q.put(curr) # This is enqueue() in
                    # C++ STL
    return min_index

# Moves given minimum element to
# rear of queue
def insertMinToRear(q, min_index):
    min_val = None
    n = q.qsize()
    for i in range(n):
        curr = q.queue[0]
        q.get()
        if (i != min_index):
            q.put(curr)
        else:
            min_val = curr
    q.put(min_val)

def sortQueue(q):
    for i in range(1, q.qsize() + 1):
        min_index = minIndex(q, q.qsize() - i)
        insertMinToRear(q, min_index)

# Driver code
if __name__ == '__main__':
    q = Queue()
    q.put(30)
    q.put(11)
    q.put(15)
    q.put(4)

    # Sort queue
    sortQueue(q)

    # Prsorted queue
    while (q.empty() == False):
        print(q.queue[0], end = " ")
        q.get()

# This code is contributed by PranchalK 
