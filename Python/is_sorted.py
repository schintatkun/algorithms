# determine if a list is sorted

list1 = [3, 5, 10, 15, 22, 31, 38, 43, 50, 87]
list2 = [2, 20, 30, 1, 15, 50, 80, 41, 99, 78]


def is_sorted(itemlist):

    for i in range(0, len(itemlist)-1):
        if (itemlist[i] > itemlist[i+1]):
            return False
    return True


print(is_sorted(list1))
print(is_sorted(list2))
