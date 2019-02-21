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
    # 2 base cases
    # idx we are at is an uppercase, then return
    if inputStr[idx].isupper():
        return inputStr[idx]
    
    # process to the end of string, current position is at last idx.
    # which mean no uppercase found.
    if idx == len(inputStr)-1:
        return "No uppercase letter found"
    return find_uppercase_recursive(inputStr, idx+1)

print(find_uppercase_recursive(inputStr2))