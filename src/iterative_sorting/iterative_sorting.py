# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for f in range(cur_index, len(arr)):
            if arr[f] < arr[smallest_index]:
                smallest_index = f


        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

array = [9, 8, 6, 7, 18, 11]
print(selection_sort(array))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # I want to iterate through the index
    for i in range(len(arr)):

        #last element should be where they need to be at
        for f in range(0, len(arr) - i - 1): 
            cur_index = f
            next_index = f + 1   
            
            #If the current element is > than the next
            if arr[cur_index] > arr[next_index]:
            #swap the elements like above function
                arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]


    return arr

#print(bubble_sort(array))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
