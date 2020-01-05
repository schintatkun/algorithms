# Merge sort with recursion

UnSortedArr = [20, 10, 22, 76, 92, 34, 8, 54, 11, 101]


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset)//2
        leftArr = dataset[:mid]
        rightArr = dataset[mid:]

        # recursively break down arrays
        mergesort(leftArr)
        mergesort(rightArr)

        # do the merging
        i = 0  # idx into the left array
        j = 0  # idx into the right array
        k = 0  # idx into merged array

        # while both left and right arrays still have content
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                dataset[k] = leftArr[i]
                i += 1
            else:
                dataset[k] = rightArr[j]
                j += 1
            k += 1

        # if left array still has values, add them
        while i < len(leftArr):
            dataset[k] = leftArr[i]
            i += 1
            k += 1

        # if right array still has values, add them
        while j < len(rightArr):
            dataset[k] = rightArr[j]
            j += 1
            k += 1


# test the merge sort
print(UnSortedArr)
mergesort(UnSortedArr)
print(UnSortedArr)
