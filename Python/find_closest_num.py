# arr = [1, 2, 4, 5, 6, 6, 8, 9]
arr = [2, 5, 6, 7, 8, 8, 9]


def find_closest_num(arr, target):
    min_diff = float("inf")
    low = 0
    high = len(arr) -1
    closest_num = None

    #Edge cases for empty List or when the list is only one element.
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    while low <= high:
        mid = (low+high) // 2

        # Ensure we don't read beyond the bound of the List
        # And obtain the left and right difference value

        if mid + 1 < len(arr):
            min_diff_right = abs(arr[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(arr[mid-1] - target)

        # check if the absolute value between left and right 
        # elements are smaller than any seen prior.

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = arr[mid-1]
        
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = arr[mid+1]

        # Move the mid point acoordingly as is done via binary search.

        if arr[mid] < target:
            low = mid+1

        elif arr[mid] > target:
            high = mid -1

        # if the element is the target itself, the closest number to it is itself.
        else:
            return arr[mid]
    return closest_num


x = find_closest_num(arr, 4)
print(x)