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
    # iterate to the end of string, which means string is empty
    if input == "":
        return 0
    # first character is not in vowels and an alphabet
    if input[0].lower() not in vowels and input[0].isalpha():
        #call recursive function input = positions start at position 1 to the end
        return 1+ recursive_count_consonants(input[1:])
    else: 
        # character is a vowel, then no +1 
        return recursive_count_consonants(input[1:])

print(iterative_consonants(inputStr1))
print(recursive_count_consonants(inputStr2))