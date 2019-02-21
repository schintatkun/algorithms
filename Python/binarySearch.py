# sorted array
myData = [1,3,5,7,10,12,15,19,23,24,28,33,37,40,55,62]

# number we are looking for
target = 40


# Linear search
def linear_search(Data, num):
    for i in range(len(Data)):
        if myData[i] == num:
            return True
    return False

print("linear serach",linear_search(myData, target))

# Iterative binary search
def binary_search(data, num):
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low+high) /2
        print(mid)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

print("Iterative binary search", binary_search(myData,target))