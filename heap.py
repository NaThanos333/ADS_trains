class PriorityElement:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class Heap:
    def __init__(self):
        self._reverse_lookup = {}
        self._heap = [None]

    def size(self) -> int:
        return len(self._heap) - 1

    def _heap_empty_error(self) -> None:
        print("Heap empty")

    def _upheap(self, index) -> None:
        parent_idx = len(self.heap) // 2
        if index > 1 and self.heap[index] > self.heap[parent_idx]:
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            self._reverse_lookup[self.heap[index].node], self._reverse_lookup[self.heap[parent_idx].node] = self._reverse_lookup[self.heap[parent_idx].node], self._reverse_lookup[self.heap[index].node]
            self._upheap(parent_idx)

    def enqueue(self, value, priority) -> None:
        self.heap.append(PriorityElement(value, priority))
        self._reverse_lookup[value] = len(self.heap) - 1
        self._upheap(len(self.heap) - 1)

    def _downheap(self, index: int) -> None:
        index_max = index

        if index*2 <= self.size() and self._heap[index_max] < self._heap[index*2]:
            index_max = index*2
        if index*2+1 <= self.size() and self._heap[index_max] < self._heap[index*2+1]:
            index_max = index*2+1
        if index_max != index:
            self._heap[index], self._heap[index_max] = self._heap[index_max], self._heap[index]
            self._reverse_lookup[self._heap[index_max].node], self._reverse_lookup[self._heap[index].node] = self._reverse_lookup[self._heap[index].node], self._reverse_lookup[self._heap[index_max].node]
            self._downheap(index_max)
        

    def remove_max(self):
        if self.size() > 0:
            return_value = self._heap[1]
            if self.size() > 1:
                self._heap[1] = self._heap.pop()
                self._downheap(1)
            else:
                self._heap.pop()
            return return_value.node
        else:
            self._heap_empty_error()
