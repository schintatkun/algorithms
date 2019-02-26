# Linear O(N)
# simple solution
def is_palindrome(str):
    i = 0
    j = len(str)-1

    while i < j:
        while not str[i].isalnum() and i < j:
            i += 1
        while not str[i].isalnum() and i < j:
            j += 1
        if str[i] != str[j]:
            return False
        i+= 1
        j-= 1
    return True

print(is_palindrome("racabe"))
print(is_palindrome("racecar"))