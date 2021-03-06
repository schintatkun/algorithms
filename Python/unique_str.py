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

def is_unique2(inputStr):
    return len(set(inputStr))== len(inputStr)

def is_unique3(inputStr):
    alpha = "abcdefghigklmnopqrstuvwxyz"

    for i in inputStr:
        if i in alpha:
            alpha = alpha.replace(i,"")
        else:
            return False
    return True

#normalize input string

str1 = normalize(str1)
str2 = normalize(str2)

print(is_unique(str1))
print(is_unique(str2))

print(is_unique2(str1))
print(is_unique2(str2))

print(is_unique3(str1))
print(is_unique3(str2))