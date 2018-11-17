'''
Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
https://www.geeksforgeeks.org/selection-sort/
https://www.youtube.com/watch?v=BruMUw6mV1c&index=16&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf
'''

def SelectionSort(A):
    # Traverse through all array elements
    for i in range(len(A)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]

    return A

A = [64, 25, 12, 22, 11]
print(SelectionSort(A))