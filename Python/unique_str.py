str1 = "AbCdefg"
str2 = "non Unique"

def normalize(inputStr):
    inputStr = inputStr.replace(" ", "")
    return inputStr.lower()

def is_unique(inputStr):
    d = dict()
    for i in inputStr:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

#normalize input string

str1 = normalize(str1)
str2 = normalize(str2)

print(is_unique(str1))
print(is_unique(str2))