class MinHeap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(i) {
    return Math.floor((i - 1) / 2);
  }

  getLeftChildIndex(i) {
    return 2 * i + 1;
  }

  getRightChildIndex(i) {
    return 2 * i + 2;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  insert(val) {
    this.heap.push(val);
    this.heapifyUp(this.heap.length - 1);
  }

  heapifyUp(index) {
    let curIdx = index;
    let parentIdx = this.getParentIndex(curIdx);

    while (curIdx > 0 && this.heap[curIdx] < this.heap[parentIdx]) {
      this.swap(curIdx, parentIdx);
      curIdx = parentIdx;
      parentIdx = this.getParentIndex(curIdx);
    }
  }

  extractMin() {
    if (this.heap.length === 0) {
      throw new Error("Heap is empty");
    }

    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown(0);

    return min;
  }

  heapifyDown(index) {
    let curIdx = index;
    let leftChildIdx = this.getLeftChildIndex(curIdx);
    let rightChildIdx = this.getRightChildIndex(curIdx);
    let smallest = curIdx;

    if (
      leftChildIdx < this.heap.length &&
      this.heap[leftChildIdx] < this.heap[smallest]
    ) {
      smallest = leftChildIdx;
    }

    if (
      rightChildIdx < this.heap.length &&
      this.heap[rightChildIdx] < this.heap[smallest]
    ) {
      smallest = rightChildIdx;
    }

    if (smallest !== curIdx) {
      this.swap(curIdx, smallest);
      this.heapifyDown(smallest);
    }
  }

  getMin() {
    if (this.heap.length === 0) {
      throw new Error("Heap is empty");
    }
    return this.heap[0];
  }

  getSize() {
    return this.heap.length;
  }
}

export default MinHeap;
