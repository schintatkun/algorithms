#Given a string, count the number of consonants.
# Note a consonant is a letter that is not a vowel,
# example a letter that is not a e i o u

inputStr1 = "abc de"
inputStr2 = "SeattleWashington"

vowels = "aeiou"

def iterative_consonants(input):
    count = 0
    for i in range(len(input)):
        if input[i].lower() not in vowels and input[i].isalpha():
            count += 1
    return count

def recursive_count_consonants(input):

    # base case
    if input == "":
        return 0
    if input[0].lower() not in vowels and input[0].isalpha():
        return 1+ recursive_count_consonants(input[1:])
    else: 
        return recursive_count_consonants(input[1:])

print(iterative_consonants(inputStr1))
print(recursive_count_consonants(inputStr2))