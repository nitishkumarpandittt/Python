"""
================================================================================
HEAPS & HEAPIFY ALGORITHM
================================================================================
A Binary Heap is a Complete Binary Tree stored efficiently as a 1D array/list.

Array Index Mapping (0-based indexing):
  For any node at index `i`:
    - Parent:       (i - 1) // 2
    - Left Child:   2 * i + 1
    - Right Child:  2 * i + 2
    - Last non-leaf node: (n // 2) - 1   [where n = len(array)]
================================================================================
"""

import heapq

# ==============================================================================
# PART 1: HEAPIFY ALGORITHM (FROM SCRATCH)
# ==============================================================================

def min_heapify(arr, n, i):
    """
    Sifts down the element at index `i` so the subtree rooted at `i`
    satisfies the Min-Heap property (parent <= children).
    Time Complexity: O(log n)
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is smaller than current smallest
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Check if right child is smaller than current smallest
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest is not the root, swap and continue sifting down
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def build_min_heap(arr):
    """
    Converts an arbitrary array into a Min-Heap in-place.
    Starts from the last non-leaf node and works backwards to the root (index 0).
    Time Complexity: O(n) (not O(n log n)!)
    """
    n = len(arr)
    # Start from the last internal node down to index 0
    start_idx = (n // 2) - 1
    for i in range(start_idx, -1, -1):
        min_heapify(arr, n, i)
    return arr


def max_heapify(arr, n, i):
    """
    Sifts down for a Max-Heap property (parent >= children).
    Time Complexity: O(log n)
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_max_heap(arr):
    """Converts an arbitrary array into a Max-Heap in-place in O(n) time."""
    n = len(arr)
    start_idx = (n // 2) - 1
    for i in range(start_idx, -1, -1):
        max_heapify(arr, n, i)
    return arr


# ==============================================================================
# PART 2: PYTHON'S BUILT-IN `heapq` MODULE
# ==============================================================================
# Note: Python's `heapq` only provides a MIN-HEAP implementation.

def heapq_demonstration():
    print("--- 1. heapq.heapify() ---")
    data = [20, 15, 30, 5, 10, 40]
    print("Before heapify:", data)
    heapq.heapify(data)  # O(n) in-place transformation
    print("After heapify (Min-Heap):", data)
    print("Smallest element is always at index 0:", data[0])
    print()

    print("--- 2. heapq.heappush() ---")
    # Pushes an item while maintaining heap invariant (O(log n))
    heapq.heappush(data, 2)
    print("After pushing 2:", data)
    print("New minimum element:", data[0])
    print()

    print("--- 3. heapq.heappop() ---")
    # Pops and returns the smallest item (O(log n))
    smallest = heapq.heappop(data)
    print("Popped item:", smallest)
    print("Heap after pop:", data)
    print()

    print("--- 4. heapq.heappushpop() ---")
    # Pushes item, then pops and returns smallest item (more efficient than push followed by pop)
    result = heapq.heappushpop(data, 7)
    print("Pushed 7, popped returned:", result)
    print("Heap state:", data)
    print()

    print("--- 5. heapq.heapreplace() ---")
    # Pops smallest item first, then pushes the new item (more efficient than pop followed by push)
    result = heapq.heapreplace(data, 25)
    print("Popped smallest, inserted 25. Returned:", result)
    print("Heap state:", data)
    print()

    print("--- 6. heapq.nsmallest() & heapq.nlargest() ---")
    numbers = [50, 10, 80, 20, 90, 40, 70]
    three_smallest = heapq.nsmallest(3, numbers)  # O(n log k)
    three_largest = heapq.nlargest(3, numbers)    # O(n log k)
    print("Numbers:", numbers)
    print("3 Smallest:", three_smallest)
    print("3 Largest:", three_largest)
    print()

    print("--- 7. Simulating a MAX-HEAP with heapq ---")
    # Trick: negate the numbers when pushing, and negate again when popping
    nums = [10, 30, 20, 400, 50]
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)

    # Pop max elements in descending order
    print("Popping elements in descending order (Max-Heap):")
    while max_heap:
        max_val = -heapq.heappop(max_heap)
        print(max_val, end=" ")
    print("\n")


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    print("=== MANUAL HEAPIFY DEMO ===")
    sample = [40, 10, 30, 5, 70, 20]
    print("Original array:", sample)
    build_min_heap(sample)
    print("Built Min-Heap (scratch):", sample)

    sample_max = [40, 10, 30, 5, 70, 20]
    build_max_heap(sample_max)
    print("Built Max-Heap (scratch):", sample_max)
    print("\n" + "=" * 50 + "\n")

    print("=== HEAPQ BUILT-IN METHODS DEMO ===")
    heapq_demonstration()

