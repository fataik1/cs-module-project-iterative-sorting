def binary_search(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        #1 compare the target element to midpoint
        mid = (high + low) // 2

        #2 If the midpoint ellemnt matches our target; then we've
        #found what we're looking for, return the midpoint index
        if target == arr[mid]:
            return mid
        #how do we find the midpoint
        # The length of the array will help us determine the midpoint
        # the "range": the left-most index and the right-most index
        # then the midpoint element is (right index + left index) / 2 
    #3 determine which half to go in; toss out the other half
        # reassign either left or right index to point to the element past the midpoint
        if target < arr[mid]:
        #cut out the right half
        # reassign high to mid - 1
            high = mid - 1
        if target > arr[mid]:
        # cut out the left half
        #reassign low to mid + 1
            low = mid + 1
    # 4. Repeat this process: we ned to loop this
    #what is our loopoing criteria? What tells us we are done looping?

    return -1

arr =[3, 4, 6, 16, 26, 28, 52, 55]
print(binary_search(arr,4))