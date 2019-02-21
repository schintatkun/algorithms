# Given a string, calculate the length of the string,using recursion.

inputStr = "SeattleWashington"
inputStr2 = "IlovePython"


# Iterative method
def iterative_str_length(str):
    strLength = 0
    for i in range(len(str)):
        strLength += 1
    return strLength

print(iterative_str_length(inputStr))
print(iterative_str_length(inputStr2))


# Recursion method
def recursive_str_length(str):

    # base cases
    if str == '':
        return 0
    return 1 + recursive_str_length(str[1:])

print(recursive_str_length(inputStr))