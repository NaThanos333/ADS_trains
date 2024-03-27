class Heap:
    def __init__(self):
        self._heap = [0]

    def size(self) -> int:
        return len(self._heap) - 1

    def _heap_empty_error(self) -> None:
        print("Heap empty")

    def _upheap(self, index: int) -> None:
        if index > 1:
            parent_index = index // 2
            if self._heap[parent_index] < self._heap[index]:
                self._heap[parent_index], self._heap[index] = self._heap[index], self._heap[parent_index]
                self._upheap(parent_index)

    def enqueue(self, value) -> None:
        self._heap.append(value)
        self._upheap(len(self._heap) - 1)

    def _downheap(self, index: int) -> None:
        left_child_index = 2 * index
        right_child_index = 2 * index + 1
        largest_index = index

        if left_child_index <= self.size() and self._heap[left_child_index] > self._heap[largest_index]:
            largest_index = left_child_index

        if right_child_index <= self.size() and self._heap[right_child_index] > self._heap[largest_index]:
            largest_index = right_child_index

        if largest_index != index:
            self._heap[index], self._heap[largest_index] = self._heap[largest_index], self._heap[index]
            self._downheap(largest_index)

    def remove_max(self):
        if self.size() > 0:
            return_value = self._heap[1]
            if self.size() > 1:
                self._heap[1] = self._heap.pop()
                self._downheap(1)
            else:
                self._heap.pop()
            return return_value
        else:
            self._heap_empty_error()