# hashtable to filter out duplicate items

fruits = ["apple", "orange", "pear", "apple",
          "banana", "orange", "pineapple", "kiwi", "banana"]

# create hashtable
filter = dict()

# loop over each item and add to hashtable
for key in fruits:
    filter[key] = 0

# create a set of keys from a hashtable
result = set(filter.keys())
print(result)
