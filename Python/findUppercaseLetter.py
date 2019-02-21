inputStr = "seattleWashington"

# iterative method
def find_uppercase_iterative(inputStr):
    for i in range(len(inputStr)):
        if inputStr[i].isupper():
            return inputStr[i]
    return "No uppercase letter found"

print(find_uppercase_iterative(inputStr))