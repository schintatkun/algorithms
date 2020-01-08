# searching for an item in an unordered list

myList = [3, 20, 10, 55, 98, 74, 2, 38]


def find_item(item, itemlist):
    for i in range(0, len(myList)):
        if item == itemlist[i]:
            return i
    return None


# Test
print(find_item(31, myList))
print(find_item(98, myList))
