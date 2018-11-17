def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - 1):               #if I have an array with 6 elements, why do I only need to make 5 iterations?    https://stackoverflow.com/questions/47529349/why-do-we-make-n-1-iterations-in-bubble-sort-algorithm
                                                #Because a swap requires at least two elements. So if you have 6 elements, you only need to consider 5 consecutive pairs

            # traverse the array from 0 to n-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # Driver code to test above
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print(bubbleSort(arr))

