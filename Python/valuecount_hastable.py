# Using hashtable to count an individual items

fruits = ["apple", "orange", "pineapple", "kiwi",
          "apple", "orange", "kiwi", "pear", "mango", "mango"]

# create a hashtable object to hold fruits and counts
counter = dict()

# iterate over fruits, and increment count for each one
for fruit in fruits:
    if (fruit in counter.keys()):
        counter[fruit] += 1
    else:
        counter[fruit] = 1

# print result
print(counter)
