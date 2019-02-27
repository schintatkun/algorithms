# Anagram

str1 = "fairy tales"
str2 = "rail safety"

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# requires n log n time
# print(sorted(str1) == sorted(str2))

def is_anagram(str1, str2):
    ht = dict()

    if len(str1) != len(str2):
        return False
    
    for i in str1:
        if i in ht:
            ht[i] += 1
        else: 
            ht[i] = 1

    for i in str2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    
    for i in ht: 
        if ht[i] != 0:
            return False
    return True

print(is_anagram(str1, str2))