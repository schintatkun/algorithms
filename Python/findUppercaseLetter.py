inputStr = "seattleWashington"
inputStr2 = "lovecoding"

# iterative method
def find_uppercase_iterative(inputStr):
    for i in range(len(inputStr)):
        if inputStr[i].isupper():
            return inputStr[i]
    return "No uppercase letter found"

print(find_uppercase_iterative(inputStr))

def find_uppercase_recursive(inputStr, idx=0):
    # base cases
    if inputStr[idx].isupper():
        return inputStr[idx]
    
    # process to the end of string
    if idx == len(inputStr)-1:
        return "No uppercase letter found"
    return find_uppercase_recursive(inputStr, idx+1)

print(find_uppercase_recursive(inputStr2))