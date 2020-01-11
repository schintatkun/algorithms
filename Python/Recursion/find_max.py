# find a maximum value using recursion

items = [5, 3, 56, 12, 1, 92, 44, 35, 71, 99]


def find_max(items):

    # breaking condition
    if len(items) == 1:
        return items[0]

    # otherwise get first item in list and call find_max again
    # to compute on the rest of list

    val1 = items[0]
    # print(val1)
    val2 = find_max(items[1:])
    # print(val2)

    if val1 > val2:
        return val1
    else:
        return val2


# print result
print(find_max(items))
