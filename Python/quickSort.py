# quicksort

unsortedArr = [10, 2, 8, 29, 89, 41, 61, 74, 19, 31, 15]


def quicksort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # sort two separated partitions
        quicksort(dataset, first, pivotIdx-1)
        quicksort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # select the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # begin searching for the crossing piont
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # if two indexes cross, then found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # When the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper


# test the mergesort
print(unsortedArr)
quicksort(unsortedArr, 0, len(unsortedArr)-1)
# print result after run mergesort
print(unsortedArr)
