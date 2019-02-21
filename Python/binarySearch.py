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

print(linear_search(myData, target))