# runtime : O(n * n) = O(n)
def selection_sort(arr):
    # iterate through the array (represent the sorted-unsorted boundary
    # moving across the array)
    for i in range(len(arr)): #O(n)
        #index of the boundary, as well as the index we're going to
        #swap the smallest element with
        boundary = i

        smallest_value = arr[boundary]
        smallest_index = boundary
        # finding the smallest element
        # in the "unsorted" portion of the array
        for unsorted_index in range(boundary, len(arr)): # O(n)
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        #`smallest` is the smallest element in the unsorted portion

        # once that's found, sqap it with the element on the right side
        # of the sorted-unsorted boundary
    return arr

arr = [5, 55, 6, 67, 12, 9, 25, 43, 16]
print(selection_sort(arr))